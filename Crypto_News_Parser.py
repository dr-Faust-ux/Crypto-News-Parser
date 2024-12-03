import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL для парсинга новостей
URL = "https://www.coindesk.com/"
OUTPUT_FILE = "crypto_news.txt"

def fetch_news(url):
    """
    Получает новости с указанного URL.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Поиск заголовков и ссылок (зависит от структуры сайта)
    articles = soup.find_all("a", class_="headline")
    news_list = []
    for article in articles[:10]:  # Берем только 10 новостей
        title = article.get_text(strip=True)
        link = article["href"]
        full_link = link if link.startswith("http") else f"{URL}{link}"
        news_list.append({"title": title, "link": full_link})
    return news_list

def save_news(news_list, file_path):
    """
    Сохраняет список новостей в текстовый файл.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Новости о криптовалютах ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        file.write("=" * 50 + "\n")
        for news in news_list:
            file.write(f"{news['title']}\n")
            file.write(f"{news['link']}\n")
            file.write("-" * 50 + "\n")

def main():
    print("Сбор новостей с CoinDesk...")
    news_list = fetch_news(URL)
    print("Сохранение новостей в файл...")
    save_news(news_list, OUTPUT_FILE)
    print(f"Новости сохранены в файл: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

