from playwright.sync_api import Page, expect
from pages.calculator_page import CalculatorPage

#Test calculator functionality
def test_full_calculator_functionality(page: Page):
    run = CalculatorPage(page)
    run.load_page()
    run.calculator_functionality()