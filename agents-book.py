## Classes provide a means of bundling data and functionality together


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
## en utils crear distance_squared y turn_heading
