import time
import allure

from model.pages.search_sber_page import SberSearchPage


@allure.tag('web')
@allure.feature("Поиск вакансии QA на python")
@allure.story("Проверка выдачи результатов")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки ввода данных и поиска")
@allure.link("https://rabota.sber.ru", name="Testing")
def test_search_python_vacancy():
    search = SberSearchPage()

    with allure.step('Открывает сайт "https://rabota.sber.ru"'):
        search.open()

    with allure.step('Вводим в строку поиска интересующий язык программирования'):
        search.fill_language_in_search('Python')
        time.sleep(2)

    if search.count_vacancy() > 0:

        with allure.step('Выбираем город Санкт-Петербург и Москва'):
            search.fill_city('Санкт-Петербург')
            search.fill_city('Москва')

        with allure.step('Выбираем профессиональную область IT: Тестирование (QA)'):
            search.fill_professional_area('IT: Тестирование (QA)')

        with allure.step('Проверяем количество выданных вакансий'):
            search.should_number_vacancies()

        with allure.step('Проверяем наличие результатов QA'):
            search.should_search_text('QA')

        print(f'Найдено {search.count_vacancy()} вакансий')

    else:
        with allure.step('Проверяем, что вакансий не найдено'):
            search.should_number_vacancies()

        print('Вакансий не найдено')
