import allure
from model.pages.search_sber_page import SberSearchPage

interests = ['Статья', 'Личный опыт', 'Личное развитие', 'Карьера в Сбере', 'Люди']


@allure.tag('web')
@allure.feature("Поиск информации")
@allure.story("Проверка выдачи результатов")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки поиска статьи")
@allure.link("https://rabota.sber.ru", name="Testing")
def test_search_information(open_sber_url):
    search = SberSearchPage()

    with allure.step('Открывает сайт https://rabota.sber.ru'):
        search.open()

    with allure.step('Переходим на вкладку "Карьерные медиа"'):
        search.switch_page('Карьерные медиа')

    with allure.step('Заполняем фильтр интересов'):
        search.fill_filter(interests)

    with allure.step('Проверяем результаты поиска'):
        search.should_search_text('Перезапуск в Сбере: как сменить профессию и стать IT-специалистом')
