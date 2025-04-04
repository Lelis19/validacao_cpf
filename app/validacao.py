import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um cpf brasileiro.

    :param cpf: CPF como string (somente números ou no formato xxx.xxx.xxx-xx)
    :return: True se for válido, false caso contrário
    """
     
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
