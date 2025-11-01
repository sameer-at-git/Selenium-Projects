from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

class TechSitesScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape_pesto(self):
        url = "https://pesto.tech/resources/top-10-websites-for-keeping-up-with-tech-news-in-2024"
        self.driver.get(url)
        time.sleep(3)
        sites = []
        # all links inside main content area
        links = self.driver.find_elements(By.XPATH, "//div[contains(@class,'post-content')]//a")
        count = 0
        for link in links:
            href = link.get_attribute("href")
            text = link.text.strip()
            if href.startswith("http") and text and count < 10:
                sites.append([count + 1, text, href, "Pesto Tech"])
                count += 1
        return sites

    def scrape_grafdom(self):
        url = "https://www.grafdom.com/blog/top-20-best-tech-websites-and-blogs/"
        self.driver.get(url)
        time.sleep(3)
        sites = []
        # links inside blog content
        links = self.driver.find_elements(By.XPATH, "//div[contains(@class,'entry-content')]//a")
        count = 0
        for link in links:
            href = link.get_attribute("href")
            text = link.text.strip()
            if href.startswith("http") and text and count < 20:
                sites.append([count + 1, text, href, "Grafdom"])
                count += 1
        return sites

if __name__ == "__main__":
    scraper = TechSitesScraper()
    pesto_sites = scraper.scrape_pesto()
    grafdom_sites = scraper.scrape_grafdom()
    scraper.driver.quit()

    all_sites = pesto_sites + grafdom_sites

    with open("top_tech_websites.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Name", "URL", "Source"])
        writer.writerows(all_sites)

    print(f"Scraped total {len(all_sites)} technology websites.")
    for site in all_sites:
        print(f"{site[0]}. {site[1]} - {site[2]} ({site[3]})")
