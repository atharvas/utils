
# coding: utf-8
# <a href="https://colab.research.google.com/github/atharvas/utils/blob/master/bs4_bullshit_2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ## Imports

# In[ ]:


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import datetime
import time
from io import StringIO

# In[ ]:
greybook_link = "https://raw.github-dev.cs.illinois.edu/cs296-25-sp19/atharva2/master/hw3/graybook-cleaned.csv?token=AAAQK942-eJG7c5l48i7SY7HHxUxZWXyks5cyW8XwA%3D%3D"

profDF = pd.read_csv(greybook_link)


# ## Helper Functions

# In[ ]:
base_url = "https://www.ratemyprofessors.com"

def getProfMetrics(link):
  url = base_url + link
  source = requests.get(url).text
  soup = BeautifulSoup(source, 'lxml')
  ratings = soup.find_all("div", class_="grade")#.text
  return [i.text.strip() for i in ratings]

# getProfMetrics("/ShowRatings.jsp?tid=1462973")


# In[ ]:


def getProfRatings(name):
  url = base_url + "/search.jsp?queryBy=teacherName&queryoption=HEADER&query=" + name.replace(" ", "+") + "&" + "facetSearch=true"
  source = requests.get(url).text
  soup = BeautifulSoup(source, 'lxml')
  link = soup.find("ul", class_="listings")
  if link is None:
    return None
  profs = link.find_all("a")
  link = profs[len(profs) - 1]['href']
  prof_metrics = getProfMetrics(link)
  prof_metrics.append(name)
  retDF = pd.DataFrame(prof_metrics).T
  print(retDF.shape[1], end="\t")
  if retDF.shape[1] <= 3:
    return None
  retDF.columns = ["Rating", "Again", "Difficulty", "Name"] 
  return retDF

# getProfRatings("Nerissa Brown")


# In[ ]:


def reverse_name(name):
  parts = name.split(", ")
  parts[1] = parts[1].split(" ")[0]
  new_name = parts[1] + " " + parts[0]  
  return new_name


# In[ ]:


cleanDF = profDF[["Employee Name", "Primary Job Title", "Primary College", "Primary Department", "Salary"]]

mask = cleanDF['Primary Job Title'] != "???"
mask2 = cleanDF['Primary Department'] != "???"
mask3 = cleanDF['Primary Job Title'] != "???"

cleanDF = cleanDF.loc[mask & mask2 & mask3]
cleanDF['Employee Name'] = cleanDF['Employee Name'].apply(lambda x: reverse_name(x))
profs = cleanDF['Employee Name'].tolist()


# In[ ]:

sleep_list = np.arange(0,10,0.5)
huge_df = list()

for prof in profs:
  print(prof, end=":\t")
  time.sleep(np.random.choice(sleep_list)) # wait some seconds before making each request to prevent DDOSing their site.
  rating = getProfRatings(prof)
  print("")
  if rating is not None:
    huge_df.append(rating)

huge_df = pd.concat(huge_df)
huge_df.to_csv("muh_data.csv")