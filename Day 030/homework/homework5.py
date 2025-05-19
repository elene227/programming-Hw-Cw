fruits = ["ვაშლი", "ფორთოხალი", "გარგარი", "ხიზილალა", "კარტოფილი", "ვაშლი", "მარწყვი"]
non_fruits = ["კარტოფილი", "კომბოსტო", "სოკო", "მაროჟნი"]

for non_fruit in non_fruits:
    if non_fruit in fruits:
        fruits.remove(non_fruit)

print(fruits)
