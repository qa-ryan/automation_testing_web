from playwright.sync_api import Page

class BrowserTabsPage:
    URL = "https://www.automationtesting.co.uk/browserTabs.html"
    
    def __init__(self, page:Page):
        self.page = page
    
    def load_page(self):
        self.page.goto(self.URL)
        
    def browser_tab(self):
        urls = [
        "https://playwright.dev/python/",
        "https://www.python.org/"
    ]

        for target_url in urls:
            with self.page.expect_popup() as popup_info:
                self.page.get_by_role("button", name="Open Tab").click()

            new_tab = popup_info.value
            new_tab.wait_for_load_state()

            # Navigate to your desired URL in the new tab
            new_tab.goto(target_url)
            print("\nOpened new tab URL:", new_tab.url)

            # Close the new tab
            self.page.bring_to_front()
            #new_tab.close()
            
        
        