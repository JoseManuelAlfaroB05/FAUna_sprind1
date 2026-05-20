# FAuna 🦎

**FAuna** es una herramienta de línea de comandos para visualizar Autómatas Finitos Deterministas (DFA) a partir de archivos JSON. Desarrollada como proyecto académico para el curso de Estructuras Discretas (EIF203) de la Escuela de Informática de la Universidad Nacional (UNA).

---

## Contexto

Este proyecto fue desarrollado en el marco del curso **EIF203 - Estructuras Discretas (I-2026)** como parte del Sprint 1 del proyecto grupal FAuna. El objetivo es aplicar conceptos de autómatas finitos y desarrollar competencias en el manejo de herramientas de desarrollo como Git, ambientes virtuales de Python y bibliotecas especializadas.

---

## Autores

| Nombre | 
|--------|
| Jose Manuel Alfaro Bogantes |
| Josué Morales Paniagua |
| Anders Ramírez Mayorga |

---

## Estado Actual

🟡 **En desarrollo — Sprint 1**

- [x] Estructura del proyecto
- [x] Lectura y validación de DFAs en formato JSON
- [x] Visualización de DFAs como imagen PNG
- [x] Ejemplos de autómatas
- [x] Tests de visualización
- [x] Documentación automática con Sphinx

---

## Estructura del Proyecto

```
fauna/
├── src/
│   └── dfa/
│       ├── fauna_main.py   # Punto de entrada principal
│       ├── model.py
│       ├── runner.py
│       ├── analysis.py
│       └── compiler.py
├── tests/
│   ├── test_visualization.py
│   └── ...
├── docs/                   # Configuración de Sphinx
├── html/                   # Documentación generada
├── examples/
│   ├── automata_1.json     # DFA: Verificador de vocales
│   ├── automata_2.json     # DFA: Semáforo inteligente
│   └── automata_3.json     # DFA: Buscador de codones
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

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución

Desde la raíz del proyecto, con el ambiente virtual activado:

```bash
# Autómata 1 - Verificador de vocales
python src\dfa\fauna_main.py examples\vocales.json

# Autómata 2 - Semáforo inteligente
python src\dfa\fauna_main.py examples\semaforo.json

# Autómata 3 - Buscador de codones
python src\dfa\fauna_main.py examples\bases.json
```

Cada comando genera una imagen PNG en la misma carpeta del JSON:

```
examples\vocales.png
examples\semaforo.png
examples\bases.png
```

### Ejecutar Tests

```bash
python -m pytest tests/test_visualization.py
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

- `automata-lib` — Validación y manejo de DFAs
- `pygraphviz` — Generación de imágenes PNG
- `sphinx` — Generación de documentación
- `pytest` — Pruebas unitarias