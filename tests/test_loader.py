from playwright.sync_api import Page

def test_loader(page: Page):
    page.goto("https://www.automationtesting.co.uk/loader.html")
    
    page.locator("#loader").wait_for(state="hidden")
    
    loading_complete = page.locator("#h2_wording").text_content()
    print(loading_complete)
    
    page.locator("#loaderBtn").click()
    
    hidden_text = page.locator("#p_wording").text_content()
    print(hidden_text)