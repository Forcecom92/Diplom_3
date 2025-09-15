import allure
from pages.base_page import BasePage
from locators import main_functions_locators as mfl
from seletools.actions import drag_and_drop


class MainFunctions(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(mfl.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по ингредиенту"')
    def click_ingredient(self):
        self.click(mfl.INGREDIENT)

    @allure.step('Ищем заголовок всплывающего окна')
    def wait_and_find_header(self):
        name = self.wait_and_find_element(mfl.POPUP_WINDOW_HEADER)
        return name

    @allure.step('Кликаем по крестику, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click(mfl.CLOSE_BUTTON)

    @allure.step('Находим невидимый крестик для закрытия окна')
    def cross_not_is_displayed(self):
        name = self.wait_and_find_element_invisible(mfl.CLOSE_BUTTON)
        return not name.is_displayed()

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(mfl.INGREDIENT)
        basket = self.wait_and_find_element(mfl.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Ищем текст по локатору ингредиента')
    def counter_ingredient_text(self):
        return self.find_text(mfl.INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(mfl.BUTTON_MAKE_ORDER)

    @allure.step('Ищем текст о подтверждении заказа')
    def wait_and_find_confirmation(self):
        name = self.wait_and_find_element(mfl.CONFIRMATION_TEXT)
        return name

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(mfl.BUTTON_ENTER)

    @allure.step('Завершить логин пользователя и оформить заказ')
    def finish_login_and_make_order(self):
        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()
