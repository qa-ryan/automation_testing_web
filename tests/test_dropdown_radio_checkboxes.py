from playwright.sync_api import Page, expect

def test_radio_buttons(page: Page):
    page.goto("https://www.automationtesting.co.uk/dropdown.html")
    
    labels = page.locator("label[for^='demo-priority-']")
    count = labels.count()
    print("\n")
    for i in range(count):
        print(labels.nth(i).inner_text())
        
    low_select = page.locator("label[for^='demo-priority-low']")
    low_select.click()
    expect(page.locator("label[for^='demo-priority-low']")).to_be_checked()
    
    normal_select = page.locator("label[for^='demo-priority-normal']")
    normal_select.click()
    expect(page.locator("label[for^='demo-priority-normal']")).to_be_checked()
    
    high_select = page.locator("label[for^='demo-priority-high']")
    high_select.click()
    expect(page.locator("label[for^='demo-priority-high']")).to_be_checked()