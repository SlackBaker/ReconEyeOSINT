from .AbstractBiography import AbstractBiography
import time

class FacebookAbstractBiography(AbstractBiography):
    def __init__(self, driver, username):
        super().__init__()
        self.driver = driver
        self.username = username


    def get_biography(self, username:str) -> str:
        print(f"Checking Facebook for: {self.username}")
        self.driver.get(f"https://www.facebook.com/{self.username}")
        time.sleep(30)  # Даємо час завантажитись
