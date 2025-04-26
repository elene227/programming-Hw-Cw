# 2) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს. და ეს რიცხვი გაყავით ამ რიცხვის ციფრთა ჯამზე. (დავუშვათ შემოიტანა მომხმარებელმა 150. ანუ 150 უნდა გაყოს 6-ზე, რადგან 1+5+0 = 6)
def users():
    num = input("enter numberr: ")
    sum = 0
       # str helps us get to all elements in number (:
    if str(num)[0] != "-":
        for i in str(num):
            sum += int(i)
    else:
        for i in str(num)[1::]:
            sum += int(i)
    return(int(num) / sum)
    

print(users())
