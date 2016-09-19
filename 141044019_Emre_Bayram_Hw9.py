
import random

global 	QUEUE, STACK, SORTEDLIST

QUEUE = [] 
STACK = []
SORTEDLIST = []

# QUEUE Data Structure Functions 
def enqueue(item):
        global QUEUE
        QUEUE = QUEUE +[item]
        return item

def dequeue():
        global QUEUE
        i=0
        if QUEUE is not None:
                ret = QUEUE[0] 
                QUEUE = QUEUE[1:len(QUEUE)]              

        return ret

# STACK Data Structure Functions 
def push(item):
        global STACK

        STACK = STACK + [item]

        return item
def pop():
        global STACK
        ret = STACK[len(STACK)-1]
        STACK = STACK[0:len(STACK)-1]
        return ret

# SORTED LIST Data Structure Functions 
def insert(item):
        global SORTEDLIST
        SORTEDLIST = SORTEDLIST + [item]
    
        for i in range(0,len(SORTEDLIST)):
                for j in range(1,len(SORTEDLIST)):
                        if (SORTEDLIST[j] > SORTEDLIST[j-1]):
                                temp = SORTEDLIST[j-1]
                                SORTEDLIST[j - 1] = SORTEDLIST[j]
                                SORTEDLIST[j] = temp
    
        return item
def remove(item):
        global SORTEDLIST
        
        flag = False
        counter = 0
        while counter < len(SORTEDLIST) and not flag :
                if(SORTEDLIST[counter] is item):
                        print (SORTEDLIST[counter+1:len(SORTEDLIST)])
                        SORTEDLIST = SORTEDLIST[0:counter] + SORTEDLIST[counter + 1:len(SORTEDLIST)]
                        flag = True
                counter += 1
                
        
def search(item):
    flag = True
    i = 0
    while (flag) and (len(SORTEDLIST) > i):
        if item is SORTEDLIST[i]:
            return True
        else:
            i+=1
    
    return False


def main():
	
	numberList = random.sample(range(0,1000),100)

	for number in numberList:
		enqueue(number)
		push(number)
		insert(number)

	print (" Numbers of QUEUE \n" ,QUEUE)
	print (dequeue())
	print (dequeue())
	print (" New Queue  >> \n" ,QUEUE)

	print (" Stack >>> \n", STACK)
	print (pop())
	print (pop())
	print (" New Stackk \n",STACK)



	print (" Sorted List >> \n",SORTEDLIST)
	number = random.randint(0,1000)
	while(not search(number)):
		number = random.randint(0,1000)

	remove(number)
	print (number,"is Removed New Sorted List \n",SORTEDLIST)

main()
