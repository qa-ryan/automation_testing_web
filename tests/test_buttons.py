from playwright.sync_api import Page, expect
from pages.buttons_page import ButtonPage
def load_page(page: Page):
    url = ButtonPage(page)
    url.goto()

#Count all buttons found on the page
def test_count_buttons(page: Page):
    load_page(page)
    print("\n")
    run = ButtonPage(page)
    run.count_button()
    
#Test web element button
def test_web_element_buttons(page: Page):
    run = ButtonPage(page)
    run.web_element_buttons
    
#Test button with javascript handler
def test_javascript_click(page: Page):
    load_page(page)
    run = ButtonPage(page)
    run.javascript_click()
#Test action move and click button
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

#Validate disabled button
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