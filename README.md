# FAuna 

**FAuna** es una herramienta de línea de comandos para visualizar, ejecutar y analizar Autómatas Finitos Deterministas (DFA) a partir de archivos JSON. Desarrollada como proyecto académico para el curso de Estructuras Discretas (EIF203) de la Escuela de Informática de la Universidad Nacional (UNA).

---

## Contexto

Este proyecto fue desarrollado en el marco del curso **EIF203 - Estructuras Discretas (I-2026)** como parte del Sprint 2 del proyecto grupal FAuna. El objetivo es aplicar conceptos de autómatas finitos y desarrollar competencias en el manejo de herramientas de desarrollo como Git, ambientes virtuales de Python y bibliotecas especializadas.

---

## Autores

| Nombre | 
|--------|
| Jose Manuel Alfaro Bogantes |
| Josué Morales Paniagua |
| Anders Ramírez Mayorga |

---

## Sprint 2
- [x] Estructura del proyecto
- [x] Modelo propio de DFA sin dependencias externas
- [x] Lectura y validación de DFAs en formato JSON
- [x] Visualización de DFAs como imagen PNG
- [x] Ejecución de DFAs con tracing
- [x] Análisis de DFAs (completitud, estados inalcanzables e inútiles)
- [x] Compilador de DFA extendido a DFA estándar
- [x] Sistema de comandos desde la terminal (`run`, `view`, `analyse`)
- [x] Ejemplos de autómatas estándar y extendido
- [x] Tests de visualización, análisis, compilación y runner
- [x] Documentación automática con Sphinx

---

## Estructura del Proyecto

```
fauna/
├── src/
│   └── dfa/
│       ├── fauna_main.py   # Punto de entrada principal con sistema de comandos
│       ├── model.py        # Modelo propio de DFA sin dependencias externas
│       ├── runner.py       # Ejecución de DFAs con tracing
│       ├── analysis.py     # Análisis de DFAs
│       └── compiler.py     # Compilador de DFA extendido a estándar
├── tests/
│   ├── test_visualization.py
│   ├── test_analysis.py
│   ├── test_compilation.py
│   └── test_runner.py
├── docs/                   # Configuración de Sphinx
├── html/                   # Documentación generada
├── examples/
│   ├── vocales.json        # DFA: Verificador de vocales
│   ├── semaforo.json       # DFA: Semáforo inteligente
│   ├── bases.json          # DFA: Buscador de codones
│   └── extended_dfa.json   # DFA extendido de ejemplo
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Ejemplos de Autómatas

### Autómata 1 — Verificador de Vocales
Verifica que una palabra contenga al menos 3 vocales y que no haya dos vocales consecutivas. Por ejemplo, `mudanza` es aceptada (tiene 3+ vocales no consecutivas), pero `aire` no lo es (tiene las vocales `a` e `i` consecutivas).

> **Nota:** Por limitaciones del alfabeto, palabras con dígrafos del español como `ll` o `ch` pueden ser aceptadas sin distinción.

### Autómata 2 — Semáforo Inteligente
Simula el comportamiento de un semáforo con múltiples estados. Cada símbolo del alfabeto representa un evento:

| Símbolo | Evento | Estado destino |
|---------|--------|----------------|
| `t` | Timer (temporizador) | Cambia de fase |
| `s` | Sensor | Ajuste de fase |
| `r` | Reset | Regresa a Rojo |
| `n` | Night | Modo Nocturno |
| `e` | Emergencia | Modo Emergencia |
| `f` | Falla | Modo Falla |
| `m` | Mantenimiento | Regresa al estado actual |

El estado inicial y final es **q0 (Rojo)**.

### Autómata 3 — Buscador de Codones
Escanea una secuencia de bases nitrogenadas (A, T, G, C) en busca de al menos uno de los codones de inicio/parada: **ATG**, **TAA** o **TGC**. El autómata avanza por los estados según el progreso en la detección del patrón.

### Autómata Extendido — Ejemplo de DFA con Expresiones Regulares
DFA extendido de ejemplo que usa expresiones regulares en sus transiciones (`[a-z]`, `\d`). Sirve como entrada para el compilador.

---

## Forma de Uso

### Requisitos previos
- Python 3.x
- [Graphviz](https://graphviz.org/download/) instalado en el sistema y en el PATH

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/JoseManuelAlfaroB05/FAUna_sprind1.git
cd FAUna_sprind1

# Crear y activar el ambiente virtual
python -m venv env
env\Scripts\activate

# en caso de no poder activar el ambiente por algun error usar

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# En Windows, si pygraphviz da error, ejecutar primero:
$env:INCLUDE = "C:\Program Files\Graphviz\include"
$env:LIB = "C:\Program Files\Graphviz\lib"

# Instalar dependencias
pip install -r requirements.txt
```

### Comandos

Desde la raíz del proyecto, con el ambiente virtual activado:

**Ejecutar un DFA contra una cadena:**
```bash
# Sin tracing (solo muestra si fue aceptada o rechazada)
python src\dfa\fauna_main.py run examples\vocales.json mudanza

# Con tracing (muestra el proceso paso a paso)
python src\dfa\fauna_main.py run examples\vocales.json mudanza --trace
python src\dfa\fauna_main.py run examples\vocales.json aire --trace
python src\dfa\fauna_main.py run examples\semaforo.json rtn --trace
python src\dfa\fauna_main.py run examples\bases.json ATGCC --trace
```

**Visualizar un DFA como PNG:**
```bash
python src\dfa\fauna_main.py view examples\vocales.json
python src\dfa\fauna_main.py view examples\semaforo.json
python src\dfa\fauna_main.py view examples\bases.json
```

**Analizar un DFA:**
```bash
python src\dfa\fauna_main.py analyse examples\vocales.json
python src\dfa\fauna_main.py analyse examples\semaforo.json
python src\dfa\fauna_main.py analyse examples\bases.json
```

**Compilar un DFA extendido:**
```bash
python -c "import sys; sys.path.insert(0, 'src/dfa'); from model import DFA; from compiler import compile_dfa; dfa = DFA.from_json('examples/extended_dfa.json'); compiled = compile_dfa(dfa); print(compiled)"
```

### Ejecutar Tests

```bash
# Todos los tests
python -m pytest tests/

# Por módulo
python -m pytest tests/test_visualization.py
python -m pytest tests/test_analysis.py
python -m pytest tests/test_compilation.py
python -m pytest tests/test_runner.py
```

---

## Documentación

La documentación generada con Sphinx se encuentra en la carpeta `html/`. Para consultarla, abre en tu navegador:

```
html\index.html
```

---

## Dependencias

Ver `requirements.txt`. Las principales son:

- `automata-lib` — Validación y manejo de DFAs (visualización Sprint 1)
- `pygraphviz` — Generación de imágenes PNG
- `sphinx` — Generación de documentación
- `pytest` — Pruebas unitarias
