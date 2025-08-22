from unicodedata import digit


def plusOne(digits):

    carry = False

    for i in range(len(digits) - 1, -1, -1):
        if carry and i == 0:
            digits[i] += 1 
            if digits[i] > 9:
                digits[i] = 0
                digits.insert(0,1)
                carry = False 
                break
            else:
                carry = False
                break 
        elif carry:
            digits[i] = digits[i] + 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                carry = False 
                break
        else:
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                carry = True 
            else:
                break 
    if carry:
        digits.insert(0,1)
    return digits