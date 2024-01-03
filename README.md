# NFL-Player-Stat-Webscraper-V2

## Introduction
This project demonstrates a basic approach to scraping data from tables within a dynamic webpage using selenium libraries in Python

## Features
- Uses selenium webdriver (Firefox) to scrape multiple dynamic webpage tables 
- Creates individual csv files for each NFL player category
- Adjust 'max_rows' to change the number of rows scraped per table (D/ST only has 32 rows)
  
## Installation
In console, 'pip install selenium' before running
  
## Usage
Simply run main.py and the program will open up an instance of Firefox to crawl through webpages from the URL list, create and update individual csv files for interpretation
## Structure and Components
- main.py: contains logic to initialize webdriver, scrape each page, and create/write to csv
## Detailed Functionality
- scrape_page(): uses webdriver to retrieve URL, parse HTML of each webpage, scrapes table headers/rows/data, appends to 'data' array
- to_csv(): uses csv writer to create and write data to individual csv files
- main(): for each url and file name in urls map, run scrape_page() and to_csv()  

## Table Key

## Contributions
Contributions to this project are welcome. Feel free to fork the repository, make changes, and submit pull requests.

## License
- N/A
## Acknowledgements
- FantasyPros -> https://www.fantasypros.com/
- Selenium -> https://www.selenium.dev/documentation/

## Contact
svela002@csusm.edu

