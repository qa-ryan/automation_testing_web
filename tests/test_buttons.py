from playwright.sync_api import Page, expect

#Count all buttons found on the page
def test_count_buttons(page: Page):
    page.goto("https://www.automationtesting.co.uk/buttons.html")
    
    buttons = page.get_by_role("button").all()
    
    #Store button that were found on the list
    enabled_buttons = []
    disabled_buttons = []
    
    for button in buttons:
        if button.is_enabled():
            enabled_buttons.append(button)
        else:
            disabled_buttons.append(button)
            
    print("\nTotal buttons:", len(buttons))
    print("Enabled buttons:", len(enabled_buttons))
    print("Disabled buttons:", len(disabled_buttons), "\n")
    
    #Print Enable button found 
    for idx, btn in enumerate(enabled_buttons, start=1):
        print(f"Enabled button {idx} text: {btn.inner_text()}")

    #Print Disable button found
    for idx, btn in enumerate(disabled_buttons, start=1):
        print(f"Disabled button {idx} text: {btn.inner_text()}")
   
def test_web_element_buttons(page: Page):
    prompt_message = None
    
    def handle_prompt(dialog):
        nonlocal prompt_message
        
        prompt_message = dialog.message
        
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        dialog.accept()
    
    page.on("dialog", handle_prompt)
    page.goto("https://www.automationtesting.co.uk/buttons.html")
    
    btn_one = page.locator("//button[@id='btn_one']")
    btn_one_text = btn_one.text_content()
    print(f"\n{btn_one_text}")
    
    btn_one.click()

def test_javascript_click(page: Page):
    prompt_message = None
    
    def handle_prompt(dialog):
        nonlocal prompt_message
        
        prompt_message = dialog.message
        
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        dialog.accept()
    
    page.on("dialog", handle_prompt)
    page.goto("https://www.automationtesting.co.uk/buttons.html")
    
    btn_two = page.locator("button#btn_two")
    btn_two_text = btn_two.text_content()
    print(f"\n{btn_two_text}")
    
    page.evaluate("""
                  () => {
                      document.querySelector("button#btn_two").click()
                  }
                  """)

def test_action_move_click(page: Page):
    prompt_message = None
    def handle_prompt(dialog):
        nonlocal prompt_message
        
        prompt_message = dialog.message
        
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        dialog.accept()
        
    page.on("dialog", handle_prompt)
    page.goto("https://www.automationtesting.co.uk/buttons.html")
    
    btn_three = page.locator("button#btn_three")
    btn_three_text = btn_three.text_content()
    print(f"\n{btn_three_text}")
    
    box = btn_three.bounding_box()
    
    if box:
        page.mouse.move(
            box["x"] + box["width"] / 2,
            box["y"] + box["height"] / 2
        )
        
        page.mouse.click(
            box["x"] + box["width"] / 2,
            box["y"] + box["height"] / 2
        )
        print("Mouse moved and clicked using coordinates.")
    else:
        print("Button not visible on the page.")

def test_disabled_button(page: Page):
    page.goto("https://www.automationtesting.co.uk/buttons.html")
    
    btn_four = page.locator("button#btn_four")
    btn_four_text = btn_four.text_content()
    print(f"\n{btn_four_text}")
    
    if btn_four.is_enabled():
        print("The buttons is enable")
    elif btn_four.is_disabled():
        print("The button is disabled")
    else:
        print("Can not found button four")
        
    expect(page.locator("button#btn_four")).to_be_disabled()