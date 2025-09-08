from playwright.sync_api import Page, expect

def test_count_iframes(page: Page):
    page.goto("https://www.automationtesting.co.uk/iframes.html")
    all_frame = page.frames
    print("Total frames:", len(all_frame))
    
    for frame in all_frame:
        print("Fame name:", frame.name)
        print("Frame URL:", frame.url)

def test_iframes_index_html(page: Page):
    page.goto("https://www.automationtesting.co.uk/iframes.html")
    iframe = page.frame_locator("iframe[src='index.html']")
    heading = iframe.locator("h1").text_content()
    print("\n")
    print(heading)
    