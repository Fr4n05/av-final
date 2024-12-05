from dataclasses import dataclass
from projeto.funcionario import Funcionario


@dataclass
class Nutricionista(Funcionario):
    crm : str
    def salario_final(self):
     return "Salario nutricionista"
    
