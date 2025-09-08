from playwright.sync_api import Page

class PopupAlertsPage:
    
    URL = "https://www.automationtesting.co.uk/popups.html"
    
    def __init__(self, page: Page):
        self.page = page
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def handle_prompt(self, dialog):
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        dialog.accept()
        
    def popup_alerts(self):
        
        with self.page.expect_popup() as popup_info:
            trigger_btn = self.page.get_by_role("button", name="Trigger Pop-up")
            trigger_btn.click()
            
        popup = popup_info.value
        popup_text = popup.locator("p").inner_text()
        print(popup_text)
        popup.close()
        print("\n")
        
        alert_btn = self.page.get_by_role("button", name="Trigger Alert")
        alert_btn.click()
        