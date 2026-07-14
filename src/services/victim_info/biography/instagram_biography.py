from .AbstractBiography import AbstractBiography
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio

class InstagramAbstractBiography(AbstractBiography):
    def __init__(self, driver, username):
        super().__init__()

        self.driver = driver
        self.username = username

    async def get_biography(self, username: str) -> str:
        print(f"Checking Instagram for: {self.username}")
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, "//meta[@property='og:description']")))
            bio = self.driver.find_element(By.XPATH, "//meta[@property='og:description']").get_attribute("content")
            print("[+] Bio found:", bio)
        except:
            print("[-] Bio not found")

        await asyncio.sleep(10)