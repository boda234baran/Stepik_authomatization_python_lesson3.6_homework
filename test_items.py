import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_card_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert (button > 0), "корзинка не найдена"
    time.sleep(10)