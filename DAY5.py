my_list=[15,25,47,95,65,12]
print('My list:\n',my_list)
my_list.insert(3,'new item= 55')
print('New item inserted:\n',my_list)
del my_list[3]
print('New item removed:\n',my_list)
lar=max(my_list)
print('Largest integer of list =',lar)
sma=min(my_list)
print('Smallest interger of list = ',sma)

my_tuple=(1,2,3,4,5)
print('\n\nMy tuple :\n',my_tuple)
new_tuple=tuple(reversed(my_tuple))
print('Reversed tuple:\n',new_tuple)

my_list=list(new_tuple)
print('\n\nMy new list:\n',my_list)
