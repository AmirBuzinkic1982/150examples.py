from array import*


simple_array=[[2,5,8],[3,7,4],[1,6,9]]
simple_array[1].append(3)
print(simple_array)

data_set={"A":{"x":54,"y":82,"z":91},"B":{"x":55,"y":33,"z":25}}

print(data_set["B"]["y"])

for i in data_set:
    print(data_set[i]["y"])

data_set ["B"]["y"]=53
print(data_set)


grades=[[33,44,55],[22,21,11],[44,55,66],[77,88,99]]
name=["Susan","Peter","Mat"]
#grades[name]={"Maths":mscore,"English":escore}