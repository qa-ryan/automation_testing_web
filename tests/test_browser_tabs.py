from playwright.sync_api import Page
from pages.browser_tabs_page import BrowserTabsPage

def load_page(page:Page):
    url = BrowserTabsPage(page)
    url.goto()
    
def test_browser_tab(page: Page):
    load_page(page)    
    run = BrowserTabsPage(page)
    run.browser_tab()
    