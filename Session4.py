#Print numbers from 1 to 100 

def number(count):
    while count <=100:            #using a 'while' loop we tell the program to count incrementing the count by '1', while count is EQUAL or LESS than 100. 
      print(count)
      count=count+1;
number(0)


#Print numbers from 100 to 1 (backwards) 

for count in range (100,0, -1): #using the function "for count in range" we establish a range '100,0-1'. The program will print all the numbers in between, backwards. 
    print (count)
    
