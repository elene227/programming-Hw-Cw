#18) მომხმარებელს შემოატანინე ასაკი, თუ ასაკი არის 18-ზე მეტი ან ტოლი, მაშინ დაპრინტეთ რომ არის სრულწლოვანი. თუ შემოიტანა 0-დან 18-მდე მაშინ დაპრინტოს, რომ არასრულწლოვანია. და სხვა შემთხვევაში დაპრინტოს რომ სისტემაში ხარვეზია

age = int(input('enter yo age: '))

if age >= 18:
    print('you are mature')
elif age < 18:
    print("you arent mature")
else:
    print("ERRRRORR")