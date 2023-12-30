def val(state_code):
    dict1={'RI': 'Rhode Island', 'CT': 'Connecticut', 'MA': 'Massachusetts', 'ME': 'Maine', 'VT': 'Vermont', 'NH': 'New Hampshire'}
    if state_code in dict1:
        return dict1[state_code]
    else:
        return None
    
n=input()
print(val(n))