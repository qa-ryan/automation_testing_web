from playwright.sync_api import Page, expect
import pytest
#This is template file, everything here will be move to specific file

def test_predictive_search(page: Page):
    page.goto("https://www.automationtesting.co.uk/predictive.html")
    
    country_input = page.locator("#myInput")
    country_input.click()
    country_input.fill("")
    country_input.type("c", delay=30)
    
    # Wait until at least one visible suggestion row appears
    page.wait_for_selector(".autocomplete-items div:visible", timeout=5000)

    # Grab only the visible suggestion rows
    rows = page.locator(".autocomplete-items div:visible")
    count = rows.count()
    assert count > 0, "No visible suggestions appeared."

    # Collect clean names: prefer hidden input value, fall back to visible text
    suggestions = []
    for i in range(count):
        row = rows.nth(i)
        val = row.locator("input[type='hidden']").get_attribute("value")
        txt = (row.text_content() or "").strip()
        clean = val or txt
        suggestions.append(clean)

    # --- Tailored print output ---
    print("\n===== Country Suggestions =====")
    for idx, country in enumerate(suggestions, start=1):
        print(f"{idx}. {country}")
    print("================================\n")

    # Example assertion
    assert any("a" in s.lower() for s in suggestions)
    
