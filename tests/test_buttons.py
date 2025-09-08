from playwright.sync_api import Page, expect
from pages.buttons_page import ButtonPage

#Count all buttons found on the page
def test_count_buttons(page: Page):
    run = ButtonPage(page)
    run.load_page()
    run.count_button()
    
#Test web element button
def test_web_element_buttons(page: Page):
    run = ButtonPage(page)
    run.load_page()
    run.web_element_buttons
    
#Test button with javascript handler
def test_javascript_click(page: Page):
    run = ButtonPage(page)
    run.load_page()
    run.javascript_click()
    
#Test action move and click button
def test_action_move_click(page: Page):
    run = ButtonPage(page)
    run.load_page()
    run.action_move_and_click()
    
#Validate disabled button
def test_disabled_button(page: Page):
    run = ButtonPage(page)
    run.load_page()
    run.disabled_button()    