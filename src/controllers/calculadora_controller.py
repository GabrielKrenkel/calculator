import os

import ipywidgets
from IPython.display import clear_output, display


class Calculator():

    def __init__(self) -> None:
        self.create_widgets()
        self.define_functions()
        self.show_number_selection()

    def create_widgets(self) -> None:

        self.number_selection = ipywidgets.IntText()
        self.select_operation = ipywidgets.Select(
            options=['Somar', 'Dividir', 'Subtrair', 'Multiplicar'],
            description='Operação:',
        )
        self.next_value = ipywidgets.Button(description=f'{self.select_operation.value}')
        self.result = ipywidgets.Button(description='Resultado')

        self.main_output = ipywidgets.Output()

    def define_functions(self) -> None:
        pass

    def show_number_selection(self) -> None:
        display(self.main_output)

        with self.main_output:
            display(self.number_selection, self.select_operation, ipywidgets.HBox([self.next_value, self.result]))
