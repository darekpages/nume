#!/usr/bin/python3.10
#------------------------------------------------------------
# Script to generate a list of numbers in the range 1y .. 1Y.
# Nota-numbers.py
# 
# Simply copy the generated list from the console, and after
# editing it in the editor, print it.
#
# Copyright (C) DAREKPAGES
# v. 1   26.09.2022
#------------------------------------------------------------
import nume

multi= nume.EEngine.Number.__mno__  #multiplier list
numstart= nume.sci(nume.y(1))       #initial value

#Create numbers list
pot= int(numstart[-2:])         #maximum power
potmax= int('-'+numstart[-2:])  #power minimal
buf= []
minsign= ''
ubase= None
for i in range(potmax, pot+1):
    if i>0:
        minsign= '+'            #for positive number
    num= '1e'+minsign+str(i)    #building scientific number
    #Create positive and negative decimal numbers
    if i<0:
        zadd= '0'   #negative
        oadd= '1'   #add 1 to negative number
    else:
        zadd= '1'   #positive
        oadd= ''    #none
    for zero in range(0, abs(i)):
        if zero==0:
            buf.append(zadd)        #'1' or '0' before dot
            if i<0:
                buf.append('.')
        buf.append('0')             #zero in number
    nwithzero= ''.join(buf)+oadd    #building decimal number
    if i==0:                        #number without unit
        nwithzero= '0.0'
        
    nsci= nume.unit(float(num))[1]  #obtaining SI unit

    #Current values
    uonc= ''
    if i%3==0:                      #occurrence of base unit
        uonc= '1'+nsci
        ubase= float(num)
    valakt= int(round(float(num)/ubase))   #value consistent with unit
        
    print(nwithzero, num, str(valakt)+nsci)
    buf= []                         #clear
