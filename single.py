# ~ Import packages ~ #
from google_patent_scraper import scraper_class
import json


# ~ Initialize scraper class ~ #
scraper=scraper_class() 

# ~~ Scrape patents individually ~~ #
patent_1 = 'US20160180719A1'
err_1, soup_1, url_1 = scraper.request_single_patent(patent_1)

# ~ Parse results of scrape ~ #
patent_1_parsed = scraper.get_scraped_data(soup_1,patent_1,url_1)



for inventor in json.loads(patent_1_parsed['inventor_name']):
    print(inventor['inventor_name'])

print(patent_1_parsed["grant_date"])

print(patent_1_parsed["patent"])


#print(patent_1_parsed)
