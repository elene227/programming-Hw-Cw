# ) შექმენით ფუნქცია სადაც მომხმარებელს შემოტანილ რიცხვს გადაიყვანთ ორობით სისტემაში.
def ret(turn):
    binary = ""

    while turn > 0:
         f = turn % 2
         binary = str(f) + binary 

         turn = turn // 2
    return binary







turn = int(input("Enter: "))
print(ret(turn))