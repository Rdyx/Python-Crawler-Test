# WiSEED Crawler Test
## How To

*Assuming you already have Python, Scraby and Apache installed on your machine*
#### **Don't forget to enable** _Cross-Origin Resource Sharing_ **add-on for your browser !**

1. Open your console, go into your project folder
2. Type **virtualenv venv**
3. Activate your virtual environnement with **source venv/bin/activate** (P.s : to desactivate, type **deactivate**)
4. Type **scrapy runspider testCrawlingWiseed.py -s FEED_EXPORT_ENCODING=utf-8 -o project.json** (This will run *testCrawlingWiseed.py* script to create the *.json* with corresponding schema you will get later, utf-8 is to avoid problems with accents)
5. Copy the **project.json** file from your *project folder* into your *server* (local or not)
6. Check if your **localhost URL** is same than the one in **app.js** (using MAMP on MacOSX here, may vary for you)
7. Open **index.html** and click on the search button