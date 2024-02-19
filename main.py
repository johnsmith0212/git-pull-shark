import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

user_profile_path = 'C:/Users/Believe/AppData/Local/Google/Chrome/User Data/Profile 2'
chrome_options.add_argument(f"user-data-dir={user_profile_path}")

totalNum = 900

def run_script():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        driver.get("https://github.com/johnsmith0212/johnsmith0212/edit/main/README.md")

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.ͼ7')))

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

        # Commit change
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-hotkey="Mod+s"][data-no-visuals="true"]')))
        button.click()

        # New branch select
        radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="radio"])[2]')))
        radio_button.click()

        # Propose change
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'types__StyledButton-sc-ws60qy-0.jutTtW')))
        button.click()

        # Create pull request
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hx_create-pr-button')))
        button.click()

        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'merge-box-button')))
        button.click()

        # Merge pull request
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-merge-commit-button')))
        button.click()

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space(text())="Delete branch"]')))
    except Exception as e:
        print(e)

    finally:
        driver.quit()

# Repeat the code 10 times
for _ in range(totalNum):
    run_script()
