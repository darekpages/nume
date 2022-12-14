# EEngine.py      v.2.2 (Python 3.10)
# SI class of number that simplifies calculations, e.g. in electronics.
# Copyright 2021 (C) DAREKPAGES
# 2021-12-10 - 2022-12-13
#--------------------------------------------------------------------------
# v.2.0 - I rewritten version 1.4 and tidied it up. This version is incompatible
# with the previous version.
# v.2.1 - I removed computing functions of electronics. I transferred them to
# the module nume.py. The class became universal.
# v.2.2 - I added four new numbers named in 2022: ronto, quecto, Ronna, Quetta.
# The scope of the module includes named numbers: 10e-30... 10e+30.
#--------------------------------------------------------------------------
class Number:
    """Class of number based on SI engineering units
    EXAMPLE:
        Number(4700).unit() --> (4.7, 'k')
        Number(4700).unit(sci=True) --> 4.7e+03
        Number(4700).k() --> 4700000 or any other unit.
    """
    __tj__= ('Q', 'R','Y','Z','E','P','T','G','M','k','','m','u','n','p','f','a','z','y', 'r', 'q')
    __mno__= (10**30, 10**27, 10**24,10**21,10**18,10**15,10**12,10**9,10**6,10**3, 1,10**-3,
          10**-6, 10**-9, 10**-12, 10**-15, 10**-18, 10**-21, 10**-24, 10**-27, 10**-30)
    __mns__= ('+30', '+27', '+24', '+21', '+18', '+15', '+12', '+09', '+06', '+03', '00', '-03',
          '-06', '-09', '-12', '-15', '-18', '-21', '-24', '-27', '-30')
    
    def __init__(self, number):
        self.number= number

    def unit(self, sci= False):
        """Convert a number to engineering notation,
         or to scientific notation like type str:
        Number(4700).unit() --> (4.7, 'k')
        Number(4700).unit(sci=True) --> 4.7e+03"""
        for m in self.__mno__:
            czyc= self.number/m
            if int(czyc)>0:
                jdn= self.__tj__[self.__mno__.index(m)]
                if sci==False:
                    return czyc, jdn
                    break
                else:
                    return str(czyc)+'e'+self.__mns__[self.__tj__.index(jdn)]
                    break
    
    def Q(self):
        """Unit e30 Quetta."""
        return self.number*self.__mno__[0]

    def R(self):
        """Unit e27 Ronna."""
        return self.number*self.__mno__[1]
        
    def Y(self):
        """Unit e24 Jotta."""
        return self.number*self.__mno__[2]

    def Z(self):
        """Unit e21 Zetta."""
        return self.number*self.__mno__[3]
    
    def E(self):
        """Unit e18 Eksa."""
        return self.number*self.__mno__[4]

    def P(self):
        """Unit e15 Peta."""
        return self.number*self.__mno__[5]

    def T(self):
        """Unit e12 Tera."""
        return self.number*self.__mno__[6]

    def G(self):
        """Unit e9 Giga."""
        return self.number*self.__mno__[7]

    def M(self):
        """Unit e6 Mega."""
        return self.number*self.__mno__[8]

    def k(self):
        """Unit e3 kilo."""
        return self.number*self.__mno__[9]

    def m(self):
        """Unit e-3 mili."""
        return self.number*self.__mno__[11]

    def u(self):
        """Unit e-6 micro."""
        return self.number*self.__mno__[12]

    def n(self):
        """Unit e-9 nano."""
        return self.number*self.__mno__[13]

    def p(self):
        """Unit e-12 pico."""
        return self.number*self.__mno__[14]

    def f(self):
        """Unit e-15 femto."""
        return self.number*self.__mno__[15]

    def a(self):
        """Unit e-18 atto."""
        return self.number*self.__mno__[16]

    def z(self):
        """Unit e-21 zepto."""
        return self.number*self.__mno__[17]

    def y(self):
        """Unit e-24 jokto."""
        return self.number*self.__mno__[18]

    def r(self):
        """Unit e-27 ronto."""
        return self.number*self.__mno__[19]

    def q(self):
        """Unit e-30 quecto."""
        return self.number*self.__mno__[20]
        
