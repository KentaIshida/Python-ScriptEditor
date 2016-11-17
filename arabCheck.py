#!/usr/bin/python


import sys, os
from lxml import etree

subfile = sys.argv[1]
mydir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(mydir, 'NF_AR_ok_letters.txt'), 'r') as f:
    ar_ok = []
    for line in f:
        chartoadd = line[2:].rstrip('\n')
        ar_ok.append(chartoadd)

ascii_ok = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '"', '.', ':', '-', ' ', '!', '/', '\\']

data = open(subfile, 'r').read()
doc = etree.HTML(data)

lastchar = ''

errorFound = False

for p in doc.xpath('//div/p'):
    allsubs = p.xpath('./span/text()')
    for line in allsubs:
        charlist = list(line)
        for singlechar in charlist:
            singlecharcode = singlechar.encode("unicode_escape")
            #print singlecharcode.strip('\u').strip(' ') + ' > ' + singlechar
            #print '---'
            if singlecharcode.strip('\u').strip(' ') not in ar_ok:
                if singlecharcode not in ascii_ok:
                    print "error > " + line
                    print '  ' + singlechar + ' [ ' + singlecharcode + ' ]'
                    errorFound = True
            else:
                if singlecharcode.strip('\u').strip(' ') == '0654' and lastchar == '0644':
                    print "error > " + line
                    print "FUCKING WRONG LAM"
                    errorFound = True
                
                if singlecharcode.strip('\u').strip(' ') == '064b' and lastchar == '0644':
                    print "error > " + line
                    print "FUCKING WRONG LAM2"
                    errorFound = True
                
                if singlecharcode.strip('\u').strip(' ') == '064f' and lastchar == '0627':
                    print "error > " + line
                    print "FUCKING WRONG Dammah"
                    errorFound = True
                
                if singlecharcode.strip('\u').strip(' ') == '0651' and lastchar == '0627':
                    print "error > " + line
                    print "FUCKING WRONG Shaddah" 
                    errorFound = True   
                    
                if singlecharcode.strip('\u').strip(' ') == '' and lastchar == '':
                    print "error > " + line
                    print "Double Space"  
                    errorFound = True  
                    
                if singlecharcode.strip('\u').strip(' ') == '064e' and lastchar == '0627':
                    print "error > " + line
                    print "Fatha on Alef"
                    errorFound = True    
                
            lastchar = singlecharcode.strip('\u').strip(' ')
            
if errorFound == False:
    print "Succeed!"
