fruits = ["apple", "banana", "cherry"]
print(fruits[2])
#เปลี่ยนค่าในlist
fruits[1]="blackcurrant"
print(fruits)
fruits[1:3]=["banana", "kiwi", "melon"] 
print(fruits)
fruits[1:3]=["blackcurrant"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปลlistทิ้งไปจากระบบ
#เรียงค่าในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมlist
vege=["carrot", "potato", "cucamber"]
all = fruits+vege
print(all)
#นายปิยวัฒน์ กำประโคน ม.6/11 เลขที่17