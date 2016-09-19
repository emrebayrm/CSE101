inp = input("Enter wanted to convert from integer squence to mors squence >>  ")
for letter in inp:
    integer_val = int(letter)
    print (integer_val)
    #start with dot
    if integer_val <= 5:
        print (("."*integer_val) + ("-"*(5-integer_val)) + "\n")     
    else:
        print (("-"*(integer_val%5)) + ("." *(10-integer_val)) + "\n")