
#eisagw arxeio .txt
Ascii_text = open("C:/Users/arisl/Desktop/two_cities_ascii.txt", "r")


#kanw read kai print to arxeio
data = Ascii_text.read()
print(data)


#Apothikeysi sto list tous ascii xaraktires tou keimenou
list = [ord(c) for c in data]



#Dimiourgia listas gia tous monous xaraktires
odd_list = []
#diatrexw tin lista me tous ascii kai vriskw tous monous
for num in list :
    if num%2 != 0 :
        odd_list = odd_list + [num]


#vriskw poioi einai oi antistoixoi xaraktires
chr_odd_list = []
for c in odd_list:
    chr_odd_list = chr_odd_list + [chr(c)]
#print(chr_odd_list) #for check



#krataw mono tous alphabetical characters xwris ta '..'
res = ""
for i in chr_odd_list:
    if i.isalpha():
        res = "".join([res, i])



#katharizoume apo pithanous kenous charaktires
while '' in chr_odd_list:
    chr_odd_list.remove('')


#vriskw to plithos twn xarakthrwn
number_of_elements = len(res)

#print(number_of_elements) #for check


#ftiaxw mia lista gia tous charactires
total_chr = []
for x in set(res):
    total_chr = total_chr + [x]
#print(values) for check


#ypologizw to pososto emfanisis tou kathe xaraktira
percentage=[]
for x in set(res):
    percentage= percentage + [round((res.count(x)/number_of_elements)*100)]
#print(percentage) #for check

#sygkentrwtiko leksiko me to pososto emfanisis kathe xaraktira
dictionary = dict(zip(total_chr,percentage))
#print(dictionary)

#display
for x in dictionary:
    print(x, '=' , dictionary[x], '%' ,'     ','status:' , dictionary[x] *  ' *')






