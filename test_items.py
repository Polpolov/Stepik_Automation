import time

def test_find_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(5)
    # time.sleep(30)
    add_to_basket_button = browser.find_element_by_css_selector("body.default:nth-child(2) div.container-fluid."
                                                                "page:nth-child(3) div.page_inner div.content:nth-"
                                                                "child(3) article.product_page div.row:nth-child(1) "
                                                                "div.col-sm-6.product_main:nth-child(2) form.add-to-"
                                                                "basket:nth-child(6) > button.btn.btn-lg.btn-primary."
                                                                "btn-add-to-basket:nth-child(3)")
    assert add_to_basket_button.is_displayed(), "Add_to_basket_button is not displayed"


