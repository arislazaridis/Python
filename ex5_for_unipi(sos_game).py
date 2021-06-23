import random       #paragwgi random stoixeiwn
import math         #gia xrisi tis math.ceil(gia tin stroggylopoihsh)


'''Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου
και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα. Στην συνέχεια θα βρίσκει το πλήθος
των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O (στρογγυλοποίηση προς τα πάνω). 
Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα, και διαγώνια. 
Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.'''

# ti diastaseis prepei na exei o pinakas
n = int(input("Give the dimensions of the table : "))

sum_horizontal = 0              #sum poses fores emfanistike to S-0-S orizontia/katheta/diagwnia for 100times
sum_vertical = 0
sum_diagonial1 = 0
sum_diagonial2 = 0
my_randoms = []
times = 1                       #metritis gia tis fores pou trexei to programma
N = 100                         #run for 100times
while times <= N:
    sos_randoms = []            #Fill with random S,O
    sos_total_list = []         #periexei ola ta S,0 se morfi wste na ginei to count
    sos_list = []               #2d array
    Horizontal = 0              #counter gia orizontia apotelesmata
    Vertical = 0                #counter gia katheta apotelesmata
    Diagonial1 = 0              #counter gia diagwnia
    Diagonial2 = 0              #counter gia diagwnia anapoda
    x = 0
    flag = 0
    while flag == 0:
        for i in range(n):
            # gemizw tis listes me tyxaia apotelesmata (S,0)  .
            sos_randoms = [random.choice(['S', 'O']) for i in range(n)]
            # dimiourgw pinaka 2 diastasewn
            sos_list = sos_list + [sos_randoms]
            # dimiourgia listas opou periexei ola ta stoixeia
            sos_total_list = sos_total_list + sos_randoms
            # metraw poses fores emfanistike to gramma "S"
            S_count = sos_total_list.count('S')
            # Thelw to plithos ton "S" na einai to 50% twn stoixeiwn me stroggylopoihsh pros ta panw
            x = math.ceil((len(sos_total_list) / 2))
        #Elegxw an isxyei oti ta "S" einai to 50% tis listas me stroggylopoihsh pros ta panw
        if x == S_count :
            flag = 1
        else:
            #kanw clear tis listes wste na ksanatreksei to programma
            sos_randoms.clear()
            sos_list.clear()
            sos_total_list.clear()
            S_count = 0
            x = 0
            flag = 0
    #print ta dedomena -round,S_count,table informations
    print("["+str(times)+"]")
    print("---------------------")
    print("---------------------")
    print("The char 'S' seems : " + str(S_count) + " " + "times")
    print("The table's dimension's are : " + str(n**2) + " " + "-->" +" "+ str(n) + " "+ "rows" + " "+ "and" + " " + str(n) + " " + "columns")

    #Print the table to being easily for the user to find the Sos
    for i in range(n):
        print(sos_list[i])


    i = 0
    # Horizontal
    for i in range(n - 2):
        for j in range(n):
            if sos_list[j][i] == 'S' and sos_list[j][i + 1] != 'S' and sos_list[j][i + 2] == 'S':
                Horizontal = Horizontal + 1
    sum_horizontal = sum_horizontal + Horizontal


    # Vertical
    for i in range(n):
        for j in range(n - 2):
            if sos_list[j][i] == 'S' and sos_list[j + 1][i] != 'S' and sos_list[j + 2][i] == 'S':
                Vertical = Vertical + 1

    sum_vertical = sum_vertical + Vertical


    # diagonial1
    for i in range(n - 2):
        for j in range(n - 2):
            if sos_list[j][i] == 'S' and sos_list[j + 1][i + 1] != 'S' and sos_list[j + 2][i + 2] == 'S':
                Diagonial1 = Diagonial1 + 1

    sum_diagonial1 = sum_diagonial1 + Diagonial1


    # diagonial2

    for i in range(n-2):

        for j in range(2,n):
            if sos_list[i][j] == 'S' and sos_list[i + 1][j - 1] != 'S' and sos_list[i + 2][j - 2] == 'S':
                Diagonial2= Diagonial2 + 1

    sum_diagonial2 = sum_diagonial2 + Diagonial2
    print("----------------------")
    print("----------------------")

    times = times + 1


    #poses fores emfanistike to sos se kathe gyro
    print("Horizontal:" + str(Horizontal))
    print("Vertical:" + str(Vertical))
    print("Diagonial[1]: " + str(Diagonial1))
    print("Diagonial[2]: "+str(Diagonial2))
    print("---------------------")
    print("---------------------")

#synoliko pososto emfanisewn SOS gia tis 100fores opou trexei to programma
print("[total percentage of displays for 100 times] : ")
print("-----------------------------------------------")

print("Total Horizontal percentage:" + str(sum_horizontal / N))
print("Total Vertical percentage:" + str(sum_vertical / N))
print("Total Diagonial percentage:" + str(sum_diagonial1/ N))
print("Total Diagonial[2] percentage:" + str(sum_diagonial2/ N))