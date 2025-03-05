from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up ChromeOptions for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
  # Navigate to the URL
  url = "https://ucla-all.policystat.com/?lt=Vf6IG3FeF6rEiJ4HvE8Ydy&next=%2Fpolicy%2F15544019%2Flatest%2F"
  driver.get(url)

  # Wait up to 60 seconds for window.pageState to be 'Loaded'
  wait = WebDriverWait(driver, 60)
  wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
  # Extract the fully rendered page source
  content = driver.page_source
  print(content)

except TimeoutException:
  print("Timed out after 60 seconds. The page may not have set window.pageState to 'Loaded'.")
finally:
  # Close the browser
  driver.quit()


breakpoint()
