import csv
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from cms_pattern import cms_patterns  
def check_meta_tag(soup):
    meta_generator = soup.find('meta', attrs={'name': 'generator'})
    if meta_generator and 'content' in meta_generator.attrs:
        return meta_generator['content'].lower()
    return None

def check_patterns(soup, patterns):
    # Check scripts
    for script in soup.find_all('script'):
        if 'src' in script.attrs:
            for pattern in patterns['scripts']:
                if pattern in script['src'].lower():
                    return True

    # Check links
    for link in soup.find_all('link'):
        if 'href' in link.attrs:
            for pattern in patterns['links']:
                if pattern in link['href'].lower():
                    return True

    return False

def detect_cms(url):
    if not url.startswith('http'):
        url = f'https://{url}'  # Add https:// if missing

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(10)

    try:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup) 

        # Check meta tag
        meta_content = check_meta_tag(soup)
        if meta_content:
            for cms, patterns in cms_patterns.items():
                if patterns['meta'] in meta_content:
                    return url, cms

        # Check patterns in scripts, links, and classes
        for cms, patterns in cms_patterns.items():
            if check_patterns(soup, patterns):
                return url, cms

        return url, 0 

    except WebDriverException as e:
        if 'ERR_NAME_NOT_RESOLVED' in e.msg:
            return url, 0
        elif 'ERR_CONNECTION_TIMED_OUT' in e.msg:
            return url, 0
        elif 'ERR_SSL_PROTOCOL_ERROR' in e.msg:
            return url, 0
        else:
            return url, 0

    finally:
        driver.quit()

def read_urls_from_csv(filename):
    urls = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Skip empty rows
                if row:
                    # Ensure the row has at least one element
                    url = row[0].strip()
                    if url:  # Skip rows with empty URL fields
                        urls.append(url)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return urls

def write_to_csv(filename, data, mode='w'):
    with open(filename, mode, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    urls = read_urls_from_csv('test.txt')
    
    # Overwrite the file at the start
    write_to_csv('websites.csv', ['URL', 'CMS detected'], mode='w')

    for url in urls:
        result = detect_cms(url)
        print(f"URL: {result[0]} -> CMS detected: {result[1]}")
        if result[1] != 0:
            write_to_csv('websites.csv', result, mode='a')

if __name__ == "__main__":
    main()
