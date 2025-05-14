# 3) შექმენით ფუქცია რომელსაც გადაეცემა სია. sorted() ფუნქციის საშუალებით დაალაგეთ ეს სია ისე, რომ ჯერ იყოს ისეთი სტრინგი სადაც ყველაზე მეტი ხმოვანი იქნება. 
def func(h):
    vowels = "aeiouAEIOU"
    count = 0
    for i in h:
        if i in vowels:
            count += 1
    return count

def ss(s):
    return sorted(s, key=func, reverse=True)

sq = ["jwhshadsia", "saaadaijfiajf", "ajsfjaidja"]
print(ss(sq))

