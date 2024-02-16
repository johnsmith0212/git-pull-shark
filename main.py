import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--log-level=INFO')

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

user_profile_path = 'C:/Users/Believe/AppData/Local/Google/Chrome/User Data/Profile 2'
chrome_options.add_argument(f"user-data-dir={user_profile_path}")

def run_script():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get("https://github.com/johnsmith0212/johnsmith0212/edit/main/README.md")
    time.sleep(4)
    # Text change
    script = """
    var spanElement = document.querySelector('span.ͼ7');
    if (spanElement) {
         var currentContent = spanElement.textContent;
         var modifiedContent = currentContent + '1';
         spanElement.textContent = modifiedContent;
    }
    """
    driver.execute_script(script)
    time.sleep(1)
    # Commit change
    button = driver.find_element(By.CSS_SELECTOR, 'button[data-hotkey="Mod+s"][data-no-visuals="true"]')
    button.click()
    time.sleep(4)
    # New branch select
    radio_button = driver.find_element(By.ID, ':rg:')
    radio_button.click()
    time.sleep(1)
    # Propose change
    button = driver.find_element(By.CLASS_NAME, 'types__StyledButton-sc-ws60qy-0.jutTtW')
    button.click()
    time.sleep(5)
    # Create pull request
    button = driver.find_element(By.CLASS_NAME, 'hx_create-pr-button')
    button.click()
    time.sleep(5)

    button = driver.find_element(By.CLASS_NAME, 'merge-box-button')
    button.click()
    time.sleep(1)
    # Merge pull request
    button = driver.find_element(By.CLASS_NAME, 'js-merge-commit-button')
    button.click()
    time.sleep(5)
    driver.quit()
# Repeat the code 10 times
for _ in range(1024):
    run_script()
