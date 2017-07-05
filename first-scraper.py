from flask import Flask, request, jsonify





import requests
import time
from lxml import etree

headers = {
    'Host': 'www.princess.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    "Referer": "http://www.princess.com/find/searchResults.do",
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '774',
    'Cookie': '_aeu=QCQ=; _aes=QSE=; dl.VoyageCode=0:; AMCV_21C91F2F575539D07F000101%40AdobeOrg=2121618341%7CMCIDTS%7C17204%7CMCMID%7C56148300087290356482859637713502094010%7CMCAAMLH-1487002432%7C6%7CMCAAMB-1487002432%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1486404832s%7CNONE%7CMCAID%7CNONE; mbox=PC#2b923f84a1cd4a0e8ad851fb2eec5451.26_3#1487607233|check#true#1486397693|session#e73b4e0147284d5296ba09bfca7783b6#1486399493; _aeu=QCQ=; __utma=169354720.1711765063.1485711551.1485882831.1486397632.7; __utmz=169354720.1485711551.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); s_nr=1486397641878-Repeat; gds=1486397641878; _fby_site_=1%7Cprincess.com%7C1485711552%7C1485882825%7C1486397639%7C1486397639%7C6%7C1%7C18; _ga=GA1.2.1711765063.1485711551; edge_check=visitor%3Dprincess%2Canyone%3Dtrue%2Cvisitor%3Dcheck; aam_uuid=55696692255689471082814727618926176926; __atuvc=17%7C5%2C1%7C6; EG-U-ID=C7a0116ae4-9a68-4766-8c06-1166fe20c82b; uk_ok=true; JSESSIONID=0001B0iDVuYG2gCpSCVXUFxeh_G:181iiqqsv; _fipc_=bg; _fipz_=8000; loc=SH3HZ63UPZQNVLEJWSLBV33V6JJPW6PRWNZCOGFHBEJITNUJ7WC5BVEM7FXBROJJ2HPRPQPIYQHKVFQW3MAW3VSIAZWR7A3O4MTBKKQ; ak_bmsc=41791536346D078D71A646D4D262EE9E02148434C32E0000BFA098583C233900~plLpEOK9z7bMFxFooBbX8+fOQeRHGkc2HkJQRFDaxrncs+NhWllnlX1mB+0xQciOxfTmemr2THS7aOTffFt3TpWzYnsjw0wHsocNbpoS8WrUGJEuLRLvwUNDAERY4zbHO8nMXxFAwOQvYQ1kABD1zjK78JEHKalNHgINkR05AiS2f9O3ThqgwmYncWMjkCXcKPWsNUXSwZtseGMtGTZta751+P3Fuz6JJ2CFYzVK0CV5Y=; COOKIE_CHECK=YES; AMCVS_21C91F2F575539D07F000101%40AdobeOrg=1; _dl.event-cache=303270276:null; booking_engine_used=PCDIR; search_counter=1; __utmb=169354720.2.10.1486397632; __utmc=169354720; __utmt=1; getLocale=%7B%22specialOffers%22%3A%22false%22%2C%22status%22%3A%22%22%2C%22primaryCurrency%22%3A%22USD%22%2C%22country%22%3A%22BG%22%2C%22countryPhone%22%3A%22%22%2C%22isEU%22%3A%22true%22%2C%22brochures%22%3A%22false%22%2C%22lastUpdated%22%3A1486397631967%7D; _dc_gtm_UA-4086206-54=1; persistValue=null; s_dfa=crbrprincessprodus%2Ccrbrcarnivalbrandsprodus; __utmt_princess=1; s_ppn=pcl%3Acruise_shopping%3Asearch_results; s_ppvl=pcl%253Acruise_shopping%253Asearch_results%2C24%2C24%2C1700%2C1920%2C560%2C1920%2C1080%2C1%2CP; s_ppv=pcl%253Acruise_shopping%253Asearch_results%2C29%2C24%2C2099%2C1920%2C560%2C1920%2C1080%2C1%2CP; gds_s=Less%20than%207%20days; s_vnum=1488319200006%26vn%3D1; s_invisit=true; s_cc=true; _gat_UA-4086206-54=1; at_carnivalbrands=segments%3D5554399; EG-S-ID=B2a983dd5f-30c5-4e32-871c-60950792bc3e; __atuvs=5898a0c70824607c000',
    'Connection': 'keep-alive'
}

time = time.asctime(time.localtime(time.time()))
print time


#--------GameStop Info-----------
# print etree.tostring(root, pretty_print=True)
# page = requests.get('http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-gray-joy-con/141820, timeout=(2.0,2.0)')

# page = requests.get('http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-neon-blue-and-neon-red-joy-con/141887')
# root = etree.HTML(page.content)
#
# product = root.xpath('//h1[@class="grid_17 ats-prod-title"]/text()')
# price = root.xpath('//h3[@class="ats-prodBuy-price"]/span/text()')
# not_available = root.xpath('//div[@class="buttonna"]/a/span/text()')
# add_to_cart = root.xpath('//div[@class="button qq"]/div/a/span/text()')


#----------DONE-------------


#--------WALMART Info-----------
# page = requests.get('https://www.walmart.com/ip/Nintendo-Switch-Gaming-Console-with-Neon-Blue-and-Neon-Red-Joy-Con-N-A/55449981')
#----------------------------------


#--------Target Info-----------

page = requests.get('https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-52052007, allow_redirects=True, headers = headers, timeout=(2.0,2.0)')
print page
root = etree.HTML(page.content)
# print etree.tostring(root, pretty_print=True)
product = root.xpath('//div[@class="price"]/span/text()')
# price = root.xpath('//h3[@class="ats-prodBuy-price"]/span/text()')
# not_available = root.xpath('//div[@class="buttonna"]/a/span/text()')
# add_to_cart = root.xpath('//div[@class="button qq"]/div/a/span/text()')


#----------DONE-------------

print page.content



print product

# print price
# print not_available
# print add_to_cart

