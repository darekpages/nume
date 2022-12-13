# nume.py    v.1.10  (Python 3.7, 3.10)
# Library for engineering calculations (with SI units) to simplify
# calculations e.g. in electronics.
# Copyright 2017-2022 (C) DAREKPAGES
# 04.01.2017 - 13.12.2022
#- -------------------------------------------------------------------
# v.1.1 - I added a help displayed with the command >> help (e).
# v.1.2 - I added a parallel connection computation function: parajoint ().
# v.1.3 - The function of selecting a resistance from the E series.
# v.1.4 - I resigned from the additional description in the header, only
# help remained.
# v.1.5 - I rearranged functions and variables. I added valofrow to the
# function error handling in case of exceeding the value from the E range.
# v.1.6 - I changed the name of the library to nume. I extended the sci()
# function to process a number with a unit (6.432, 'k') which is of
# type tuple.
# v.1.7 - I added the parajointfind () function which computes an
# additional resistor to the second one with the expected resultant
# parallel resistance.
# v.1.8 - I added EEngine.py module import options in linux. The directory
# nume is to be placed in /home/user/bin.
# v.1.9 - I supplemented with additional resistance series E6, E48, E96.
# v.1.10 -  I added four new number functions ronto, quecto, Ronna, Quetta.
#--------------------------------------------------------------------
"""Engineering calculations with SI units.
The library is an extension of the EEngine library.

It is best to import the module with a command
    from nume import*
or
    python -i -c "from nume import *"
or
    import nume
or 
    import nume as e
    
The module allows calculations with defined SI units
    Jotta, Zetta, Eksa, Peta, Tera, Giga, Mega, kilo, mili, micro, nano,
    pico, femto, atto, zepto, jokto.
Calculation of parallel and serial connections, selecting values
standard series E12, E24.

EXAMPLE:
    k(22)*u(123) --> 2.7059999999999995 (V= 22kOm*150uA)
    m(500)/k(4.7) --> 0.00010638297872340425
    sci(2400) --> '2.4e+03'
    sci(0.00010638297872340425) --> '1.0638e-04'
    sci((6.432, 'k')) --> '6.432e+03'
    unit(6432) --> (6.432, 'k')
    valofrow(13) --> 12
    valofrow(13, 'E24') --> 13
    E6, E12 lub E24 --> [1.0, 1.2,... 820.0] -listing of a resistive series
    parajoint([1.2, 5.6, 2.2]) --> 0.682
    parajoint([1.2, 5.6, 2.2], 1) --> 9.0
    parajointfind(1.3, [4.7, 15]) --> 2.042
"""
import sys
if sys.platform=='linux':
    sys.path.append(sys.path[0]) #adding a launch path
    import EEngine
else:
    import EEngine
del(sys)

E6= (1.0, 1.5, 2.2, 3.3, 4.7, 6.8, 10.0, 15.0, 22.0, 33.0, 47.0, 68.0,
     100.0, 150.0, 220.0, 330.0, 470.0, 680.0)
E12= (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8,
          8.2, 10.0, 12.0, 15.0, 18.0, 22.0, 27.0, 33.0, 39.0,
          47.0, 56.0, 68.0, 82.0, 100.0, 120.0, 150.0, 180.0, 220.0,
          270.0, 330.0, 390.0, 470.0, 560.0, 680.0, 820.0)
E24= (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
          3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2,
          9.1, 10.0, 11.0, 12.0, 13.0, 15.0, 16.0, 18.0, 20.0, 22.0,
          24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 43.0, 47.0, 51.0, 56.0,
          62.0, 68.0, 75.0, 82.0, 91.0, 100.0, 110.0, 120.0, 130.0,
          150.0, 160.0, 180.0, 200.0, 220.0, 240.0, 270.0, 300.0,
          330.0, 360.0, 390.0, 430.0, 470.0, 510.0, 560.0, 620.0,
          680.0, 750.0, 820.0, 910.0)
E48= (1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.33, 1.4, 1.47, 1.54, 1.62, 1.69,
      1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87,
      3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87,
      5.11, 5.36, 5.62, 5.9, 6.19, 6.49, 6.81, 7.15, 7.5, 7.87, 8.25, 8.66,
      9.09, 9.53, 10.0, 10.5, 11.0, 11.5, 12.1, 12.7, 13.3, 14.0, 14.7,
      15.4, 16.2, 16.9, 17.8, 18.7, 19.6, 20.5, 21.5, 22.6, 23.7, 24.9,
      26.1, 27.4, 28.7, 30.1, 31.6, 33.2, 34.8, 36.5, 38.3, 40.2, 42.2,
      44.2, 46.4, 48.7, 51.1, 53.6, 56.2, 59.0, 61.9, 64.9, 68.1, 71.5,
      75.0, 78.7, 82.5, 86.6, 90.9, 95.3, 100.0, 105.0, 110.0, 115.0, 121.0,
      127.0, 133.0, 140.0, 147.0, 154.0, 162.0, 169.0, 178.0, 187.0, 196.0,
      205.0, 215.0, 226.0, 237.0, 249.0, 261.0, 274.0, 287.0, 301.0, 316.0,
      332.0, 348.0, 365.0, 383.0, 402.0, 422.0, 442.0, 464.0, 487.0, 511.0,
      536.0, 562.0, 590.0, 619.0, 649.0, 681.0, 715.0, 750.0, 787.0, 825.0,
      866.0, 909.0, 953.0)
E96= (1.0, 1.02, 1.05, 1.07, 1.1, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.3,
      1.33, 1.37, 1.4, 1.43, 1.47, 1.5, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74,
      1.78, 1.82, 1.87, 1.91, 1.96, 2.0, 2.05, 2.1, 2.15, 2.21, 2.26, 2.32,
      2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.8, 2.87, 2.94, 3.01, 3.09,
      3.16, 3.24, 3.32, 3.4, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12,
      4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49,
      5.62, 5.76, 5.9, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32,
      7.5, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76,
      10.0, 10.2, 10.5, 10.7, 11.0, 11.3, 11.5, 11.8, 12.1, 12.4, 12.7, 13.0,
      13.3, 13.7, 14.0, 14.3, 14.7, 15.0, 15.4, 15.8, 16.2, 16.5, 16.9, 17.4,
      17.8, 18.2, 18.7, 19.1, 19.6, 20.0, 20.5, 21.0, 21.5, 22.1, 22.6, 23.2,
      23.7, 24.3, 24.9, 25.5, 26.1, 26.7, 27.4, 28.0, 28.7, 29.4, 30.1, 30.9,
      31.6, 32.4, 33.2, 34.0, 34.8, 35.7, 36.5, 37.4, 38.3, 39.2, 40.2, 41.2,
      42.2, 43.2, 44.2, 45.3, 46.4, 47.5, 48.7, 49.9, 51.1, 52.3, 53.6, 54.9,
      56.2, 57.6, 59.0, 60.4, 61.9, 63.4, 64.9, 66.5, 68.1, 69.8, 71.5, 73.2,
      75.0, 76.8, 78.7, 80.6, 82.5, 84.5, 86.6, 88.7, 90.9, 93.1, 95.3, 97.6,
      100.0, 102.0, 105.0, 107.0, 110.0, 113.0, 115.0, 118.0, 121.0, 124.0,
      127.0, 130.0, 133.0, 137.0, 140.0, 143.0, 147.0, 150.0, 154.0, 158.0,
      162.0, 165.0, 169.0, 174.0, 178.0, 182.0, 187.0, 191.0, 196.0, 200.0,
      205.0, 210.0, 215.0, 221.0, 226.0, 232.0, 237.0, 243.0, 249.0, 255.0,
      261.0, 267.0, 274.0, 280.0, 287.0, 294.0, 301.0, 309.0, 316.0, 324.0,
      332.0, 340.0, 348.0, 357.0, 365.0, 374.0, 383.0, 392.0, 402.0, 412.0,
      422.0, 432.0, 442.0, 453.0, 464.0, 475.0, 487.0, 499.0, 511.0, 523.0,
      536.0, 549.0, 562.0, 576.0, 590.0, 604.0, 619.0, 634.0, 649.0, 665.0,
      681.0, 698.0, 715.0, 732.0, 750.0, 768.0, 787.0, 806.0, 825.0, 845.0,
      866.0, 887.0, 909.0, 931.0, 953.0, 976.0)

def Q(number):
    """Unit e30 Quetta."""
    return EEngine.Number(number).Q()

def R(number):
    """Unit e27 Ronna."""
    return EEngine.Number(number).R()

def Y(number):
    """Unit e24 Jotta."""
    return EEngine.Number(number).Y()

def Z(number):
    """Unit e21 Zetta."""
    return EEngine.Number(number).Z()

def E(number):
    """Unit e18 Eksa."""
    return EEngine.Number(number).E()

def P(number):
    """Unit e15 Peta."""
    return EEngine.Number(number).P()

def T(number):
    """Unit e12 Tera."""
    return EEngine.Number(number).T()

def G(number):
    """Unit e9 Giga."""
    return EEngine.Number(number).G()

def M(number):
    """Unit e6 Mega."""
    return EEngine.Number(number).M()
   
def k(number):
    """Unit e3 kilo."""
    return EEngine.Number(number).k()

def m(number):
    """Unit e-3 mili."""
    return EEngine.Number(number).m()

def u(number):
    """Unit e-6 micro."""
    return EEngine.Number(number).u()

def n(number):
    """Unit e-9 nano."""
    return EEngine.Number(number).n()

def p(number):
    """Unit e-12 pico."""
    return EEngine.Number(number).p()

def f(number):
    """Unit e-15 femto."""
    return EEngine.Number(number).f()

def a(number):
    """Unit e-18 atto."""
    return EEngine.Number(number).a()

def z(number):
    """Unit e-21 zepto."""
    return EEngine.Number(number).z()

def y(number):
    """Unit e-24 jokto."""
    return EEngine.Number(number).y()

def r(number):
    """Unit e-27 ronto."""
    return EEngine.Number(number).r()

def q(number):
    """Unit e-30 quecto."""
    return EEngine.Number(number).q()
    
def unit(number):
    """He adds the appropriate SI unit to the number:
    unit(6400) --> (6.4, 'k')"""
    return EEngine.Number(number).unit()

def sci(number):
    """Converts a decimal or SI number to the scientific format:
    sci(6432) --> '6.432e+03'
    sci((6.432, 'k')) --> '6.432e+03'"""
    typ= type(number) is tuple
    if typ!=True:
        return EEngine.Number(number).unit(sci= True)
    else: 
        uni= number[1]  #unit number
        mul= EEngine.Number.__tj__.index(uni) #multiplier
        nNumb= number[0]*EEngine.Number.__mno__[mul] #regular number
        return EEngine.Number(nNumb).unit(sci= True)

def valofrow(value, rowE='E12'):
    """Selecting the setpoint from the resistance series.
    Series E12 is default series:
    valofrow(1.3) --> 1.2
    valofrow(1.3,'E12') --> 1.2
    valofrow(1.3, 'E24') --> 1.2
    EE(900).valofrow() --> -820 the value given is greater
    than the nominal value.
    EE(0.5).valofrow() --> -1 the stated value is less
    than the nominal value.
    """
    tmplist= []
    #When value is out of range, limit the value
    if value<1:
        value= 1
    elif value>680 and rowE=='E6':
        value= 680
    elif value>820 and rowE=='E12':
        value= 820
    elif value>910 and rowE=='E24':
        value= 910
    elif value>953 and rowE=='E48':
        value= 953
    elif value>976 and rowE=='E96':
        value= 976
    #Association of resistive series with the appropriate list
    elif rowE=='E6':
        row= E6
    if rowE=='E12':
        row= E12
    elif rowE=='E24':
        row= E24
    elif rowE=='E48':
        row= E48
    elif rowE=='E96':
        row= E96    
    #Selecting from series of two similar values
    for n in row:
        if value<=n:
            tmplist.append(n)
    zSzerWieksza= tmplist[0]
    for n in row:
        if value>=n:
            tmplist.append(n)
    zSzerMniejsza= tmplist[-1]
    #Final value and result
    if (value-zSzerMniejsza)<(zSzerWieksza-value):
        return zSzerMniejsza
    else:
        return zSzerWieksza
    
def parajoint(listvalue, conn=0):
    """Calculation of parallel and series connection:
    parajoint([1.2, 5.6, 2.2]) --> 0.682 the default is parallel connection;
    parajoint([1.2, 5.6, 2.2], 1) --> 9.0 serial connection.
    """
    if conn==0:    #parallel
        ro= 0
        for r in listvalue:
            ro+= 1/r
        return 1/ro
    elif conn==1:   #serial
        return sum(listvalue)

def parajointfind(valuepararell, values):
    '''The function returns the value of the missing resistor in a parallel
    connection.
    parajointfind(resistor_parallel, resistor_or_list_resistors)--> resistor_searched.
    parajointfind(1.3, [4.7, 15]) --> 2.042
    '''
    howtype= lambda tp: str(type(tp))[str(type(tp)).find("'")+1:-2]
    if howtype(valuepararell)=='str':
        valuepararell= float(valuepararell)
    if (howtype(values)== 'int') or (howtype(values)=='float'):
        rres= 1/(1/valuepararell-1/values)
    if howtype(values)=='list':
        rres= 1/(1/valuepararell-1/parajoint(values))
    return rres
