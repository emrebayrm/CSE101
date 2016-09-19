#
#	seymayucer
#	18.12.2015
#	basic drawer functions
#	you will convert this python code to C code.
#	
import sys # to use stdout,in c stdio.h


#basic terminal user interface
def drawerMenu():
	print "Welcome To Drawer's Home!"	
	print "[1] Triangle"
	print "[2] Rhomboid"
	print "[3] Circle"
	print "[4] Exit"
	print "Select a Shape:"


#main and function calls
def main():

	while 1:
		drawerMenu()
		user_choise =input("->")

		if user_choise ==1:
			traingleDrawer()

		elif user_choise ==2:
			rhomboidDrawer()

		elif user_choise ==3:
			circleDrawer()		

		elif user_choise ==4:
			break
		else:
			print "invalid input,please try again!"

# Draws rhomboid according to size of edges
def rhomboidDrawer():
	w =input("Enter w side size->")
	h =input("Enter h side size->")
	i,j=0,0
	for i in range(h):
		j=0
		for x in range(i):
			sys.stdout.write(' ') # prints something in terminal like print, but more useful to stay in same line instead of print
		for j in range(w):
			j+=1
			sys.stdout.write('* ')
		i+=1
		sys.stdout.write('\n')	    

	return

# Draws traingle according to height
def traingleDrawer():
	h =input("Enter height of triangle ->")
	i,k=1,0
	while i<=h:
		space=1
		while space<=h-i:
			sys.stdout.write(' ')
			space+=1

		while k!=2*i-1:
			sys.stdout.write('*')
			k+=1

		k=0
		i+=1
		sys.stdout.write('\n')
    
	return
# Draws circle according to radius
def circleDrawer():
	
	r =input("Enter Radius ->")
	r_out = r + 0.4
	y = r
	while y >= -r:
		x = -r    
		while x < r_out:
			value = x * x + y * y
			if value <= r_out * r_out :        
				sys.stdout.write('*')
			else:            
				sys.stdout.write(' ')
			x += 0.5   

		sys.stdout.write('\n')
		y-=1 
 
	return


if __name__ == "__main__":
    main()