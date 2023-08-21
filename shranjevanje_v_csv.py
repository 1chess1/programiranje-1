import csv

def shranjevanje_v_csv():
    imena1 = ""
    st_ostala = 0
    genres1 = ""
    jezik1 = ""
    chapter_number1 = ""
    volume_number1 = ""
    with open("together.csv", "w", encoding='UTF8', newline='') as together:
        with open("imena.txt", "r") as imena:
            with open("genres.txt", "r") as genres:
                with open("jezik.txt", "r") as jezik:
                    with open("chapter_number.txt", "r") as chapter_number:
                            with open("volume_number.txt", "r") as volume_number:
                                fieldnames = ['id', 'imena', 'žanri', 'jeziki', 'št poglavij']
                                writer = csv.DictWriter(together, fieldnames=fieldnames)
                                writer.writeheader()
                                while True:
                                    genres1 = genres.readline().strip()
                                    jezik1 = jezik.readline().strip()
                                    chapter_number1 = chapter_number.readline().replace("Chap", "").replace("nedoločen", "0").strip()
                                    imena1 = imena.readline().strip()
                                    if jezik1.strip() == "":
                                        break
                                    writer.writerow({"id" : st_ostala, "imena": imena1,
                                                     "žanri" : genres1, "jeziki": jezik1, "št poglavij": chapter_number1})
                                    st_ostala += 1 
                                    
                                
shranjevanje_v_csv()
