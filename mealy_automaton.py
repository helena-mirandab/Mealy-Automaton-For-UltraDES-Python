# mealy_automaton.py

from System.Collections.Generic import List
from UltraDES import Transition, Event, DeterministicFiniteAutomaton

# Wrapper para objetos State e Event no UltraDES Python
from __main__ import (
    state, event, is_controllable,
    transitions, initial_state, read_fsm,
    show_automaton
)

class MealyAutomaton:
    def __init__(self, transitions, initial, name):
        """
        transitions: lista de (estado_origem, evento_entrada, evento_saida, estado_destino)
        initial: estado inicial (State)
        name: nome do automato
        """
        self.initial = initial
        self.name = name
        self.f = {}  # função de transição: (estado, entrada) -> próximo estado
        self.h = {}  # função de saída: (estado, entrada) -> saída
        self.states = set()
        self.trans = List[Transition]()

        for (s_from, e_in, e_out, s_to) in transitions:
            input_label = str(e_in)
            output_label = str(e_out)
            state_from_label = str(s_from)
            state_to_label = str(s_to)

            combined_label = f"{input_label}|{output_label}"
            e_combined = Event(combined_label, e_in.Controllability)

            self.trans.Add(Transition(s_from, e_combined, s_to))

            self.f[(state_from_label, input_label)] = state_to_label
            self.h[(state_from_label, input_label)] = output_label
            self.states.update([state_from_label, state_to_label])

        self.automaton = DeterministicFiniteAutomaton(self.trans, self.initial, self.name)

    def get_automaton(self):
        return self.automaton

    def get_f(self):
        return self.f

    def get_h(self):
        return self.h

    def show(self):
        return show_automaton(self.automaton)

    def print_transitions(self):
        for t in self.trans:
            origem = str(t.Origin)
            destino = str(t.Destination)
            evento = str(t.Trigger)

            if '|' in evento:
                entrada, saida = evento.split('|')
            else:
                entrada, saida = evento, "?"

            print(f"({origem}) -- {entrada} | {saida} --> ({destino})")

    def export_fsm(self, path):
        self.automaton.ToFsmFile(path)

    def export_xml(self, path):
        self.automaton.ToXMLFile(path)

    def export_ads(self, path):
        self.automaton.ToAdsFile(path)

    @staticmethod
    def from_fsm(path):
        G = read_fsm(path)
        transitions_raw = transitions(G)
        initial = initial_state(G)
        name = G.Name

        mealy_transitions = []

        for (s_from, ev, s_to) in transitions_raw:
            event_label = str(ev)
            if "|" in event_label:
                entrada, saida = event_label.split("|")
            else:
                entrada, saida = event_label, "?"

            e_in = event(entrada, controllable=is_controllable(ev))
            e_out = event(saida, controllable=is_controllable(ev))
            mealy_transitions.append((s_from, e_in, e_out, s_to))

        return MealyAutomaton(mealy_transitions, initial, name)