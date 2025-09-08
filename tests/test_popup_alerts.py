from playwright.sync_api import Page
from pages.popup_alerts_page import PopupAlertsPage

    
def test_popup_alerts(page: Page):
    run = PopupAlertsPage(page)
    page.on("dialog", run.handle_prompt)
    run.load_page()
    run.popup_alerts()