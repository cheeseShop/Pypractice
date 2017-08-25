class Fraction:
    def __init__(self,top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num, "/", self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self, otherFraction):
        newNumer = self.num*otherFraction.den + self.den*otherFraction.num
        newDenom = self.den * otherFraction.den
        commonDiv = gcd(newNumer,newDenom)
        return Fraction(newNumer//commonDiv,newDenom//commonDiv)
    def __sub__(self, otherFraction):
        newNumer = self.num*otherFraction.den - self.den*otherFraction.num
        newDenom = self.den * otherFraction.den
        commonDiv = gcd(newNumer,newDenom)
        return Fraction(newNumer//commonDiv,newDenom//commonDiv)
    def __mul__(self, other):
        newNumer1 = self.num * other.num
        newDenom1 = self.den * other.den
        common = gcd(newNumer1,newDenom1)
        return Fraction(newNumer1//common, newDenom1//common)
    def __truediv__(self, other):
        newNumer2 = self.num * other.den
        newDenom2 = self.den * other.num
        common = gcd(newNumer2, newDenom2)
        return Fraction(newNumer2 // common, newDenom2 // common)
    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num *self.den
        return firstNum == secondNum
    def __lt__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num *self.den
        return firstNum < secondNum
    def __gt__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num *self.den
        return firstNum > secondNum



#to check common div
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n



x=Fraction(21,28)
y=Fraction(3,4)
print(x+y)
print(x==y)
print(x<y)
print(x>y)
