class LoginPage:
    def __init__(self, page):
        self.page = page
        self.sign_in_button = page.locator("[data-test='nav-sign-in']")
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".btnSubmit")
        self.inv_cred = page.locator("[data-test='login-error']")

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")
        self.page.wait_for_load_state("networkidle")

    def login(self, email, password):
        self.sign_in_button.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()


    