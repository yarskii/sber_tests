from selene import browser
import allure

from model.pages.search_sber_page import SberSearchPage


@allure.tag('web')
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки работы кнопки Telegram")
@allure.link("https://rabota.sber.ru", name="Testing")
def test_telegram_button(open_sber_url):
    search = SberSearchPage()

    with allure.step('Открывает сайт "https://rabota.sber.ru"'):
        search.open()

    with allure.step('Находим кнопку Telegram и проверяем, что она видима и кликабельна'):
        search.social_button('https://t.me/careersber')

    with allure.step('Переключаемся на новую вкладку'):
        browser.switch_to_next_tab()

    with allure.step('Проверяем URL новой вкладки'):
        search.should_new_link('https://t.me/careersber')
