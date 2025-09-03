from playwright.sync_api import Page, expect

def test_hidden_elements(page: Page):
    page.goto("https://www.automationtesting.co.uk/hiddenElements.html")
    print("\n")
    
    visible_paragraph = page.get_by_text("This is a visible paragraph.")
    visible_print= visible_paragraph.text_content()
    
    hidden_paragraph = page.locator("p[hidden]")
    hidden_print = hidden_paragraph.text_content()
    
    print(visible_print)
    expect(visible_paragraph).to_have_text("This is a visible paragraph.")
    print(hidden_print)
    expect(hidden_paragraph).to_have_text("This paragraph should be hidden.")
    
    toogle_btn = page.get_by_role("button", name="Toggle")
    toogle_btn.click()
    hidden_text = page.locator("#myDIV")
    hidden_print = hidden_text.text_content()
    print(hidden_print)
    expect(page.locator("#myDIV")).to_contain_text("You have displayed the hidden text!")