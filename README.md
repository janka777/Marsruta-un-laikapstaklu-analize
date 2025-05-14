# Laikapstaklu-un-marsruta-analize
## Projekta uzdevums

### Situācijas apraksts

Mūsdienās cilvēki ir ļoti saistīti ar tehnoloģijām un bez tā nevar dzīvot. Bet ar tām jāmāk pareizi rīkoties, lai ietaupītu savu dārgo laiku. Rīgā ir viena ļoti liela problēma kas nav sastopama citās Latvijas pilsētās-sastrēgumi. Lai nestāvētu tik ilgi sastrēgumstundās , ātrāk ir braukt ar motociklu , vai arī sabiedriskais transports ir laba alternatīva. Bet ar motociklu lietus laikā braukt ir nepatīkami un bīstami, tāpēc katru rītu cilvēks pavada laiku , lai paskatītos un parbaudītu laikapstākļus un maršrutu , kuru izmantot.

### Darba Uzdevums:

1. Izveidot kodu kas var atvieglot motociklista dzīvi, kurš dzīvo pie Origo.

2. Pārbaudīt laikapstākļu mājaslapā kāda ir šodien dienas laika prognoze.

3. Ja līst lietus , kods piedāvā braukt ar sabiedrisko transportu- uzreiz piedāvā maršrutu un patērēto laiku.

4. Ja nokrišņu daudzums ir mazāks par 50% , tad motociklists brauks ar savu motociklu un kods arī piedāvā laiku un maršrutu , tikai ar motociklu šoreiz.

5. Nokrišņu daudzums, kurā cilvēks brauks jau brauks ar autobusu ir kad nokrišņu daudzums būs lielāks par 50%

### Darba Aktualitāte:
Šis kods ietaupīs laiku daudziem motociklistiem , jo kods uzreiz ar vienu klikšķi iesaka ar ko un pa kādu maršrutu braukt. Kods to izdarītu daudz atrāk nekā cilvēks manuāli, jo cilvēkam būtu jāiet uzreiz divos resursos.

## Izmantotās python bibliotēkas:
Mēs izmantojam četras dažādas bibliotēkas (**requests, beautifulSoup, webbrowser un datetime**)

**requests** - mēs izmantojam lai veiktu HTTP pieprasījumus. Mūsu gadījumā Requests.get(adrese) izmantojam, lai veiktu GET pieprasījumu uz noteiktu tīmekļa lapu (https://www.meteounradars.lv/laikazinas/riga/6508658), kur tiek iegūti laikapstākļu dati

**beautifulSoup**- šo bibliotēku izmantojam HTML dokumentu parsēšanai. Kad lapas saturs ir iegūts ar requests, BeautifulSoup tiek izmantots, lai analizētu HTML struktūru un iegūtu nepieciešamos datus, piemēram, laikapstākļu prognozes.

**Webbrowser** - mēs izmantojam šo bibliotēku, lai atvērtu URL adreses mūsu tīmekļa pārlūkprogrammā. Kad esam ieguvuši prognozi un noteikuši, vai šodien braukt ar motociklu vai autobusu, mēs izveidojam Google Maps maršruta URL. Tad atveram šo saiti pārlūkā, lai uzreiz redzētu maršrutu no Origo līdz Rīgas Tehniskajai universitātei.

**Datetime** - mēs izmantojam šo bibliotēku, lai strādātu ar datumiem un laikiem, kas mums ir vajadzīgs, lai noteiktu šodiena datumu.

## Projekta laikā mūsu izmantotās datu struktūras
Projekta laikā mēs izmantojām mūsu izveidoto vārdnīcu latvian_months , mēs šo izmantojam lai pārveidotu skaitli, par cilvēkam saprotamu mēneša nosaukumu.

## Programmas izmantošanas metodes:
Programmas izmantošana būs ļoti izdevīga motociklistiem , jo šī programmatūra , automatizē to, ko motociklists dara no rīta. Arī pārstrādājot nedaudz programmu varam pārveidot tā lai , programma derētu arī velosipēdistiem, vai visiem kuru pārvietošanās ir atkarīga no laikapstākļiem.

### Darba Autori:
Vadims Kirsanovs 241RDB090

Jānis Meškovskis 241RDB048
