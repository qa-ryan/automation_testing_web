from playwright.sync_api import Page, expect

class ActionsPage:
    URL = "https://www.automationtesting.co.uk/actions.html"
    dragdrop_text = "The p element was dropped into an accepted rectangle"
    
    def __init__(self, page:Page):
        self.page = page
        self.source_locator = page.locator("#main div").filter(has_text="Drag me!").nth(3)
        self.target_locator = page.locator("div:nth-child(3)")
        self.dragdrop_text_validation = page.locator("#demo")
        self.clickhold_text = page.locator("div#click-box")
        self.dbclick_locator = page.locator("#doubleClickArea")
        self.dbclick_text_before = self.page.get_by_text("Double Click Here")
        self.dbclick_text_after = self.page.get_by_text("Well Done!")
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def drag_and_drop(self):
        #Setting source and target location
        self.source_locator
        self.target_locator
        
        #Executing drag and drop to target
        self.source_locator.drag_to(self.target_locator)
    
        #Validate text after drag and drop executed
        expect(self.dragdrop_text_validation).to_have_text(self.dragdrop_text)
    
    def click_and_hold(self):
        #Default text before action/click
        text_before_click = self.clickhold_text.text_content()
        expect(self.clickhold_text).to_have_text("Click and Hold!")
        print(text_before_click)
        
        
        #Hover mouse to target box then use mouse.down() for click-hold
        element = self.page.locator("#holdDown")
        element.hover()
        self.page.mouse.down()
        
        #Text shown while click and hold
        text_hold_click = self.clickhold_text.text_content()
        expect(self.clickhold_text).to_have_text("Keep holding down!")
        print(text_hold_click)
        
        #Holding mouse click for several time then release
        self.page.wait_for_timeout(200)
        self.page.mouse.up()
        
        #Text shown after releasing click
        text_release_click = self.clickhold_text.text_content()
        expect(self.clickhold_text).to_have_text("No, don't let go :(")
        print(text_release_click)
    
    def double_click(self):
        #Default text before double click the area
        text_before_dbclick = self.dbclick_text_before.first.text_content()
        expect(self.dbclick_text_before).to_have_text("Double Click Here")
        print(text_before_dbclick)
        
        #Double click area executed
        self.dbclick_text_before.first.dblclick()
        
        #Text shown after double click the area
        text_after_dbclick = self.dbclick_text_after.first.text_content()
        expect(self.dbclick_text_after).to_have_text("Well Done!")
        print(text_after_dbclick)
        
    def hold_and_shift(self):
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
        
        self.page.on("dialog", handle_prompt)

        self.page.goto("https://www.automationtesting.co.uk/actions.html")
        
        element = self.dbclick_locator.nth(1)
        element.click()
        
        # Perform shift + click action
        print("\nPerforming Shift + Click...")
        self.page.keyboard.down("Shift")
        element.click()
        self.page.keyboard.up("Shift")
        
        
        
        
                
        