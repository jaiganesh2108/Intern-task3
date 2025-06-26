import requests
from bs4 import BeautifulSoup

# Target news website
url = 'https://www.bbc.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2') 
    extracted_headlines = []
    for idx, headline in enumerate(headlines):
        text = headline.get_text(strip=True)
        if text:
            extracted_headlines.append(f"{idx + 1}. {text}")

    # Save headlines to a text file
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(extracted_headlines))

    print(f"Successfully saved {len(extracted_headlines)} headlines to 'headlines.txt'.")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
