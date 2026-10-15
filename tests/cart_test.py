from pages.catalog_page import Catalog
from pages.checkout_page import CheckOut
from playwright.sync_api import expect

def test_add_to_cart(page):
    checkout = CheckOut(page)
    catalog = Catalog(page)

    catalog.navigate()
    catalog.select_item()
    checkout.add_to_cart()
    expect(checkout.cart_badge).to_have_text("1")