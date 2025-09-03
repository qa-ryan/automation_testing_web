from playwright.sync_api import Page
#Test Upload File basic
def test_file_upload(page: Page):
    page.goto("https://www.automationtesting.co.uk/fileupload.html")
    file_input = page.locator("#fileToUpload")
    file_input.set_input_files(r"D:\ryn_playground\automation_testing_web\uploadFolder\sample.txt")
    
    submit_btn = page.get_by_role("button", name="Submit")
    submit_btn.click()
    page.pause()