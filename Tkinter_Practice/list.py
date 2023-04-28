f="area","op",64

print(f)
print(type(f))

d={'twisha':21 , 'rinku':21}
d.pop('twisha')
print(d)

data  = {'Name' : 'Danish Ali' , 'Age' : 17 }

remove_pop = data.pop('Age')

print('Remove Data Using Pop Function is {} '.format(remove_pop))
print(remove_pop)

tup=(1,2,[1,2,34],7)
tup[2].pop()
tup[2].append(45)
tup[2].remove(2)
print(tup)


set1={1,2,2,3,4,"rinku","rinku"}
set1.remove(3)
print(set1)