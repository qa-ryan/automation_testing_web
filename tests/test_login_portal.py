from playwright.sync_api import Page, expect
import pytest
#This is template file, everything here will be move to specific file
test_data = [
    ("test", "test123"), #valid
    ("", ""),            #invalid
    ("teest", "test123"),#invalid
    ("test", "teeet12"), #invalid
    ("teest", "teest123")#invalid
]

def handle_prompt(dialog):
    print(f"Prompt detected!")
    print(f"Prompt message: {dialog.message}")
    print(f"Dialog type: {dialog.type}")
    dialog.accept()
    expect(dialog.message).to_be_visible()
    
@pytest.mark.parametrize("username, password", test_data)
def test_login_portal(page: Page, username, password):
    page.on("dialog", handle_prompt)
    page.goto("https://www.automationtesting.co.uk/loginPortal.html")
    print("\n")
    page.locator("#login_text").fill(username)
    page.locator("#login_password").fill(password)
    page.locator("#login_btn").click()
    
    
    
    