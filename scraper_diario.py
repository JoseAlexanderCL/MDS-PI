import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
from datetime import date, timedelta
import re
import scraper_lib.py


#Consumimos una la funcion que hace todo el proceso para el día de ayer
process_yesterday()