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
    ADD_SOURCE = 'Добавить источник'
    DELETE = 'Удалить'
    EDIT = 'Редактировать'
    MAX_LENGTH_ERROR = 'Максимальная длина 255 символов'
    APPLY = 'Применить'

    OR = 'или'
    AND = 'и'
    NO = 'не'

    AT_LEAST_ONE_CONDITION = 'хотя бы одному из условий'
    ALL_CONDITIONS = 'всем условиям'
    NO_CONDITIONS = 'ни одному из условий'

    FILTER = 'Фильтр'
    CHOOSE_ALL = 'Выбрать все'
    DESELECT_ALL = 'Снять выделение'

    def create_audience(self, name, source=KEYWORDS, data={}):
        self.is_not_visible(self.locators.AUDIENCE_CREATION_MODAL)
        self.set_audience_name(name)
        self.add_source(source, data)
        self.save_audience()

    def save_audience(self):
        if not self.is_not_visible(self.locators.SOURCE_CREATION_MODAL):
            return False

        self.click(self.locators.SAVE_AUDIENCE)
        return True

    def add_source(self, source=KEYWORDS, data={}):
        self.is_not_visible(self.locators.SOURCE_CREATION_MODAL)

        self.click(self.locators.BY_TEXT(self.ADD_SOURCE))
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
        self.click(self.locators.BY_TEXT(self.DELETE))
        self.click(self.locators.BY_TEXT(self.DELETE))

    def open_edit_modal(self, name):
        menu = self.locators.AUDIENCE_DETAILS(name)
        self.hover(menu)
        self.click(menu)
        self.click(self.locators.BY_TEXT(self.EDIT))

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

    def long_name_error(self):
        return self.form_error(self.locators.AUDIENCE_NAME, self.MAX_LENGTH_ERROR)

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
        if rule == self.OR:
            self.click(self.locators.BY_TEXT(self.AT_LEAST_ONE_CONDITION))
        elif rule == self.AND:
            self.click(self.locators.BY_TEXT(self.ALL_CONDITIONS))
        elif rule == self.NO:
            self.click(self.locators.BY_TEXT(self.NO_CONDITIONS))

    def filter_audiences(self, shown=[KEYWORDS]):
        self.is_not_visible(self.locators.AUDIENCE_CREATION_MODAL)

        self.click(self.locators.BY_TEXT(self.FILTER))
        self.click(self.locators.BY_TEXT(self.CHOOSE_ALL))
        self.click(self.locators.BY_TEXT(self.DESELECT_ALL))

        for item in shown:
            self.click(self.locators.AUDIENCE_FILTER_VALUE(item))

        self.click(self.locators.BY_TEXT(self.APPLY))

    def get_audience_names(self):
        elems = self.find_multiple(self.locators.SHOWN_AUDIENCES)
        return [elem.text for elem in elems]

    def creation_modal_closed(self):
        return self.is_not_visible(self.locators.AUDIENCE_CREATION_MODAL)
