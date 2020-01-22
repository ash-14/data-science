import requests
import csv
from time import sleep
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from pprint import pprint

url = "https://www.ebay.com/b/Cell-Phone-Smartphone-Parts/43304/bn_151926?_pgn=1"
data = requests.get(url)
path = '//*[@id="w7-items[0]"]'

sleep(2)
# print(type(data))
byte_string = data.content
source_code = html.fromstring(byte_string)
# print(type(byte_string))
tree = source_code.xpath(path)
print(len(tree))
pprint(tree[0].text_content())
