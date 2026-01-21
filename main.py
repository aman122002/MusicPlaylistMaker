import requests
from soup import BeautifulSoup
URL = "https://www.billboard.com/charts/hot-100/"
date_to_use = "2002-02-12"
"""input("Which year would you like to travel? (YYYY-MM-DD)")"""

headers = {
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

response = requests.get(f"{URL}/{date_to_use}", headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

song_names = [name.getText().strip() for name in soup.select("li ul li h3")]
print(song_names)