
import random

global 	QUEUE, STACK, SORTEDLIST

QUEUE = [] 
STACK = []
SORTEDLIST = []

# QUEUE Data Structure Functions 
def enqueue(item):
	print "implement enqueue function for QUEUE data structure"

def dequeue():
	print "implement dequeue function for  QUEUE data structure"

# STACK Data Structure Functions 
def push(item):
	print "implement push function for STACK data structure"

def pop():
	print "implement pop function for STACK data structure"

# SORTED LIST Data Structure Functions 
def insert(item):
	print "implement insert function for SORTED LIST data structure"

def remove(item):
	print "implement remove function for SORTED LIST data structure"

def search(item):
	print "implement search function for SORTED LIST data structure"	
	


def main():
	
	numberList = random.sample(xrange(0,1000),100)

	for number in numberList:
		enqueue(number)
		push(number)
		insert(number)

	print QUEUE
	print dequeue()
	print dequeue()
	print QUEUE

	print STACK
	print pop()
	print pop()
	print STACK

	print SORTEDLIST
	number = random.randint(0,1000)
	while(not search(number)):
		number = random.randint(0,1000)

	remove(number)
	print SORTEDLIST

main()



