#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the required libraries
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[ ]:


#importing the urls for plagiarism check
Scorebuddy_Blog_Urls = pd.read_csv(r"/Users/rajkupekar/Desktop/Copyscape_MII.csv",encoding="UTF-8")
URLs=Scorebuddy_Blog_Urls["URLs"]


# In[ ]:


#Creating empty list for outputs
Query=[]
Query_Words=[]
Query_Cost=[]
Query_Copies=[]
Plagiarized_With=[]
Matched_Words=[]
Copyscape_Result=[]
Pretiffied_Output=[]
i=1


# In[ ]:


#looping to the urls for plagiarism check
for url in URLs:
    response= requests.get("https://www.copyscape.com/api/?u=xxx&k=xxx&o=csearch&q={}".format(url))
    response_content= response.content
    response_soup= bs(response_content,'lxml')
    pretiffied_output=response_soup.prettify()
    Pretiffied_Output.append(pretiffied_output)
    
    try:
        query=response_soup.find("query").text
        Query.append(query)
    except:
        Query.append("error")
    
    try:
        query_words=response_soup.find("querywords").text
        Query_Words.append(query_words)
    except:
        Query_Words.append("error")
    
    try:
        query_cost=response_soup.find("cost").text
        Query_Cost.append(query_cost)
    except:
        Query_Cost.append("error")

    try:
        query_copies= response_soup.find("count").text
        Query_Copies.append(query_copies)
    except:
        Query_Copies.append("error")
        
    result_containers= response_soup.find_all('result')
    plagiarized_urls=[]
    matched_words=[]
    copyscape_results=[]
    for container in result_containers:
        try:
            plagiarized_url= container.find("url").text
            plagiarized_urls.append(plagiarized_url)
        except:
            plagiarized_urls.append("error")
    
        try:
            matched_word= container.find("minwordsmatched").text
            matched_words.append(matched_word)
        except:
            matched_words.append("error")
    
        try:
            copyscape_result= container.find("viewurl").text
            copyscape_results.append(copyscape_result)
        except:
            copyscape_results.append("error")
    
    Plagiarized_With.append(plagiarized_urls)
    Matched_Words.append(matched_words)
    Copyscape_Result.append(copyscape_results)
   
    print("Plagiarized url:",query,"Query Words:",query_words,"Query Copies:",query_copies)
    print("Done with:",i)
    i=i+1
    


# In[ ]:


#creating a dataframe for the appended output list
data = {
    "Query": Query,
    "Query_Words": Query_Words,
    "Query_Cost": Query_Cost,
    "Query_Copies": Query_Copies,
    "Plagiarized_With": Plagiarized_With,
    "Matched_Words": Matched_Words,
    "Copyscape_Result": Copyscape_Result,
    "Pretiffied_Output": Pretiffied_Output
}

df = pd.DataFrame(data)


# In[ ]:


#printing the top rows of the dataframe
df.head(30)


# In[ ]:


#writing the dataframe on local machine
df.to_csv(r'your desired path goes in here', index=False)


# In[ ]:





# In[ ]:




