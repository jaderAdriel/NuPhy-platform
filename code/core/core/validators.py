from django.core.exceptions import ValidationError

def validate_cpf (cpf):

    def getDigit(cpf) :
        sum = 0

        for i, number in enumerate( range( len(cpf) + 1, 1, -1 ) ): 
            sum += int(cpf[i]) * number

        res = sum % 11
        digit = 0

        if res > 1:
            digit = 11 - res

        return cpf + str(digit) 


    special_character = ['-','.']
    formated = ''

    for digit in cpf:
        if not digit in special_character:
            formated += digit

    if not str(formated).isnumeric() or len(str(formated)) > 11:
        raise ValidationError("Wrong format")
    
    for index, digit in enumerate(formated):
            if (digit in special_character) and (index not in [3,7,9]) or \
                (digit == '-' and index != 11) :
                raise ValidationError("Wrong format")
    
    cpf_with_first_digit = getDigit(formated[:-2])
    valid_cpf = getDigit(cpf_with_first_digit)

    if valid_cpf != formated or int(valid_cpf) < 1:
        raise ValidationError("Invalid CPF")
    else: 
        return valid_cpf