from playwright.sync_api import Page, expect

def test_checkboxes(page: Page):
    page.goto("https://www.automationtesting.co.uk/dropdown.html")
    print("\n")
    
    checkboxes = page.locator("input[type='checkbox']")
    total = checkboxes.count()
    print(f"Checkboxes found on the page: {total}")
    
    checked = page.locator("input[type=checkbox]:checked").count()
    print(f"Checked checkbox found on the page: {checked}")
    
    unchecked = page.locator("input[type=checkbox]:not(:checked)").count()
    print(f"Unchecked checkbox found on the page: {unchecked}")
    
    for i in range(total):
        cb = checkboxes.nth(i)
        print("Checkbox id:", cb.get_attribute("id"))
        
    cb_green = page.get_by_text("Green")
    cb_green.check()
    
    cb_blue = page.get_by_text("Blue")
    cb_blue.check()
    
    cb_red = page.get_by_text("Red", exact=True)
    cb_red.uncheck()