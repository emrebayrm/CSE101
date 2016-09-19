#-*-coding: utf-8-*-
# author emre bayram
# date   29.10.2015
# resources: 
#           https://docs.python.org/2/library/urllib.html 
#           http://www.tutorialspoint.com/python/python_dictionary.htm  (also if you dont remember dictionaries in python)
#!/usr/bin/env python

import urllib2          #to url connections 
import re               #to get links in url
import webbrowser       #connection the your browser

#!! this function: 
#!!         opens a studentlist file and reads them
#!!         creates a dictionary that have keys: student number and values: student name
#!!         and shows this html file in web browser 
def createADictionary():

    file = open("StudentList.txt","r")  #open the given txt file in read mode
   
    d = {}                              # empty dictionary definition

    words = file.read().split()         #read file space by space
    wnum=0                              # for key value seperation
    key=""                              # empty key initilization
    for w in words:                     # a loop word by word in file
        wnum+=1                         # wnum keeps word num in file 
        ##print wnum
        if wnum%2 == 1:                 # if word num is odd w is a key
            key=int(w)            
        elif wnum%2 == 0:               # if word num is even w is a value
            d[key]=w                    # insert the dictionary new key and value

    return d                            #returns dictionary to external use

    
def displayDictionaryInTerminal(dictinory):
    i = 0
    for elem in dictinory.keys():
        print i,".eleman", "Name = " , dictinory[elem] , "Number = " ,elem
        i=i+1
    return 

#!! this function: 
#!!         takes a dictionary as a paremeter
#!!         creates a html file using the dictionary context
#!!         and shows this html file in web browser 
def createAndDisplayHtmlFile(dict):
    f = open('studentlist.html','w')    #open the given txt file in read mode

    message = """<html>                
                <head>STUDENT LIST</head>
                <body><p>"""            #prepare text to write

    for key in dict.items():
        message+= """<p>"""+str(key)+"""</p>""" 

    message+= """</p></body>
                </html>"""

    f.write(message)                    #write in file
    f.close()                           #file close

    webbrowser.open_new_tab('studentlist.html')  #open and show in web browser



def connectAndLoadInFile(url):

    website = urllib2.urlopen(url)      #connect to a URL
    html = website.read()               #read html code

                                        #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://[a-z,A-Z,0-9]+.*?)"', html)
   
    file = open('example.html',"w+")
    
    file.write(html)
    
    file.close()
    
    webbrowser.open_new_tab('example.html')

#function calls
dict= createADictionary()
createAndDisplayHtmlFile(dict)
connectAndLoadInFile("http://www.gtu.edu.tr/")
displayDictionaryInTerminal(dict)