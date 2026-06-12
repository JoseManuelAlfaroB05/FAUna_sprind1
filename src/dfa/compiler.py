"""
Módulo para compilar un DFA extendido a un DFA estándar.
Implementa parse_sre para expandir expresiones regulares simples.

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""

import string
from model import DFA

# Vocabulario V
VOCAB = (
    list(string.ascii_letters) +   # 52 letras
    list(string.digits) +          # 10 dígitos
    [' ', '\t', '\n', '.', ',', '\\', '[', ']', '-', '^']
)


def parse_sre(pV: list, pInput: str) -> list:
    """
    Parsea una expresión regular simple (SRE) y retorna
    la lista de caracteres que denota.

    :param pV: Vocabulario de caracteres válidos
    :type pV: list[str]
    :param pInput: Expresión regular a parsear
    :type pInput: str
    :return: Lista de caracteres que la SRE denota
    :rtype: list[str]
    """
    # Operador OR: dividir por '|' y unir resultados
    if '|' in pInput:
        varResult = []
        for varPart in pInput.split('|'):
            for varChar in parse_sre(pV, varPart):
                if varChar not in varResult:
                    varResult.append(varChar)
        return varResult

    # Punto: todo el vocabulario
    if pInput == '.':
        return list(pV)

    # Clases escapadas
    if pInput == '\\d':
        return list(string.digits)
    if pInput == '\\s':
        return ['\n', '\t']
    if pInput == '\\w':
        return list(string.ascii_letters + string.digits + '_')
    if pInput == '\\n':
        return ['\n']
    if pInput == '\\t':
        return ['\t']

    # Rango negado: [^a-z]
    if pInput.startswith('[^') and pInput.endswith(']'):
        varInner = pInput[2:-1]
        varDash = varInner.index('-')
        varStart = varInner[:varDash]
        varEnd = varInner[varDash+1:]
        varRange = [chr(c) for c in range(ord(varStart), ord(varEnd)+1)]
        return [c for c in pV if c not in varRange]

    # Rango: [a-z]
    if pInput.startswith('[') and pInput.endswith(']'):
        varInner = pInput[1:-1]
        varDash = varInner.index('-')
        varStart = varInner[:varDash]
        varEnd = varInner[varDash+1:]
        return [chr(c) for c in range(ord(varStart), ord(varEnd)+1)]

    # Caracter simple escapado: \x
    if pInput.startswith('\\') and len(pInput) == 2:
        return [pInput[1]]

    # Caracter simple
    if len(pInput) == 1:
        return [pInput]

    return []


def compile_dfa(pDfa: DFA) -> DFA:
    """
    Convierte un DFA extendido a un DFA estándar
    expandiendo las expresiones regulares en las transiciones.

    :param pDfa: DFA extendido a compilar
    :type pDfa: DFA
    :return: DFA estándar equivalente
    :rtype: DFA
    """
    varNewTransitions = {}

    for varState, varTrans in pDfa.varTransitions.items():
        varNewTransitions[varState] = {}
        for varSre, varDest in varTrans.items():
            varChars = parse_sre(VOCAB, varSre)
            for varChar in varChars:
                varNewTransitions[varState][varChar] = varDest

    varNewAlphabet = set()
    for varTrans in varNewTransitions.values():
        varNewAlphabet.update(varTrans.keys())

    return DFA(
        pStates=pDfa.varStates,
        pAlphabet=varNewAlphabet,
        pTransitions=varNewTransitions,
        pInitialState=pDfa.varInitialState,
        pFinalStates=pDfa.varFinalStates
    )