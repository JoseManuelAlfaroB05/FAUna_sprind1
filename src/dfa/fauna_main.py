"""
Módulo principal de FAuna para la visualización de Autómatas Finitos Deterministas (DFA).
Este módulo lee un autómata en formato JSON, lo valida usando la librería automata-lib
y genera una representación gráfica en formato PNG usando pygraphviz.
:course: EIF203 - Estructuras Discretas
:university: Escuela de Informática – Universidad Nacional (UNA)
:semester: I-2026
:authors:
    - Jose Manuel Alfaro Bogantes
    - Josué Morales Paniagua
    - Anders Ramírez Mayorga
"""
import sys
import json
import os
from automata.fa.dfa import DFA
from collections import defaultdict
import pygraphviz as pgv

def generar_dot(dfa):
    dot = "digraph DFA {\n"
    dot += "    rankdir=LR;\n"
    dot += "    nodesep=0.5;\n"
    dot += "    ranksep=0.9;\n"
    dot += "    overlap=false;\n"
    dot += "    splines=true;\n"
    dot += "    node [shape=circle, fontsize=14];\n"
    dot += "    edge [fontsize=11];\n"
    dot += f'    "" -> {dfa.initial_state};\n'
    for estado in dfa.final_states:
        dot += f'    {estado} [shape=doublecircle];\n'
    for estado in dfa.states:
        if estado not in dfa.final_states:
            dot += f'    {estado} [shape=circle];\n'
    for estado, transiciones in dfa.transitions.items():
        grupos = defaultdict(list)
        for simbolo, destino in transiciones.items():
            grupos[destino].append(simbolo)
        for destino, simbolos in grupos.items():
            label = ",".join(simbolos)
            dot += f'    {estado} -> {destino} [label="{label}"];\n'
    dot += "}\n"
    return dot

def generar_png(dot, archivo_png):
    grafo = pgv.AGraph(string=dot)
    grafo.layout(prog='dot')
    grafo.draw(archivo_png, format='png')

def main():
    if len(sys.argv) != 2:
        print("Uso: python src\\dfa\\fauna_main.py examples\\automata.json")
        return
    ruta_json = sys.argv[1]
    if not os.path.exists(ruta_json):
        print("Error: archivo no encontrado")
        return
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    dfa = DFA(
        states=set(data["states"]),
        input_symbols=set(data["alphabet"]),
        transitions=data["transitions"],
        initial_state=data["initial_state"],
        final_states=set(data["final_states"])
    )
    print("DFA cargado correctamente")
    dot = generar_dot(dfa)
    carpeta = os.path.dirname(ruta_json)
    nombre_base = os.path.splitext(os.path.basename(ruta_json))[0]
    archivo_png = os.path.join(carpeta, nombre_base + ".png")
    generar_png(dot, archivo_png)
    print(f"Imagen generada: {archivo_png}")

if __name__ == "__main__":
    main()