from playwright.sync_api import Page
from pages.predictive_search_page import PredictiveSearchPage

#This is template file, everything here will be move to specific file
def test_predictive_search(page: Page):
    run = PredictiveSearchPage(page)
    run.load_page()
    run.predicive_search()
