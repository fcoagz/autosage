import pickle
import tempfile
import platform
import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from autosage.public.page import Poe
from autosage.exception.invalid_exceptions import (
    InvalidEmailException,
    InvalidPasswordException
    )

class Client:
    def __init__(
            self,
            name_session: str = 'my_account',
            email: str = None
    ):
        self.name_session = name_session
        self.email = email
        self.cookies = f'{tempfile.gettempdir()}/{self.name_session}.cookies'

    def _cookies(self):
        if os.path.isfile(self.cookies):
            cookies = pickle.load(open(self.cookies, 'rb'))
            for cookie in cookies:
                try:
                    self.driver.add_cookie(cookie)
                except:
                    return False
            self.driver.get('https://poe.com/')

            return True

    def connect(self):
        self.driver = Poe().driver
        self.driver.get('https://poe.com/')
        self.wait = WebDriverWait(self.driver, 30)

        if not self._cookies():
            if self.email is None:
                while True:
                    value = input('Introduzca el correo electrónico:')
                    if not value:
                        continue

                    self.email = value
                    break

            enter_email = self.wait.until(
                expected.element_to_be_clickable((
                    By.XPATH, '//button[@class="Button_buttonBase__0QP_m Button_flat__1hj0f undefined"]'
                ))
            )
            enter_email.click()

            self._add_email = self.wait.until(
                expected.element_to_be_clickable((
                    By.XPATH, '//input[@placeholder="Email address"]'
                ))
            )
            self._add_email.send_keys(self.email)
            self._add_email.send_keys(Keys.RETURN)

            while True:
                try:
                    if self.driver.find_element(By.XPATH, '//span[@class="LoadingDots_loader__aMPLK"]'):
                        continue
                except:
                    break 
            try: 
                if self.driver.find_element(By.XPATH, '//div[@class="InfoText_infoText__Coy92 InfoText_error__OQwmg"]').text == 'The email you entered is not valid. Please try again.':
                        raise InvalidEmailException('Invalid email address.') 
            except: pass   
            
    def send_verification_code(self, verification_code: str):
        add_code = self.wait.until(
            expected.element_to_be_clickable((
                By.XPATH, '//input[@placeholder="Code"]'
            ))
        )
        add_code.send_keys(verification_code)
        add_code.send_keys(Keys.RETURN)
        
        while True:
            try:
                if self.driver.find_element(By.XPATH, '//span[@class="LoadingDots_loader__aMPLK"]'):
                    continue
            except:
                break
        try:
            if self.driver.find_element(By.XPATH, '//div[@class="InfoText_infoText__Coy92 InfoText_error__OQwmg"]').text:
                raise InvalidPasswordException('The code you entered is not valid.')
        except:
            pickle.dump(self.driver.get_cookies(), open(self.cookies, 'wb'))

    def sage(self, prompt: str):
        self.prompt = prompt

        add_message = self.wait.until(
            expected.element_to_be_clickable((
                By.XPATH, '//textarea[@placeholder="Type a message..."]'
            ))
        )
        add_message.send_keys(self.prompt)

        send_message = self.wait.until(
            expected.element_to_be_clickable((
                By.XPATH, '//button[@class="Button_buttonBase__0QP_m Button_primary__pIDjn ChatMessageInputView_sendButton__reEpT"]'
            ))
        )
        send_message.click()

        while True:
            try:
                if self.driver.find_element(By.XPATH, '//button[@class="Button_buttonBase__0QP_m Button_tertiary__yq3dG undefined"]').text == 'Like':
                    break
            except:
                continue

        response = self.driver.find_elements(By.XPATH, '//div[@class="Message_botMessageBubble__CPGMI "]')[-1].text

        return response
