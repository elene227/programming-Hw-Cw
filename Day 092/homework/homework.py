# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სია. sorted() ფუნქციის საშუალებით დაალაგეთ ეს სია ისე, რომ პირველ რიგში იყოს ის სტრინგი სადაც ყველაზე ცოტა ასო 'a' იქნება. 
def count(s):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    return count

def final(star):
    return sorted(star, key=count)

sta = ["hallo", 'aaaaaagahaa', 'ahhahhahahahahah', 'hehehehaHA']
print(final(sta))