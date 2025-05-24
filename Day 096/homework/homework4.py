def most_frequent_item_count(collection):
    
    Count = 0
    
    for num in collection:
        if collection.count(num) > Count:
            Count = collection.count(num)
    return Count
def most_frequent_item_count(collection):
    Count = 0
    
    for num in collection:
        if collection.count(num) > Count:
            Count = collection.count(num)
    return Count