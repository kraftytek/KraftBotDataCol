#Script created by Kraftytek
import praw
import urllib.request
import pandas as pd
import time
import pyodbc
import datetime

pageNum = 0

#get list of pages to scrape images from
with open("prawpages.txt", "r") as p:    
    pageList = p.read().split('\n')

#prawkey configured same order as connection bellow with each being on a new line 
with open("prawkey.txt", "r") as f:
    lines = f.read().split('\n')
    
#with open("sqlConnect.txt", "r") as g:
#    sqlLines = g.read().split('\n')

#create a function to perform the scrape
      
def scrapeToDB():
    
    reddit = praw.Reddit(
        client_id=lines[0],
        client_secret=lines[1],
        user_agent=lines[2],
    )
     
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql.kraftytek.ca;DATABASE=ApiDump;UID=sa;PWD=S!lver88')
    cursor = conn.cursor()
    print(conn)
    
    for submission in reddit.subreddit(pageList[pageNum]).hot(limit=1000):        
        
        textString = "[" + submission.title + "]"
        
        query = "insert into dataDumper(dataString, datestamp) values(?, getdate())"    
        data = (textString)
        cursor.execute(query, data)
        conn.commit()  
        
#Loop through provided pages using the function   
for i in pageList:
    print("Scraping: " + pageList[pageNum]) 
    scrapeToDB()
    time.sleep(3)
    pageNum += 1   

        