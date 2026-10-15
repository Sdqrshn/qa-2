from pages.login_page import LoginPage
from pages.account_page import AccountPage
from playwright.sync_api import expect

def test_successful_login(page):
    login = LoginPage(page)
    acc = AccountPage(page)
    login.navigate()
    login.login("customer2@practicesoftwaretesting.com", "welcome01")

    expect(acc.user_menu).to_be_visible()

def test_login_error(page):
    login = LoginPage(page)
    login.navigate()
    login.login("random@mail", "random")

    expect(login.inv_cred).to_be_visible()