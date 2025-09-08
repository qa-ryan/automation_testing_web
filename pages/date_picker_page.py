from playwright.sync_api import Page

class DatePickerPage:
    
    URL = "https://www.automationtesting.co.uk/datepicker.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self):
        self.page.goto(self.URL)
    
    def basic_datetime_typing(self):
        self.page.eval_on_selector("#basicDate", "el => el.removeAttribute('readonly')")
        date_input = self.page.locator("#basicDate")

        date_input.fill("")
        date_input.type("2025-09-02")
        assert date_input.input_value() == "2025-09-02"
        
    def datepicker_popup(self):
        self.page.click("#basicDate")
        
        calendar = self.page.locator(".flatpickr-calendar.open")
        year_dropdown = calendar.locator("input.cur-year")
        year_dropdown.fill("2000")
        self.page.keyboard.press("Enter")
        
        calendar.locator(".flatpickr-day", has_text="20").first.click()  
        
        date_value = self.page.locator("#basicDate").input_value()
        print("Selected Date:", date_value)
        
        assert date_value != ""
    