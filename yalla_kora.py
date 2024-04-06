from bs4 import BeautifulSoup
import requests
import csv


date = input("Please enter the data in this format MMDDYYYY needed for the champion: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")
#print(site.status_code)
def main(page):
    """
        this function is where we gonna finish our main work
    """
    if page.status_code == 200:
        src = page.content
        soup = BeautifulSoup(src, 'lxml')
        matches_detail = []
        championships = soup.find_all('div', {'class': 'matchCard'})

    def scraping_match_info(championships):
        """
        """
        championship_title = championships[1].find('h2').text.strip()
        print(championship_title)

    scraping_match_info(championships)         

main(page=page)