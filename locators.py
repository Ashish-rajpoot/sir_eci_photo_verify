from selenium.webdriver.common.by import By

class LoginPageLocators:
    USER_ID = (By.NAME, "userId")


class HomePageLocators:
    SIR_CARD = (By.XPATH, '//*[@id="textContent"]/div[2]/div/a[1]')
    NEXT_LINK = (By.XPATH, '//*[@id="textContent"]/div[2]/div/div[2]/div/div/div[5]/div[2]/a')


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, '//*[@id="react-select-2-input"]')
    # SEARCH_BUTTON = (By.XPATH, '//*[@id="tabWrapper"]/div/div[2]/div/button')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="tabWrapper"]/div[1]/div[2]/div/button')

    TABLE = (By.XPATH, '//*[@id="tabWrapper"]/div[3]/div/table[1]')
    TABLE_ROWS = (By.XPATH, '//*[@id="tabWrapper"]/div[3]/div/table[1]/tbody/tr')

    POPUP = (By.XPATH, '//*[@id="customModal"]')

    NEXT_PAGE_BUTTON = (By.XPATH, '//*[@id="tabWrapper"]/div[4]/div/div/button[3]')
    FIRST_PAGE_BUTTON = (By.XPATH, '//*[@id="tabWrapper"]/div[4]/div/div/button[1]')
