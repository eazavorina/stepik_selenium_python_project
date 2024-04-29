from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_promo_url(self):
        assert '?promo=' in self.browser.current_url, (f"Current url {self.browser.current_url} "
                                                       f"does not contain '?promo=newYear'")

    def should_be_good_added_message(self):
        assert self.is_element_present(*ProductPageLocators.GOOD_ADDED_MESSAGE), ("Good added message "
                                                                                  "is not present")

    def should_be_correct_title(self):
        original_title = self.browser.find_element(*ProductPageLocators.ORIGINAL_TITLE).text
        good_added_message_title = self.browser.find_element(*ProductPageLocators.GOOD_ADDED_MESSAGE).text
        assert original_title == good_added_message_title, (f"Title in good added message '{good_added_message_title}'"
                                                            f" is not equal to original title '{original_title}'")

    def should_be_total_message(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_MESSAGE), "Total message is not present"

    def should_be_total_equal_to_price(self):
        original_price = self.browser.find_element(*ProductPageLocators.ORIGINAL_PRICE).text
        total_message_price = self.browser.find_element(*ProductPageLocators.TOTAL_MESSAGE).text
        assert original_price == total_message_price, (f"Total price in total message '{total_message_price}' is not "
                                                       f"equal to original price '{original_price}'")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.GOOD_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.GOOD_ADDED_MESSAGE), \
            "Success message is presented, but should disappear"
