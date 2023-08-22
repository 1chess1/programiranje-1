import requests
from fake_useragent import UserAgent

def pobiranje_podatkov(link):
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    req1 = requests.get(link, headers=headers).text
    return req1

def v_datoteko(st_strani):
    vsebina = ""
    link2 = "https://mangareader.to/az-list?page="
    stevec = 1
    with open("vsebina.html", "w") as shranjena_vsebina:
        while stevec < st+1:
            try:
                vsebina = pobiranje_podatkov(link2)              
                link2 = "https://mangareader.to/az-list?page="+str(stevec)
                shranjena_vsebina.write(vsebina)
            except:
                continue
            stevec += 1
    return None

def poberi_vse(): #če želiš pobrati čisto vse podatke
    vsebina = ""
    link2 = "https://mangareader.to/az-list?page="
    stevec = 1
    with open("vsebina.html", "w") as shranjena_vsebina:
        while True:
            try:
                vsebina = pobiranje_podatkov(link2)              
                link2 = "https://mangareader.to/az-list?page="+str(stevec)
                shranjena_vsebina.write(vsebina)
            except:
                if stevec > 650:
                    return None
            stevec += 1
v_datoteko(639)
