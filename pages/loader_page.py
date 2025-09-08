from playwright.sync_api import Page

class LoaderPage:
    
    URL = "https://www.automationtesting.co.uk/loader.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self):
        self.page.goto(self.URL)
        
    def loader(self):    
        self.page.locator("#loader").wait_for(state="hidden")
        
        loading_complete = self.page.locator("#h2_wording").text_content()
        print(loading_complete)
        
        self.page.locator("#loaderBtn").click()
        
        hidden_text = self.page.locator("#p_wording").text_content()
        print(hidden_text)