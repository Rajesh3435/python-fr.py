negatives=positives=zeros=0
print("enter -1 to exit....")
while(1):
    num=int(input("enter any number : "))
    if(num==-1):
        break
if(num==0):
    zeroes=zeroes+1
elif(num>0):
    positives=positives+1
else:
            negatives=negatives+1
print("count of positive numbers entered :",positives)
print("count of negatives numbers entered :",negatives)
print("count of zeros entered :",zeroes)