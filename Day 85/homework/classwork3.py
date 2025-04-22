# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის ჩათვლით შეკრიბავთ ყველა მარტივ რიცხვს
def prime():
    my = []
    for number in [3, 345, 34, 2]:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            my.append(number)
    return my

print(prime())
