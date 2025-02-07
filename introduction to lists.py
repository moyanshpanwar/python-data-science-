#assign list to a variable
my_list=[1,2,3,4]
print(my_list)
my_list=['a string',23,100.232,'o',True]
print(my_list)
print(len(my_list))

#list indexing
loss_function=['mean absolute error','mean squared error','huber loss','log loss','hinge loss']
print(loss_function[0])
print(len(loss_function))
print(loss_function[3])
print(loss_function[-1])
print(loss_function[-3])

#list slicing
print(loss_function)
print(loss_function[1:4])
print(loss_function[2:])
print(loss_function[:4])
print(loss_function[:])
print(loss_function[-4:])
print(len(loss_function))

#list operations
print(loss_function)
print(loss_function+['kullback-leibler'])
#make list double
print(len(loss_function*5))
# len()
print(len(loss_function))
# min()
new_list=[6,9,1,3,5.5]
print(min(new_list))
my_new_list=['c','b','z','y','m']
print(min(my_new_list))
#max()
new_list=['argue','burglar','parent','linear','shape']
print(max(new_list))
#sum()
new_list=[6,9,1,3,5.5]
print(sum(new_list))
#sorted()
new_list=[6,9,1,3,5.5]
print(sorted(new_list))
new_list=['argue','burglar','parent','linear','shape']
print(sorted(new_list))

#list methods
my_list=[1,2,3,1,1,1,3,10,5,8]
print(my_list)
#append()
my_list=['a string',23,100.232,'o',True]
print(len(my_list))
my_list.append('append me!')
print(my_list)
print(len(my_list))
my_list.append(2.73)
print(my_list)
print(len(my_list))
my_list.append([1,2,3])
print(my_list)
print(len(my_list))
my_list.append([10,[19,20],30])
print(my_list)
print(len(my_list))
#extend()
print(my_list)
my_list.extend(['wubba','lubba','dub dub'])
print(my_list)
print(len(my_list))
#pop()
print(my_list)
print(my_list.pop())
print(my_list.pop(1))
#remove()
print(my_list)
print(my_list.remove([10,[19,20],30]))
print(my_list)
print(my_list.remove([1,2,3]))
print(len(my_list))
print(my_list.remove(1))
print(len(my_list))
#count()
print(my_list)
print(my_list.count('append me!'))
print(my_list.count(1))
#index()
print(my_list)
print(my_list.index('wubba'))
#sort()
new_list=[6,9,1,3,5.5]
new_list.sort()
print(new_list)
new_list.sort(reverse=True)     #decending order
print(new_list)
boolean_list=[True,False]
boolean_list.sort(reverse=True) #decending order
print(boolean_list)
#reverse()
my_list=[1,1,1,1,1.43,2,3,3,5,8,10,'lubba','dub dub']
my_list.reverse()
print(my_list)
#nested list
list_1=[1,2,3]
list_2=['b','a','d']
list_3=[7,8,9]
list_of_lists=[list_1,list_2,list_3]
print(list_of_lists)
print(type(list_of_lists))
print(list_of_lists[1])

