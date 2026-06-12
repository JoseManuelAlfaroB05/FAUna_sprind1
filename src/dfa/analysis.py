"""
Módulo para analizar un Autómata Finito Determinista (DFA).
Verifica completitud, estados inalcanzables y estados inútiles.

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""

from model import DFA


class Analyser:
    """
    Analiza un DFA del modelo propio.

    :param pDfa: Autómata a analizar
    :type pDfa: DFA
    """

    def __init__(self, pDfa):
        self.varDfa = pDfa

    def is_complete(self):
        """
        Verifica si el DFA es completo.
        Un DFA es completo si todos los estados tienen
        transición para cada símbolo del alfabeto.

        :return: True si es completo, False si no
        :rtype: bool
        """
        for varState in self.varDfa.varStates:
            for varSymbol in self.varDfa.varAlphabet:
                if varState not in self.varDfa.varTransitions:
                    return False
                if varSymbol not in self.varDfa.varTransitions[varState]:
                    return False
        return True

    def unreachable_states(self):
        """
        Encuentra los estados inalcanzables desde el estado inicial.

        :return: Conjunto de estados inalcanzables
        :rtype: set
        """
        varVisited = set()
        varQueue = [self.varDfa.varInitialState]

        while varQueue:
            varCurrent = varQueue.pop(0)
            if varCurrent in varVisited:
                continue
            varVisited.add(varCurrent)
            if varCurrent in self.varDfa.varTransitions:
                for varSymbol, varNext in self.varDfa.varTransitions[varCurrent].items():
                    if varNext not in varVisited:
                        varQueue.append(varNext)

        return self.varDfa.varStates - varVisited

    def useless_states(self):
        """
        Encuentra los estados inútiles, es decir, desde los que
        nunca se puede llegar a un estado de aceptación.

        :return: Conjunto de estados inútiles
        :rtype: set
        """
        varUseful = set(self.varDfa.varFinalStates)
        varChanged = True

        while varChanged:
            varChanged = False
            for varState in self.varDfa.varStates:
                if varState in varUseful:
                    continue
                if varState in self.varDfa.varTransitions:
                    for varNext in self.varDfa.varTransitions[varState].values():
                        if varNext in varUseful:
                            varUseful.add(varState)
                            varChanged = True
                            break

        return self.varDfa.varStates - varUseful