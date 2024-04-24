#begin
import math
#1 
# class Kvadrat:
#     def __init__(self , a) :
#         self.a = a
#     def pr(self):
#         P= self.a*4
#         print(P)

# kv = Kvadrat(6)
# kv.pr



#2
# class Kvadrat:
#     def __init__(self,a):
#         self.a = a

#     def yuza(self):
#         S = self.a**2
#         print(S)
# a2 = Kvadrat(7)
# a2.yuza()

#3
# class Tortburchak:
#     def __init__(self, a , b):
#         self.a = a
#         self.b = b
#     def S(self):
#         S  = self.a*self.b
#         print(S)
#     def P(self):
#         P = 2*(self.a+self.b)
#         print(P)

# a3 = Tortburchak(5,5)
# a3.S()
# a3.P()

#4
# class Aylana:
#     def __init__(self,d,  p = 3.14):
#         self.p = p
#         self.d = d
#     def uzunlig(self):
#         L= self.d**self.p
#         print(L)
# a4 = Aylana(5)
# a4.uzunlig()
    
#5
# class KUb:
#     def __init__(self,a):
#         self.a = a
#     def hajm(self):
#         V= self.a**3
#         print(V)
#     def sirti(self):
#         S = 6*(a**2)
#         print(S)

# a5 = KUb(6)
# a5.hajm()
# a5.sirti()

#6
# class paralepeped:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def hajm(self):
#         V = self.a*self.b*self.c
#         print(V)
#     def sirti(self):
#         S = 2*(self.a*self.b+self.b*self.c+self.a*self.c)
#         print(S)
# a6 = paralepeped(4,5,4)
# a6.hajm()
# a6.sirti()

#7
# class Doira:
#     def __init__(self , r,p=3.4):
#         self.r = r
#         self.p = p
#     def uzunligi(self):
#         L = 2*self.p*self.r
#         print(L)
#     def yuza(self):
#         S = self.p*self.r**2
#         print(S)
# a7 = Doira(6)
# a7.uzunligi()
# a7.yuza()

#8
# class l8:
#     def __init__(self,a,b) :
#         self.a =a 
#         self.b = b
#     def ar(self):
#         print(self.a+self.b/2)

# a8 = l8(6,7)
# a8.ar()

#9
# class l9:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def geometrig(self):
#         geo = math.sqrt(self.a*self.b)
#         print(geo)
# a9 = l9(6,9)
# a9.geometrig()

#10
# class l10:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def yigindi(self):
#         print(self.a+self.b)
#     def kopaytma(self):
#         print(self.a*self.b)
#     def kv1(self):
#         print(self.a**2)
#     def kv2(self):
#         print(self.b**2)
# a10 = l10(8,6)
# a10.yigindi()
# a10.kopaytma()
# a10.kv1()
# a10.kv2()

#11
# class l11:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def yigindi(self):
#         print(self.a+self.b)
#     def kupaytma(self):
#         print(self.a*self.b)
#     def module_a(self):
#         md = abs(self.a)
#         print(md)
#     def module_b(self):
#         md2 = abs(self.b)
#         print(md2)

# a11 = l11(-8,-9)
# a11.kupaytma()
# a11.yigindi()
# a11.module_a()
# a11.module_b()


#12
# class l12:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def gipotenuza(self):
#         c = (self.a**2+self.b**2)**0.5
#         print(c)
#     def per(self):
#         P = self.a+self.b+self.c
#         print(P)

# a12 = l12(4,5)
# a12.gipotenuza()
# a12.per()


#13
# class l13:
#     def __init__(self,R1,R2,p=3.14):
#         self.R1 = R1
#         self.R2 = R2
#         self.p = p
#     def Yuza1(self):
#         S1 = self.p*self.R1
#         print(S1)
#     def Yuza2(self):
#         S2 = self.p*self.R2
#         print(S2)
#     def Yuza3(self):
#         S3 = self.p*(self.R1-self.R2)
#         print(S3)

# a13 = l13(10,15)
# a13.Yuza1()
# a13.Yuza2()
# a13.Yuza3()

#14
# class l14:
#     def __init__(self,L):
#         self.L = L
#         self.p = 3.14
#     def radius(self):
#         R = self.L/2*self.p
#         print(R)
#     def yuza(self):
#         S = self.p*self.L/2*self.p**2
#         print(S)
 
# a14 = l14(45)
# a14.radius()
# a14.yuza()

#15
# class l15:
#     def __init__(self,S):
#         self.S = S
#         self.p = 3.14
#     def Radius(self):
#         R = self.S/self.p
#         print(R)
#     def Diametr(self):
#         D = 2* self.S/self.p
#         print(D)

# a15 = l15(9)
# a15.Diametr()
# a15.Radius()

#16
# class l16:
#     def __init__(self,x1,x2):
#         self.x1 = x1
#         self.x2 = x2
#     def module(self):
#         c = abs(self.x1-self.x2)  
#         print(c)
# a16 = l16(7,7)
# a16.module()


# #17
# class l17:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def AC(self):
#         k = abs(self.a+self.b)
#         print(k)
#     def BS(self):
#         k2 = abs(self.a +self.b)
#         print(k2)
# a17 = l17(5,3,4)
# a17.AC()
# a17.BS()

#18
# class l18:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def AC(self):
#         k = abs(self.a*self.b)
#         print(k)
#     def BS(self):
#         k2 = abs(self.a *self.b)
#         print(k2)
# a17 = l18(5,3,4)
# a17.AC()
# a17.BS()