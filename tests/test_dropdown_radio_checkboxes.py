from playwright.sync_api import Page, expect
from pages.dropdown_radio_page import DropdownRadioPage

#Test radio button functionality
def test_radio_buttons(page: Page):
    run = DropdownRadioPage(page)
    run.load_page()
    run.radio_buttons()

#Test checkboxes functionality
def test_checkboxes(page: Page):
    run = DropdownRadioPage(page)
    run.load_page()
    run.checkboxes()

#Test Nav Menu functionality
def test_nav_menu(page: Page):
    run = DropdownRadioPage(page)
    run.load_page()
    run.nav_menu()
        
#Test dropdown menu      
def test_dropdown_menu(page: Page):
    run = DropdownRadioPage(page)
    run.load_page()
    run.dropdown_menu()