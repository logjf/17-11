#for จะเป็น definite loop หรือ loopที่มีการทำงานที่ชัดเจน
#forกับ
for i in range(1,11,1):
    print(i)
print('finish')
#for กับ list
list1 = ["apple","blueberry","kiwi","papaya"]
for element in list1:
    print(element)
#for กับ dic
dic1 = {'name':'soranum','age':30,'hobbies':'football'}
for key,value in dic1.item():
    print(key,value)
#while indefinite loop หรือ loopที่ทำงานไม่ชัดเจน
i =1
while i<10:
    print(i)
    i +=1
    #นายปิยวัฒน์ กำประโคน เลขที่17 ม.6/11