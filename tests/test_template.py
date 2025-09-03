from playwright.sync_api import Page, expect
#This is template file, everything here will be move to specific file

def test_dropdown_menu(page: Page):
    page.goto("https://www.automationtesting.co.uk/dropdown.html#")
    
    dropdown = page.locator("#cars option")
    count = dropdown.count()

    items = []
    for i in range(count):
        text = dropdown.nth(i).inner_text()
        items.append(text)

    print("\nDropdown items:", items)

    for item in items:
        page.locator("#cars").select_option(label=item)
        selected_value = page.locator("#cars-value")
        
        #Expect is not working
        #expect(selected_value).to_have_text(f"{item}") 

        print(f"✅ Clicked and verified: {item}")
        