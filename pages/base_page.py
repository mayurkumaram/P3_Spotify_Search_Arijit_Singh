from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def fill(self, selector: str, value: str):
        self.page.wait_for_selector(selector, timeout=60000)
        self.page.fill(selector, value)

    def press_enter(self):
        self.page.keyboard.press("Enter")

    def click(self, selector: str):
        self.page.wait_for_selector(selector, timeout=60000)
        self.page.click(selector)

    def screenshot(self, name: str):
        self.page.wait_for_load_state("networkidle")
        self.page.screenshot(path=name)
