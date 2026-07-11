from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sites = {
    "github": {
        "url": "https://github.com/search?q={}&type=users",
    },

    "reddit": {
        "url": "https://www.reddit.com/search/?q={}",
    },

    "youtube": {
        "url": "https://www.youtube.com/results?search_query={}",
    }
}
def findsimilar():
    nickname = input("Nickname: ")

    driver = webdriver.Chrome()

    for name, site in sites.items():

        url = site["url"].format(nickname)

        print(f"[+] Searching in {name}")

        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        if nickname.lower() in driver.page_source.lower():
            print(f"[FOUND] {name}")

        else:
            print(f"[NOT FOUND] {name}")

    driver.quit()
