import os

from base.base import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.pharmacosmetica.ru/'
        super().__init__(browser, url)

# локаторы для шапки сайта

    LOGO_BUTTON = ('css', '[title="logo"]')
    ALL_HEADERS_CENTRAL_MENU = ('css', 'li[class^=" dropdown"]')
    GUEST_BUTTON = ('css', '.dropdown-click')
    BASKET_BUTTON = ('xpath', '//*[@id="basket-desktop-block"]')
    NUMBER_IN_BASKET = ('xpath', '//*[@id="basket-desktop-block"]/span[1]/b')

# локаторы для всплывающего меню авторизации

    INPUT_BUTTON = ('css', 'div[class="col-sm-12"]>button')
    INPUT_EMAIL = ('xpath', '//*[@id="inputLogin3"]')
    INPUT_PASS = ('xpath', '//*[@id="inputPassword3"]')
    REGISRATION_BUTTON = ('xpath', '//ul[@class="dropdown-menu"]/li/a[text()="Регистрация"]')

# локаторы для строки поиска

    SEARCH_STRING = ('xpath', '//div[@id="search-3"]//input')
    SEARCH_BUTTON = ('xpath', '//*[@id="go33"]')
    SEARCH_PAGE_ITEMS = ('css', 'div[class="digi-product"]')
    SEARCH_PAGE_SORT_MENU_CATEGORIES_HEADER = ('xpath', '//div[@class="digi-facet__header"]')
    SEARCH_PAGE_SORT_PAGE_PRICE = ('xpath', '//span[@class="digi-product-price-variant digi-product-price-variant_actual"]')
    SEARCH_PAGE_SORT_BLOCK_PRICE = ("xpath", '//span[@class="multiselect__single"]')
    SEARCH_PAGE_SORT_BLOCK_LOW_PRICE = ('xpath', '//li[@class="multiselect__element"][2]//span//span')
    SEARCH_PAGE_SORT_MENU_FOR_HAIR = ('xpath', '//button[@class="digi-facet-category"]//span[text()="Для волос"]')
    SEARCH_PAGE_SORT_MENU_FOR_HAIR_AMOUNT = ('xpath', '//ul/li[6]/button/span[2]')
    SEARCH_PAGE_SORT_MENU_FOR_CHILDREN_AMOUNT = ('xpath', '//ul/li[5]/button/span[2]')


# локаторы для центральной части

    CENTRAL_MENU_HEADER_BRANDS = ('xpath', '//li[@class=" dropdown yamm-fw"][1]')
    CENTRAL_MENU_HEADER_BRANDS_POP_UP_STRING = ('xpath', '//a[@class="ancLinks"]')
    All_CATEGORIES_BUTTON = ('xpath', '//li[@class="active dropdown yamm-fw"]')
    All_LINKS_NAV_MENU_BRANDS = ('css', 'div[data-vsp="vsp1"]')
    LEFT_MENU_LINK_FOR_FACE = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[1]')
    LEFT_MENU_LINK_FOR_HAIR = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[2]')
    LEFT_MENU_LINK_NEW_COLOR = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[3]')
    LEFT_MENU_LINK_SUN = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[4]')
    LEFT_MENU_LINK_FOR_BODY = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[5]')
    LEFT_MENU_LINK_FOR_CHILD = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[6]')
    LEFT_MENU_LINK_FOR_TEETH = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[7]')
    LEFT_MENU_LINK_FOR_HEALTH = ('xpath', '(//ul[@class="submenu dropdown-menu submenu-left"]/li)[8]')
    All_CATEGORIES_POP_UP_MENU = ('css', '.col-md-4')
    CENTRAL_TAB_MENU_BESTSELLERS = ('xpath', '//*[@id="rrDefaultTabPers"]/span')
    CENTRAL_TAB_MENU_SALE = ('xpath', '//a[@class="rr-tabLink rr-tab__popularSale"]')
    CENTRAL_TAB_MENU_NEW = ('xpath', '//a[@class="rr-tabLink rr-tab__categoryLatest"]')

# подвал сайта

    FOOTER_PAGE_YANDEX = ('xpath', '//div[@class="ft_ya_reviews"]')
    FOOTER_PAGE_ABOUT_SHOP = ('css', 'div[class="col-md-3 col-sm-6 col-xs-6 footerlogos"]')
    FOOTER_PAGE_FOR_USERS = ('css', 'div[class="col-md-3 col-sm-6 col-xs-6"]')
    FOOTER_PAGE_CONTACTS = ('css', 'div[class="col-md-3 hidden-sm hidden-xs"]')
    FOOTER_LINK_ABOUT = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[1]/a')
    FOOTER_LINK_TEN_REASONS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[2]/a')
    FOOTER_LINK_FIVE_METHODS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[3]/a')
    FOOTER_LINK_CORPORATIV = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[4]/a')
    FOOTER_LINK_OFERTA= ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[5]/a')
    FOOTER_LINK_POLITICS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[6]/a')
    FOOTER_LINK_CONTACTS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6 footerlogos"]/p[7]/a')
    FOOTER_LINK_REGISTRATION = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[1]/a')
    FOOTER_LINK_DELIVERY = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[2]/a')
    FOOTER_LINK_REVIEWS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[3]/a')
    FOOTER_LINK_RETURN = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[4]/a')
    FOOTER_LINK_CONSULTATION = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[5]/a')
    FOOTER_LINK_POINTS = ('xpath', '//div[@class="col-md-3 col-sm-6 col-xs-6"]/p[6]/a')
    FOOTER_LINK_GOOGLE_APP = ('css', '[title="googlepay"]')
    FOOTER_LINK_APPSTORE = ('css', '[title="apple"]')


