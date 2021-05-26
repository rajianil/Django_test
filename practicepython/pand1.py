import pandas as pd
import numpy as np
from functools import reduce
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
print(ds.tolist())
ds1 = pd.Series([2, 3, 5, 7, 9])
print(ds1)
print(ds1+ds)
print(ds==ds1)
print(ds.equals(ds1))
dicti={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(pd.Series(dicti))
nddata=np.array([1,2,3])
print(pd.Series(nddata))
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
dset=pd.DataFrame(d)
print(dset['col1'])
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)
print(ds.idxmax(),ds.idxmin())
print(pd.concat([ds,ds1]))
print(ds.append(ds1))
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x:x[0])
print(subject_marks)
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['make'])
print("\nSorting the List of dictionaries :")
print(sorted_models)
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even= filter(lambda x: x%2==0,num)
print(list(even))

startwith = lambda x : True if x.startswith('A') else False
print(startwith('RAnil'))
num=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
cnt=dict(map(lambda x: (x , num.count(x)),num)  )
print((cnt))

d={}
for i in num:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

dict(map(lambda x: (x,num.count(x)),num))
nums_str = ['4','12','45','7','0','100','200','-12','-500']

print(sorted(nums_str, key=lambda x:int(x),reverse=True))
print(sorted(nums_str, key=lambda x:int(x)))
nums=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print(sorted(nums,key=lambda x:str(x),reverse=True))
lidata=[10, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
print(max(enumerate(lidata),key=lambda x:x[0]))
print(min(enumerate(lidata),key=lambda x:x[1]))
nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print(tuple(map(lambda x: sum(x) / float(len(x)), nums)))
print(tuple(map(lambda x: sum(x) / float(len(x)), nums)))
nums1 = [4, 3, 2, 2, -1, 18]
print(reduce(lambda x,y: x*y,nums1,1))
colors_list = ["Red", "Green", "Blue", "White", "Black"]
print(list(map(lambda x: "".join(reversed(x)), colors_list)))
nums1 = [2,1,4,6,8,10,12,14,16,17]
def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[0:]):
        print(i,e,key(e))
        if key(e) < key(nums[i]):
            return False
    return True
print(is_sort_list(nums1))