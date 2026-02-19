from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
    
    def wait_for_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_url_contains(self, url_part: str):
        self.page.wait_for_url(f"**/{url_part}/**")

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()