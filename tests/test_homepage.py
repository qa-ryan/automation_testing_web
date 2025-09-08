from playwright.sync_api import Page, expect
from pages.home_page import HomePage


# Get all link from the page
def test_get_all_link(page: Page):
    run = HomePage(page)
    run.load_page()
    run.get_all_link()
    


# Validate all links that were found
def test_validate_links(page: Page):
    run = HomePage(page)
    run.load_page()
    run.validate_links()
    
