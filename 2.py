x=[1,3,2,3,4,3]
x.remove(3)
print(x)
#Solution 1
#[1,2,3,4,3]
for i in x:
    if i==3:
        x.remove(3)
print(x)
#Solution 2
#[1,2,4]


