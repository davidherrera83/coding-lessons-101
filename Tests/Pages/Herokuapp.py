from pylenium.driver import Pylenium

class Herokuapp:
    def __init__(self, py: Pylenium):
        self.py = py

    def visit_herokuapp(self):
         self.py.visit('https://the-internet.herokuapp.com/')

         return self
    
    def click_on_example(self, example: str):
         self.py.get(f'{example}').click()

    def login_process(self):
         pass