# 3)შექმენით ფუნქცია,პარამეტრად გადაეცით ცვლადი,რომელიც მიიღებს მნიშვნელობად სტრინგს --> "ale4qs6and3re'' , შენი დავალებაა ამ სტრინგიდან ამოშალო ყველა რიცცხვი და დააბრუნო ეს სტრინგი რიცხვების გარეშე
def parag(vale):
    res = ""
    for i in vale:
        if not('0'<= i <= '6'):
            res += i
    return res
    
print(parag("ale4qs6and3re"))