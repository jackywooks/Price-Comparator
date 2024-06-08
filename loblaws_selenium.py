import re
import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 

# Define the Chrome webdriver options
options = webdriver.ChromeOptions() 
options.add_argument("--headless") # Set the Chrome webdriver to run in headless mode for scalability
#Will Get ssl handshake error when the browser asks you to accept the certificate from a website. 
#Can add options to ignore these errors by default in order avoid these errors.
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--ignore-ssl-errors')

# By default, Selenium waits for all resources to download before taking actions.
# However, we don't need it as the page is populated with dynamically generated JavaScript code.
options.page_load_strategy = "none"

# Pass the defined options objects to initialize the web driver 
driver = Chrome(options=options) 
# Set an implicit wait of 5 seconds to allow time for elements to appear before throwing an exception
driver.implicitly_wait(5)

URL = "https://www.loblaws.ca/collection/featured-items?icid=gr_weekly-flyer_productcarousel_0_hp"
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(6)

product_dict = {}

#find the product card root
product_cards = driver.find_elements(By.CSS_SELECTOR,"div.chakra-linkbox.css-vhnn8v")
# extract price and name element inside using find_element
for product_card in product_cards:
    name_raw = product_card.find_element(By.CSS_SELECTOR, "h3[data-testid='product-title']").text.strip()
    price_raw = product_card.find_element(By.CSS_SELECTOR, ".css-idkz9h").text.strip()
    # extract the price in the raw price text by regex, getting only numbers after the dollar sign
    match = re.search(r"\$(\d+\.\d+)", price_raw)
    # cast it to float
    price = float(''.join(match.group(1)))
    # append the price and product name in a dictionary
    product_dict[name_raw]=price

print(product_dict)
# next step is to handle the pagination, and store the info in a db

#helper function
##driver.page_source ->get the full html
f = open("html.txt", "w")
f.write(driver.page_source)
f.close()


driver.quit()