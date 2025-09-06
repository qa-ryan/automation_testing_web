from playwright.sync_api import Page
from pages.accordion_page import AccordionPage

def load_page(page: Page):
    
    url = AccordionPage(page)
    url.goto()
    
#Testing functionality, clicking accordions
def test_accordion_functionality(page: Page):
    
    load_page(page)
    print("\n")
    run = AccordionPage(page)
    run.functionality()
    
#Testing content validation, clicking accordions then validate the content
def test_content_validation(page: Page):
    
    load_page(page)
    print("\n")
    run = AccordionPage(page)
    run.content_validation()
    
    