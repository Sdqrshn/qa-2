class AccountPage:
    def __init__(self, page):
        self.page = page
        self.user_menu = page.locator("[data-test='nav-menu']")