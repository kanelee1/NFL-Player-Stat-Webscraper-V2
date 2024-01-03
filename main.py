from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv


driver = webdriver.Firefox(options=Options()) # initialize Firefox webdriver
driver.implicitly_wait(1)   # wait 1 sec for webpage to load


# map urls to respective CSV filenames
urls = {
    'https://www.fantasypros.com/nfl/stats/qb.php?scoring=PPR': 'qb.csv',
    'https://www.fantasypros.com/nfl/stats/rb.php?scoring=PPR': 'rb.csv',
    'https://www.fantasypros.com/nfl/stats/wr.php?scoring=PPR': 'wr.csv',
    'https://www.fantasypros.com/nfl/stats/te.php?scoring=PPR': 'te.csv',
    'https://www.fantasypros.com/nfl/stats/k.php?scoring=PPR': 'k.csv',
    'https://www.fantasypros.com/nfl/stats/dst.php?scoring=PPR': 'dst.csv',
}


def scrape_page(url, max_rows=50):

    driver.get(url) 
    data = []

    # find table body element
    tbody = driver.find_element(By.XPATH, '//*[@id="data"]/tbody')

    # extract table headers:
    # QB thru TE 
    if 'qb.php' in url or 'rb.php' in url or 'wr.php' in url or 'te.php' in url: 
        header_row = driver.find_element(By.XPATH, '//*[@id="data"]/thead/tr[2]')
        headers = [header.text for header in header_row.find_elements(By.TAG_NAME, 'th')] 
    # K and D/DST
    else:
        header_row = driver.find_element(By.XPATH, '//*[@id="data"]/thead')
        headers = [header.text for header in header_row.find_elements(By.TAG_NAME, 'th')]
    
    data.append(headers) 

    # find table rows in tbody
    rows = tbody.find_elements(By.XPATH, './/tr')[:max_rows]  # Limiting rows to max_rows

    for tr in rows:
        # extract table data into 'row'
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
        data.append(row)
    return data

    
def to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)    # initialize csv writer
        csv_writer.writerows(data)          # write data to file


def main():
    for url, filename in urls.items():
        data = scrape_page(url) 
        to_csv(data, filename)
        

if __name__ == "__main__":
    main()
    print('Done!')
