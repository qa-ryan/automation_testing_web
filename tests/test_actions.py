from playwright.sync_api import Page, expect
import time

#Drag and Drop
def drag_and_drop(page: Page):
    page.goto("https://www.automationtesting.co.uk/actions.html")
    
    #Setting source and target location
    source = page.locator("#main div").filter(has_text="Drag me!").nth(3)
    target = page.locator("div:nth-child(3)")
    
    #Executing drag and drop to target
    source.drag_to(target)
    
    #Validate text after drag and drop executed
    expect(page.locator("#demo")).to_have_text("The p element was dropped into an accepted rectangle")

#Click and Hold
def test_click_and_hold(page: Page):
    page.goto("https://www.automationtesting.co.uk/actions.html")

    #Text shown before click
    text_before_click = page.locator("div#click-box").text_content()
    print(text_before_click)
    
    #Hover mouse to target box then use mouse.down() for click-hold
    element = page.locator("#holdDown")
    element.hover()
    page.mouse.down()
    
    #Text shown while click and hold
    text_hold_click = page.locator("div#click-box").text_content()
    print(text_hold_click)
    
    #Holding mouse click for several time then release
    page.wait_for_timeout(200)
    page.mouse.up()
    
    #Text shown after releasing click
    text_release_click = page.locator("div#click-box").text_content()
    print(text_release_click)
    
#Double click
def test_double_click(page: Page):
    page.goto("https://www.automationtesting.co.uk/actions.html")
    
    #Text show before double click the area
    text_before_dbclick = page.locator("#doubleClickArea").first.text_content()
    print(text_before_dbclick)
    
    #Double click area executed
    page.locator("#doubleClickArea").first.dblclick()
    
    #Text shown after double click the area
    text_after_dbclick = page.locator("#doubleClickArea").first.text_content()
    print(text_after_dbclick)
    
    
    
#Hold Shfit and Click
def test_hold_shift_and_click(page: Page):    

    prompt_message = None
    user_input = "Test Input"  
    
    def handle_prompt(dialog):
        nonlocal prompt_message
        
        prompt_message = dialog.message
        
        print(f"Prompt detected!")
        print(f"Prompt message: {dialog.message}")
        print(f"Dialog type: {dialog.type}")
        
        # Handle different dialog types
        if dialog.type == "prompt":
            print(f"Entering input: '{user_input}'")
            dialog.accept(user_input)  
        elif dialog.type == "alert":
            print("Alert detected, clicking OK")
            dialog.accept()
        elif dialog.type == "confirm":
            print("Confirm dialog detected, clicking OK")
            dialog.accept()  
    
    page.on("dialog", handle_prompt)

    page.goto("https://www.automationtesting.co.uk/actions.html")
    
    element = page.locator("#doubleClickArea").nth(1)
    element.click()
    
    # Perform shift + click action
    print("\nPerforming Shift + Click...")
    page.keyboard.down("Shift")
    element.click()
    page.keyboard.up("Shift")
    
    
    
    