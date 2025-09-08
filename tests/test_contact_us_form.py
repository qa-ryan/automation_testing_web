from playwright.sync_api import Page, expect
from pages.contact_us_form_page import ContactUsPage
import pytest

test_data = [
    ("John", "Doe", "john.doe@example.com", "This is a test message"),
    ("Jane", "Smith", "jane.smith@example.com", "Another test message"), 
    ("Joni", "Jono", "joni.jono@example.com", "Testing contact form automation")
    
]

#Test contact form 
@pytest.mark.parametrize("first_name, last_name, email, comments", test_data)
def test_contact_us_form(page: Page, first_name, last_name, email, comments):
    run = ContactUsPage(page)
    run.load_page()
    run.contact_us_form(first_name, last_name, email, comments)