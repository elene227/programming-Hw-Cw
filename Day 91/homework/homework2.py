# 5) ახსენით sorted() რას აკეთებს და ყველაფერი რაც იცით.

# sorted - ალაგებს ელემენტებს სიას იტერაციას ისე როგორც ჩვენ ვეტყვით მოყვება reverse თუ რევერს გაუწერთ True მაშინ ელემენტები პირიქით დადგებიან კლებადობით, Key ს გადავცემთ რის მიხედვით დალაგდეს ელემენტები სიგრძის მაგ key=len
# examples:


# 1
strings = ["name", "hello", "hai", "hi"]

so = sorted(strings, key=len, reverse=True)

print(so)



# 2

integers = [1,2,3,4,5,6,7,8,9,10]

sa = sorted(integers, reverse=True)
 #key=lenს ვერ გაუწერთ ინტეჯერებს ანუ რიცხვებს 

print(sa)