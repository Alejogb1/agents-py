## en utils crear distance_squared y turn_heading

from statistics import mean
from time import sleep
import random
import copy
import collections
import numbers

## una clase es una forma de juntar datos y en una misma funcionalidad
class Thing:
    ## thing es cualquier cosa que puede aparecer en el entorno
    ## en este caso tratamos con una funcion incorporada de python
    ## repr nos recrea un objeto con el MISMO VALOR y si no funciona devuelve una descripcion...
    def __repr__(self):
        ## self representa la instancia de nuestra clase
        ## __name__ es el nombre del modulo actual
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))
    def is_alive(self):
        # devuelve true si esta vivo
        return hasattr(self, 'alive') and self.alive
    def show_state(self):
        print("no se como mostrar el estado")


class Agent(Thing):
    ## el agente solo tiene UN espacio
    ## .program es un espacio, no un metodo
    def __init__(self, program=None):
        self.alive = True
        self.bump = False 
        self.holding = []
        self.performance = 0
        ## isinstance es un builtin q me devuelve True si el objeto del argumento es una instancia o subclase
        if program is None or not isinstance(program, collections.abc.Callable):
            print("No encuentra el programa para {}".format(self.__clas__.__name__))

            ## al metodo 
            def program(percept):
                ## eval se usa para ejecutar codigos arbitrarios
                ## format convierte un valor a una representacion con formato
                return eval(input('Percept={}; action? '.format(percept)))
            
        self.program = program

        def can_grab(self, thing):
            ## devuele true si es que lo puede agarrar
            return False

def TraceAgent(agent):
    """me ayuda a saber que es lo q hace el agente, devuelve el valor de input y output"""
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print('{} perceives {} and does {}'.format(agent, percept, action))
        return action
    agent.program  = new_program
    return agent

def SimpleReflexAgentProgram(rules,  interpret_input):
    """ toma una accion solo en base a la percepcion"""
    def program(percept):
        state = interpret_input(percept)
        rule = rule_match(state, rules)
        action = rule.action
        return action
    return program

def ModelBasedReflexAgentProgram(rules, update_state, model):
    def program(percept):
        program.state = update_state(program.state, program.action, percept, model)
        rule = rule_match(program.state, rules)
        action = rule.action
    program.state = program.action = None
    return program


def rule_match(state, rules):
    for rule in rules:
        if rule.matches(state):
            return rule