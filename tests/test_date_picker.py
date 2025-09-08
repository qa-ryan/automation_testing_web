from datetime import datetime, timedelta
from playwright.sync_api import Page
from pages.date_picker_page import DatePickerPage

#Work in Progress, still figure out how to check date picker
#Test Case 1: Typing date directly, bypass clicking element
def test_basic_datetime_typing(page: Page):
    run = DatePickerPage(page)
    run.load_page()
    run.basic_datetime_typing()
    
#Test Case 2: Typing date manually, still figure out how to handle month
def test_datepicker_popup(page: Page):
    run = DatePickerPage(page)
    run.load_page()
    run.datepicker_popup()
#It is not the end, working on the other then I will go back here