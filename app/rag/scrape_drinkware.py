import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Target URL
url = "https://shop.zuscoffee.com/collections/tumbler"
driver.get(url)

# Wait for product cards to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "product-card")))

# Optional: scroll down to trigger lazy loading
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Get full rendered HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract product cards
cards = soup.select("product-card")

# Ensure output directory exists
output_path = "app/rag/data/drinkware.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write extracted data
with open(output_path, "w", encoding="utf-8") as f:
    for card in cards:
        title_tag = card.select_one(".product-card__title a")
        price_tag = card.select_one("sale-price")

        title = title_tag.text.strip() if title_tag else "No title"
        price = price_tag.text.strip() if price_tag else "No price"

        f.write(f"{title}: {price}\n")
        print(f"✅ {title} - {price}")

driver.quit()
print(f"\n✅ Done. Scraped products saved to {output_path}")
