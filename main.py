from selenium.webdriver.support.ui import WebDriverWait
import time

from config import URL, WAIT_TIME
from locators import HomePageLocators
from actions import (
    build_driver,
    fill_user_id_if_needed,
    click_when_ready,
    read_excel_values,
    search_value,
    process_all_pages_for_value,
    reset_for_next_search,
)

EXCEL_FILE = r'data.xlsx'


def main():
    driver = build_driver()
    wait = WebDriverWait(driver, WAIT_TIME)

    driver.get(URL)
    fill_user_id_if_needed(wait)

    click_when_ready(wait, HomePageLocators.SIR_CARD, "SIR card")
    click_when_ready(wait, HomePageLocators.NEXT_LINK, "Next link")

    values = read_excel_values(EXCEL_FILE, sheet_name="Sheet1")

    for value in values:
        print(f"\n========== Processing value: {value} ==========")
        # reset_for_next_search(driver, wait)
        # search_value(driver, wait, value)
        driver.refresh()

        # wait until page is ready again
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(5)
        ok = search_value(driver, wait, value)
        if not ok:
            print(f"{value} | moving to next value")
            continue
        process_all_pages_for_value(driver, wait, value)

    print("All Excel values processed.")


if __name__ == "__main__":
    main()
    