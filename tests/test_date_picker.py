from datetime import datetime, timedelta
from playwright.sync_api import Page

#Work in Progress, still figure out how to check date picker
#Test Case 1: Typing date directly, bypass clicking element
def test_basic_datetime_typing(page: Page):
    page.goto("https://www.automationtesting.co.uk/datepicker.html")
    
    page.eval_on_selector("#basicDate", "el => el.removeAttribute('readonly')")
    date_input = page.locator("#basicDate")

    date_input.fill("")
    date_input.type("2025-09-02")
    assert date_input.input_value() == "2025-09-02"

#Test Case 2: Typing date manually, still figure out how to handle month
def test_datepicker_popup(page: Page):
    page.goto("https://www.automationtesting.co.uk/datepicker.html")
    
    page.click("#basicDate")
    
    calendar = page.locator(".flatpickr-calendar.open")
    
    year_dropdown = calendar.locator("input.cur-year")
    year_dropdown.fill("2000")
    page.keyboard.press("Enter")
    
    calendar.locator(".flatpickr-day", has_text="20").first.click()  
    
    date_value = page.locator("#basicDate").input_value()
    print("Selected Date:", date_value)
    
    assert date_value != ""
    
#It is not the end, working on the other then I will go back here