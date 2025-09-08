from playwright.sync_api import Page
from pages.browser_tabs_page import BrowserTabsPage
    
def test_browser_tab(page: Page): 
    run = BrowserTabsPage(page)
    run.load_page()
    run.browser_tab()
    