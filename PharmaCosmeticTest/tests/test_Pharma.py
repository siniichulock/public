# pytest -v test_Pharma.py
import pytest

from config import *

from base.mainPage import MainPage


def test_logo_button_is_visible(go_browser):
    page = MainPage(go_browser)
    assert page.is_visible(*MainPage.LOGO_BUTTON)


def test_logo_link(go_browser):
    page = MainPage(go_browser)
    page.open_link(*MainPage.LOGO_BUTTON)
    assert page.get_current_url() == url


def test_search(go_browser):
    page = MainPage(go_browser)
    page.search_page_open(text_for_search, *MainPage.SEARCH_STRING, *MainPage.SEARCH_BUTTON)
    assert len(page.are_present(*MainPage.SEARCH_PAGE_ITEMS)) > 0


def test_search_page_sort_menu_headers(go_browser):
    page = MainPage(go_browser)
    page.search_page_open(text_for_search, *MainPage.SEARCH_STRING, *MainPage.SEARCH_BUTTON)
    actual_headers = page.get_list_of_elements_text(*MainPage.SEARCH_PAGE_SORT_MENU_CATEGORIES_HEADER)
    assert actual_headers == expected_headers_sort_menu


def test_search_page_valid_amount_in_sort_menu(go_browser):
    page = MainPage(go_browser)
    page.search_page_open(text_for_search, *MainPage.SEARCH_STRING, *MainPage.SEARCH_BUTTON)
    amount = int(page.get_text(*MainPage.SEARCH_PAGE_SORT_MENU_FOR_HAIR_AMOUNT))
    page.open_link(*MainPage.SEARCH_PAGE_SORT_MENU_FOR_HAIR)
    assert amount == len(page.are_present(*MainPage.SEARCH_PAGE_ITEMS))


@pytest.mark.xfail(reason="AssertionError")
def test_search_page_invalid_amount_in_sort_menu(go_browser):
    page = MainPage(go_browser)
    page.search_page_open(text_for_search, *MainPage.SEARCH_STRING, *MainPage.SEARCH_BUTTON)
    amount = int(page.get_text(*MainPage.SEARCH_PAGE_SORT_MENU_FOR_CHILDREN_AMOUNT))
    page.open_link(*MainPage.SEARCH_PAGE_SORT_MENU_FOR_HAIR)
    assert amount == len(page.are_present(*MainPage.SEARCH_PAGE_ITEMS))


def test_search_page_sort_by_price(go_browser):
    page = MainPage(go_browser)
    page.search_page_open(text_for_search, *MainPage.SEARCH_STRING, *MainPage.SEARCH_BUTTON)
    page.open_link(*MainPage.SEARCH_PAGE_SORT_MENU_FOR_HAIR)
    page.open_link(*MainPage.SEARCH_PAGE_SORT_BLOCK_PRICE)
    page.open_link(*MainPage.SEARCH_PAGE_SORT_BLOCK_LOW_PRICE)
    all_price = page.are_present(*MainPage.SEARCH_PAGE_SORT_PAGE_PRICE)
    all_price_list = page.get_text_from_elements(all_price)
    all_prices = [float(p.replace(' ', '')) for p in all_price_list[:5]]
    assert all_prices == sorted(all_prices)


def test_headers_central_menu_are_visible(go_browser):
    page = MainPage(go_browser)
    assert page.are_visible(*MainPage.ALL_HEADERS_CENTRAL_MENU)


def test_list_headers_central_menu(go_browser):
    page = MainPage(go_browser)
    actual_headers = page.get_list_of_elements_text(*MainPage.ALL_HEADERS_CENTRAL_MENU)
    assert actual_headers == expected_headers


def test_open_all_categories_pop_up_menu(go_browser):
    page = MainPage(go_browser)
    page.open_link(*MainPage.All_CATEGORIES_BUTTON)
    assert page.is_visible(*MainPage.All_CATEGORIES_POP_UP_MENU)


def test_invisible_all_categories_pop_up_menu_without_click(go_browser):
    page = MainPage(go_browser)
    assert page.is_not_present(*MainPage.All_CATEGORIES_POP_UP_MENU)


def test_button_basket_link(go_browser):
    page = MainPage(go_browser)
    page.open_link(*MainPage.BASKET_BUTTON)
    assert page.get_relative_link() == basket_page


def test_amount_in_basket(go_browser):
    page = MainPage(go_browser)
    assert page.get_text(*MainPage.NUMBER_IN_BASKET) == "0"


def test_guest_button_is_visible(go_browser):
    page = MainPage(go_browser)
    assert page.is_visible(*MainPage.GUEST_BUTTON)


@pytest.mark.parametrize('locator', [MainPage.INPUT_BUTTON, MainPage.INPUT_EMAIL, MainPage.INPUT_PASS,
                                     MainPage.REGISRATION_BUTTON])
def test_auth_menu_pop_up_invisible_without_click(go_browser, locator):
    page = MainPage(go_browser)
    assert page.is_not_present(*locator)


@pytest.mark.parametrize('locator', [MainPage.INPUT_BUTTON, MainPage.INPUT_EMAIL, MainPage.INPUT_PASS,
                                     MainPage.REGISRATION_BUTTON])
def test_auth_menu_pop_up_input_button_is_visible(go_browser, locator):
    page = MainPage(go_browser)
    page.open_link(*MainPage.GUEST_BUTTON)
    assert page.is_visible(*locator)


def test_elements_of_central_tab_bestsellers_is_visible(go_browser):
    page = MainPage(go_browser)
    assert page.is_visible(*MainPage.CENTRAL_TAB_MENU_BESTSELLERS)


def test_elements_of_central_tab_sale_is_visible(go_browser):
    page = MainPage(go_browser)
    assert page.is_visible(*MainPage.CENTRAL_TAB_MENU_SALE)


def test_elements_of_central_tab_new_is_visible(go_browser):
    page = MainPage(go_browser)
    assert page.is_visible(*MainPage.CENTRAL_TAB_MENU_NEW)


def test_scroll_down_page(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_PAGE_YANDEX)


def test_scroll_down_page_and_nav_menu_is_visible(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_PAGE_YANDEX) and page.are_visible(*MainPage.ALL_HEADERS_CENTRAL_MENU)


def test_footer_is_visible_about_shop(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_PAGE_ABOUT_SHOP)


def test_footer_is_visible_for_users(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_PAGE_FOR_USERS)


def test_footer_is_visible_contacts(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_PAGE_CONTACTS)


@pytest.mark.parametrize('locator, link',
                         [(MainPage.LEFT_MENU_LINK_FOR_FACE, '/eshop/uxod-za-litsom/'),
                          (MainPage.LEFT_MENU_LINK_FOR_HAIR, '/eshop/uxod-za-volosami/'),
                          (MainPage.LEFT_MENU_LINK_SUN, '/eshop/zaschita-ot-solntsa/'),
                          (MainPage.LEFT_MENU_LINK_FOR_BODY, '/eshop/uxod-za-telom/'),
                          (MainPage.LEFT_MENU_LINK_FOR_CHILD, '/eshop/mama-i-malysh/'),
                          (MainPage.LEFT_MENU_LINK_FOR_TEETH, '/eshop/uhod-za-polostyu-rta/'),
                          (MainPage.LEFT_MENU_LINK_FOR_HEALTH, '/eshop/zozh/'),
                          (MainPage.FOOTER_LINK_TEN_REASONS, '/10-prichin-pokupat-kosmetiku-u-nas.html'),
                          (MainPage.FOOTER_LINK_ABOUT, '/about.html'),
                          (MainPage.FOOTER_LINK_FIVE_METHODS, '/skidki-do-100.html'),
                          (MainPage.FOOTER_LINK_CORPORATIV, '/korporativnye-podarki.html'),
                          (MainPage.FOOTER_LINK_OFERTA, '/polzovatelskoe-soglashenie.html'),
                          (MainPage.FOOTER_LINK_POLITICS, '/politika-konfedencialnosti.html'),
                          (MainPage.FOOTER_LINK_CONTACTS, '/kontakty.html'),
                          (MainPage.FOOTER_LINK_REGISTRATION, '/customers/register.html'),
                          (MainPage.FOOTER_LINK_DELIVERY, '/courier/'),
                          (MainPage.FOOTER_LINK_REVIEWS, '/reviews/'),
                          (MainPage.FOOTER_LINK_RETURN, '/reglament-oformleniya-oplaty-i-vozvrata-zakazov.html'),
                          (MainPage.FOOTER_LINK_CONSULTATION, '/consultation/'),
                          (MainPage.FOOTER_LINK_POINTS, '/delites-svoim-mneniem-poluchayte-bally-uvelichivayte-svoyu'
                                                        '-skidku.html')
                          ])
def test_footer_link_ten_reasons(go_browser, locator, link):
    page = MainPage(go_browser)
    page.open_link_in_footer(*locator)
    assert page.get_relative_link() == link


def test_footer_google_app(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_LINK_GOOGLE_APP)


def test_footer_app_store(go_browser):
    page = MainPage(go_browser)
    page.scroll_down()
    assert page.is_visible(*MainPage.FOOTER_LINK_APPSTORE)
