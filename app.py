import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

number_of_pages = 5
ua = UserAgent(verify_ssl=False, use_cache_server=False)
header = {'User-Agent': str(ua.chrome), 'Accept-Encoding': 'utf-8'}
page = 0
rows = []
while page < number_of_pages:
    page += 1
    result = requests.get("https://www.webnames.ru/domains/deleted?page_no={}&param=1&sorting=1".format(page),
                          headers=header)
    content = result.content
    soup = BeautifulSoup(content, "html.parser")
    # skip header
    main_item_tr_list = soup.find_all('tr')[1:]

    for item in main_item_tr_list:
        td1 = item.find_all("td")
        row = dict()
        row['id'] = td1[0].text
        row['domain'] = td1[1].text
        row['date'] = td1[3].text
        row['rate'] = td1[4].find('div').find('span').text
        rows.append(row)
        # print(td1[0].text + td1[1].text + td1[3].text, td1[4].find('div').find('span').text)
print(rows)
