#These are called collection classes in python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);

#list and python is used when we want to store data in sequence

#Ascending
list=[45,67,11,9,8,2]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)

#Descending
list=[87,62,45,18,8,2]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)