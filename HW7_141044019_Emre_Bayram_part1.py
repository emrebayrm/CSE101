import random
import timeit

def linear_search(list,key):
	if(len(list) == 0):
		print "list is empty"

	for i in range(0,len(list)):
		if (key == list[i]):
			return True

	return False




def Binary_search(list,key):

    if(len(list) == 0):
        return False
    if(list[len(list)/2] == key):
        return True
    elif(list[len(list)/2] > key):
        return Binary_search(list[0:(len(list)/2)-1],key)
    elif(list[len(list)/2] < key):
        return Binary_search(list[(len(list)/2)+1:len(list)],key)


def CreateRandomintFile(min,max,times,filename):
	
	file = open(filename,"w")

	for i in range(0,times):
		randomnum = random.randint(min,max)
		file.write(str(randomnum))
		file.write(" ")
		
def Sort(list):
    for i in range(1,len(list)):
        val = list[i]
        
        counter = i

        while (counter > 0 and list[counter - 1] > val):
            temp = list[counter]
            list[counter] = list[counter -1]
            list[counter -1] = temp
            counter -= 1
            

def main ():
    
    minval = int(raw_input("Enter minumum value of random number range >>"))
    maxval = int(raw_input("Enter Maximum value of random number range >>"))
    times  = int(raw_input("How many number you want ? >>"))
    filename = str(raw_input("I know you bored, lastly Enter filename >> "))

    CreateRandomintFile(minval,maxval,times,filename)
	
    file =open(filename,"r")
    readlist=[]
    
    readed = file.read()
    
    yeni = readed.split(" ")
    
    for count in range(0,len(yeni)-1):
        readlist.append(int(yeni[count]))
    
    print readlist
    
    Sort(readlist)
    
    print readlist
    
    key = input("What do you wanna search >> ") 
    start = timeit.default_timer()
    print Binary_search(readlist,key)
    stop = timeit.default_timer()
    
    print "Using Binary search, Serched in " ,(stop - start)*1000 , " ms."

    start = timeit.default_timer()
    print linear_search(readlist,key)
    stop = timeit.default_timer()
    
    print "Using Linear search, Serched in " ,(stop - start)*1000 , " ms."
    
        
main()
