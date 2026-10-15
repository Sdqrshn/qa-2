import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.account_page import AccountPage

@pytest.fixture
def logged_in_page(page):
    """Fixture to auto log-in"""
    login = LoginPage(page)
    acc = AccountPage(page)
    
    login.navigate()
    login.login("customer2@practicesoftwaretesting.com", "welcome01")
    
    expect(acc.user_menu).to_be_visible()
    
    return page