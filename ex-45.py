import re

def is_valid_postcode(postcode):
    pattern = r'^[A-Z]{2}\d{1,2}\s\d{1}[A-Z]{2}$'
    if re.match(pattern, postcode):
        return True
    else:
        return False

n=input()
print(is_valid_postcode(n))