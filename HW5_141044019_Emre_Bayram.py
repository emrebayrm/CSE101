import sys

def main(argv):
    filename = argv[1]

    flag = 0
    for char in filename:
        if(char == '.'):
            if(filename[-1] == 'e' and filename[-2] == 'x' and filename[-3] == 'e'):
                flag = 1
    
    if(flag):
        file = open(filename,"rb")
        print " ###############  Writing binary  ##############\n"
        
        for bit in file.read():
            
            print bin(ord(bit))
        
        file.close()
        
        file = open(filename,"rb")
        
        print "\n##############  Wrinting as a hexadecimal #########\n"
        while True:
            hexa = file.read(1)
            
            if not hexa:
                break
            
            print hex(ord(hexa))
           
        file.close()
        
        file = open(filename, "rb")
        
        print "\n##############  Wrinting as a Decimal ###########\n"
        
        while True:
            deci = file.read(1)
            
            if not deci:
                break
            
            print ord(deci)
    else:
        print " IT IS NOT EXE FILE !!!!"
        SystemExit()
        
main(sys.argv)