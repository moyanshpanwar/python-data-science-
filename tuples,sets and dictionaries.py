#creating a tuple
my_tuple=(1,'a',3)
print(my_tuple)
my_list=[1]
print(type(my_list))
my_tuple=(1,)
print(type(my_tuple))
my_tuple=(1,2,3,4)
print(len(my_tuple))

#tuple indexing
another_tuple=('one',2,4.53,'asbc')
print(another_tuple)
print(another_tuple[0])
print(another_tuple[3])
print(another_tuple[-1])
print(another_tuple[-3])

#tuple slicing
print(another_tuple)
print(another_tuple[1:3])
print(another_tuple[2:])
print(another_tuple[:6])
print(another_tuple[-4:])
random_tuple=(1,5,6,2)
print(sorted(random_tuple))

#tuple methods
# index()
my_tuple=(1,2,3,4,5,6,1,1,2)
print(my_tuple.index(2)) 
print(my_tuple.count(1)) 
#tuple is immutable
my_tuple=(1,2,3,4,5,6,1,1,2)
print(my_tuple)
print(my_tuple[0])

#sets
empty_set=set()
print(type(empty_set))
non_empty_set={1,6,4,'abc'}
print(type(non_empty_set))
my_object={}
print(type(my_object))
empty_set=set()
print(type(empty_set))
my_list=[1,1,2,2,3,4,5,6,1,1]
my_set=set(my_list)
print(my_set)
my_set={1,2,(2,3)}
print(my_set)
#add()
my_set=set()
my_set.add('a')
print(my_set)
my_set.add(2)
print(my_set)
#update()
my_set={5,3,7,9}
my_set.update([2,3,4])
print(my_set)
#remove()
non_empty_set={1,5,6,73,2}
non_empty_set.remove(5)
print(non_empty_set)
#union()/|
A={1,2,3,4,5}
B={4,5,6,7,8}
A.union(B)
print(A)
A|B
print(A)
#intersection()
A={1,2,3,4,5}
B={4,5,6,7,8}
A.intersection(B)
A&B
#difference()
A={1,2,3,4,5}
B={4,5,6,7,8}
A.difference(B)
B-A
#symmetric_difference()
A={1,2,3,4,5}
B={4,5,6,7,8}
A.symmetric_difference(B)
A^B

#dictionaries
#creating a dictionary
marvel_dict={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['iron man','captain america'],'abc':{1,2}}
print(marvel_dict)
print(marvel_dict['place'])
print(type(marvel_dict))
print(marvel_dict['name'])
print(marvel_dict['weapon'])
print(marvel_dict['alibies'])
print(type(['abc']))

#dictionary methods
#keys()
print(marvel_dict.keys())
print(list(marvel_dict.keys()))
#values()
print(marvel_dict.values())
print(list(marvel_dict.values()))
#items()
print(marvel_dict.items())
#get()
print(marvel_dict.get('place'))
print(marvel_dict.get('random'))

employee_dict={'name':'saket','skills':['python','machine learning','deep learning'],'band':6.0,'promotion year':[2016,2018,2020]}
print(len(employee_dict))
print(employee_dict.keys())
print(employee_dict['skills'])
print(employee_dict['skills'][0])
print(employee_dict['skills'][0].upper())
employee_dict['designation']='senior data scientist'
#update()
employee_dict.update({'salary':200000})
print(employee_dict)
employee_dict.update({'name':'varun saini'})
print(employee_dict)
#subtract 123 from value
employee_dict['name']=employee_dict['name']+' '+'raj'
print(employee_dict)
#dict()
country_list=['india','australia','united states','england']
city_list=['new delhi','canberra','washington DC','london']
country_city_list=list(zip(country_list,city_list))
print(country_city_list)
print(dict(country_city_list))
#pop()
country_list=['india','australia','united states','england']
city_list=['new delhi','canberra','washington DC','london']
country_city_list=dict(zip(country_list,city_list))
print(country_city_list)
country_city_list.pop('england')
print(country_city_list)
#zip() and dict()
name=['manjeet','nikhil','sambhavi']
marks=[40,70,90]
mapped=zip(name,marks)
print(mapped)
print(dict(mapped))