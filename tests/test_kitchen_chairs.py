from pages.kitchen_page import KitchenPage
from pages.locators import KitchenPageLocators
import allure


@allure.label('testType', 'screenshotDiff')
@allure.title('Проверка отображения большого списка товаров')
def test_large_list_display(request, browser, url):
    client = KitchenPage(browser)
    client.open(url)
    client.go_to_kitchen_section_chairs()
    image = client.create_screenshot_element(request, locator=KitchenPageLocators.KITCHEN_BLOCK)
    client.reconciliation_with_images(request, image_path=image)


@allure.label('testType', 'screenshotDiff')
@allure.title('Проверка отображения маленького списка товаров')
def test_small_list_display(request, browser, url):
    client = KitchenPage(browser)
    client.open(url)
    client.go_to_kitchen_section_chairs()
    client.click_to_element(*KitchenPageLocators.ICON_SMALL_LIST)
    image = client.create_screenshot_element(request, locator=KitchenPageLocators.KITCHEN_BLOCK)
    client.reconciliation_with_images(request, image_path=image)


@allure.title('Проверка отображения иконок товара по ховеру')
def test_display_of_icons_and_buttons_of_the_product_card(browser, url):
    client = KitchenPage(browser)
    client.open(url)
    client.go_to_kitchen_section_chairs()
    client.check_product_icons(product_id=KitchenPageLocators.ID_PRODUCT_1)
    client.check_product_icons(product_id=KitchenPageLocators.ID_PRODUCT_2)
    client.check_product_icons(product_id=KitchenPageLocators.ID_PRODUCT_3)
    client.check_product_icons(product_id=KitchenPageLocators.ID_PRODUCT_4)
