from playwright.sync_api import Page, expect
import pytest
from pages.login_portal_page import LoginPortalPage

#This is template file, everything here will be move to specific file
test_data = [
    ("test", "test123"), #valid
    ("", ""),            #invalid
    ("teest", "test123"),#invalid
    ("test", "teeet12"), #invalid
    ("teest", "teest123")#invalid
]

@pytest.mark.parametrize("username, password", test_data)
def test_login_portal(page: Page, username, password):
    run = LoginPortalPage(page)
    page.on("dialog", run.handle_prompt)
    run.load_page()
    run.login_portal(username, password)
    
    
    
    