import json
import operator
import itertools
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
jsobj=json.loads(python_obj)
print(jsobj)
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(dict(sorted(d.items(),key=operator.itemgetter(1))))
d.update({5:5})
print(d)
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict, key=(lambda k: my_dict[k]))
key_min = min(my_dict, key=(lambda k: my_dict[k]))
print(key_max)
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'


test = dictObj()
print(test.__dict__)
d={1:1}
print(bool(d))
lid=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(set(j for i in lid for j in i.values()))
li=[]
dict1={'1':['a','b'], '2':['c','d']}
for i in dict1.values():
    print(itertools.product(i))
print(li)
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
print(dict(zip(class_list,id_list)))

marks={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(marks.keys())
for k in marks.keys():
    print(k)
    print(marks[k])
    val=zip(marks[k])
    result = [dict(zip(k, v)) for v in val]
    print(result)
def generatormeth(x):
    for i in range(x):
        yield(i)


gen=(generatormeth(5))
for i in gen:
    print(i)
d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}

#for k,v in d2.items():
#    d1[k]=v

#print(d1)
#d1.update(d2)
#print({**d1,**d2})
print({**d1})