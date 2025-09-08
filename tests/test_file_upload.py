from playwright.sync_api import Page
from pages.file_upload_page import FileUploadPage
#Test Upload File basic
def test_file_upload(page: Page):
    run = FileUploadPage(page)
    run.load_page()
    run.file_upload()