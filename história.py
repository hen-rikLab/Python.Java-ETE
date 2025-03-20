name_protagonista = input("Qual o nome do(a) personagem? ")
local = input("Onde será a história? ")
arma = input("Escolha uma arma para o combate: ")

print(f"{name_protagonista} desafiou Elon Musk para um x1 dos crias bate panela. "
      f"Na {local}, cercados por uma multidão vibrante, começaram o duelo. "
      f"{name_protagonista} mostrou seu ritmo impecável, enquanto Elon usou uma {arma} "
      "construída para criar raios de lesões extraídos do jogador Neymar Jr. "
      "No final, as panelas soltaram faíscas e Elon admitiu: “Você ganhou. Mas da próxima vez, levarei uma baubau!”")
print("DESEJA CONTINUAR A HISTÓRIA?")
continuar = input("Digite S ou N: ")
if continuar == "S":
      print(f"Elon Musk: Você pensou que acabou? hahahahha. Eu treinei tomei o SUCOOO, agora estou mais forte, você não consegue me vencer mais. {name_protagonista}: Eu vou treinar!!!")
      upgrade = input("Escolha seu upgrade: ")
      print(f"Depois do upgrade({upgrade}), mais uma vez o Elon musk levou baubau!!")
else:
      print("Fim da História")
