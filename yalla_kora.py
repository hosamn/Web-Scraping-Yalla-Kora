from bs4 import BeautifulSoup
import requests
import csv


date = input("Please enter the data in this format MMDDYYYY needed for the champion: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")
#print(site.status_code)
def main(page):
    """
        this is the main function
    """
    
    matches_detail = []

    if page.status_code == 200:
        src = page.content
        soup = BeautifulSoup(src, 'lxml')
        championships = soup.find_all('div', {'class': 'matchCard'})
        number_of_championships = len(championships)
             
    def scraping_match_info(championships):
        """
        """
        championship_title = championships.find('div', class_="title").find('h2').text.strip()
        all_matches = championships.find_all('div', class_= 'teamsData')
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            #get teams name 
            teamA = all_matches[i].find('div', class_='teamA').text.strip()
            teamB = all_matches[i].find('div', class_='teamB').text.strip()
            
            #get matches score             
            match_result = all_matches[i].find('div', class_='MResult').find_all('span', class_='score')
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            #get matches time 
            match_time = all_matches[i].find('div', class_='MResult').find('span', class_='time')

            #save them in match_detail list
            matches_detail.append({
                "Championship Title": championship_title,
                "Team 1": teamA,
                "Team 2": teamB,
                "Score": score,
                "Timing": match_time
            })

    for i in range(number_of_championships):
        scraping_match_info(championships[i])    



main(page=page)