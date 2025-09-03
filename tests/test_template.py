from playwright.sync_api import Page, expect
#This is template file, everything here will be move to specific file

def test_loader_two(page: Page):
    page.goto("https://www.automationtesting.co.uk/loadertwo.html")
    print("\n")
    page.locator("#loader").wait_for(state="hidden")
    
    loading_complete = page.locator("#appears").text_content()
    print(loading_complete)
    
    expect(page.locator("#appears")).to_have_text("This is a new paragraph that appears after 8 seconds.")