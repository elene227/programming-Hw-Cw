def validate_number(st):    
    st = st.replace("-","")
    
    if st[0:2] == "07" and len(st) == 11:
        return "In with a chance"
    elif st[0:3] == "+44" and len(st) == 13:
        return "In with a chance"
    else:
        return "Plenty more fish in the sea"
        
    
        
        
      