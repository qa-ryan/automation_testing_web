from playwright.sync_api import Page, expect

class HomePage:
    URL = "https://www.automationtesting.co.uk/"

    def __init__(self, page: Page):
        self.page = page
        self.features_section = page.locator(".features")

    def load_page(self):
        self.page.goto(self.URL)

    def get_all_link(self):
        headers = self.page.locator(".features").locator("h3")
        count = headers.count()

        links = []
        for i in range(count):
            link = headers.nth(i).locator("a")
            href = link.get_attribute("href")
            text = link.inner_text().strip()
            if href:
                links.append((text, href))   # (visible text, href)
        
        print(f"\nCollected {len(links)} links:")

        for idx, (text, href) in enumerate(links, 1):
            print(f"[{idx}]. {text} -> {href}")
            assert text != ""
            assert href != ""
            
    def validate_links(self):
        headers = self.page.locator(".features").locator("h3")
        count = headers.count()

        links = []
        for i in range(count):
            link = headers.nth(i).locator("a")
            href = link.get_attribute("href")
            text = link.inner_text().strip()
            if href:
                links.append((text, href))   # (visible text, href)
            
        print(f"\nCollected {len(links)} links:")
        
        for idx, (text, href) in enumerate(links, 1):
            print(f"\n[{idx}]. Checking: {text} -> {href}")
            self.page.goto(href)
            expect(self.page).not_to_have_url("about:blank")
