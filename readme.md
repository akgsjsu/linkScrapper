# Link Scrapper

## Required: Python and Python libraries - Flask, requests, and BeautifulSoup

The core objective of this project is to develop a dynamic website capable of scanning and extracting all the hyperlinks present within a given webpage. To accomplish this, the project makes use of the Python programming language along with essential Python libraries such as Flask, requests, and BeautifulSoup.

When initiated, the project's main functionality is encapsulated within the "main.py" file. Executing this file triggers the web application to run, allowing users to interact with the website. Upon entering the URL of the desired webpage, the application sends a request to the provided URL through the "requests" library, fetching the HTML content of the page.

The retrieved HTML content is then processed by the "BeautifulSoup" library, which systematically extracts and identifies all the hyperlinks present within the page's HTML structure. These extracted links are collected and displayed on the website's interface, offering users a comprehensive list of the URLs contained on the entered webpage.
