from playwright.sync_api import Page

def test_browser_tab(page: Page):
    page.goto("https://www.automationtesting.co.uk/browserTabs.html")
    
    urls = [
        "https://playwright.dev/python/",
        "https://www.python.org/"
    ]

    for target_url in urls:
        with page.expect_popup() as popup_info:
            page.get_by_role("button", name="Open Tab").click()

        new_tab = popup_info.value
        new_tab.wait_for_load_state()

        # Navigate to your desired URL in the new tab
        new_tab.goto(target_url)
        print("\nOpened new tab URL:", new_tab.url)

        # Close the new tab
        page.bring_to_front()
        #new_tab.close()
        
        
        