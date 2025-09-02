from datetime import datetime, timedelta
from playwright.sync_api import Page

def test_date_picker(page: Page):
    page.goto("https://www.automationtesting.co.uk/datepicker.html")
    
    # -------- Basic Date Picker --------
    today = datetime.today()
    date_label = today.strftime("%B %#d, %Y")   # e.g. "August 31, 2025"
    expected_value = today.strftime("%Y-%m-%d") # e.g. "2025-08-31"

    page.click("#basicDate")
    page.click(f".flatpickr-day[aria-label='{date_label}']")

    basic_value = page.input_value("#basicDate")
    assert basic_value == expected_value

    # -------- Date & Time Picker --------
    tomorrow = today + timedelta(days=1)
    date_label_time = tomorrow.strftime("%B %-d, %Y")  # e.g. "September 1, 2025"
    expected_date_time = tomorrow.strftime("%Y-%m-%d 10:00")

    page.click("#dateAndTimePicker")
    page.click(f".flatpickr-day[aria-label='{date_label_time}']")

    # Select time → use flatpickr hour/minute selectors
    page.click(".flatpickr-hour")      # click hour box
    page.keyboard.press("Control+A")   # clear
    page.keyboard.type("10")

    page.click(".flatpickr-minute")    # click minute box
    page.keyboard.press("Control+A")   # clear
    page.keyboard.type("00")

    page.keyboard.press("Enter")       # close picker

    datetime_value = page.input_value("#dateAndTimePicker")
    assert datetime_value.startswith(expected_date_time)

    # -------- Disabled Range Picker --------
    page.click("#disableRangePicker")

    # Attempt to click a disabled date → should not set input
    disabled_day = page.locator(".flatpickr-day.disabled").first
    disabled_day.click(force=True)  # force click (still won’t change input)

    disabled_value = page.input_value("#disableRangePicker")
    assert disabled_value == ""  # still empty

    # Now pick an allowed day
    allowed_day = page.locator(".flatpickr-day:not(.disabled)").first
    allowed_label = allowed_day.get_attribute("aria-label")
    allowed_day.click()

    final_value = page.input_value("#disableRangePicker")
    assert final_value != "" and allowed_label in final_value