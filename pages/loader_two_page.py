from playwright.sync_api import Page, expect

class LoaderTwoPage: 
    
    URL = "https://www.automationtesting.co.uk/loadertwo.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self):
        self.page.goto(self.URL)
        
    def loader_two(self):
        self.page.locator("#loader").wait_for(state="hidden")
        
        loading_complete = self.page.locator("#appears").text_content()
        print(loading_complete)
        
        expect(self.page.locator("#appears")).to_have_text("This is a new paragraph that appears after 8 seconds.")