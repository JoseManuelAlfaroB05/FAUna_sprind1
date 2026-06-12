"""
Módulo de pruebas para el runner de DFAs.

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'dfa'))

import pytest
from model import DFA
from runner import Runner


@pytest.fixture
def dfa_simple():
    return DFA(
        pStates={'q0', 'q1'},
        pAlphabet={'a', 'b'},
        pTransitions={
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q0'}
        },
        pInitialState='q0',
        pFinalStates={'q1'}
    )


def test_cadena_aceptada(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('a') == True


def test_cadena_rechazada(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('b') == False


def test_cadena_vacia(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('') == False


def test_cadena_larga_aceptada(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('bba') == True


def test_cadena_larga_rechazada(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('bab') == False


def test_simbolo_invalido(dfa_simple):
    r = Runner(dfa_simple)
    assert r.run('abc') == False