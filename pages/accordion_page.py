from playwright.sync_api import Page

class AccordionPage:
    URL = "https://www.automationtesting.co.uk/accordion.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def goto(self):
        self.page.goto(self.URL)
    
    