# ~ Import packages ~ #
from google_patent_scraper import scraper_class
import json


# ~ Initialize scraper class ~ #
scraper=scraper_class(return_abstract=True)  #<- TURN ON ABSTRACT TEXT  

# ~~ Scrape patents individually ~~ #
patent_1 = 'US20160180719A1'
err_1, soup_1, url_1 = scraper.request_single_patent(patent_1)

# ~ Parse results of scrape ~ #
patent_1_parsed = scraper.get_scraped_data(soup_1,patent_1,url_1)



for inventor in json.loads(patent_1_parsed['inventor_name']):
    print(inventor['inventor_name'])

print(patent_1_parsed["grant_date"])

print(patent_1_parsed["patent"])
print(patent_1_parsed["abstract_text"])

# print(patent_1_parsed["image_urls"])

for link in patent_1_parsed['image_urls']:
    print(link)


#print(patent_1_parsed)


#https://patentimages.storage.googleapis.com/ec/41/7b/76047542d0f945/US20160180719A1-20160623-D00003.png.  <full size
#https://patentimages.storage.googleapis.com/86/97/3f/4faca62a0cda7e/US20160180719A1-20160623-D00003.png    <thumbnail
#https://patentscope.wipo.int/search/en/detail.jsf?docId=US243297659 < possibly use this url to manually or scrape patent images