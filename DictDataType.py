my_dict1={'name':'jaga','age':30,'status':'pass'};
my_dict2={'name':'raja','age':35,'status':'pass'};
my_dict1.update(my_dict2)
my_dict1.pop()#pop expected atleast 1 argument,got 0
my_dict1.pop('age')
my_dict1.popitem()#always delete last key:value pair
del my_dict1
#del my_dict1['age']  #del my_dict
my_dict1.clear()#{}
#key:value pair-duplicates not allowed
#duplicate key not allowed
#duplicate values are allowed for different keys
