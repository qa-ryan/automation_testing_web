from playwright.sync_api import Page, expect

class AccordionPage:
    URL = "https://www.automationtesting.co.uk/accordion.html"
    portability_text = "Testing is a repetitive process. The slightest modification in code must be tested to ensure that the software is providing the desired functionality and result. Repeating tests manually is a time consuming and costly process. Automated tests can be run repetitively at no additional costs. Selenium is a highly portable tool that runs on multiple platforms as well as browsers. It therefore allows automation engineers the ease of writing code without worrying about the platform on which it will run."
    language_support = "Software is written in a number of languages. One of the challenges faced by automated testers is integrating the automation tools with the development environment for CI. With Selenium bindings for Java, .NET, Ruby, Perl, Python, PHP, Groovy and JavaScript, it is very easy to integrate with the development environment."
    selenium_grid = "The remote control server of Selenium allows automation testers to create a test infrastructure that is spread across multiple locations (including cloud) to drive the scripts on a large set of browsers."
    headings = ["Platform Portability", "Language Support", "Selenium Grid"]
    
    def __init__(self, page: Page):
        self.page = page
        self.text_locator = page.locator("#main")
        
    def goto(self):
        self.page.goto(self.URL)
        
    def functionality(self):
        headings = self.headings
        for _ in range(5):   
            for heading in headings:
                self.page.get_by_text(heading).click()
                
    def content_validation(self):
        headings = self.headings
        for heading in headings:
            action = self.page.get_by_text(heading)
            action.click()
            if action == "Platform Portability":
                expect(self.text_locator).to_contain_text(self.portability_text)
            elif action == "Language Support":
                expect(self.text_locator).to_contain_text(self.language_support)
            else:
                expect(self.text_locator).to_contain_text(self.selenium_grid)

