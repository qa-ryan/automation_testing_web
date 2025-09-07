from playwright.sync_api import Page, expect
from pages.buttons_page import ButtonPage
def load_page(page: Page):
    url = ButtonPage(page)
    url.goto()

#Count all buttons found on the page
def test_count_buttons(page: Page):
    load_page(page)
    print("\n")
    run = ButtonPage(page)
    run.count_button()
    
#Test web element button
def test_web_element_buttons(page: Page):
    run = ButtonPage(page)
    run.web_element_buttons
    
#Test button with javascript handler
def test_javascript_click(page: Page):
    load_page(page)
    run = ButtonPage(page)
    run.javascript_click()
    
#Test action move and click button
def test_action_move_click(page: Page):
    load_page(page)
    run = ButtonPage(page)
    run.action_move_and_click()
    
#Validate disabled button
def test_disabled_button(page: Page):
    load_page(page)
    run = ButtonPage(page)
    run.disabled_button()    