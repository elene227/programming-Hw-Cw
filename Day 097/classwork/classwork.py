def validate_number(st):    
    if st == "":
        return 'In with a chance'
        st = st.replace("-"," ")
    elif st[0:2] != "07" or len(st) != 11:
        return 'Plenty more fish in the sea' 
    elif st[0:3] == "+44":
        return 'Plenty more fish in the sea'
    
    
    
    
    # would u like fancy cuppa mate??????
    # B'OA 'O WoAh 

    