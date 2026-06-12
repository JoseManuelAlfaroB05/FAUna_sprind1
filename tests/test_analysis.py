"""
Módulo de pruebas para el análisis de DFAs.

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
from analysis import Analyser


@pytest.fixture
def dfa_completo():
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


@pytest.fixture
def dfa_incompleto():
    return DFA(
        pStates={'q0', 'q1'},
        pAlphabet={'a', 'b'},
        pTransitions={
            'q0': {'a': 'q1'},
            'q1': {'a': 'q1', 'b': 'q0'}
        },
        pInitialState='q0',
        pFinalStates={'q1'}
    )


@pytest.fixture
def dfa_con_inalcanzable():
    return DFA(
        pStates={'q0', 'q1', 'q2'},
        pAlphabet={'a', 'b'},
        pTransitions={
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q0'},
            'q2': {'a': 'q2', 'b': 'q2'}
        },
        pInitialState='q0',
        pFinalStates={'q1'}
    )


@pytest.fixture
def dfa_con_inutil():
    return DFA(
        pStates={'q0', 'q1', 'q2'},
        pAlphabet={'a', 'b'},
        pTransitions={
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'q1', 'b': 'q0'},
            'q2': {'a': 'q2', 'b': 'q2'}
        },
        pInitialState='q0',
        pFinalStates={'q1'}
    )


def test_dfa_completo(dfa_completo):
    a = Analyser(dfa_completo)
    assert a.is_complete() == True


def test_dfa_incompleto(dfa_incompleto):
    a = Analyser(dfa_incompleto)
    assert a.is_complete() == False


def test_estados_inalcanzables(dfa_con_inalcanzable):
    a = Analyser(dfa_con_inalcanzable)
    assert a.unreachable_states() == {'q2'}


def test_sin_estados_inalcanzables(dfa_completo):
    a = Analyser(dfa_completo)
    assert a.unreachable_states() == set()


def test_estados_inutiles(dfa_con_inutil):
    a = Analyser(dfa_con_inutil)
    assert a.useless_states() == {'q2'}


def test_sin_estados_inutiles(dfa_completo):
    a = Analyser(dfa_completo)
    assert a.useless_states() == set()