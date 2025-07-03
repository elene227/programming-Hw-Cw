# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ სიტყვას და ამ სიტყვას დააბრუნებთ ისე რომ ხმოვნები იყოს დაფარული 
def vows(text):
    vowels = "aeiouAEIOU"
    hide = ""
 
    for i in text:
        if i in vowels:
            hide += "*"
        else: 
            hide += i
    return hide
text = input("type: ")


print(vows(text))


 
            
    
            
          
            



    




