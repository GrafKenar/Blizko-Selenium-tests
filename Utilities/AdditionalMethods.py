from datetime import datetime
from Utilities.Settings import Settings


def get_total_sum_for_product(product_price, additional_products):
    """Вычисление итоговой суммы по товару и форматирование ее в тот вид, который отображается на странице"""
    product_sum = product_price * (1+additional_products)
    formated_sum = '{0:,}'.format(product_sum).replace(',', ' ').replace(".0", '') + " руб."
    return formated_sum


def get_screenshot(driver):
    now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    driver.save_screenshot(Settings.screenshot_folder + name_screenshot)
