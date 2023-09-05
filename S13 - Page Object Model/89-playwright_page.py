from playwright.sync_api import Page, Locator


class PlaywrightPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://playwright.dev/python")

        self.docs_link = self.page.get_by_role(
            "link", name="Docs"
        )

        self.search_input = self.page.get_by_placeholder("Search docs")

    
    def visit_docs(self):
        self.docs_link.click()


    def search(self, query):
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)


    def search_results(self) -> Locator:
        print("Search Results:")
        for result in self.page.locator("span.DocSearch-Hit-title").all():
            print(result.inner_text())

        return self.page.locator("div.DocSearch-Dropdown")