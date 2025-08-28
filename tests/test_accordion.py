from playwright.sync_api import Page

def test_case_1(page: Page):
    page.goto("https://www.automationtesting.co.uk/accordion.html")
    
    # Define the accordion headings you want to click
    headings = ["Platform Portability", "Language Support", "Selenium Grid"]

    # Repeat clicking cycle a few times
    for _ in range(5):   
        for heading in headings:
            page.get_by_text(heading).click()
    
