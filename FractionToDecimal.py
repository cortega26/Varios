def fractionToDecimal(numerator,denominator):
    result=""
    result+=str(numerator//denominator)
    result+="."
    quotient_num = []
    while numerator:
        remainder = numerator % denominator
        if remainder == 0:
            for i in quotient_num:
                result += str(i[-1])
            break
        numerator = remainder*10
        quotient = numerator // denominator
        if [numerator, quotient] not in quotient_num:
            quotient_num.append([numerator, quotient])
        elif [numerator, quotient] in quotient_num:
            index = quotient_num.index([numerator, quotient])
            for i in quotient_num[:index]:
                result += str(i[-1])
            result += "("
            for i in quotient_num[index:]:
                result += str(i[-1])
            result += ")"
            break
    if result[-1:]==".":
        result=result[:-1]
    return result

print(fractionToDecimal(1881,139))
