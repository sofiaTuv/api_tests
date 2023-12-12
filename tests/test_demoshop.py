from allure_commons._allure import step
from selene import browser, have

from page.demowebshop_api import DemoWebshopAPI


def test_add_1_item_to_cart_with_api(browser_setup):
    response = DemoWebshopAPI.api_request_post('/addproducttocart/catalog/31/1/1',
                                               data={"addtocart_31.EnteredQuantity": 1})
    DemoWebshopAPI.get_and_set_cookie(response)

    with step('Open cart'):
        browser.open('/cart')

    with step('Check one product'):
        browser.all('.cart-item-row').should(have.size(1))
        browser.element('.cart-item-row').should(have.text('14.1-inch Laptop'))
        browser.element('[name^="itemquantity"]').should(have.value('1'))


def test_add_10_items_to_cart_with_api(browser_setup):
    response = DemoWebshopAPI.api_request_post('/addproducttocart/details/45/1',
                                               data={"addtocart_45.EnteredQuantity": 10})

    DemoWebshopAPI.get_and_set_cookie(response)

    with step("Open cart"):
        browser.open('/cart')

    with step('Check ten products'):
        browser.all('.cart-item-row').should(have.size(1))
        browser.element('.cart-item-row').should(have.text('Fiction'))
        browser.element('[name^="itemquantity"]').should(have.value('10'))
        browser.element('.product-unit-price').should(have.text('24.00'))
    with step("Check total"):
        browser.element('.cart-total-right').should(have.text('240.00'))
