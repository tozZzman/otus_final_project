from pages.living_room_page import LivingRoom
from pages.locators import LivingRoomPageLocators
import allure
import pytest


@allure.title('Фильтрация товаров по цене')
@pytest.mark.parametrize('min_price, max_price', ((0, 0),
                                                  (999999, 999999),
                                                  (0, 999999),
                                                  (0, 12390),
                                                  (20000, 42690))
                         )
def test_filtration_products_by_price(browser, url, min_price, max_price):
    client = LivingRoom(browser)
    client.open(url)
    client.go_to_living_room_walls()
    client.enter_text(*LivingRoomPageLocators.FILTER_MIN_PRICE, text=min_price)
    client.enter_text(*LivingRoomPageLocators.FILTER_MAX_PRICE, text=max_price)
    price_list = client.get_list_goods_by_price()
    if price_list == [] and min_price == max_price:
        return
    for price in price_list:
        assert min_price <= price <= max_price,  'Цена товара не удовлетворяет результатам фильтрации'


@allure.title('Фильтрация товаров по предложениям')
def test_filtration_products_by_offers_advise(browser, url):
    client = LivingRoom(browser)
    client.open(url)
    client.go_to_living_room_walls()
    client.click_to_element(*LivingRoomPageLocators.CHECKBOX_ADVISE)
    client.check_sticker_display_advise()
