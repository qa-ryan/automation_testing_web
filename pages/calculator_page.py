from playwright.sync_api import Page, expect

class CalculatorPage:
    
    URL = "https://www.automationtesting.co.uk/calculator.html"
    
    def __init__(self, page: Page):
        self.page = page
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def calculator_functionality(self):
        
        display = self.page.locator("#result")

        def click_val(val: str):
            self.page.locator(f"input[type='button'][value='{val}']").click()

        # 1) Test digits 0–9 individually
        for digit in map(str, range(10)):
            click_val("c")   # reset before each test
            click_val(digit)
            expect(display).to_have_value(digit)
            print(f"Digit {digit} OK")

        # 2) Test multi-digit input
        click_val("c")
        sequence = "0123456789"
        for ch in sequence:
            click_val(ch)
        expect(display).to_have_value(sequence)
        print(f"Multi-digit sequence '{sequence}' OK")

        # 3) Test basic operations
        operations = [
            ("12", "+", "7", "=", "19"),
            ("20", "-", "4", "=", "16"),
            ("6", "*", "3", "=", "18"),
            ("8", "/", "2", "=", "4"),
        ]
        for a, op, b, eq, expected in operations:
            click_val("c")
            for ch in a + op + b + eq:
                click_val(ch)
            expect(display).to_have_value(expected)
            print(f"Operation {a}{op}{b} = {expected} OK")

        # 4) Test clear mid-calculation
        click_val("c")
        click_val("9")
        click_val("+")
        click_val("1")
        click_val("c")  # clear mid input
        expect(display).to_have_value("")  # after clear, display should be empty
        print("Clear button works correctly ✅")
