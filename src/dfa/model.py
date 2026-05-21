"""
Modelo propio de un Autómata Finito Determinista (DFA).
No depende de ninguna librería externa.

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""

import json

class DFA:

    """
    Representa un Autómata Finito Determinista (DFA).

    :param states: Conjunto de estados
    :param alphabet: Conjunto de símbolos del alfabeto
    :param transitions: Diccionario de transiciones {estado: {simbolo: estado}}
    :param initial_state: Estado inicial
    :param final_states: Conjunto de estados de aceptación
    """

    def __init__(self, pStates, pAlphabet, pTransitions, pInitialState, pFinalStates):
        self.varStates = set(pStates)
        self.varAlphabet = set(pAlphabet)
        self.varTransitions = pTransitions
        self.varInitialState = pInitialState
        self.varFinalStates = set(pFinalStates)
    
    
    @classmethod
    def from_json(cls, pPath):
        with open(pPath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(
            pStates=data["states"], 
            pAlphabet=data["alphabet"],
            pTransitions=data["transitions"],
            pInitialState=data["initial_state"],
            pFinalStates=data["final_states"]
        )

    def __repr__(self):
        return (
            f"DFA(\n"
            f"  states={self.varStates},\n"
            f"  alphabet={self.varAlphabet},\n"
            f"  initial_state={self.varInitialState},\n"
            f"  final_states={self.varFinalStates}\n"
            f")"
        )