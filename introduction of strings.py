#creating a string
my_first_string="algebra"
print(my_first_string)

#entire phrase
phrase="statistics sits at the heart of machine learning"
print(phrase)

#symbols
hashtag="#"
print(hashtag)
print(type(hashtag))

#playing with string
algo="re  on"
print(len(algo))

#string indexing
string="principal component analysis!"
print(string)
print(string[-2])
print(string[15])
print(len(string))
print(string[28])

#string slicing
print(string)
print(string[1:])
print(string[13])
print(string[12])
print(string[10:])
print(string[3:5])
print(string[2:4])
print(string[-2])
print(string[-1:-4])
print(string[::3])
print(string[5:15:5])
print(string[::1])
print(string[::-1])
print(string[2:4:-1])
s="foobar"
print(s[0::-3])

#string properties

#concatenate string
str1="abc"
str2="def"
print(str1 +' '+str2)
print(str1 +' 4 '+str2)
num=4
print(str1+str(num)+str2)
string="hello"
print(string+"concatenate me")
letters="wubba"
print(letters*2)

#string functions and methods
algorithm="Neural Networks"
print(algorithm)
print(len(algorithm))
print(algorithm.lower())
print(algorithm.upper())
# count()
print(algorithm.count('Networks'))
print(algorithm.count('eu'))
print(algorithm.count(' '))
print(algorithm.count('Neurla'))
# find()
print(algorithm.find('r'))
print(algorithm.find('Neural'))
print(algorithm.find('box'))
# replace()
print(algorithm.replace(' ','-'))
print(algorithm.replace('N','L'))

#printing strings differently
first_name="rahul"
last_name="modi"
full_name=f'left plus right makes {last_name} {first_name}'
print(full_name)
print(first_name+" "+last_name)
first_name="vikash"
middle_name=' '
last_name="srivastava"
print(f'I am none other than {first_name}{middle_name}{last_name}.I am a data scientist')

#check if string has particular word or character
my_string="Albert Einstien"
found="thomson" in my_string
print(found)
found="alberta" in my_string
print(found)
