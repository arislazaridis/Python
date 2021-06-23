#using for random numbers
import random
#using for math.ceil
import math


# the user give the dimensions of the square
n = int(input("Give the dimensions of the square : "))

sum_horizontal = 0
sum_vertical = 0
sum_diagonial = 0
sum_diagonial2 = 0

N = 100 #how many times the program runs
times = 1
while times <= N :
    #create list for randoms
    list = []
    #my_randoms for 2d array
    my_randoms = []
    #check_list with elements (1,0)
    check_list = []
    horizontal_counter = 0
    vertical_counter = 0
    diagonial_counter = 0
    diagonial_counter2 = 0
    x = 0
    flag = 0
    while flag == 0:
        for i in range(n):
            # Fill the list with randoms (1,0)
            list = [random.randrange(0, 2, 1) for i in range(n)]
            # Create 2d array
            my_randoms = my_randoms + [list]
            # Create list with elements (1,0)
            check_list = check_list + list
            # Count element 1 in the list
            One_count = check_list.count(1)
            # The element 1 must be >=50% of the len(check_list)/2
            x = math.ceil((len(check_list) / 2))
        #Check if the elements 1 is 50% of  the len(check_list)/2 with rounding upwards
        if x == One_count :
            flag = 1
        else:
            #Clear the lists
            list.clear()
            check_list.clear()
            my_randoms.clear()
            One_count = 0
            x = 0
            flag = 0
    #Display data -round,One_count,table's informations
    print("["+str(times)+"]")
    print("---------------------")
    print("---------------------")
    print("The number '1' seems : " + str(One_count) + " " + "times")
    print("The table's dimension's are : " + str(n**2) + " " + "-->" +" "+ str(n) + " "+ "rows" + " "+ "and" + " " + str(n) + " " + "columns")

    #Print the table to being easy for the user to  find the 1-1-1-1 matches .
    for i in range(n):
        print(my_randoms[i])


    i = 0
    # Horizontal
    for i in range(n):
        for j in range(n - 3):
            if my_randoms[i][j] == 1 and my_randoms[i][j + 1] == 1 and my_randoms[i][j + 2] == 1 and my_randoms[i][ j + 3] == 1:
                horizontal_counter = horizontal_counter + 1
    sum_horizontal = sum_horizontal + horizontal_counter


    # Vertical
    for i in range(n):
        for j in range(n - 3):
            if my_randoms[j][i] == 1 and my_randoms[j + 1][i] == 1 and my_randoms[j + 2][i] == 1 and my_randoms[j + 3][ i] == 1:
                vertical_counter = vertical_counter + 1
    sum_vertical = sum_vertical + vertical_counter

    # diagonial1
    for i in range(n-3):
        for j in range(n - 4):
            if my_randoms[j][i] == 1 and my_randoms[j + 1][i + 1] == 1 and my_randoms[j + 2][i + 2] == 1 and my_randoms[j + 3][i + 3] == 1:
                    diagonial_counter = diagonial_counter + 1
    sum_diagonial = sum_diagonial + diagonial_counter


    # diagonial2

    for i in range(n - 3):
        for j in range(3, n):
            if my_randoms[i][j] == 1 and my_randoms[i + 1][j - 1] == 1 and my_randoms[i + 2][j - 2] == 1 and  my_randoms[i + 3][j - 3] == 1:
                    diagonial_counter2 = diagonial_counter2 + 1
    sum_diagonial2 = sum_diagonial2 + diagonial_counter2

    print("----------------------")
    print("----------------------")

    times = times + 1


    #Display the data(How many times find the (1-1-1-1 matches) for each round
    print("Horizontal:" + str(horizontal_counter))
    print("Vertical:" + str(vertical_counter))
    print("Diagonial[1]: " + str(diagonial_counter))
    print("Diagonial[2]: "+str(diagonial_counter2))
    print("---------------------")
    print("---------------------")

#Total percentage of the displays(1-1-1-1 matches) for 100times
print("[total percentage of displays for 100 times] : ")
print("-----------------------------------------------")

print("Total Horizontal percentage:" + str(sum_horizontal / N))
print("Total Vertical percentage:" + str(sum_vertical / N))
print("Total Diagonial percentage:" + str(sum_diagonial/ N))
print("Total Diagonial[2] percentage:" + str(sum_diagonial2/ N))