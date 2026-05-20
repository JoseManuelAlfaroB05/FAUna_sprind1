"""
Módulo de pruebas para la visualización de Autómatas Finitos Deterministas (DFA).

:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática - Universidad Nacional (UNA)
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
from automata.fa.dfa import DFA
from fauna_main import generar_dot


@pytest.fixture
def dfa_simple():
    return DFA(
        states={'q0', 'q1'},
        input_symbols={'a', 'b'},
        transitions={
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q0'}
        },
        initial_state='q0',
        final_states={'q1'}
    )

def test_dot_contiene_digraph(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert "digraph DFA {" in dot

def test_dot_contiene_rankdir(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert "rankdir=LR" in dot

def test_dot_estado_inicial(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert '"" -> q0' in dot

def test_dot_estado_final_doublecircle(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert 'q1 [shape=doublecircle]' in dot

def test_dot_estado_normal_circle(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert 'q0 [shape=circle]' in dot

def test_dot_contiene_transiciones(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert '->' in dot

def test_dot_transiciones_agrupadas():
    dfa = DFA(
        states={'q0', 'q1'},
        input_symbols={'a', 'b'},
        transitions={
            'q0': {'a': 'q1', 'b': 'q1'},
            'q1': {'a': 'q1', 'b': 'q1'}
        },
        initial_state='q0',
        final_states={'q1'}
    )
    dot = generar_dot(dfa)
    assert 'label="a,b"' in dot or 'label="b,a"' in dot

def test_dot_cierra_llave(dfa_simple):
    dot = generar_dot(dfa_simple)
    assert dot.strip().endswith("}")