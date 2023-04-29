import os
import platform
import requests
from bs4 import BeautifulSoup
import urllib.request
import zipfile

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PATH = 'autosage/lib/chromedriver'

def status_code_and_return_content(response: requests.Response):
    if not response.status_code == requests.codes.ok:
        raise ValueError('Unsuccessful communication with chromedriver server.')
    
    return response.content

def get_version_by_class(soup: BeautifulSoup):
    specific_version = []
    versions = soup.find_all("span", "C9DxTc aw5Odc")
    for version in versions:
        specific_version.append(version.text.strip().split(' ')[-1])
        
    return specific_version[1]

class ChromeDriver:
    url_page = 'https://chromedriver.chromium.org/downloads'
    url_api = 'https://chromedriver.storage.googleapis.com/{0}/chromedriver_{1}.zip'

    def get_version(self):
        response = status_code_and_return_content(
            requests.get(self.url_page)
        )
        soup = BeautifulSoup(response, 'html.parser')
        section_current_releases = soup.find(
            "div", "tyJCtd mGzaTb Depvyb baZpAe"
        )
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        if platform.system() == 'Windows':
            self.url_api = self.url_api.format(get_version_by_class(section_current_releases), 'win32')
        elif platform.system() == 'Linux':
            self.url_api = self.url_api.format(get_version_by_class(section_current_releases), 'linux64')
        print(self.url_api)
        urllib.request.urlretrieve(self.url_api, PATH + '/chromedriver.zip')

        with zipfile.ZipFile(PATH + '/chromedriver.zip', 'r') as zip_ref:
            zip_ref.extractall(PATH)

def file_chrome_driver():
    if not os.path.isfile(PATH + '/chromedriver.zip'):
        ChromeDriver().get_version()
        
        return Service('autosage/lib/chromedriver/chromedriver') 
    return Service('autosage/lib/chromedriver/chromedriver') 

service = file_chrome_driver()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

class Poe:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )