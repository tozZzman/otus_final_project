from pages.user_page import BasePage
from pages.locators import HomePageLocators, BasePageLocators
import allure


@allure.title('Добавление товара в корзину из меню по ховеру')
def test_add_product_to_cart(browser, url, removing_products_from_the_sidebar):
    client = BasePage(browser)
    client.open(url)
    client.add_items_from_the_menu_by_hover(*HomePageLocators.PRODUCT_SOFA)
    client.click_to_element(*BasePageLocators.BASKET)
    assert client.get_value(*BasePageLocators.PRODUCT_BASKET, attribute='alt') == 'Диван Iceberg', \
        'Неверное название товара добавленного в корзину'


@allure.title('Очистка корзины')
def test_emptying_the_basket(browser, add_product_to_cart):
    client = BasePage(browser)
    client.click_to_element(*BasePageLocators.BASKET)
    client.click_to_element(*BasePageLocators.REMOVE_BASKET)
    client.waiting_for_element_not_present(*BasePageLocators.PRODUCT_BASKET)


@allure.title('Добавление товара в избранное из меню по ховеру')
def test_add_item_to_favorites(browser, url, removing_products_from_the_sidebar):
    client = BasePage(browser)
    client.open(url)
    client.add_items_from_the_menu_by_hover(*HomePageLocators.PRODUCT_LITTLE_TABLE)
    client.click_to_element(*BasePageLocators.FAVORITES)
    client.click_to_element(*BasePageLocators.HEADER_TABS_FAVORITES)
    assert client.get_value(*BasePageLocators.PRODUCT_FAVORITES, attribute='alt') == \
           'Комплект журнальных столиков Twinz', 'Неверное название товара добавленного в избранное'


@allure.title('Добавление товара в сравнение из меню по ховеру')
def test_add_product_to_comparison(browser, url):
    client = BasePage(browser)
    client.open(url)
    client.add_items_from_the_menu_by_hover(*HomePageLocators.PRODUCT_KITCHEN)
    client.click_to_element(*BasePageLocators.COMPARISON)
    assert client.get_value(*BasePageLocators.PRODUCT_COMPARISON, attribute='alt') == 'Модульная кухня Zermann', \
        'Неверное название товара добавленного в сравнение'
    client.click_to_element(*BasePageLocators.REMOVE_PRODUCT_COMPARISON)
