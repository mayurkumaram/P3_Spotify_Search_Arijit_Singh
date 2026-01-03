from pages.base_page import BasePage

class FeaturePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def search(self, text):
        self.fill("input#search, input[name='search_query'], input[type='search'], input[name='q']", text)

    def submit_search(self):
        self.press_enter()

    def wait_for_results(self):
        self.page.wait_for_load_state('networkidle')
