# pytest --language=es test_items.py
# pytest --language=fr test_items.py

import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_product_page_contains_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')

    assert button, '"Add to basket" button is not displayed on the page.'

