#Script created by Kraftytek
#Reddit API image scraper
import praw
import urllib.request
import time
import datetime
import cleanDupes

#create list of reddit pages that you would like to scrape images from in the following format ["page1", "page2", "Page3"]
pageNum = 0
todayz = str(datetime.datetime.now())
savePath = "E:\\python\\backgrounds\\"

#get list of pages to scrape images from
with open("prawpages.txt", "r") as p:    
    pageList = p.read().split('\n')

#prawkey configured same order as connection bellow with each being on a new line 
with open("prawkey.txt", "r") as f:
    lines = f.read().split('\n')

#create a function to perform the scrape
def pageScrape():
    count = 0
    #provide connection information for API access
    reddit = praw.Reddit(
        client_id=lines[0],
        client_secret=lines[1],
        user_agent=lines[2],
    )
    print(pageList[pageNum])
    
    for submission in reddit.subreddit(pageList[pageNum]).hot(limit=60):
     
        textString = str(submission.title)
        texturl = str(submission.url)
        textArray.append({'text':textString, 'url':texturl}) 
     
        df = pd.DataFrame(textArray)  

        df.to_csv("e:/python/Scrapes/data_scrape.csv", index=False, header=False)   
  
#Loop through provided pages using the function   
for i in pageList:
    pageScrape()
    time.sleep(3)
    pageNum += 1   

        