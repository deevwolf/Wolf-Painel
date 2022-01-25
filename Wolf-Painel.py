import pyfiglet as pf
import requests
import json
from os import system
system('cls')
system('clear')
print("""
                      .
                      00
                      000
                     00000                  .
                     000000                00
      .             0000000              0000
      0000          0000000            00000
      00000         00000000          000000
       000000       00000000        0000000
        0000000     00000000      000000000
        0000000      0000000     000000000
         0000000     00000000   000000000
           000000000  0000000   00000000
             0000000   000000  0000000            .
              000000  00000  0000000        000000
   .           000000  0000  000000    000000000
    0000000     000000 000   0000   00000000000
     0000000000   0000  00  0000  00000000000
       00000000000  000 00 000  0000000000
          00000000000 00 0 0  000000000
             00000000000000 0000
                      000000000
                    000     000000
""")
print(pf.figlet_format("WOLF-SCRIPT "))
print("[-]Welcome To My Script")
print("#################################################")
print("[1]- Menu De Opções")
print("[99]- Exit")
print("#################################################")
enter_menu = input(">>> ")
if enter_menu == '1':
    system('cls')
    print("#################################################")
    print("[1]- Consultar CEP")
    print("[2]- Consultar IP")
    print("[99]- Exit")
    print("")
    print("Versão Alpha 0,1")
    print("#################################################")
    enter1 = input(">>> ")
if enter1 == '1':
    cep_input=input("Digite o Cep: ")

    if len(cep_input) != 8:
        print("Quantidade De Digitos Invalida! ")
        exit()
        

    wolf_cep= requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    cep_address = wolf_cep.json()

    if 'erro' not in cep_address:
        print("#################################")
        print("CEP LOCALIZADO!")
        print("")
        print('CEP: {}'.format(cep_address['cep']))
        print('LONGADOURO: {}'.format(cep_address['logradouro']))
        print('complemento: {}'.format(cep_address['complemento']))
        print('BAIRRO: {}'.format(cep_address['bairro']))
        print('LOCALIDADE: {}'.format(cep_address['localidade']))
        print('DDD: {}'.format(cep_address['ddd']))
        print("#################################")
        print("                              By WOLF-SCRIPT")
        print("")
        print("")
        menu_input = input("Deseja Voltar Ao Menu? [s/n] ")
        if menu_input == 's':
            system('python teste.py')
        else:
            print("Ok , Saindo..")
        
    else:
        print("{} é Um Cep Invalido ;(!".format(cep_input))
    
if enter1=='2':
    ip_input=input("Digite O IP: ")
    #if len(ip_input) != 14:
    #	print("Quantidade De Digitos Invalida! ")
    #	exit()
        
    wolf_ip= requests.get('https://ipwhois.app/json/{}'.format(ip_input))

    ip_address = wolf_ip.json()

    if 'ip' in ip_address:
       print('IP: {}'.format(ip_address['ip']))
       print('CONTINENTE: {}'.format(ip_address['continent']))
       print('PAIS: {}'.format(ip_address['country']))
       print('CAPITAL: {}'.format(ip_address['country_capital']))
       print('ESTADO: {}'.format(ip_address['region']))
       print('CIDADE: {}'.format(ip_address['city']))
       print('LATITUDE: {}'.format(ip_address['latitude']))
       print('LONGITUDE: {}'.format(ip_address['longitude']))
    else:
        print("{} é Um IP Invalido ;(!".format(ip_input))
      
    print("")
    menu_input = input("Deseja Voltar Ao Menu? [s/n] ")
    if menu_input == 's':
        system('python teste.py')
    else:
        print("Ok , Saindo..")
if enter1=='99':
    system('exit')
else:
    print("Opção Invalida")
    enter_menu = input(">>> ")