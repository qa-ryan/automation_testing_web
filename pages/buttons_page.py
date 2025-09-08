from playwright.sync_api import Page, expect

class ButtonPage:
    URL = "https://www.automationtesting.co.uk/buttons.html"
    def __init__(self, page: Page):
        self.page = page
        self.button_count = page.get_by_role("button")
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def count_button(self):
        buttons = self.button_count.all()
        
        #Store button that were found on the list
        enabled_buttons = []
        disabled_buttons = []
        
        for button in buttons:
            if button.is_enabled():
                enabled_buttons.append(button)
            else:
                disabled_buttons.append(button)
                
        print("Total buttons:", len(buttons))
        print("Enabled buttons:", len(enabled_buttons))
        print("Disabled buttons:", len(disabled_buttons), "\n")
        
        #Print Enable button found 
        for idx, btn in enumerate(enabled_buttons, start=1):
            print(f"Enabled button {idx} text: {btn.inner_text()}")

        #Print Disable button found
        for idx, btn in enumerate(disabled_buttons, start=1):
            print(f"Disabled button {idx} text: {btn.inner_text()}")

    def web_element_buttons(self):
        prompt_message = None
    
        def handle_prompt(dialog):
            nonlocal prompt_message
            
            prompt_message = dialog.message
            
            print(f"Prompt detected!")
            print(f"Prompt message: {dialog.message}")
            print(f"Dialog type: {dialog.type}")
            dialog.accept()
        
        self.page.on("dialog", handle_prompt)
        self.page.goto("https://www.automationtesting.co.uk/buttons.html")
        
        btn_one = self.page.locator("//button[@id='btn_one']")
        btn_one_text = btn_one.text_content()
        print(f"\n{btn_one_text}")
        
        btn_one.click()
        
    def javascript_click(self):
        prompt_message = None
    
        def handle_prompt(dialog):
            nonlocal prompt_message
            
            prompt_message = dialog.message
            
            print(f"Prompt detected!")
            print(f"Prompt message: {dialog.message}")
            print(f"Dialog type: {dialog.type}")
            dialog.accept()
        
        self.page.on("dialog", handle_prompt)
        self.page.goto("https://www.automationtesting.co.uk/buttons.html")
        
        btn_two = self.page.locator("button#btn_two")
        btn_two_text = btn_two.text_content()
        print(f"\n{btn_two_text}")
        
        self.page.evaluate("""
                    () => {
                        document.querySelector("button#btn_two").click()
                    }
                    """)    
        
    def action_move_and_click(self):
        prompt_message = None
        def handle_prompt(dialog):
            nonlocal prompt_message
            
            prompt_message = dialog.message
            
            print(f"Prompt detected!")
            print(f"Prompt message: {dialog.message}")
            print(f"Dialog type: {dialog.type}")
            dialog.accept()
            
        self.page.on("dialog", handle_prompt)
        self.page.goto("https://www.automationtesting.co.uk/buttons.html")
        
        btn_three = self.page.locator("button#btn_three")
        btn_three_text = btn_three.text_content()
        print(f"\n{btn_three_text}")
        
        box = btn_three.bounding_box()
        
        if box:
            self.page.mouse.move(
                box["x"] + box["width"] / 2,
                box["y"] + box["height"] / 2
            )
            
            self.page.mouse.click(
                box["x"] + box["width"] / 2,
                box["y"] + box["height"] / 2
            )
            print("Mouse moved and clicked using coordinates.")
        else:
            print("Button not visible on the page.")
            
    def disabled_button(self):
        btn_four = self.page.locator("button#btn_four")
        btn_four_text = btn_four.text_content()
        print(f"\n{btn_four_text}")
        
        if btn_four.is_enabled():
            print("The buttons is enable")
        elif btn_four.is_disabled():
            print("The button is disabled")
        else:
            print("Can not found button four")
        
        expect(self.page.locator("button#btn_four")).to_be_disabled()