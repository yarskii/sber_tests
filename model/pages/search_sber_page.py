from selene import browser, be, by, have
from selene.core.exceptions import TimeoutException


class SberSearchPage:
    def open(self):
        browser.open()

        if browser.element('.hVnStJ').should(be.visible):
            browser.element('.hVnStJ').should(be.visible).element(by.text('Хорошо')).click()

    def switch_page(self, page):
        browser.element('.gOPfAc').should(be.visible).element(by.text(page)).click()

    def fill_language_in_search(self, language):
        browser.element('.crUkSt').should(be.visible).type(language).press_enter()

    def count_vacancy(self):
        return len(browser.all('.sc-bdvvtL>.fmUtEX'))

    def fill_city(self, city):
        browser.element('.bANYmh').should(be.visible).type(city)
        browser.element('.ftDrAW').should(be.visible).element(by.text(f'г {city}')).click()

    def fill_professional_area(self, area):
        browser.element('.bSXks').should(be.visible).click()

        if area == 'all':
            for element in browser.all('.hvRHtH'):
                element.click()
        else:
            browser.element('.fUuyoW').should(be.visible).element(by.text(area)).click()

    def should_number_vacancies(self):
        if self.count_vacancy() > 0:
            browser.element('.gNzDRP').should(be.visible).should(have.text(
                f'Найдено вакансий: {self.count_vacancy()}'))
        else:
            browser.element('.hePNzJ').should(be.visible).should(have.text('Ничего не нашлось'))

    def fill_filter(self, interests):
        if interests == 'all':
            browser.element('.btitRc').click()
            for element in browser.all('.hvRHtH'):
                element.click()
            browser.element('.hynlfB').click()

        elif interests == 'clear':
            browser.element('.gqakuA').click()
            browser.element('.bJHLon').should(be.visible).element(by.text('Сбросить все')).click()

        else:
            browser.element('.btitRc').click()
            for interest in interests:
                browser.element('.bRwUWm').should(be.visible).element(by.text(interest)).click()
            browser.element('.hynlfB').click()

    def should_search_text(self, text):
        try:
            browser.element('.hePNzJ').should(be.visible).should(have.text(text))
        except TimeoutException:
            browser.element('.dxlUbY').should(be.visible).should(have.text(text))

    def social_button(self, link):
        footer = browser.element('.lfGoOI')
        telegram_button = footer.element(f'a[href="{link}"]')
        telegram_button.should(be.visible)
        telegram_button.should(be.clickable).click()

    def should_new_link(self, link):
        browser.should(have.url_containing(f'{link}'))
        browser.close_current_tab()
