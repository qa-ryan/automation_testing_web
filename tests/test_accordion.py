from playwright.sync_api import Page
from pages.accordion_page import AccordionPage

#Testing functionality, clicking accordions
def test_accordion_functionality(page: Page):
    run = AccordionPage(page)
    run.load_page()
    run.functionality()
    
#Testing content validation, clicking accordions then validate the content
def test_content_validation(page: Page):
    run = AccordionPage(page)
    run.load_page()
    run.content_validation()
    
    