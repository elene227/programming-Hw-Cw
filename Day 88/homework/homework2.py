# 3) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს და გაიგებთ ამ რიცხვიდან თუ ამოდის ფესვი. თუ ფესვი ზუსტად ამოდის მაშინ True დააბრუნოს, სხვა შემთხევაში False
def needd(need):

    for i in range(1, need): 
        if need / i == float(i):
            return True
        else:
            return False
        
need = int(input("give a num: "))
   
print(needd(need))

