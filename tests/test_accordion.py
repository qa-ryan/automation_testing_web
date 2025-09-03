from playwright.sync_api import Page, expect

#Testing functionality, clicking accordions
def test_accordion_functionality(page: Page):
    page.goto("https://www.automationtesting.co.uk/accordion.html")
    
    # Define the accordion headings you want to click
    headings = ["Platform Portability", "Language Support", "Selenium Grid"]

    # Repeat clicking cycle a few times
    for _ in range(5):   
        for heading in headings:
            page.get_by_text(heading).click()

#Testing functionality with conotent validation
def test_content_validation(page: Page):
    page.goto("https://www.automationtesting.co.uk/accordion.html")
    
    page.get_by_text("Platform Portability").click()
    expect(page.locator("#main")).to_contain_text("Testing is a repetitive process. The slightest modification in code must be tested to ensure that the software is providing the desired functionality and result. Repeating tests manually is a time consuming and costly process. Automated tests can be run repetitively at no additional costs. Selenium is a highly portable tool that runs on multiple platforms as well as browsers. It therefore allows automation engineers the ease of writing code without worrying about the platform on which it will run.")
    page.get_by_text("Language Support").click()
    expect(page.locator("#main")).to_contain_text("Software is written in a number of languages. One of the challenges faced by automated testers is integrating the automation tools with the development environment for CI. With Selenium bindings for Java, .NET, Ruby, Perl, Python, PHP, Groovy and JavaScript, it is very easy to integrate with the development environment.")
    page.get_by_text("Selenium Grid").click()
    expect(page.locator("#main")).to_contain_text("The remote control server of Selenium allows automation testers to create a test infrastructure that is spread across multiple locations (including cloud) to drive the scripts on a large set of browsers.")
