from playwright.sync_api import Page, expect

class LoginPortalPage:
    
    URL = "https://www.automationtesting.co.uk/loginPortal.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self): 
        self.page.goto(self.URL)
        
    def handle_prompt(self, dialog):
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        dialog.accept()
        expect(dialog.message).to_be_visible()
        
    def login_portal(self, username, password):
        self.page.locator("#login_text").fill(username)
        self.page.locator("#login_password").fill(password)
        self.page.locator("#login_btn").click()