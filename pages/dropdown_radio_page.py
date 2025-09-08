from playwright.sync_api import Page, expect

class DropdownRadioPage: 
    
    URL = "https://www.automationtesting.co.uk/dropdown.html"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self):
        self.page.goto(self.URL)
        
    def radio_buttons(self):
        labels = self.page.locator("label[for^='demo-priority-']")
        count = labels.count()
        print("\n")
        for i in range(count):
            print(labels.nth(i).inner_text())
            
        low_select = self.page.locator("label[for^='demo-priority-low']")
        low_select.click()
        expect(self.page.locator("label[for^='demo-priority-low']")).to_be_checked()
        
        normal_select = self.page.locator("label[for^='demo-priority-normal']")
        normal_select.click()
        expect(self.page.locator("label[for^='demo-priority-normal']")).to_be_checked()
        
        high_select = self.page.locator("label[for^='demo-priority-high']")
        high_select.click()
        expect(self.page.locator("label[for^='demo-priority-high']")).to_be_checked()

    def checkboxes(self):
        checkboxes = self.page.locator("input[type='checkbox']")
        total = checkboxes.count()
        print(f"Checkboxes found on the page: {total}")
        
        checked = self.page.locator("input[type=checkbox]:checked").count()
        print(f"Checked checkbox found on the page: {checked}")
        
        unchecked = self.page.locator("input[type=checkbox]:not(:checked)").count()
        print(f"Unchecked checkbox found on the page: {unchecked}")
        
        for i in range(total):
            cb = checkboxes.nth(i)
            print("Checkbox id:", cb.get_attribute("id"))
            
        cb_green = self.page.get_by_text("Green")
        cb_green.check()
        print("Green Checked")
        
        cb_blue = self.page.get_by_text("Blue")
        cb_blue.check()
        print("Blue Checked")
        
        cb_red = self.page.get_by_text("Red", exact=True)
        cb_red.uncheck()
        print("Red Unchecked")
    
    def nav_menu(self):
        print("\n")
        
        animals_sub = ["Mouse", "Cat", "Fish", "Dog"]
        dogs = ["German Shepard", "Labrador", "Norwegian Ridgeback"]
        sports = ["Football", "Tennis", "Rugby"]
        
        for animal in animals_sub:
            self.page.get_by_role("link", name="Animals").hover()
            if animal == "Mouse":
                self.page.get_by_role("link", name=animal, exact=True).click()
                
            elif animal == "Dog":
                self.page.get_by_role("link", name="Dog").click()
                
                output_locator = self.page.locator("#outputMessage")
                text_output = output_locator.inner_text()
                assert text_output == text_output
                print(text_output)
                
                for dog in dogs:
                    self.page.get_by_role("link", name=dog).click()
                    output_locator = self.page.locator("#outputMessage")
                    text_output = output_locator.inner_text()
                    assert text_output == text_output
                    print(text_output)
                continue
                    
            else:
                self.page.get_by_role("link", name=animal).click()
                
            output_locator = self.page.locator("#outputMessage")
            text_output = output_locator.inner_text()
            assert text_output == text_output
            print(text_output)
            
        for sport in sports:
            self.page.get_by_role("link", name="Sports").hover()
            self.page.get_by_role("link", name=sport).click()
            output_locator = self.page.locator("#outputMessage")
            text_output = output_locator.inner_text()
            assert text_output == text_output
            print(text_output)
            
    def dropdown_menu(self):
    
        dropdown = self.page.locator("#cars option")
        count = dropdown.count()

        items = []
        for i in range(count):
            text = dropdown.nth(i).inner_text()
            items.append(text)

        print("\nDropdown items:", items)

        for item in items:
            self.page.locator("#cars").select_option(label=item)
            print(f"✅ Clicked and verified: {item}")
            

