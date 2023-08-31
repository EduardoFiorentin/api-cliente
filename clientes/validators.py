import re
from validate_docbr import CPF

def cpf_valido(cpf): 
    '''verifica se cpf é válido'''
    # cpf = CPF()
    # print(CPF.validate(cpf))
    return len(cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    # modelo: xx 9xxxx-xxxx
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    
    return re.findall(modelo, celular)
