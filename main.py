import requests
from bs4 import BeautifulSoup

def scrape_data(url: str, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    return soup

def extract_links(soup):
    body = soup.find("body")
    write_to_file("tf-idf", str(body))
    links = body.find_all("a")
    wikis = []
    externals = []
    cleaned = []
    for link in links:
        link = link["href"]
        if link.startswith("/wiki"):
            wikis.append(link)
            continue
        if link.startswith("https"):
            externals.append(link)
            continue
        if link.startswith("#"):
            continue

        cleaned.append(link)

    write_to_file("tf-idf-wikis", str(wikis))
    write_to_file("tf-idf-externals", str(externals))
    write_to_file("tf-idf-others", str(cleaned))
    return

def write_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return

def main():
    soup = scrape_data("https://en.wikipedia.org/wiki/Tf%E2%80%93idf", {"User-Agent": "Mozilla/5.0"})
    extract_links(soup)
    print("DATA WRITTEN TO VARIOUS FILES")
    return

if __name__ == "__main__":
    main()
