# 2) შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ რამე სიტყვას მანამ სანამ არ შემოიტანს 'საკმარისია'. ყველა შემოტანილი სიტყვა სიაში დაამატეთ. შემდეგ ეს სია გასორტეთ ისე რომ ყველაზე ცოტა სიმბოლო სადაც იქნება ჯერ ეგ რომ იყოს და შემდეგ გაიზარდოს.
user = input("enter: ")
words = []

while user != "enough":
    words.append(user)
    user = input("enter: ")

worss= sorted(words, key=len, reverse=True)

for i in worss:
    print(i)


