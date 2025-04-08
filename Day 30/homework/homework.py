names = ["გიორგი", "ნინო", "თამარ", "ალექსანდრე", "ირაკლი", "მარიამი", "ლუკა", "ანასტასია", "ზურაბი", "დავით"]
filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)
