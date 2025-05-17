# list.remove("rame")
#
#   
#
#
#display: flex;
# // // // //
# 
# 
#
## 2 4 luwi
# შექმენი ფუნქცია რომელიც გამოითვლის სიაში მყოფ ლუწი რიცხვების რაოდენობას და კენტი რიცხვების ჯამს
def caunt(x):
    luwi = 0
    kenti = 0
    for i in x:
        if i % 2 == 0:
            luwi += 1
        elif i % 2 == 1:
            kenti += i
    return (luwi, kenti)


x = [23,4566,78433,4,55,3,3,34,34,3,2]
print(caunt(x))