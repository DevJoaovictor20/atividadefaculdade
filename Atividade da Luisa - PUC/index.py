#mostrando o menu inicial
print("--- MENU PRINCIPAL ---")
print("(1) Gerenciar estudantes")
print("(2) Gerenciar professores")
print("(3) Gerenciar disciplinas")
print("(4) Gerenciar turmas")
print("(5) Gerenciar matrículas")
print("(6) Sair")

#Executando a opcao desejada
entrada = (input("Selecione a opção desejada no menu: "))
if entrada in ("1", "2", "3", "4", "5", "9"):
   opcao = int(entrada)
   if opcao == 1 :
      print("Voce escolheu a opcao  {entrada} - Estudantes")
   elif opcao == 2 :
      print("Voce escolheu a opcao  {entrada} - Professores")
   elif opcao == 3 :
      print("Voce escolheu a opcao  {entrada} - Disciplinas")
   elif opcao == 4 :
      print("Voce escolheu a opcao  {entrada} - Turmas")
   elif opcao == 5 :
      print("Voce escolheu a opcao  {entrada} - Matrículas")
   elif opcao == 6 :
       print("Voce escolheu a opcao {entrada} - Sair")
       
       
#Menu de operacoes
if opcao != 6:
   print("1. Incluir")
   print("2. Listar")
   print("3. Atualizar")
   print("4. Excluir")
   print("5. Voltar ao menu")
   entrada2 = input("Escolha a opcao desejada")
   if entrada2 in ("1", "2", "3", "4", "5"):
      opcao2 = int(entrada2)
      if opcao2 == 1:
         print("A opcao escolhida foi {entrada2} - Incluir")
      elif opcao2 == 2 :
         print("A opcao escolhida foi {entrada2} - Listar")
      elif opcao2 == 3:
         print("A opcao escolhida foi {entrada2} - Autorizar")
      elif opcao2 == 4:
         print("A opcao escolhida foi {entrada2} - Excluir")
   else:
      print("Opcao invalida")
         
      

