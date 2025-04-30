## MealyAutomaton Extension for UltraDES-Python

This module extends the UltraDES-Python library to support the creation and manipulation of Mealy-type automata, using event labels of the form input|output. It is fully compatible with the C#-based UltraDES core and designed for use in environments such as Google Colab via clr integration.

Features

✅ Define Mealy automata with transitions of the form input_event | output_event

✅ Automatically constructs transition function f and output function h

✅ Visualizes automata using built-in UltraDES visualization tools

✅ Exports to .fsm, .xml, and .ads file formats

✅ Imports from .fsm and reconstructs Mealy structure

Installation

Ensure you have UltraDES Python configured for use with pythonnet in Google Colab or JupyterNotebook.

Save mealy_automaton.py in your project directory.

Import into your script:

from mealy_automaton import MealyAutomaton

Basic Example

# States and Events (use UltraDES native definitions)
s1 = state("s1", marked=True)
s2 = state("s2")

e1 = event("e1", controllable=True)
e2 = event("e2", controllable=False)
e3 = event("e3")
e4 = event("e4")

# Define Mealy Automaton
mealy = MealyAutomaton([
    (s1, e1, e3, s2),
    (s2, e2, e4, s1)
], s1, "MealyExample")

# Visualize
show_automaton(mealy.get_automaton())

# View transitions
mealy.print_transitions()

# Access f and h functions
print(mealy.get_f())
print(mealy.get_h())

Exporting

mealy.export_fsm("mealy.fsm")
mealy.export_xml("mealy.xml")
mealy.export_ads("mealy.ads")

Importing from FSM

mealy2 = MealyAutomaton.from_fsm("mealy.fsm")
mealy2.print_transitions()

Integration Notes

Event names must follow the format input|output.

This wrapper reuses UltraDES's native types (State, Event, Transition).

All output events inherit the controllability of their corresponding input events.

License
Developed by: Miranda, Lima, Cabral, de Queiroz.
