import requests
from bs4 import BeautifulSoup


url = 'https://free-proxy-list.net/'
url2 = 'http://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{}'
def get_ip_port():
    lol = requests.get(url)
    soup = BeautifulSoup(lol.content, 'html.parser')
    for tr in soup.tbody.find_all('tr'):
        ip, port = tr.contents[0].text, tr.contents[1].text
        proxy = ip+':'+port
        yield proxy

def get_ip_port2():
    for i in range(6):
        lol = requests.get(url2.format(str(i+1)))
        soup = BeautifulSoup(lol.content, 'html.parser')
        for tr in soup.find_all('tr', class_ = 'cells')[1:-1]:
            proxy = tr.find_all('td')[1].text+':'+tr.find_all('td')[2].text
            yield proxy



if __name__ == '__main__':
    get_ip_port()
    get_ip_port2()