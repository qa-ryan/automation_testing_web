from playwright.sync_api import Page, expect
from pages.actions_page import ActionsPage

def load_page(page: Page):
    url = ActionsPage(page)
    url.goto()

#Drag and Drop
def test_drag_and_drop(page: Page):
    load_page(page)
    print("\n")
    run = ActionsPage(page)
    run.drag_and_drop()
    
#Click and Hold
def test_click_and_hold(page: Page):
    load_page(page)
    print("\n")
    run = ActionsPage(page)
    run.click_and_hold()
    
#Double click
def test_double_click(page: Page):
    load_page(page)
    print("\n")
    run = ActionsPage(page)
    run.double_click()
    
#Hold Shfit and Click
def test_hold_shift_and_click(page: Page):    
    load_page(page)
    print("\n")
    run = ActionsPage(page)
    run.hold_and_shift()
    