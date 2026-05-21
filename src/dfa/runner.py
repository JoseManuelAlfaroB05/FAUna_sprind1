"""
Módulo para ejecutar un DFA contra una cadena de entrada.
Incluye tracing del proceso de ejecución.

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""

from model import DFA


class Runner:
    """
    Ejecuta un DFA contra una cadena de entrada.

    :param pDfa: Autómata a ejecutar
    :type pDfa: DFA
    """

    def __init__(self, pDfa):
        self.varDfa = pDfa

    def run(self, pInput, pTrace=False):
        """
        Ejecuta el DFA contra una cadena de entrada.

        :param pInput: Cadena de entrada
        :type pInput: str
        :param pTrace: Si True, muestra el tracing paso a paso
        :type pTrace: bool
        :return: True si la cadena es aceptada, False si no
        :rtype: bool
        """
        varCurrentState = self.varDfa.varInitialState

        if pTrace:
            print(f"Estado inicial: {varCurrentState}")

        for varSymbol in pInput:
            if varSymbol not in self.varDfa.varAlphabet:
                print(f"Error: símbolo '{varSymbol}' no está en el alfabeto")
                return False

            varNextState = self.varDfa.varTransitions[varCurrentState][varSymbol]

            if pTrace:
                print(f"{varCurrentState} --{varSymbol}--> {varNextState}")

            varCurrentState = varNextState

        varAccepted = varCurrentState in self.varDfa.varFinalStates

        if pTrace:
            if varAccepted:
                print(f"Estado final: {varCurrentState} ACEPTADA")
            else:
                print(f"Estado final: {varCurrentState} RECHAZADA")

        return varAccepted