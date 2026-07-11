from src.services.victim_info.biography.facebook_biography import FacebookAbstractBiography
from src.services.victim_info.biography.instagram_biography import InstagramAbstractBiography
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def initialize():
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    try:
        driver = webdriver.Chrome(options=options)
    except:
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    username = input("Enter username: ")

    fb = FacebookAbstractBiography(driver, username)
    insta = InstagramAbstractBiography(driver, username)

    insta.get_biography(username)
    fb.get_biography(username)

    input("press enter to exit...")
    driver.quit()