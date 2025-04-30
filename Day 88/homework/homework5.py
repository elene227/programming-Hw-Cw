# 6) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ სიტყვას და შეამოწმებთ არის თუ არა ეს სიტყვა პალინდრომე, ოღონდ სიტყვა შეაბრუნეთ for loop-ით. 
def palind(reverse):
    iss = ""

    for i in reverse:
        iss = i + iss 


    return iss == reverse

# 







reverse = input("enter: ")

print(palind(reverse))