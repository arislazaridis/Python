import json             #metatrepei ta dedomena se leksiko gia na ta epeksergastei i python
from datetime import datetime as date , timedelta as delta
import requests         #epitrepei tin epikoinwnia tis glwssas me istoselidas gia tin eisagwgi kai epeksergasia dedomenwn

'''Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python για να εμφανίσετε
 τα στατιστικά των αριθμών που κερδίζουν την πρώτη κλήρωση της ημέρας για το ΚΙΝΟ τον τρέχον μήνα.'''

#current date
currentDate = date.now()
#one month (30days)
firstDay = currentDate - delta(30)

API_URL = "https://api.opap.gr/draws/v3.0/1100/draw-date/{date:%Y-%m-%d}/{date:%Y-%m-%d}/draw-id"
nums = []   #winning_numbers
array = []  #first_draws
total_nums_results = 0


while firstDay <= currentDate :
    print("loading")
    formatedUrl = API_URL.format(date=firstDay)   # formatedUrl = Url gia kathe mera tou mina
    response = requests.get(formatedUrl)          #kanei klisi sto url/anaktisi istoselidas
    responsetoText = response.text                #anathetei stin metavliti response tin entoli text kata tin opoia tha diabasei ta dedomena tis istoselidas
    draws = json.loads(responsetoText)            #metatrepei to eksagwmeno keimeno se leksiko / draws-ids
    first_draws = draws[0]                        #draws-ids twn prwtwn klirwsewn tis imeras
    array.append(first_draws)                     #pinakas me tis prwtes klirwseis tou mina
    firstDay = firstDay + delta(days=1)           #days++



#gia tis prwtes klirwseis tou mina opou einai apothikeymenes ston array
for d in array :
    url = "https://api.opap.gr/draws/v3.0/1100/" + str(d)
    r = requests.get(url)
    html = r.text
    data = json.loads(html)
    nums = nums + data["winningNumbers"]["list"]


max = 1
#statistics
for i in range(1,81) :
    print(i, ': ', 'Emfanistike', nums.count((i)), 'fores')

    #arithmos me tis perissoteres emfaniseis
    if nums.count(i) > max :
            number = i
            max1 = nums.count(i)
            max = max1
print("O arithmos me tis perissoteres emfaniseis einai to : " + str(number) + " , " +"Me arithmo emfanisewn: " + str(max))
