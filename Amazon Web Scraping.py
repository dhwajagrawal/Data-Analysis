#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries 
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[6]:


# Connect to Website and pull in data

url='https://www.amazon.com/Feelin-Good-Tees-There-Light/dp/B017AO6XHW/ref=d_pd_di_sccai_cn_sccl_1_1/147-9290675-7604003?pd_rd_w=Re70O&content-id=amzn1.sym.e13de93e-5518-4644-8e6b-4ee5f2e0b062&pf_rd_p=e13de93e-5518-4644-8e6b-4ee5f2e0b062&pf_rd_r=42T201WVH1HTRZ2NB65J&pd_rd_wg=zojZi&pd_rd_r=bea56b9a-788d-4a9b-bb44-83cef343a9f0&pd_rd_i=B017AO6XHW&psc=1'
req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
html_page = urlopen(req).read()

soup1 = BeautifulSoup(html_page, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='price_inside_buybox').get_text()


print(title)
print (price)


# In[7]:


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[8]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[9]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[16]:


import pandas as pd

df = pd.read_csv(r'C:\Users\dh212182\OneDrive - Dunnhumby Ltd\Desktop\Projects\AmazonWebScraper\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


#Combine all of the above code into one function


def check_price():

          url='https://www.amazon.com/Feelin-Good-Tees-There-Light/dp/B017AO6XHW/ref=d_pd_di_sccai_cn_sccl_1_1/147-9290675-7604003?pd_rd_w=Re70O&content-id=amzn1.sym.e13de93e-5518-4644-8e6b-4ee5f2e0b062&pf_rd_p=e13de93e-5518-4644-8e6b-4ee5f2e0b062&pf_rd_r=42T201WVH1HTRZ2NB65J&pd_rd_wg=zojZi&pd_rd_r=bea56b9a-788d-4a9b-bb44-83cef343a9f0&pd_rd_i=B017AO6XHW&psc=1'
          req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
          html_page = urlopen(req).read()

          soup1 = BeautifulSoup(html_page, 'html.parser')

          soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

          title = soup2.find(id='productTitle').get_text()

          price = soup2.find(id='price_inside_buybox').get_text()

          price = price.strip()[1:]
          title = title.strip()
        
        
          print(title)
          print (price)
          
          import datetime

          today = datetime.date.today()
    
          import csv 

          header = ['Title', 'Price', 'Date']
          data = [title, price, today]

          with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
               writer = csv.writer(f)
               writer.writerow(data)  


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\alexf\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('dhwajsankar@gmail.com','Dr@vid2702')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'dhwajsankar@gmail.com',
        msg
     
    )


# In[ ]:




