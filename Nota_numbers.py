#!/usr/bin/python3.10
#------------------------------------------------------------
# Script to generate a list of numbers in the range min .. max,
# in terms of known units.
# Nota-numbers.py
# 
# Simply copy the generated list from the console, and after
# editing it in the editor, print it.
#
# Copyright (C) DAREKPAGES
# v. 2   26.09.2022-12.12.2022
#------------------------------------------------------------
# v.2 - new better version.
#------------------------------------------------------------
import EEngine
ee= EEngine
multis= list(ee.Number.__mno__)
fir= '%e' % multis[0]
for j in range(1, 3):    #two additional values to start with
    np= int(str(fir)[-2:])+j
    multis.insert(0, float('1e'+str(np)))
flg= False
elem= int(('%10.0e' % multis[0]).strip()[-2:]) #1-st value
cval= [100, 10, 1]

for n in range(0, elem*2-1):
    order= elem-n
    if order==-1:            #negative value
        flg= True
    if flg==True:            #negative value occurs
        cor= 1
        plus= ''
        cval= [1, 10, 100]
    else: 
        cor= 0
        plus= '+'            #for positive value
    zeros= ''
    for z in range(0, abs(order)-cor): #number zeros
        zeros= zeros+'0'     #str zeros
    if flg==False:           #str positive value
        decz= '1'+zeros 
    else:                    #str negative value
        decz= '0.'+zeros+'1'
    vl= '1e'+plus+str(order) #scientific record
    uni= ee.Number(float(vl)).unit()[1] #unit
    cuni= cval[n % 3]                   #number units
    print(decz, vl, cuni, uni)
