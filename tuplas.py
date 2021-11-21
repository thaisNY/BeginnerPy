#creating a empety tuple
Tuple1 = ()
print(Tuple1)
#creating a tuple with strings
Tuple2 = ('Thais','Lucas','Vanessa','Yago','fifth','aaaaa','bbbbb')
print(Tuple2)
#creating a tuple with a list
lista = [1,2,3,4,5,'sixth']
Tuple3 = tuple(lista)
print(Tuple3)
#crating a tuple with built in function
Tuple4 = tuple("Queiroz")
print(Tuple4)
#creating a tuple with a variaty of datatypes
Tuple5 = (1,2,3,'hello','a',4)
print(Tuple5)
#creating nested tuples
Tuple6 = ('a','b','c')
Tuple7 = ('d','e','f')
Tuple8 = (Tuple6, Tuple7)
print(Tuple8)
#creating tuples with loops
Tuple9 = ('Facebook')
for i in range(5):
    Tuple9 = (Tuple9,)
    print(Tuple9)
#tuple with repeticion
Tuple10 = ('hello',)*5
print(Tuple10)
#acess with index
print(Tuple10[1])
#tuple unpack
Tuple11 = ('Thais','Larissa','Rodrigues')
a, b, c = Tuple11
print(a)
print(b)
print(c)
#concatenecion
Tuple12 = (1,2,3)
Tuple13 = (4,5,6)
print(Tuple12 + Tuple13)
#Slice
#Remove the first element
print(Tuple12[1:])
#Reverse
print(Tuple12[::-1])
#print on range
Tuple13 = (1,2,3,4,5,6,7,8,9)
print(Tuple13[3:7])
#delet a tuple
Tuple14 = (1,2,3,4,2022)
print(Tuple14)
del(Tuple14)
#print(Tuple14)
#Tuple Method (2)
#count
Tuple15 = ('Hello','Recife','I','miss','you','Hello')
print(Tuple15.count('Hello'))
#index
print(Tuple15.index('I'))
print('**'*20)
#Built-In functions
Tuple16 = ()
all1 = all(Tuple15)
all2 = all(Tuple16)
print(all1)
print(all2)
any1 = any(Tuple15)
any2 = any(Tuple16)
print(any1)
print(any2)
Tuple17 = (10,2,39,41,44,66,8)
max_ = max(Tuple17)
print(max_)
min_ = min(Tuple17)
print(min_)
sum_ = sum(Tuple17)
print(sum_)
len_ = len(Tuple17)
print(len_)
print(sorted(Tuple17))
Tuple18 = ('abracadabra', 'the', 'world','turn', 'magic')
for count, word in enumerate(Tuple18):
    print(count, word)





