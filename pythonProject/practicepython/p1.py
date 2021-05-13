Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
print(Dictionary1)
print(type(Dictionary1.keys()))
print(type(Dictionary1.values()))
print(type(Dictionary1.items()))
print(list(Dictionary1.keys()))
print((Dictionary1.values()))
print((Dictionary1.items()))
Dictionary1.update({'d':'go'})


print(Dictionary1.keys())
li1=[1,2,3,4]
li2=[4,5,6,7]
d=dict(zip(li1,li2))
print(d)