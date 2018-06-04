"""
Titulo: Programa em python para cadastro de funcionário
Descricao: programa com modulos para criacao e edicao de banco de dados e cadastro de funcionarios
Versão: 1.0
"""
from gerenciador import *
from cadastro import *

def main():
    code=0;
    while(1):
        print("\n-- Digite a opcao desejada --\n")
        print("(1) cadastrar pessoa\n(2)consultar pessoa\n(3)opcoes de banco")
        opt=int(input("op = "))
        if(opt==1):
            Cad_pessoaf()
            code+=1;
        elif (opt==2): Lista_pessoaf()
        elif opt==3: cria_banco("clientes")
        else: break 


    
main()
