import bs4
import requests


def get_html(url):
    '''Получаем данные с сайта'''
    r = requests.get(url)
    return r.text


def write(data_set):
    '''Записываем наши прокси в текстовый файл'''
    with open("proxies.txt", "a+") as f:
        for i in data_set:
            f.write(i + '\n')


def get_page_data(html):
    global data_set
    '''Получение всех ip, в ads ~200 айпишников'''
    soup = bs4.BeautifulSoup(html, "lxml")

    ads = soup.find("table").find("tbody").find_all("tr")
    data_set = []

    for ad in ads:
        try:
            ip = ad.find_all("td")[0].text
            port = ad.find_all("td")[1].text
        except Exception as error:
            print(error)

        # Формируем полный адрес и вызываем функцию записи
        data = str(ip) + ":" + str(port)
        data_set.append(data)


def main():
    url = "https://www.us-proxy.org/"
    get_page_data(get_html(url))
    write(data_set)


if __name__ == "__main__":
    main()
