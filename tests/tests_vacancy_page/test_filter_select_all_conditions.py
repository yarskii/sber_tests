import allure
from selene import browser
from model.pages.search_sber_page import SberSearchPage


@allure.tag('web')
@allure.feature("Отмечаем все пункты фильтрации вакансий")
@allure.story("Проверяем количество отмеченных позиций")
@allure.label("owner", "Ярослав Гусев")
@allure.link("https://rabota.sber.ru", name="Testing")
def test_choice_conditions():
    search = SberSearchPage()

    with allure.step('Открывает сайт "https://rabota.sber.ru"'):
        search.open()

    with allure.step('Переходим на вкладку "Вакансии"'):
        search.switch_page('Вакансии')

    with allure.step('Выбираем все'):
        search.fill_professional_area('all')

    with allure.step('Проверяем количество выбранных позиций'):
        assert len(browser.all('.ePIYCB')) == 44, f'Выбранных позиций должно быть 44'
