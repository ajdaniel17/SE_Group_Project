import re
# referenced from:
# https://softhints.com/regex-phone-number-find-validation-python/
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/


# email format (name)@(something).(something)
def emailCheck(input_email):
    format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(format, input_email):
        #print(str(input_email) + " is a valid email")
        return True
    else:
        #print(str(input_email) + " is NOT a valid email")
        return False
 
# credit card format 16 digits or (4 digits) - (4 digits) - (4 digits) - (4 digits)
def creditCardCheck(input_card):
    format = r'^[0-9]{16}|[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    if re.match(format, input_card):
        #print(str(input_card) + " is a valid credit card number")
        return True
    else:
        #print(str(input_card) + " is NOT a valid credit card number")
        return False

# phone number format (numbers) OR +1(numbers) OR (numbers) numbers numbers
def phoneNumberCheck(input_phone):
    format = r'[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    if re.match(format, input_phone):
        #print(str(input_phone) + " is a valid number")
        return True
    else:
        #print(str(input_phone) + " is NOT a valid number")
        return False
