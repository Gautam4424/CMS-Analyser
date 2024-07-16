# cms_patterns.py
cms_patterns = {
    'WordPress': {
        'meta': 'wp',
        'scripts': ['wp-'],
        'links': ['wp-', 'wp-content', 'wp-includes'],
        'classes': ['wp-', 'wp-admin'],
        'unique_pages': ['wp-admin', 'wp-login.php'] 
    },
    'Joomla': {
        'meta': 'joomla',
        'scripts': ['joomla'],
        'links': ['joomla'],
        'classes': ['joomla'],
        'unique_pages': ['administrator']
    },
    'Drupal': {
        'meta': 'drupal',
        'scripts': ['drupal.js'],
        'links': ['drupal.css'],
        'classes': ['drupal'],
        'unique_pages': ['user/login', 'user/register']
    },
    'Shopify': {
        'meta': 'shopify',
        'scripts': ['shopify.js'],
        'links': ['shopify.css'],
        'classes': ['shopify'],
        'unique_pages': ['admin']
    },
    'Prestashop': {
        'meta': 'prestashop',
        'scripts': ['prestashop.js'],
        'links': ['prestashop.css'],
        'classes': ['prestashop'],
        'unique_pages': ['admin']
    },
    'TYPO3': {
        'meta': 'typo3',
        'scripts': ['typo3'],
        'links': ['typo3'],
        'classes': ['typo3'],
        'unique_pages': ['typo3']
    },
    'Blogger': {
        'meta': 'blogger',
        'scripts': ['blogger'],
        'links': ['blogger'],
        'classes': ['blogger'],
        'unique_pages': ['b/']
    },
    'Bitrix': {
        'meta': 'bitrix',
        'scripts': ['bitrix'],
        'links': ['bitrix'],
        'classes': ['bitrix'],
        'unique_pages': ['bitrix/admin']
    },
    'Concrete5': {
        'meta': 'concrete5',
        'scripts': ['concrete5'],
        'links': ['concrete5'],
        'classes': ['concrete5'],
        'unique_pages': ['dashboard']
    },
    'Django': {
        'meta': 'django',
        'scripts': ['django'],
        'links': ['django'],
        'classes': ['django'],
        'unique_pages': ['admin']
    },
    'ExpressionEngine': {
        'meta': 'expressionengine',
        'scripts': ['expressionengine'],
        'links': ['expressionengine'],
        'classes': ['expressionengine'],
        'unique_pages': ['cp']
    },
    'Tilda': {
        'meta': 'tilda',
        'scripts': ['tilda.ws', 'tilda.cc', 'tildacdn.com'],
        'links': ['tilda.ws', 'tilda.cc', 'tildacdn.com'],
        'classes': ['tilda'],
        'unique_pages': ['tilda-blocks', 'tilda-articles']
    },
    'vBulletin': {
        'meta': 'vbulletin',
        'scripts': ['vbulletin'],
        'links': ['vbulletin'],
        'classes': ['vbulletin'],
        'unique_pages': ['admincp']
    },
    'XenForo': {
        'meta': 'xenforo',
        'scripts': ['xenforo'],
        'links': ['xenforo'],
        'classes': ['xenforo'],
        'unique_pages': ['admin.php']
    },
    'phpBB': {
        'meta': 'phpbb',
        'scripts': ['phpbb'],
        'links': ['phpbb'],
        'classes': ['phpbb'],
        'unique_pages': ['adm']
    },
    'SMF': {
        'meta': 'smf',
        'scripts': ['smf'],
        'links': ['smf'],
        'classes': ['smf'],
        'unique_pages': ['index.php?action=admin']
    },
    'osCommerce': {
        'meta': 'oscommerce',
        'scripts': ['oscommerce'],
        'links': ['oscommerce'],
        'classes': ['oscommerce'],
        'unique_pages': ['admin']
    },
    'OpenCart': {
        'meta': 'opencart',
        'scripts': ['opencart'],
        'links': ['opencart'],
        'classes': ['opencart'],
        'unique_pages': ['admin']
    },
    'DotNetNuke': {
        'meta': 'dotnetnuke',
        'scripts': ['dnn.js'],
        'links': ['dnn.css'],
        'classes': ['dnn'],
        'unique_pages': ['dnn/admin']
    },
    'Umbraco': {
        'meta': 'umbraco',
        'scripts': ['umbraco'],
        'links': ['umbraco'],
        'classes': ['umbraco'],
        'unique_pages': ['umbraco']
    },
    'Sitecore': {
        'meta': 'sitecore',
        'scripts': ['sitecore'],
        'links': ['sitecore'],
        'classes': ['sitecore'],
        'unique_pages': ['sitecore']
    },
    'Kentico': {
        'meta': 'kentico',
        'scripts': ['kentico'],
        'links': ['kentico'],
        'classes': ['kentico'],
        'unique_pages': ['admin']
    },
    'Weebly': {
        'meta': 'weebly',
        'scripts': ['weebly'],
        'links': ['weebly'],
        'classes': ['weebly'],
        'unique_pages': ['login']
    },
    'Squarespace': {
        'meta': 'squarespace',
        'scripts': ['squarespace'],
        'links': ['squarespace'],
        'classes': ['squarespace'],
        'unique_pages': ['config']
    },
    'Wix': {
        'meta': 'wix',
        'scripts': ['wix'],
        'links': ['wix'],
        'classes': ['wix'],
        'unique_pages': ['editor']
    },
    'Ghost': {
        'meta': 'ghost',
        'scripts': ['ghost.js'],
        'links': ['ghost.css'],
        'classes': ['ghost'],
        'unique_pages': ['ghost']
    },
    'craftcms': {
        'meta': 'craftcms',
        'scripts': ['craft.js', 'craftcms'],
        'links': ['craft.css', 'craftcms'],
        'classes': ['craftcms'],
        'unique_pages': ['admin']
    },
    'Grav': {
        'meta': 'grav',
        'scripts': ['grav.js'],
        'links': ['grav.css'],
        'classes': ['grav'],
        'unique_pages': ['admin']
    },
    'MODX': {
        'meta': 'modx',
        'scripts': ['modx.js'],
        'links': ['modx.css'],
        'classes': ['modx'],
        'unique_pages': ['manager']
    },
    'OctoberCMS': {
        'meta': 'octobercms',
        'scripts': ['october.js'],
        'links': ['october.css'],
        'classes': ['octobercms'],
        'unique_pages': ['backend']
    },
    'SilverStripe': {
        'meta': 'silverstripe',
        'scripts': ['silverstripe.js'],
        'links': ['silverstripe.css'],
        'classes': ['silverstripe'],
        'unique_pages': ['admin']
    },
    'Textpattern': {
        'meta': 'textpattern',
        'scripts': ['textpattern.js'],
        'links': ['textpattern.css'],
        'classes': ['textpattern'],
        'unique_pages': ['textpattern']
    },
    'Contao': {
        'meta': 'contao',
        'scripts': ['contao.js'],
        'links': ['contao.css'],
        'classes': ['contao'],
        'unique_pages': ['contao']
    },
    'ProcessWire': {
        'meta': 'processwire',
        'scripts': ['processwire.js'],
        'links': ['processwire.css'],
        'classes': ['processwire'],
        'unique_pages': ['admin']
    },
    'Statamic': {
        'meta': 'statamic',
        'scripts': ['statamic.js'],
        'links': ['statamic.css'],
        'classes': ['statamic'],
        'unique_pages': ['cp']
    },
    'Amplience': {
        'meta': 'amplience',
        'scripts': ['amplience.min.js', 'dc-integration.js'],
        'links': ['amplience.css'],
        'classes': ['amplience', 'dc-content'],
        'unique_pages': ['content-item']
    },
    'Subrion': {
        'meta': 'subrion',
        'scripts': ['subrion.js'],
        'links': ['subrion.css'],
        'classes': ['subrion'],
        'unique_pages': ['panel']
    },
    'ForkCMS': {
        'meta': 'forkcms',
        'scripts': ['fork.js'],
        'links': ['fork.css'],
        'classes': ['forkcms'],
        'unique_pages': ['private']
    },
    'ImpressPages': {
        'meta': 'impresspages',
        'scripts': ['ip.js'],
        'links': ['ip.css'],
        'classes': ['impresspages'],
        'unique_pages': ['admin']
    },
    'Tiki Wiki CMS Groupware': {
        'meta': 'tikiwiki',
        'scripts': ['tiki.js'],
        'links': ['tiki.css'],
        'classes': ['tikiwiki'],
        'unique_pages': ['tiki-admin']
    },
    'TYPOlight': {
        'meta': 'typolight',
        'scripts': ['typolight.js'],
        'links': ['typolight.css'],
        'classes': ['typolight'],
        'unique_pages': ['typolight']
    },
    'FrogCMS': {
        'meta': 'frogcms',
        'scripts': ['frog.js'],
        'links': ['frog.css'],
        'classes': ['frogcms'],
        'unique_pages': ['admin']
    },
    'dotCMS': {
        'meta': 'dotcms',
        'scripts': ['dotcms.js'],
        'links': ['dotcms.css'],
        'classes': ['dotcms'],
        'unique_pages': ['admin']
    },
    'Sitefinity': {
        'meta': 'sitefinity',
        'scripts': ['sitefinity.js'],
        'links': ['sitefinity.css'],
        'classes': ['sitefinity'],
        'unique_pages': ['Sitefinity']
    },
    'Liferay': {
        'meta': 'liferay',
        'scripts': ['liferay.js'],
        'links': ['liferay.css'],
        'classes': ['liferay'],
        'unique_pages': ['group/control_panel']
    },
    'Plone': {
        'meta': 'plone',
        'scripts': ['plone.js'],
        'links': ['plone.css'],
        'classes': ['plone'],
        'unique_pages': ['login']
    },
    'Webflow': {
        'meta': 'webflow',
        'scripts': ['webflow.js'],
        'links': ['webflow.css'],
        'classes': ['webflow'],
        'unique_pages': ['editor']
    },
    'Magnolia': {
        'meta': 'magnolia',
        'scripts': ['magnolia.js'],
        'links': ['magnolia.css'],
        'classes': ['magnolia'],
        'unique_pages': ['admincentral']
    },
    'Contentful': {
        'meta': 'Contentful',
        'scripts': ['contentful', 'cdn.contentful.com' , 'contentful'],
        'links': ['cdn.contentful.com', 'contentful' , 'contentful'],
        'json_keys': ['sys', 'fields'],
        'unique_pages': ['/contentful/api/spaces']
    },
    'Strapi': {
        'meta': 'strapi',
        'scripts': ['strapi.js'],
        'links': ['strapi.css'],
        'classes': ['strapi'],
        'unique_pages': ['admin']
    },
    'ButterCMS': {
        'meta': 'buttercms',
        'scripts': ['buttercms.js'],
        'links': ['buttercms.css'],
        'classes': ['buttercms'],
        'unique_pages': ['admin']
    },
    'Sanity': {
        'meta': 'sanity',
        'scripts': ['sanity.js'],
        'links': ['sanity.css'],
        'classes': ['sanity'],
        'unique_pages': ['studio']
    },
    'Agility CMS': {
        'meta': 'agilitycms',
        'scripts': ['agility.js'],
        'links': ['agility.css'],
        'classes': ['agilitycms'],
        'unique_pages': ['admin']
    },
    'Directus': {
        'meta': 'directus',
        'scripts': ['directus.js'],
        'links': ['directus.css'],
        'classes': ['directus'],
        'unique_pages': ['admin']
    },
    'Contentstack': {
        'meta': 'contentstack',
        'scripts': ['contentstack.js'],
        'links': ['contentstack.css'],
        'classes': ['contentstack'],
        'unique_pages': ['#!/stack']
    },
    'Cosmic JS': {
        'meta': 'cosmicjs',
        'scripts': ['cosmic.js'],
        'links': ['cosmic.css'],
        'classes': ['cosmicjs'],
        'unique_pages': ['bucket']
    },
    'GraphCMS': {
        'meta': 'graphcms',
        'scripts': ['graphcms.js'],
        'links': ['graphcms.css'],
        'classes': ['graphcms'],
        'unique_pages': ['cms']
    },
    'Kentico Kontent': {
        'meta': 'kenticokontent',
        'scripts': ['kontent.js'],
        'links': ['kontent.css'],
        'classes': ['kenticokontent'],
        'unique_pages': ['admin']
    },
    'Prismic': {
        'meta': 'prismic',
        'scripts': ['prismic.js'],
        'links': ['prismic.css'],
        'classes': ['prismic'],
        'unique_pages': ['studio']
    },
    'Storyblok': {
        'meta': 'storyblok',
        'scripts': ['storyblok.js'],
        'links': ['storyblok.css'],
        'classes': ['storyblok'],
        'unique_pages': ['editor']
    },
    'Webiny': {
        'meta': 'webiny',
        'scripts': ['webiny.js'],
        'links': ['webiny.css'],
        'classes': ['webiny'],
        'unique_pages': ['admin']
    },
    'Zesty.io': {
        'meta': 'zesty',
        'scripts': ['zesty.js'],
        'links': ['zesty.css'],
        'classes': ['zesty'],
        'unique_pages': ['zesty']
    },
    'Squiz Matrix': {
        'meta': 'squizmatrix',
        'scripts': ['squizmatrix.js'],
        'links': ['squizmatrix.css'],
        'classes': ['squizmatrix'],
        'unique_pages': ['_admin']
    },
    'Concrete CMS': {
        'meta': 'concretecms',
        'scripts': ['concrete.js', 'concrete'],
        'links': ['concrete.css' ,'concrete'],
        'classes': ['concretecms'],
        'unique_pages': ['dashboard']
    },
    '1C-Bitrix': {
        'meta': 'bitrix',
        'scripts': ['bitrix', 'bitrix24.js'],
        'links': ['bitrix.css', 'bitrix24.css'],
        'classes': ['bitrix', 'bitrix24'],
        'unique_pages': ['bitrix', 'admin', 'bitrix/admin']
    },

    'Anchor CMS': {
        'meta': 'anchor',
        'scripts': ['anchor.js'],
        'links': ['anchor.css'],
        'classes': ['anchor'],
        'unique_pages': ['admin']
    },
    'GetSimple CMS': {
        'meta': 'getsimple',
        'scripts': ['getsimple.js'],
        'links': ['getsimple.css'],
        'classes': ['getsimple'],
        'unique_pages': ['admin']
    },
    'Monstra CMS': {
        'meta': 'monstra',
        'scripts': ['monstra.js'],
        'links': ['monstra.css'],
        'classes': ['monstra'],
        'unique_pages': ['admin']
    },
    'Pagekit': {
        'meta': 'pagekit',
        'scripts': ['pagekit.js'],
        'links': ['pagekit.css'],
        'classes': ['pagekit'],
        'unique_pages': ['admin']
    },
    'WonderCMS': {
        'meta': 'wondercms',
        'scripts': ['wonder.js'],
        'links': ['wonder.css'],
        'classes': ['wondercms'],
        'unique_pages': ['login']
    },
    'Kirby': {
        'meta': 'kirby',
        'scripts': ['kirby.js'],
        'links': ['kirby.css'],
        'classes': ['kirby'],
        'unique_pages': ['panel']
    },
    'Bolt': {
        'meta': 'bolt',
        'scripts': ['bolt.js'],
        'links': ['bolt.css'],
        'classes': ['bolt'],
        'unique_pages': ['bolt']
    },
    'Pico': {
        'meta': 'picocms',
        'scripts': ['pico.js'],
        'links': ['pico.css'],
        'classes': ['picocms'],
        'unique_pages': ['admin']
    },
    'Automad': {
        'meta': 'automad',
        'scripts': ['automad.js'],
        'links': ['automad.css'],
        'classes': ['automad'],
        'unique_pages': ['dashboard']
    },
    'GravCMS': {
        'meta': 'gravcms',
        'scripts': ['grav.js'],
        'links': ['grav.css'],
        'classes': ['gravcms'],
        'unique_pages': ['admin']
    },
    'Canvas': {
        'meta': 'canvas',
        'scripts': ['canvas.js'],
        'links': ['canvas.css'],
        'classes': ['canvas'],
        'unique_pages': ['admin']
    },
    'Fae CMS': {
        'meta': 'faecms',
        'scripts': ['fae.js'],
        'links': ['fae.css'],
        'classes': ['faecms'],
        'unique_pages': ['admin']
    },
    'WebGarden': {
        'meta': 'webgarden',
        'scripts': ['webgarden.js'],
        'links': ['webgarden.css'],
        'classes': ['webgarden'],
        'unique_pages': ['admin']
    },
    'Neos CMS': {
        'meta': 'neos',
        'scripts': ['neos.js'],
        'links': ['neos.css'],
        'classes': ['neos'],
        'unique_pages': ['neos']
    },
    'Backdrop CMS': {
        'meta': 'backdrop',
        'scripts': ['backdrop.js'],
        'links': ['backdrop.css'],
        'classes': ['backdrop'],
        'unique_pages': ['admin']
    },
    'Concrete5 CMS': {
        'meta': 'concrete5',
        'scripts': ['concrete5.js' , 'concrete5'],
        'links': ['concrete5.css' , 'concrete5'],
        'classes': ['concrete5',],
        'unique_pages': ['dashboard']
    },
    'Enduro.js': {
        'meta': 'enduro',
        'scripts': ['enduro.js'],
        'links': ['enduro.css'],
        'classes': ['enduro'],
        'unique_pages': ['admin']
    },
    'Jekyll': {
        'meta': 'jekyll',
        'scripts': ['jekyll.js'],
        'links': ['jekyll.css'],
        'classes': ['jekyll'],
        'unique_pages': ['admin']
    },
    'Hugo': {
        'meta': 'hugo',
        'scripts': ['hugo.js'],
        'links': ['hugo.css'],
        'classes': ['hugo'],
        'unique_pages': ['admin']
    },
    'Middleman': {
        'meta': 'middleman',
        'scripts': ['middleman.js'],
        'links': ['middleman.css'],
        'classes': ['middleman'],
        'unique_pages': ['admin']
    },
    'Gatsby': {
        'meta': 'gatsby',
        'scripts': ['gatsby.js'],
        'links': ['gatsby.css'],
        'classes': ['gatsby'],
        'unique_pages': ['admin']
    },
    'Hexo': {
        'meta': 'hexo',
        'scripts': ['hexo.js'],
        'links': ['hexo.css'],
        'classes': ['hexo'],
        'unique_pages': ['admin']
    },
    'Brunch': {
        'meta': 'brunch',
        'scripts': ['brunch.js'],
        'links': ['brunch.css'],
        'classes': ['brunch'],
        'unique_pages': ['admin']
    },
    'Wintersmith': {
        'meta': 'wintersmith',
        'scripts': ['wintersmith.js'],
        'links': ['wintersmith.css'],
        'classes': ['wintersmith'],
        'unique_pages': ['admin']
    },
    'Metalsmith': {
        'meta': 'metalsmith',
        'scripts': ['metalsmith.js'],
        'links': ['metalsmith.css'],
        'classes': ['metalsmith'],
        'unique_pages': ['admin']
    },
    'Nuxt.js': {
        'meta': 'nuxt',
        'scripts': ['nuxt.js'],
        'links': ['nuxt.css'],
        'classes': ['nuxt'],
        'unique_pages': ['admin']
    },
    'Next.js': {
        'meta': 'nextjs',
        'scripts': ['next.js'],
        'links': ['next.css'],
        'classes': ['nextjs'],
        'unique_pages': ['admin']
    },
    'Sapper': {
        'meta': 'sapper',
        'scripts': ['sapper.js'],
        'links': ['sapper.css'],
        'classes': ['sapper'],
        'unique_pages': ['admin']
    },
    'Eleventy': {
        'meta': 'eleventy',
        'scripts': ['eleventy.js'],
        'links': ['eleventy.css'],
        'classes': ['eleventy'],
        'unique_pages': ['admin']
    },
    'HubSpot': {
        'meta': 'hubspot',
        'scripts': ['hs-scripts'],
        'links': ['hs-scripts', 'hs-internal', 'hubspot'],
        'classes': ['hs-main'],
        'unique_pages': ['_hcms']
    },
    
    'Progress Sitefinity': {
        'meta': 'progress-sitefinity',
        'scripts': ['sitefinity.js', 'progress.js'],
        'links': ['sitefinity.css', 'progress.css'],
        'classes': ['sitefinity', 'progress'],
        'unique_pages': ['admin', 'sitefinity']
    },
    'WooCommerce': {
        'meta': 'woocommerce',
        'scripts': ['woocommerce/'],
        'links': ['woocommerce/'],
        'classes': ['woocommerce'],
        'unique_pages': ['admin']
    },
    'BigCommerce': {
        'meta': 'bigcommerce',
        'scripts': ['bigcommerce/'],
        'links': ['bigcommerce/'],
        'classes': ['bigcommerce'],
        'unique_pages': ['admin']
    },
    'Volusion': {
        'meta': 'volusion',
        'scripts': ['volusion/'],
        'links': ['volusion/'],
        'classes': ['volusion'],
        'unique_pages': ['admin']
    },
    '3dcart': {
        'meta': '3dcart',
        'scripts': ['3dcart/'],
        'links': ['3dcart/'],
        'classes': ['3dcart'],
        'unique_pages': ['admin']
    },
    'GoDaddy Website Builder': {
        'meta': 'godaddy',
        'scripts': ['godaddy/'],
        'links': ['godaddy/'],
        'classes': ['godaddy'],
        'unique_pages': ['admin']
    },
    'Jimdo': {
        'meta': 'jimdo',
        'scripts': ['jimdo/'],
        'links': ['jimdo/'],
        'classes': ['jimdo'],
        'unique_pages': ['admin']
    },
    'Adobe Commerce': {
        'meta': 'adobe-commerce',
        'scripts': ['adobe-commerce/'],
        'links': ['adobe-commerce/'],
        'classes': ['adobe-commerce'],
        'unique_pages': ['admin']
    },
    'Adobe Experience Manager': {
        'meta': "Adobe CQ",
        'scripts': ['etc.clientlibs', 'cq.wcm.foundation', 'granite/ui'],
        'links': ['etc.clientlibs', 'etc/designs'],
        'classes': ['aem', 'cq'],
        'unique_pages': ['content/dam', 'content/experience-fragments', 'libs/granite/core/content/login.html']
        },
    'Zen Cart': {
        'meta': 'zencart',
        'scripts': ['zencart/'],
        'links': ['zencart/'],
        'classes': ['zencart'],
        'unique_pages': ['admin']
    },
    'X-Cart': {
        'meta': 'xcart',
        'scripts': ['xcart/'],
        'links': ['xcart/'],
        'classes': ['xcart'],
        'unique_pages': ['admin']
    },
    'Shopware': {
        'meta': 'shopware',
        'scripts': ['shopware/'],
        'links': ['shopware/'],
        'classes': ['shopware'],
        'unique_pages': ['admin']
    },
    'Lithium': {
        'meta': 'lithium',
        'scripts': ['lithium.js', '/lithium/'],
        'links': ['/lithium/'],
        'classes': ['lithium'],
        'unique_pages': ['li-community-page', 't5/']
    },
    'CS-Cart': {
        'meta': 'cscart',
        'scripts': ['cscart/'],
        'links': ['cscart/'],
        'classes': ['cscart'],
        'unique_pages': ['admin']
    },
    'TomatoCart': {
        'meta': 'tomatocart',
        'scripts': ['tomatocart/'],
        'links': ['tomatocart/'],
        'classes': ['tomatocart'],
        'unique_pages': ['admin']
    },
    'VirtueMart': {
        'meta': 'virtuemart',
        'scripts': ['virtuemart/'],
        'links': ['virtuemart/'],
        'classes': ['virtuemart'],
        'unique_pages': ['admin']
    },
    'Spree Commerce': {
        'meta': 'spree',
        'scripts': ['spree/'],
        'links': ['spree/'],
        'classes': ['spree'],
        'unique_pages': ['admin']
    },
    'CMS Made Simple': {
        'meta': 'cmsmadesimple',
        'scripts': ['cmsmadesimple/'],
        'links': ['cmsmadesimple/'],
        'classes': ['cmsmadesimple'],
        'unique_pages': ['admin']
    },
    'SilverStripe': {
        'meta': 'silverstripe',
        'scripts': ['silverstripe/'],
        'links': ['silverstripe/'],
        'classes': ['silverstripe'],
        'unique_pages': ['admin']
    }
}
