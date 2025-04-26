def needd(need):

    for i in range(1, need):
        if need / i == float(i):
            return True
        else:
            return False
need = int(input("give a num: "))
   
print(needd(need))

