import urllib3
import json             #metatrepei ta dedomena se leksiko gia na ta epeksergastei i python
import datetime
import urllib
import requests         #epitrepei tin epikoinwnia tis glwssas me istoselidas gia tin eisagwgi kai epeksergasia dedomenwn
from datetime import datetime as date ,timedelta as delta  #mas dinei tin simerini imerominia/wra

'''Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python
 για να βρείτε τον αριθμό που εμφανίζεται συχνότερα στο ΚΙΝΟ κάθε μέρα του τρέχοντα μήνα.'''

#currentday
currentday = date.now()

#one-month
firstday = currentday - delta(30)   #delta = datetime.timedelta

Api_url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{date:%Y-%m-%d}/{date:%Y-%m-%d}/draw-id"
nums = []          #winning_numbers
array = []         #draws-ids

# vriskoume ta urls twn klirwsewn gia ton trexon mina
while firstday < currentday:
    print("loading..")
    formated_Url = Api_url.format(date=firstday)        #url gia kathe mera tou mina
    response = requests.get(formated_Url)               #klisi sto url//anaktisi istoselidas
    responsetotext = response.text                      #anathetei stin metavliti response tin entoli text kata tin opoia tha diabasei ta dedomena tis istoselidas
    draws = json.loads(responsetotext)                  #metatrepei to eksagwmeno keimeno se leksiko / draws-ids
    array.append(draws)                                 #gemizei ton array me ta draws-ids
    #print(draws)  #draws-ids gia ton trexon mina
    firstday = firstday + delta(days=1)

#gia kathe draw vriskoume ta winning numbers
for d in draws:
    url = "https://api.opap.gr/draws/v3.0/1100/" + str(d)
    r = requests.get(url)
    html = r.text
    data = json.loads(html)
    nums = nums + data["winningNumbers"]["list"]

max = 1
#eyresi tou arithmou pou emfanistike tis perissoteres fores
for i in range(1, 81):
    if nums.count(i) > max:
        max = nums.count(i)
        number = i

print("O arithmos me tis perissoteres emfaniseis einai to : " + str(number) + " , " +"Me arithmo emfanisewn: " + str(max))






