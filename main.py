import urllib.request
from bs4 import BeautifulSoup
#import re
#import csv
import url

print(url.request_get('https://s.taobao.com/list',{'q':'秋装新品','cat':16,'style':'grid','seller_type':'taobao','sort':'sale-desc'}))
