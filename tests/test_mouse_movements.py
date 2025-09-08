from playwright.sync_api import Page, expect

def test_mouse_movement(page: Page):
    page.goto("https://www.automationtesting.co.uk/mouse.html")

    # Locate elements (adjust selectors if needed)
    left_zone = page.locator("#leftArea")    # the left rectangle
    right_zone = page.locator("#rightArea")  # the right rectangle
    counter_one = page.locator("#div1")      # counter for left
    counter_two = page.locator("#div2")      # counter for right

    # Get initial counter values
    initial_one = int(counter_one.text_content().split(":")[-1].strip())
    initial_two = int(counter_two.text_content().split(":")[-1].strip())

    # Move mouse into left zone (hover in)
    left_zone.hover()
    # Move mouse out (hover out)
    page.mouse.move(0, 0)

    # Assert counter one incremented
    updated_one = int(counter_one.text_content().split(":")[-1].strip())
    assert updated_one == initial_one + 1, "Counter One should increment after entering and exiting left zone"

    # Assert counter two still the same
    updated_two = int(counter_two.text_content().split(":")[-1].strip())
    assert updated_two == initial_two, "Counter Two should not change on hover in/out"

    # Now move inside left zone then leave completely (mouse leave event)
    left_box = left_zone.bounding_box()
    page.mouse.move(left_box["x"] + 10, left_box["y"] + 10)   # inside left zone
    page.mouse.move(left_box["x"], left_box["y"] - 50)        # move above (leave)

    updated_two_after = int(counter_two.text_content().split(":")[-1].strip())
    assert updated_two_after == initial_two + 1, "Counter Two should increment when leaving left zone"
