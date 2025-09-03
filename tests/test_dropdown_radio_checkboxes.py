from playwright.sync_api import Page, expect

#Test radio button functionality
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

#Test checkboxes functionality
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
    print("Green Checked")
    
    cb_blue = page.get_by_text("Blue")
    cb_blue.check()
    print("Blue Checked")
    
    cb_red = page.get_by_text("Red", exact=True)
    cb_red.uncheck()
    print("Red Unchecked")

#Test Nav Menu functionality
def test_nav_menu(page: Page):
    page.goto("https://www.automationtesting.co.uk/dropdown.html#")
    print("\n")
    
    animals_sub = ["Mouse", "Cat", "Fish", "Dog"]
    dogs = ["German Shepard", "Labrador", "Norwegian Ridgeback"]
    sports = ["Football", "Tennis", "Rugby"]
    
    for animal in animals_sub:
        page.get_by_role("link", name="Animals").hover()
        if animal == "Mouse":
            page.get_by_role("link", name=animal, exact=True).click()
            
        elif animal == "Dog":
            page.get_by_role("link", name="Dog").click()
            
            output_locator = page.locator("#outputMessage")
            text_output = output_locator.inner_text()
            assert text_output == text_output
            print(text_output)
            
            for dog in dogs:
                page.get_by_role("link", name=dog).click()
                output_locator = page.locator("#outputMessage")
                text_output = output_locator.inner_text()
                assert text_output == text_output
                print(text_output)
            continue
                
        else:
            page.get_by_role("link", name=animal).click()
            
        output_locator = page.locator("#outputMessage")
        text_output = output_locator.inner_text()
        assert text_output == text_output
        print(text_output)
        
    for sport in sports:
        page.get_by_role("link", name="Sports").hover()
        page.get_by_role("link", name=sport).click()
        output_locator = page.locator("#outputMessage")
        text_output = output_locator.inner_text()
        assert text_output == text_output
        print(text_output)

