from playwright.sync_api import Page, expect
import pytest

class ContactUsPage: 
    
    URL = "https://www.automationtesting.co.uk/contactForm.html"
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self):
        self.page.goto(self.URL)
    
    def contact_us_form(self, first_name, last_name, email, comments):
        # Fill form fields
        self.page.get_by_role("textbox", name="First Name").fill(first_name)
        self.page.get_by_role("textbox", name="Last Name").fill(last_name)
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Comments").fill(comments)

        # Submit the form
        self.page.get_by_role("button", name="SUBMIT").click()

        # Validate success message
        success_message = self.page.get_by_role("heading", level=3, name="Thank you for your mail!")
        expect(success_message).to_be_visible()
