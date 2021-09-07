from pages.user_page import UserPage
from pages.locators import BasePageLocators, UserPageLocators, PersonalDataLocators
import time
import allure


@allure.title('Создание нового пользователя')
def test_create_account(browser, url):
    login = 'autotest_' + str(time.time())
    email = login + '@mail.com'
    password = 'autotest1234'
    client = UserPage(browser)
    client.open(url)
    client.click_to_element(*BasePageLocators.ENTRANCE)
    client.check_login_form()
    client.click_to_element(*UserPageLocators.REGISTRATION_BUTTON)
    client.fill_in_the_data_of_a_new_user(name=login, email=email, password=password)
    client.click_to_element(*BasePageLocators.ENTRANCE)
    client.click_to_element(*PersonalDataLocators.PERSONAL_DATA)
    assert client.get_value(*PersonalDataLocators.PERSONAL_DATA_NAME, attribute='value') == login, \
        "Неверное имя зарегестрированного пользователя"
    assert client.get_value(*PersonalDataLocators.PERSONAL_DATA_EMAIL, attribute='value') == email, \
        "Неверный email зарегестрированного пользователя"
    client.click_to_element(*PersonalDataLocators.EXIT)
