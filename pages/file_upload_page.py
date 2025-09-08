from playwright.sync_api import Page

class FileUploadPage:
    
    URL = "https://www.automationtesting.co.uk/fileupload.html"
    
    def __init__(self, page: Page):
        self.page = page
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def file_upload(self):
        file_input = self.page.locator("#fileToUpload")
        file_input.set_input_files(r"D:\ryn_playground\automation_testing_web\uploadFolder\sample.txt")
        
        submit_btn = self.page.get_by_role("button", name="Submit")
        submit_btn.click()
    