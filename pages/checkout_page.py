class CheckOut:
    def __init__(self, page):
        self.page = page
        #add to cart
        self.add_to_cart_btn = page.locator("[data-test='add-to-cart']")
        self.cart_badge = page.locator("[data-test='cart-quantity']")
        #fill billing address
        self.postal_code = page.locator("[data-test='postal_code']")
        self.house_no = page.locator("[data-test='house_number']")
        #checkout
        self.cart_btn = page.locator("[data-test='nav-cart']")
        self.proceed_1_btn = page.locator("[data-test='proceed-1']")
        self.proceed_2_btn = page.locator("[data-test='proceed-2']")
        self.proceed_3_btn = page.locator("[data-test='proceed-3']")
        self.check_payment_btn = page.locator("[data-test='finish']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.payment_success_msg = page.locator("[data-test='payment-success-message']")
        

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def go_to_cart(self):
        self.cart_btn.click()

    def proceed_buttons(self):
        self.proceed_1_btn.click()
        self.proceed_2_btn.click()

    def fill_address(self, country_name: str, postal_code: str, house_no: str):
        self.page.locator("[data-test='country']").select_option(label=country_name)
        self.postal_code.fill(postal_code)
        self.house_no.fill(house_no)
        self.proceed_3_btn.click()

    def cod(self):
        self.page.locator("[data-test='payment-method']").select_option(label="Cash on Delivery")
        self.check_payment_btn.click()

    def bank_transfer(self, bank_name, acc_name, acc_no):
        self.page.locator("[data-test='payment-method']").select_option(label="Bank Transfer")
        self.page.locator("[data-test='bank_name']").fill(bank_name)
        self.page.locator("[data-test='account_name']").fill(acc_name)
        self.page.locator("[data-test='account_number']").fill(acc_no)
        self.check_payment_btn.click()

    def cc(self, card_no, exp, cvv, card_name):
        self.page.locator("[data-test='payment-method']").select_option(label="Credit Card")
        self.page.locator("[data-test='credit_card_number']").fill(card_no)
        self.page.locator("[data-test='expiration_date']").fill(exp)
        self.page.locator("[data-test='cvv']").fill(cvv)
        self.page.locator("[data-test='card_holder_name']").fill(card_name)
        self.check_payment_btn.click()

    def bnpl(self, month):
        self.page.locator("[data-test='payment-method']").select_option(label="Buy Now Pay Later")
        self.page.locator("[data-test='monthly_installments']").select_option(value=month)
        self.check_payment_btn.click()

    def gift_card(self, gift_no, code):
        self.page.locator("[data-test='payment-method']").select_option(label="Gift Card")
        self.page.locator("[data-test='gift_card_number']").fill(gift_no)
        self.page.locator("[data-test='validation_code']").fill(code)
        self.check_payment_btn.click()   

    def finish(self):
        self.finish_btn.click()