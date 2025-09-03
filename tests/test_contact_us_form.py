from playwright.sync_api import Page, expect
import pytest

test_data = [
    ("John", "Doe", "john.doe@example.com", "This is a test message"),
    ("Jane", "Smith", "jane.smith@example.com", "Another test message"), 
    ("Joni", "Jono", "joni.jono@example.com", "Testing contact form automation")
    
]

#Test contact form 
@pytest.mark.parametrize("first_name, last_name, email, comments", test_data)
def test_contact_us_form(page: Page, first_name, last_name, email, comments):
    page.goto("https://www.automationtesting.co.uk/contactForm.html")
    
    # Fill form fields
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").fill(last_name)
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Comments").fill(comments)

    # Submit the form
    page.get_by_role("button", name="SUBMIT").click()

    # Validate success message
    success_message = page.get_by_role("heading", level=3, name="Thank you for your mail!")
    expect(success_message).to_be_visible()
