import bs4
import requests
import os


def get_html(url):
    r = requests.get(url)
    return r.text


def check_file():
    try:
        os.remove("proxies.txt")
    except:
        pass


def write(data):
    with open("proxies.txt", "a+") as f:
        f.write(data + "\n")


def get_page_data(html):
    soup = bs4.BeautifulSoup(html, "lxml")

    ads = soup.find("table").find("tbody").find_all("tr")

    for ad in ads:
        try:
            ip = ad.find_all("td")[0].text
        except:
            ip = ""
        try:
            port = ad.find_all("td")[1].text
        except:
            port = ""

        data = str(ip) + ":" + str(port)
        write(data)


def main():
    url = "https://www.us-proxy.org/"
    check_file()
    get_page_data(get_html(url))


if __name__ == "__main__":
    main()
