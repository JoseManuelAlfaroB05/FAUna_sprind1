"""
Módulo principal de FAuna para la gestión de Autómatas Finitos Deterministas (DFA).
Permite ejecutar, visualizar y analizar DFAs desde la terminal.

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
from collections import defaultdict
from model import DFA
from runner import Runner
from analysis import Analyser
import pygraphviz as pgv


def generar_dot(pDfa):
    # Detectar si es modelo propio o automata-lib
    if hasattr(pDfa, 'varInitialState'):
        varInitial = pDfa.varInitialState
        varFinals = pDfa.varFinalStates
        varStates = pDfa.varStates
        varTransitions = pDfa.varTransitions
    else:
        varInitial = pDfa.initial_state
        varFinals = pDfa.final_states
        varStates = pDfa.states
        varTransitions = pDfa.transitions

    dot = "digraph DFA {\n"
    dot += "    rankdir=LR;\n"
    dot += "    nodesep=0.5;\n"
    dot += "    ranksep=0.9;\n"
    dot += "    overlap=false;\n"
    dot += "    splines=true;\n"
    dot += "    node [shape=circle, fontsize=14];\n"
    dot += "    edge [fontsize=11];\n"
    dot += f'    "" -> {varInitial};\n'
    for varState in varFinals:
        dot += f'    {varState} [shape=doublecircle];\n'
    for varState in varStates:
        if varState not in varFinals:
            dot += f'    {varState} [shape=circle];\n'
    for varState, varTrans in varTransitions.items():
        varGroups = defaultdict(list)
        for varSymbol, varDest in varTrans.items():
            varGroups[varDest].append(varSymbol)
        for varDest, varSymbols in varGroups.items():
            varLabel = ",".join(varSymbols)
            dot += f'    {varState} -> {varDest} [label="{varLabel}"];\n'
    dot += "}\n"
    return dot

def cmd_run(pJsonPath, pInput, pTrace=False):
    dfa = DFA.from_json(pJsonPath)
    r = Runner(dfa)
    r.run(pInput, pTrace)


def cmd_view(pJsonPath):
    dfa = DFA.from_json(pJsonPath)
    dot = generar_dot(dfa)
    varFolder = os.path.dirname(pJsonPath)
    varBaseName = os.path.splitext(os.path.basename(pJsonPath))[0]
    varPngPath = os.path.join(varFolder, varBaseName + ".png")
    grafo = pgv.AGraph(string=dot)
    grafo.layout(prog='dot')
    grafo.draw(varPngPath, format='png')
    print(f"Imagen generada: {varPngPath}")


def cmd_analyse(pJsonPath):
    dfa = DFA.from_json(pJsonPath)
    a = Analyser(dfa)
    print(f"Completo: {a.is_complete()}")
    print(f"Estados inalcanzables: {a.unreachable_states()}")
    print(f"Estados inútiles: {a.useless_states()}")


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python src\\dfa\\fauna_main.py run <archivo.json> <input> [--trace]")
        print("  python src\\dfa\\fauna_main.py view <archivo.json>")
        print("  python src\\dfa\\fauna_main.py analyse <archivo.json>")
        return

    varCommand = sys.argv[1]
    varJsonPath = sys.argv[2]

    if not os.path.exists(varJsonPath):
        print(f"Error: archivo '{varJsonPath}' no encontrado")
        return

    if varCommand == "run":
        if len(sys.argv) < 4:
            print("Error: falta la cadena de entrada")
            print("Uso: python src\\dfa\\fauna_main.py run <archivo.json> <input> [--trace]")
            return
        varInput = sys.argv[3]
        varTrace = "--trace" in sys.argv
        cmd_run(varJsonPath, varInput, varTrace)

    elif varCommand == "view":
        cmd_view(varJsonPath)

    elif varCommand == "analyse":
        cmd_analyse(varJsonPath)

    else:
        print(f"Error: comando '{varCommand}' no reconocido")
        print("Comandos disponibles: run, view, analyse")


if __name__ == "__main__":
    main()