def descending_order(num):
    str_nums = str(num)
    new_list = []
    res = ""
    
    for i in str_nums:
        new_list.append(i)
        sort = sorted(new_list, reverse =True)
        
    for x in sort:
        res += x
    return int(res)