class Catalog:
    def __init__(self, page):
        self.page = page
        self.out_of_stock_badge = page.locator("[data-test='out-of-stock']")
        
        self.click_item = (
            page.locator("a.card")
            .filter(has_not=self.out_of_stock_badge)
            .first
        )

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")
    
    def select_item(self):
        self.navigate()
        self.click_item.click()