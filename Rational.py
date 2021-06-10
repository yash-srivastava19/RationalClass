""" [Rational Class:] Representing Rationals in Python(Easy version of fractions class in Python)"""
import math
class Rational:
    def __init__(self,numerator:int=0,denominator:int=1) -> None:
        self.num,self.denom=0,1
        self.__setNumerator(numerator)
        self.__setDenominator(denominator)
        self.__set_Number()
        self.__reduceRational()    
    def __setNumerator(self,numerator:int)->None:
        """ [Validate the entered numerator] """
        try :
            self.num=int(numerator)
        except ValueError as _:
            raise Exception("[INPUT ERROR(VALUE ERROR)][MESSAGE]:Numerator entered is wrong")
    
    def __setDenominator(self,denominator:int)->None:
        """ [Validate the entered denominator] """
        try:
            assert self.denom!=0
        except AssertionError as _:
            raise Exception("[INPUT ERROR(ZERODIVISION ERROR)][MESSAGE]:Denominator cannot be zero")
        try:
            self.denom=int(denominator)
        except ValueError as _:
            raise Exception("[INPUT ERROR(VALUE ERROR):][MESSAGE]Denominator entered is wrong")                        

    def __getNumerator(self)->int:
        return self.num

    def __getDenominator(self)->int:
        return self.denom

    def __set_Number(self)->None:
        if (self.__getNumerator()<0 and self.__getDenominator()<0) or (self.__getDenominator()<0 and self.__getNumerator()>0):
            self.__setNumerator(-1*self.__getNumerator())
            self.__setDenominator(-1*self.__getDenominator())

    def printRational(self):
        """ [Display the Rational number in the form p/q] """
        self.__reduceRational()
        if self.__getNumerator()==0:
            print("{}".format(0))
        elif self.__getNumerator()==self.__getDenominator():
            print("{}".format(1))
        elif self.__getDenominator()==1:
            print("{}".format(self.__getNumerator()))     
        else:
            print("{}/{}".format(self.__getNumerator(),self.__getDenominator()))    
    
    def Reciprocal(self)->'Rational':
        """ [Returns the reciprocal of the Rational number] """
        new_num=self.__getDenominator()
        new_denom=self.__getNumerator()
        return Rational(new_num,new_denom)

    def __reduceRational(self)->None:
        """ [Reduce the fraction] """
        cf=math.gcd(self.__getNumerator(),self.__getDenominator())
        self.__setNumerator(self.__getNumerator()/cf) 
        self.__setDenominator(self.__getDenominator()/cf) 
    
    #Overridden Methods
    def __add__(self,other:'Rational')->'Rational':
        try:
            res_num=self.__getNumerator()*other.denom + self.__getDenominator()*other.num
            res_denom=self.__getDenominator()*other.denom
            return Rational(res_num,res_denom)
        except AttributeError as _:
            raise Exception("[TYPE MISMATCH][MESSAGE]:Addtion allowed only between Rationals")
    
    def __sub__(self,other:'Rational')->'Rational':
        try:
            res_num=self.__getNumerator()*other.denom - self.__getDenominator()*other.num
            res_denom=self.__getDenominator()*other.denom    
            return Rational(res_num,res_denom)
        except AttributeError as _:
            raise Exception("[TYPE MISMATCH][MESSAGE]:Subtraction allowed only between Rationals")
    
    def __mul__(self,other:'Rational')->'Rational':
        """ [Multiply rational numbers] """
        try:
            res_num=self.__getNumerator()*other.num
            res_denom=self.__getDenominator()*other.denom    
            return Rational(res_num,res_denom)
        except AttributeError as _:
            raise Exception("[TYPE MISMATCH][MESSAGE]:Multiplication allowed only between Rationals")
    
    def __truediv__(self,other:'Rational')->'Rational':
        """ [Divide rational numbers] """
        try:
            res_num=self.__getNumerator()*other.denom
            res_denom=self.__getDenominator()*other.num    
            return Rational(res_num,res_denom)
        except AttributeError as _:
            raise Exception("[TYPE MISMATCH][MESSAGE]:Division allowed only between Rationals")                        
    
    def __pow__(self,n:int=1)->'Rational':
        """ [Raise fraction to a power] """
        new_num=(self.__getNumerator())**n
        new_denom=(self.__getDenominator())**n
        return Rational(new_num,new_denom)
    
    def __repr__(self) -> str:
        """ [Represent Rational object] """
        return "Rational({},{})".format(self.num,self.denom)

#Object Instantiation:
x=Rational(2,13)
y=Rational(1,2)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
