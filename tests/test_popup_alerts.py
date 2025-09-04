from playwright.sync_api import Page

def handle_prompt(dialog):
    print(f"Prompt detected!")
    print(f"Prompt message: {dialog.message}")
    print(f"Dialog type: {dialog.type}")
    dialog.accept()
    
def test_popup_alerts(page: Page):
    page.on("dialog", handle_prompt)
    page.goto("https://www.automationtesting.co.uk/popups.html")
    print("\n")
    with page.expect_popup() as popup_info:
        trigger_btn = page.get_by_role("button", name="Trigger Pop-up")
        trigger_btn.click()
        
    popup = popup_info.value
    popup_text = popup.locator("p").inner_text()
    print(popup_text)
    popup.close()
    print("\n")
    
    alert_btn = page.get_by_role("button", name="Trigger Alert")
    alert_btn.click()