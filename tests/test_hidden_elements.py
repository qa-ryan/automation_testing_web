from playwright.sync_api import Page, expect
from pages.hidden_elements_page import HiddenElementsPage

def test_hidden_elements(page: Page):
    run = HiddenElementsPage(page)
    run.load_page()
    run.hidden_elements()