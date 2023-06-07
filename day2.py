#variable

artcell = 2002
print(artcell)

black = 2001

aurthohin = artcell - black 

print(aurthohin) #black


#string

firstName = "MK"
lastName = " Hridoy"

fullName = firstName + lastName
print(fullName) # MK Hridoy

myName = "MKH"
yourName = "TasTan"

ourName = myName + ' ' + yourName

print(ourName) #MKH TasTan


# string Concatenation

print('Hello '+ 'Hridoy') # Hello Hridoy
#  print('Hi ' + 5)     # error . Bcoz => String & int can't be add .

#formatted string

singer = "kabir"
age = 56

print(f'Hi {singer} . How are you . I think you are {age} years old ')

#String Indexing

king = "The Great Hridoy"
print(king) 

print(king[0]) #t
print(king[6]) #e
print(king[0:3]) #The
print(king[4:]) # Great Hridoy