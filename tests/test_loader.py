from playwright.sync_api import Page
from pages.loader_page import LoaderPage

def test_loader(page: Page):
    run = LoaderPage(page)
    run.load_page()
    run.loader()