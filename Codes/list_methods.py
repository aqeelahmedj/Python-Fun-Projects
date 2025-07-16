'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''


listA=['alice', 'bunty', 'apple', 'banana', 'organe', 'cherry', 'watermelon', 'strawberyy', 'alice', 'bunty']
print(listA)


i=0

while i<len(listA):
    print(listA[i])
    i = i+1


print("----:using For Loooop:----")

for x in range(len(listA)):
    print(listA[x])

print(":----------Using Listing Comprehension-------:")

[print(x) for x in listA]



new_list = []

for i in listA:
    if "a" in i:
        new_list.append(i)

print(new_list)


new_list = [i for i in listA if "a" in i]