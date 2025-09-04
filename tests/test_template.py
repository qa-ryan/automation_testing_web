from playwright.sync_api import Page, expect
import pytest
#This is template file, everything here will be move to specific file

def test_tables(page: Page):
    page.goto("https://www.automationtesting.co.uk/tables.html")

    cells = page.locator("//table[@id='table1']//td")
    assert cells.count() > 0
    for i in range(cells.count()):
        print(cells.nth(i).inner_text().strip())