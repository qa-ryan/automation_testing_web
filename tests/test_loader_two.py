from playwright.sync_api import Page, expect
from pages.loader_two_page import LoaderTwoPage

def test_loader_two(page: Page):
    run = LoaderTwoPage(page)
    run.load_page()
    run.loader_two()