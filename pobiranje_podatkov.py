import requests
from fake_useragent import UserAgent

def pobiranje_podatkov(link):
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    req1 = requests.get(link, headers=headers).text
    return req1

def v_datoteko(st):
    vsebina = ""
    link2 = "https://mangareader.to/az-list?page="
    i = 1
    with open("vsebina.html", "w") as shranjena_vsebina:
        while i < st+1:
            try:
                vsebina = pobiranje_podatkov(link2)              
                link2 = "https://mangareader.to/az-list?page="+str(i)
                shranjena_vsebina.write(vsebina)
            except:
                continue
            i += 1
    return None
v_datoteko(639)