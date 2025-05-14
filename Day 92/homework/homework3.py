# 5) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია. sorted() ფუნქციის გამოყენებით დაალაგეთ ეს სია ისე რომ ჯერ იყოს რიცხვები სადაც ყველაზე მეტჯერ მეორდება რიცხვი 3. 
def numbers(n):
    count = 0
    for i in str(n):
        if i == 3:  
            count += 1
    return (count)
def final(func):
    return sorted(func, key=numbers, reverse=True)


func = [4,45,6,33,333333,33,34,523,333113313131333333333333,11019199101]
print(final(func))