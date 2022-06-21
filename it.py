
from fastapi import FastAPI, HTTPException

import re
from pydantic import AnyUrl, HttpUrl, ValidationError, BaseModel
import collections as _collections
from fastapi_health import health
from typing import Dict, Pattern
import timeit


import requests
from bs4 import BeautifulSoup

r: AnyUrl = requests.get('https://www.bbc.co.uk')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find('html').text
cc = re.sub('[^A-Za-z]+', ' ', links)
kk = cc.split()
print(dict(_collections.Counter(kk).most_common()))
