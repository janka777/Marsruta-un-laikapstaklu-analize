import requests
from bs4 import BeautifulSoup
import webbrowser
import datetime

latvian_months = {
    1: "Janvāris",
    2: "Februāris",
    3: "Marts",
    4: "Aprīlis",
    5: "Maijs",
    6: "Jūnijs",
    7: "Jūlijs",
    8: "Augusts",
    9: "Septembris",
    10: "Oktobris",
    11: "Novembris",
    12: "Decembris"
}

today = datetime.date.today()
formatted = f"{today.day}. {latvian_months[today.month]}"
print("Šodienas datums:", formatted)

adrese = "https://www.meteounradars.lv/laikazinas/riga/6508658"
lapa = requests.get(adrese)

if lapa.status_code == 200:
    lapa.encoding = 'utf-8'
    saturs = BeautifulSoup(lapa.content, "html.parser")

    prognozes = saturs.find_all(class_="description")
    
    if not prognozes:
        print("Prognoze not found.")
        exit()

    for prognoze in prognozes:
        teksts = prognoze.get_text().strip()

        if teksts.endswith("%"):
            try:
                procents = int(teksts.replace("%", "").strip())
                print(f"Nokrišņu iespējamība: {procents}%")

                # Origo -> RTU, piemērojam transporta veidu
                end = "Rīgas+Tehniskā+universitāte"
                start = "Origo+Rīga"

                if procents <= 50:
                    print("Brauc ar motociklu.")
                    mode = "two_wheeler"
                else:
                    print("Brauc ar autobusu.")
                    mode = "transit"

                # Veidojam Google Maps maršruta URL
                maps_url = f"https://www.google.com/maps/dir/?api=1&origin={start}&destination={end}&travelmode={mode}"
                print("Maršruts:", maps_url)

                # Atveram pārlūkā
                webbrowser.open(maps_url)
                break  # iziet pēc pirmās atrastās prognozes

            except ValueError:
                print(f"Nevaru pārveidot tekstu uz skaitli: {teksts}")
else:
    print("Neizdevās ielādēt lapu.")
