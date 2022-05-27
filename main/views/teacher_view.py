import PySimpleGUI as sg
from main.views.base_view import BaseView


class TeacherView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - Professor', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Olá, Professor', font=('Open Sans', 20), text_color='black',)],
            [self.blue_button('Cadastrar aula', 1)],
            [self.blue_button('Adicionar créditos', 2)],
            [self.blue_button('Ver faturamento', 3)],
            [sg.Text('0', font=('Open Sans', 20), text_color='black', )],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def register_lesson(self):
        pass

    def add_credits(self):
        pass

    def see_billing(self):
        pass
