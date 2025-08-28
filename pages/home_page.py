from playwright.sync_api import Page

class HomePage:
    URL = "https://www.automationtesting.co.uk/"

    def __init__(self, page: Page):
        self.page = page
        self.features_section = page.locator(".features")

    def goto(self):
        self.page.goto(self.URL)

    def get_feature_links(self):
        headers = self.features_section.locator("h3")
        count = headers.count()

        links = []
        for i in range(count):
            link = headers.nth(i).locator("a")
            href = link.get_attribute("href")
            text = link.inner_text().strip()
            if href:
                links.append((text, href))   # (visible text, href)
        return links
