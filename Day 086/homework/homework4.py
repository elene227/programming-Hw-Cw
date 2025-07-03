# 5)შექმენი ფუნქცია რომელიც პარამეტრად მიიღებს ორ ცვლადს და ეს ცვლადები მნიშვნელობად მიიღებენ რიცხვებით სავსე სიებს,შენი დავალება იქნება რომ პირველი სიიდან ამოიღო ლუწი რიცხვები ხოლო მეორე სიიდან ამოიღო კენტი რიცხვები,შემდეგ გააერთიანე ეს რიცხვები ერთმანეთში და ამ გაერთიანებული სიიდან გამოიტანე ყოველ კენტ იდექსზე მდგომი რიცხვების ჯამი
def  prerea(first, second):

    evens = []
    for num in first:
        if num % 2 == 0:
            evens.append(num)

    odds = []
    for num in second:
        if num % 2 == 1:
            odds.append(num)
    
    combine = evens + odds

    suem = 0
    for i in range(len(combine)):
        if i % 2 == 1:
            suem += combine[i]
    return suem

first = [234,5,56,678,56,6,34,6]
second = [23,6,7,89,2,579,6,89]

print(prerea(first, second))
    
    


    