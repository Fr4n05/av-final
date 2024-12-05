from projeto.engenheiro import Engenheiro
from projeto.nutricionista import Nutricionista
from projeto.endereco import Endereco


engenheiro=Engenheiro(
    nome = input ("Digite seu nome:"),
    email = input ("Infome o seu email:"),
    crea = input ("Digite o seu cod. CREA:"),
    salario= float(input("Informe o seu salario:")),
    endereco= Endereco(
    logradouro= input(" Informe o seu logradouro:"),
    complemento = input("Informe o seu complemento:"),
    numero= input("Informe o numero residencial:")
 )
) 
engenheiro.salario_final()

nutricionista = Nutricionista(
     nome = input("\nDigite seu nome:"),
     email = input("Digite seu email:"),
     crm= input("Digite seu cod. CRM:"),
     salario = float(input("Digite seu valor salarial:")),
     endereco= Endereco(
     logradouro = input("Digite o nome do logradouro:"),
     complemento= input("Informe o seu complemento:"),
     numero= input("Informe o seu numero residencial:")
  )
)
nutricionista.salario_final()