# KraftBotDataCol
 kraftbot adapted to data analytics

This bot is designed to connect to a SQL database to store scraped data for later analytics. 

it uses 3 text files, prawkey.txt, prawPage.txt, and sqlConnect.txt

prawkey.txt needs to have your personal reddit api key in the following order:

client id
client secret
user agent

for more information read https://www.reddit.com/dev/api/

prawPage.txt is where you add the pages you want to scrape, enter one page per line like this:

page1
page2
page3
page4

sqlConnect.txt is your credentials to access the sql database

by default the database name should be ApiDump

the connection info should all be on one line and look like this:

DRIVER={ODBC Driver 17 for SQL Server};SERVER=<sql_server_ip or domain>;DATABASE=ApiDump;UID=<user_name>;PWD=<password>

the code is designed to create the table it uses if one does not exist, so no need to make one.
