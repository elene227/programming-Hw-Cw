# 6) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია. ეს სია უნდა დაალაგოთ ისე რომ ჯერ იყოს ისეთი სტრინგი რომელიც იწყება 'g'-ზე.
def func(string):
    sr = ""
    #for i in string:
    if string[0] == "g":
        sr += string
    return(sr)

def final(f):
    return sorted(f, key=func, reverse=True)
sq = ['fafafafafaa', 'ana', 'gart',  "randomestnamggeyouwillsee", "halllo", 'gal']

print(final(sq))
