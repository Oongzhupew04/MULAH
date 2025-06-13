import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone


def get_headlines() :
    url = "https://www.theverge.com"
    titles = []


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else 'No Title Found'
    titles.append(title)

    for title in titles:
        print("Titles: ", title)





    base_url = 'https://www.theverge.com'
    seen_titles = set()
    cutoff_date = datetime(2022, 1, 1, tzinfo=timezone.utc)
    headlines = []
    headline_tag = soup.find_all('a', class_='_1lkmsmo1')
    time_tag = soup.find('time')

    if headline_tag and time_tag and time_tag.has_attr('datetime'):
        article_date = datetime.fromisoformat(time_tag['datetime'])
        if article_date >= cutoff_date:
            for hdline_tag in headline_tag:
                headline = hdline_tag.get_text(strip=True)
                href = hdline_tag.get('href')
                full_url = href if href.startswith('http') else base_url + href
                if headline not in seen_titles:
                    seen_titles.add(headline)
                    headlines.append((article_date, headline, full_url))



    headlines.sort(reverse=True)
    # Display the headlines
    for date, headline, link in headlines:
        print("Headlines: ", headline)
        #print("Headlines: ", headline, "    ", link, "    ", date.date())

    return headlines