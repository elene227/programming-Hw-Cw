# 4) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგად გრძელი წინადადება. შემდეგ sorted() ფუნქციის გამოყენებით სტრინგი გახლიჩეთ და დაალაგეთ ისე რომ პირველ რიგში ის სტრინგი იყოს სადაც ყველაზე მეტი სიმბოლოების რაოდენობა იქნება.
def long(g):
    sp = g.split()


    words = sorted(sp, key=len, reverse=True)

    return ' '.join(words)
g ="heeleeoel skdad sdskad d gg  dda"
print(long(g))
