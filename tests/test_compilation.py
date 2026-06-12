"""
Módulo de pruebas para el compilador de DFAs extendidos.

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
from compiler import parse_sre, VOCAB


def test_parse_sre_punto():
    resultado = parse_sre(VOCAB, '.')
    assert resultado == VOCAB


def test_parse_sre_rango():
    resultado = parse_sre(VOCAB, '[a-z]')
    assert resultado == [chr(c) for c in range(ord('a'), ord('z')+1)]


def test_parse_sre_rango_negado():
    resultado = parse_sre(VOCAB, '[^a-z]')
    rango = [chr(c) for c in range(ord('a'), ord('z')+1)]
    assert all(c not in rango for c in resultado)


def test_parse_sre_clase_digito():
    resultado = parse_sre(VOCAB, '\\d')
    assert resultado == list('0123456789')


def test_parse_sre_clase_espacio():
    resultado = parse_sre(VOCAB, '\\s')
    assert '\n' in resultado
    assert '\t' in resultado


def test_parse_sre_or():
    resultado = parse_sre(VOCAB, '[a-z]|\\d')
    letras = [chr(c) for c in range(ord('a'), ord('z')+1)]
    digitos = list('0123456789')
    for c in letras:
        assert c in resultado
    for c in digitos:
        assert c in resultado


def test_parse_sre_caracter_simple():
    resultado = parse_sre(VOCAB, 'a')
    assert resultado == ['a']