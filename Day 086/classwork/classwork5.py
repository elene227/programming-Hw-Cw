# 2)შექმენით ფუნქცია,პარამეტრად გაეაეცით name ცვლადი რომელშიც შენაახული  იქნება სტრინგი,შენი დავალებაა დააურბონო ეს სტრინგი შემოტრიალებული
def part(name):
    reverse = ""
    for i in name:
        reverse = i + reverse
    return reverse
print(part("Lamar"))
