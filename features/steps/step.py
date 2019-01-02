from behave import *

use_step_matcher("re")


@when("on the login page")
def step_impl(self):
    from features.steps.function import on_the_login_page
    on_the_login_page()


@then("display the (?P<element>.+)")
def step_impl(self, element):
    from features.steps.function import display_the_element
    display_the_element(element)


@then("the (?P<element>.+) is displayed correctly")
def step_impl(self, element):
    from features.steps.function import the_element_is_displayed_correctly
    the_element_is_displayed_correctly(element)


@when("after loading the login page")
def step_impl(self):
    from features.steps.function import after_loading_the_login_page
    after_loading_the_login_page()


@then("cursor is focusing on 'USERNAME' textbox")
def step_impl(self):
    from features.steps.function import cursor_is_focusing_on_username_textbox
    cursor_is_focusing_on_username_textbox()


@given("on the login page")
def step_impl(self):
    from features.steps.function import on_the_login_page
    on_the_login_page()


@when("typing '12345678901234567890' into (?P<element>.+) textbox")
def step_impl(self, element):
    from features.steps.function import typing_12345678901234567890_into_element_textbox
    typing_12345678901234567890_into_element_textbox(element)


@then("can type '12345678901234567890' into (?P<element>.+) textbox")
def step_impl(self, element):
    from features.steps.function import can_type_12345678901234567890_into_element_textbox
    can_type_12345678901234567890_into_element_textbox(element)


@when("typing '123456789012345678901' into (?P<element>.+) textbox")
def step_impl(self, element):
    from features.steps.function import typing_123456789012345678901_into_element_textbox
    typing_123456789012345678901_into_element_textbox(element)


@then("can only type '12345678901234567890' into (?P<element>.+) textbox")
def step_impl(self, element):
    from features.steps.function import can_only_type_12345678901234567890_into_element_textbox
    can_only_type_12345678901234567890_into_element_textbox(element)


@given("cursor is focused on (?P<element>.+)")
def step_impl(self, element):
    from features.steps.function import cursor_is_focused_on_element
    cursor_is_focused_on_element(element)


@when("press the 'Tab' key on the keyboard")
def step_impl(self):
    from features.steps.function import press_the_Tab_key_on_the_keyboard
    press_the_Tab_key_on_the_keyboard()

@then("move the focused elements to (?P<next>.+)")
def step_impl(self, next):
    from features.steps.function import move_the_focused_elements_to_next
    move_the_focused_elements_to_next(next)


@when("pressed the 'Enter' key on the keyboard")
def step_impl(self):
    from features.steps.function import pressed_the_Enter_key_on_the_keyboard
    pressed_the_Enter_key_on_the_keyboard()


@then("performing login")
def step_impl(self):
    from features.steps.function import performing_login
    performing_login()


