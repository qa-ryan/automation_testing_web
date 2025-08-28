from playwright.sync_api import Page, expect
from pages.home_page import HomePage


# Get all link from the page
def test_case_1(page: Page):
    home = HomePage(page)
    home.goto()

    links = home.get_feature_links()
    print(f"\nCollected {len(links)} links:")

    for idx, (text, href) in enumerate(links, 1):
        print(f"[{idx}]. {text} -> {href}")
        assert text != ""
        assert href != ""


# Validate all links that were found
def test_case_2(page: Page):
    home = HomePage(page)
    home.goto()

    links = home.get_feature_links()

    for idx, (text, href) in enumerate(links, 1):
        print(f"\n[{idx}]. Checking: {text} -> {href}")
        page.goto(href)
        expect(page).not_to_have_url("about:blank")
