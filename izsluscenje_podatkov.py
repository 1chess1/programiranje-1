
from bs4 import BeautifulSoup



def pobiranje_podatkov():
    with open("vsebina.html") as dat:
        soup = BeautifulSoup(dat, 'html.parser')
        lists =soup.find_all('div', class_ = "manga-detail") 
        lists = izbris_duplikatov(lists)
    with open("preverjanje.txt", "w") as test:  
        i = 0
        for list in lists:
            test.write(str(list))
            i += 1
    a = names(lists)
    b = genres(lists)
    c = chapter_number(lists)
    return lists


def izbris_duplikatov(podatki):
    
    podatki_izbris = list(dict.fromkeys(podatki))
    return podatki_izbris

def names(podatki):
    imena = []
    i = 0
   
    for podatek in podatki:
        imena.append(podatek.find('h3').get_text())
                   
    with open("imena.txt", "w") as dat:
        i = 0
        for ime in imena:
            i += 1
            dat.write(ime.strip()+'\n')
    return imena

def genres(podatki):
    genres = []
    genres_pomozni = []
    test = 0
    i = 0
    for podatek in podatki:
            test += 1
            vsebina = str(podatek)
            for i in range(10):
                try:
                    stevilo = vsebina.find('genre')
                    vsebina = vsebina[stevilo:]
                    zacetek = vsebina.find('>')
                    konec = vsebina.find('<')
                    if vsebina[zacetek+1:konec] == "" and i == 0:
                        genres_pomozni.append("nedoločen")
                    if vsebina[zacetek+1:konec] == "":
                        break
                    genres_pomozni.append(vsebina[zacetek+1:konec])
                    vsebina = vsebina[konec:]
                except: 
                    break
            if genres_pomozni != []:
                genres.append(genres_pomozni)
            else:
                genres.append("nedoločen")
            i = 0
            genres_pomozni = []
            
    with open("genres.txt", "w") as dat:
        i = 0
        while i < len(genres):
            
            dat.write(str(genres[i])+'\n')
            i += 1    
    return genres
def chapter_number(podatki):
    chap = []
    for podatek in podatki:
        try:
            if podatek.find('div', class_="chapter") == None:
                chap.append("nedoločen")
            else:
                chap.append(podatek.find('div', class_="chapter"))
        except:
            continue
    v_chap_list(chap)
    v_jezik_list(podatki)
    v_volume_list(chap)
    return chap
def v_chap_list(podatki):
    zacetek = 0
    konec = 0
    vsebina = ""
    i = 0
    with open("chapter_number.txt", "w") as chapter:
        for podatek in podatki:
            if podatek == "nedoločen":
                chapter.write("nedoločen"+'\n')
            else:
                vsebina = str(podatek)
                zacetek = vsebina.find("</i>Chap") 
                if zacetek > -1:
                    konec = vsebina.find("[")
                    chapter.write(vsebina[zacetek+4:konec].strip()+'\n')
                else:
                    chapter.write("nedoločen"+'\n')
            i += 1
        
def v_jezik_list(podatki):
    vsebina = ""
    i = 0
    with open("jezik.txt", "w") as chapter:
        for podatek in podatki:
            vsebina = str(podatek)           
            if vsebina.find("[EN]") != -1:
                chapter.write("EN"+'\n')
            elif vsebina.find("[JA]") != -1:
                chapter.write("JA"+'\n')
            else:
                chapter.write("nedoločen"+'\n')
            
            i += 1
                
        
def v_volume_list(podatki): #zaradi pomankanja podatkov sem se kasneje odločil, da teh informacij ne bom obdeloval
    zacetek = 0
    konec = 0
    vsebina = ""
    i = 0
    with open("volume_number.txt", "w") as volume:
        for podatek in podatki:
            if podatek == "nedoločen":
                volume.write("nedoločen"+'\n')
            else:
                vsebina = str(podatek)
                zacetek = vsebina.find("Vol") 
                vsebina = vsebina[zacetek::]
                zacetek = vsebina.find("Vol")
                if zacetek > -1:
                    konec = vsebina.find("[")
                    volume.write(vsebina[zacetek:konec]+'\n')
                else:
                    volume.write("nedoločen"+'\n')
                i += 1


a = pobiranje_podatkov() #kodo samo poženeš
#print(names(a))
