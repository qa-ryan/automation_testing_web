"""from playwright.sync_api import Page, expect

def test_table_sorting(page: Page):
    # 1. Open the page
    page.goto("https://www.automationtesting.co.uk/tables.html")

    # 2. Select header cells (for sorting)
    headers = page.locator("table th")  # all header columns

    # 3. Assert initial order (first row first name)
    first_row_first_cell = page.locator("table tr:nth-of-type(2) td:nth-of-type(1)")
    initial_first_name = first_row_first_cell.text_content().strip()

    # Print for visibility
    print("Initial first name:", initial_first_name)

    # 4. Click the "First Name" header to sort
    # Assuming header text equals "First Name"
    page.get_by_role("columnheader", name="First Name").click()

    # Wait for potential sort update
    page.wait_for_timeout(500)

    # 5. After sorting, fetch the first row again
    sorted_first_name = page.locator("table tr:nth-of-type(2) td:nth-of-type(1)").text_content().strip()

    # Print sorted result
    print("After sort, first name:", sorted_first_name)

    # 6. Basic assertion: the first name should change order (just ensuring a sort happened)
    assert initial_first_name != sorted_first_name, (
        "Table should be sorted; first row value should change after clicking the header."
    )
