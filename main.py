import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MailAutomate:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def login(self, login, password):
        try:
            self.driver.get(url='https://mail.ru/')
            # push the button: Sign in
            sign_in_btn = self.driver.find_element(By.CLASS_NAME, 'ph-login').click()
            time.sleep(2)
            # store iframe web element
            iframe = self.driver.find_element(By.CLASS_NAME, "ag-popup__frame__layout__iframe")
            # switch to selected iframe
            self.driver.switch_to.frame(iframe)
            # fill out input element: username
            self.driver.find_element(By.NAME, "username").send_keys(login)
            time.sleep(2)
            # push the button: Enter password
            self.driver.find_element(By.XPATH, "//button[@data-test-id='next-button']").click()
            time.sleep(2)
            # fill out input element: password
            self.driver.find_element(By.NAME, "password").send_keys(password)
            time.sleep(2)
            # push the button: Sign in
            self.driver.find_element(By.XPATH, "//button[@data-test-id='submit-button']").click()
        except Exception as ex:
            print(ex)
        finally:
            time.sleep(100)
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    mail = MailAutomate()
    mail.login('login', 'password')
