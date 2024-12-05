from abc import ABC, abstractmethod
from dataclasses import dataclass
from projeto.endereco import Endereco


@dataclass
class Funcionario(ABC):
  nome: str
  email: str
  salario: float
  endereco: Endereco


@abstractmethod
def salario_final(self):
   pass
