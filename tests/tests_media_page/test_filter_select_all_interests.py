import time

import allure
from model.pages.search_sber_page import SberSearchPage
from selene import browser, have


@allure.tag('web')
@allure.feature("Отмечаем все пункты фильтра интересов")
@allure.story("Проверка выдачи результатов")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки работы фильтра")
@allure.link("https://rabota.sber.ru", name="Testing")
def test_search_information(open_sber_url):
    search = SberSearchPage()

    with allure.step('Открывает сайт https://rabota.sber.ru'):
        search.open()

    with allure.step('Переходим на вкладку "Карьерные медиа"'):
        search.switch_page('Карьерные медиа')

    with allure.step('Полностью заполняем фильтр интересов'):
        search.fill_filter('all')

        with allure.step('Проверяем количество отмеченных фильтров'):
            assert browser.element('.gqakuA').should(have.text('17')), 'Должно быть 17 фильтров'

    with allure.step('Проверяем результаты поиска'):
        search.should_search_text('Нет результатов')

    with allure.step('Полностью очищаем фильтр интересов'):
        search.fill_filter('clear')
        time.sleep(2)

        with allure.step('Проверяем, что фильтры отчистились'):
            assert len(browser.all('.SKAwE')) > 0, 'Фильтры не отчистились'
