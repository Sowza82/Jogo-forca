import random


def escolher_palavra():
  palavras = [
      "python", "programação", "jogo", "desenvolvimento", "aplicativo",
      "openai", "inteligencia", "cachorro" ,"famìlia","formiga","otorrinolaringologista",
      "android","apartamento","constitução","padaria","dedo","pão","francês", "trem"
  ]
  return random.choice(palavras)


def obter_nivel():
  niveis = {1: 6, 2: 4, 3: 3}
  while True:
    try:
      nivel = int(input("Escolha o nível de dificuldade (1, 2 ou 3): "))
      if nivel in niveis:
        return niveis[nivel]
      else:
        print("Por favor, escolha um nível válido.")
    except ValueError:
      print("Por favor, digite um número válido.")


def jogar_forca():
  palavra_escolhida = escolher_palavra()
  palavra_oculta = ["_" for _ in palavra_escolhida]
  tentativas_restantes = obter_nivel()

  while "_" in palavra_oculta and tentativas_restantes > 0:
    letra = input(
        f"Palavra: {' '.join(palavra_oculta)}\nDigite uma letra: ").lower()

    if letra.isalpha() and len(letra) == 1:
      if letra in palavra_escolhida:
        print("Acertou!")
        for i in range(len(palavra_escolhida)):
          if palavra_escolhida[i] == letra:
            palavra_oculta[i] = letra
      else:
        if tentativas_restantes > 1:
          print(f"Errou! Tentativas restantes: {tentativas_restantes - 1}")
        else:
          print("Errou! Ultima tentativa.")

        if tentativas_restantes > 1:
          tentativas_restantes -= 1
        else:
          tentativas_restantes -= 2

  if "_" not in palavra_oculta:
    print(f"ParabÃ©ns, você ganhou! A palavra era: {palavra_escolhida}")
  else:
    print(f"Fim de jogo. Você perdeu. A palavra era: {palavra_escolhida}")


if __name__ == "__main__":
  while True:
    print("Bem-vindo ao Jogo da Forca!")
    jogar_forca()

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
      print("Obrigado por jogar! Então até a próxima.")
      break
    else:
      print("Ótimo! Vamos jogar novamente.")
