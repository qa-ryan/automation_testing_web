from playwright.sync_api import Page, expect

class HiddenElementsPage: 
    
    URL = "https://www.automationtesting.co.uk/hiddenElements.html"
    
    def __init__(self, page: Page):
        self.page = page
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def hidden_elements(self):
        visible_paragraph = self.page.get_by_text("This is a visible paragraph.")
        visible_print= visible_paragraph.text_content()
        
        hidden_paragraph = self.page.locator("p[hidden]")
        hidden_print = hidden_paragraph.text_content()
        
        print(visible_print)
        expect(visible_paragraph).to_have_text("This is a visible paragraph.")
        print(hidden_print)
        expect(hidden_paragraph).to_have_text("This paragraph should be hidden.")
        
        toogle_btn = self.page.get_by_role("button", name="Toggle")
        toogle_btn.click()
        hidden_text = self.page.locator("#myDIV")
        hidden_print = hidden_text.text_content()
        print(hidden_print)
        expect(self.page.locator("#myDIV")).to_contain_text("You have displayed the hidden text!")
            
    