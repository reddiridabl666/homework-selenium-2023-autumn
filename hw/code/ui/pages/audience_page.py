from ui.pages.hq_page import HqPage
from ui.locators import basic_locators


def keywords_payload(name='Название', keywords='образование', days='15'):
    return {
        'name': name,
        'keywords': keywords,
        'days': days
    }


class AudiencePage(HqPage):
    url = 'https://ads.vk.com/hq/audience'
    locators = basic_locators.AudiencePageLocators

    KEYWORDS = 'Ключевые фразы'
    OTHER_AUDIENCE = 'Существующая аудитория'

    def create_audience(self, name, source=KEYWORDS, data={}):
        self.is_not_visible(self.locators.AUDIENCE_CREATION_MODAL)
        self.set_audience_name(name)
        self.add_source(source, data)
        self.save_audience()

    def save_audience(self):
        self.is_not_visible(self.locators.SOURCE_CREATION_MODAL)
        self.click(self.locators.SAVE_AUDIENCE)

    def add_source(self, source=KEYWORDS, data={}):
        self.is_not_visible(self.locators.SOURCE_CREATION_MODAL)

        self.click(self.locators.BY_TEXT('Добавить источник'))
        self.click(self.locators.BY_TEXT(source))

        if (source == self.KEYWORDS):
            self.add_keywords(data)

        if (source == self.OTHER_AUDIENCE):
            self.add_other_audience(data)

        self.click(self.locators.SAVE_SOURCE)

    def delete_audience(self, name):
        menu = self.locators.AUDIENCE_DETAILS(name)
        self.hover(menu)
        self.click(menu)
        self.click(self.locators.BY_TEXT('Удалить'))
        self.click(self.locators.BY_TEXT('Удалить'))

    def open_edit_modal(self, name):
        menu = self.locators.AUDIENCE_DETAILS(name)
        self.hover(menu)
        self.click(menu)
        self.click(self.locators.BY_TEXT('Редактировать'))

    def set_audience_name(self, name):
        self.click(self.locators.CREATE_AUDIENCE)
        self.fill_in(self.locators.AUDIENCE_NAME, name)

    def add_keywords(self, data):
        self.fill_in(self.locators.SOURCE_NAME, data['name'])
        self.fill_in(self.locators.KEYWORDS, data['keywords'])

        self.clear(self.locators.DAYS_INPUT)
        self.fill_in(self.locators.DAYS_INPUT, data['days'])

    def add_other_audience(self, data):
        self.click(self.locators.AUDIENCE_SELECT)
        self.click(self.locators.AUDIENCE_SELECT_ITEM(data))

    def has_long_name_error(self):
        self.has_error(self.locators.AUDIENCE_NAME,
                       'Максимальная длина 255 символов')

    def get_source(self, id, type='keyword'):
        source = self.find(self.locators.AUDIENCE_SOURCE(id))
        name = self.find_from(source, self.locators.AUDIENCE_SOURCE_NAME)
        items = self.find_multiple_from(
            source, self.locators.AUDIENCE_SOURCE_ITEM)
        if type == 'keyword':
            return keywords_payload(name=name.text, keywords=items[0].text, days=items[1].text.split(' ')[0])

    def get_rule(self):
        return self.find(self.locators.RULE).text.lower()

    def set_rule(self, rule):
        self.is_not_visible(self.locators.SOURCE_CREATION_MODAL)

        self.click(self.locators.RULE_SELECTOR)
        if rule == 'или':
            self.click(self.locators.BY_TEXT('хотя бы одному из условий'))
        elif rule == 'и':
            self.click(self.locators.BY_TEXT('всем условиям'))
        elif rule == 'не':
            self.click(self.locators.BY_TEXT('ни одному из условий'))

    def filter_audiences(self, shown=[KEYWORDS]):
        self.is_not_visible(self.locators.AUDIENCE_CREATION_MODAL)

        self.click(self.locators.BY_TEXT('Фильтр'))
        self.click(self.locators.BY_TEXT('Выбрать все'))
        self.click(self.locators.BY_TEXT('Снять выделение'))

        for item in shown:
            print(f'Clicking {item}')
            self.click(self.locators.AUDIENCE_FILTER_VALUE(item))

        self.click(self.locators.BY_TEXT('Применить'))

    def get_audience_names(self):
        elems = self.find_multiple(self.locators.SHOWN_AUDIENCES)
        return [elem.text for elem in elems]
