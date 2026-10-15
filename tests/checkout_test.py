import pytest
from playwright.sync_api import expect
from pages.checkout_page import CheckOut
from pages.catalog_page import Catalog

@pytest.fixture
def checkout_at_payment(logged_in_page):
    catalog = Catalog(logged_in_page)
    checkout = CheckOut(logged_in_page)
    
    catalog.select_item()
    checkout.add_to_cart()
    expect(checkout.cart_badge).not_to_have_text("0")
    checkout.go_to_cart()
    checkout.proceed_buttons()
    checkout.fill_address("India", "12345", "42")

    yield checkout
    
    expect(checkout.payment_success_msg).to_have_text("Payment was successful")
    checkout.finish()

def test_cod(checkout_at_payment):
    checkout_at_payment.cod()

def test_bank_transfer(checkout_at_payment):
    checkout_at_payment.bank_transfer("World Bank", "John Doe", "1234567890")

def test_cc(checkout_at_payment):
    checkout_at_payment.cc("1234-5678-9000-0000", "03/9999", "333", "John Doe")

def test_bnpl(checkout_at_payment):
    checkout_at_payment.bnpl("12")


def test_gift_card(checkout_at_payment):
    checkout_at_payment.gift_card("12345qwertgh78jk90", "1a1a")