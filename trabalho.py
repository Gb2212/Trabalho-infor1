

import time
import sys


C_AMARELO = '\033[93m'
C_AZUL = '\033[96m'
C_VERDE = '\033[92m'
C_BRANCO = '\033[97m'
C_VERMELHO = '\033[91m'
C_ROXO = '\033[95m'
C_RESET = '\033[0m'
C_BOLD = '\033[1m'


def colorir(texto, cor):
    return f"{cor}{texto}{C_RESET}"


def write_slow(texto, delay):
    i = 0
    while i < len(texto):
        if texto[i] == '\033':
            fim = texto.find('m', i)
            if fim != -1:
                sys.stdout.write(texto[i:fim+1])
                i = fim + 1
                continue
        sys.stdout.write(texto[i])
        sys.stdout.flush()
        if texto[i] == ' ' and delay < 0.02:
            time.sleep(delay / 2.5)
        else:
            time.sleep(delay)
        i += 1


def digitar(texto, delay=0.04):
    write_slow(texto, delay)
    print()


def input_digitado(texto, delay=0.04):
    write_slow(texto, delay)
    return input()


def desenhar_arte(texto, delay=0.002):
    write_slow(texto, delay)
    print()


def linha(char="═", tamanho=56, cor=C_BRANCO):
    digitar(colorir(char * tamanho, cor), delay=0.005)


def escolher_lado(msg_extra=""):
    while True:
        if msg_extra:
            digitar(msg_extra)
        digitar(
            "  " + colorir("[ 1 ]", C_VERDE + C_BOLD) + colorir(" Esquerda", C_VERDE) +
            "     " +
            colorir("[ 2 ]", C_AZUL + C_BOLD) + colorir(" Direita", C_AZUL)
        )
        opcao = input_digitado(colorir("  ▶ Sua escolha: ", C_BRANCO)).strip()
        if opcao == "1":
            return "esquerda"
        elif opcao == "2":
            return "direita"
        else:
            digitar(colorir("  ⚠ Opção inválida! Digite 1 ou 2.", C_VERMELHO))
            print()


def campo_ascii(time_a, gols_a, time_b, gols_b):
    ta = time_a[:3].upper().center(3)
    tb = time_b[:3].upper().center(3)
    # Formatação fixa para evitar que os emojis desalinhem as bordas laterais
    placar_str = f"{ta} {gols_a} x {gols_b} {tb}"


def boneco_jogada(nome, lado, cor_time, titulo="JOGADA DECISIVA"):
    seta = "======>" if lado == "direita" else "<======"
    nome_formatado = nome[:18].center(20)
    lado_formatado = f"({lado})".center(9)
   
    desenhar_arte(colorir(f"""
        ⚽ {titulo} ⚽
        ──────────────────────────────────────
                |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|                  
                |       O        |                  
                |      /|\       |                  
                |      / \       |                  
              O                              
             /|\\ ⚽                          
             / \\                            
           {nome_formatado}                  
        ──────────────────────────────────────
    """, cor_time))


def boneco_goleiro(nome, lado, cor_time):
    if lado == "esquerda":
        goleiro_art = r"  \O/ [PEGO]"
    else:
        goleiro_art = r"  [PEGO] \O/"
   
    nome_formatado = f"({nome[:12]} - {lado[:3]})".center(20)
   
def cena_barreira(batedor, goleiro, lado_chute, cor_batedores, cor_goleiro):
    print()
    digitar(colorir("  🧱  A barreira está sendo formada...", C_AMARELO), delay=0.05)
    time.sleep(0.5)


    for passo in range(1, 5):
        jogadores = "  O " * passo
        sys.stdout.write("\r" + colorir(f"     Formando: {jogadores}", C_VERMELHO))
        sys.stdout.flush()
        time.sleep(0.15)


    print()
    desenhar_arte(colorir(r"""
    ┌──────────────────────────────────────────────────┐
      |‾‾‾‾‾‾‾‾‾‾‾‾‾|
      |      O      |                      
      |     /|\     |                                  
      |     / \     |  O    O    O    O                        
                      /|\  /|\  /|\  /|\                      
                      / \  / \  / \  / \  
                                    O                
                                ⚽ /|\    
                                   / \              
    ──────────────────────────────────────────────────
    """, C_BRANCO))


    time.sleep(0.6)
    digitar(colorir(f"  {batedor} posiciona a bola...", C_BRANCO), delay=0.04)
    time.sleep(0.4)


    if lado_chute == "direita":
        digitar(colorir("  💨  Chuta no canto DIREITO, por cima da barreira!", C_AMARELO), delay=0.04)
        bola_trajeto = r"                 ⚽ ↗ (Voando pro canto direito!)"
    else:


        digitar(colorir("  💨  Enfia pelo canto ESQUERDO, rasteiro!", C_AMARELO), delay=0.04)
        bola_trajeto = r"   ⚽ ➔ (Rasteiro no canto esquerdo!)"


    time.sleep(0.5)
   
    batedor_f = batedor[:12].ljust(12)
    desenhar_arte(colorir(f"""
    ──────────────────────────────────────────────────
      |‾‾‾‾‾‾‾‾‾‾‾‾‾|{bola_trajeto.ljust(41)}
      |      O      |                      
      |     /|\     |                                  
      |     / \     |  O   O   O   O                        
                      /|\\ /|\\ /|\\ /|\\                      
                      / \\ / \\ / \\ / \\  
                                    O                
                                ⚽ /|\\  <-- {batedor_f}  
                                   / \\                
    ──────────────────────────────────────────────────
    """, cor_batedores))
    time.sleep(0.8)


def cena_gol(nome, cor_time, msg="G O O O O O L !"):
    desenhar_arte(colorir(f"""
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
         \\O/   {msg}
          |    ({nome})
         / \\
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """, cor_time))


def cena_defesa(goleiro, cor_time):
    desenhar_arte(colorir(f"""
  X X X X X X X X X X X X X X X X X X X X X X X X X X X
         DEFENDEU! {goleiro} voou no canto!
               \\O/  ⚽
                |
               / \\
  X X X X X X X X X X X X X X X X X X X X X X X X X X X
    """, cor_time))


def cena_trave():
    desenhar_arte(colorir(r"""
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         NA TRAVE!!! Que agonia!!!
           O     ⚽ ➔ | TRAVE!
          /|\         |
          / \         |
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """, C_VERMELHO))


TITULARES_BRASIL = ["Alisson", "Danilo", "Marquinhos", "Gabriel Magalhães",
                    "Alex Sandro", "Casemiro", "Bruno Guimarães", "Neymar",
                    "Raphinha", "Vinícius Júnior", "Endrick"]
TITULARES_ARGENTINA = ["Emiliano Martínez", "Nahuel Molina", "Nicolás Otamendi",
                       "Lisandro Martínez", "Marcos Acuña", "Leandro Paredes",
                       "Rodrigo De Paul", "Alexis Mac Allister", "Nico González",
                       "Lautaro Martínez", "Lionel Messi"]
POSICOES_BASE = ["GOL", "LAD", "ZAG", "ZAG", "LAE",
                 "VOL", "MEI", "MEI", "ATA", "ATA", "ATA"]


COR_POS = {
    "GOL": C_AMARELO,
    "LAD": C_VERDE,
    "LAE": C_VERDE,
    "ZAG": C_AZUL,
    "VOL": C_ROXO,
    "MEI": C_ROXO,
    "ATA": C_VERMELHO,
}
def cor_da_posicao(pos):
    return COR_POS.get(pos, C_BRANCO)


def cena_escalacao(nome, numero, seu_time, adversario, titulares,
                   goleiro_adv, cor_seu, cor_adv):
    linha()
    digitar("📋  ESCALAÇÃO OFICIAL — FINAL DA COPA DO MUNDO  📋")
    time.sleep(0.5)
    linha()


    digitar(f"  É a manhã da FINAL, {nome}.")
    time.sleep(0.6)
    digitar("  Você mal dormiu. O coração não para.")
    time.sleep(0.5)


    if seu_time == "Brasil":
        tecnico = "Ancelotti"
        msg = (f'  "Bom dia, {nome}. Eu vi você nos treinos desta semana."',
               f'  "Sua gana, sua técnica... decidi: você começa como titular."',
               f'  "Mostre ao mundo quem você é. Vamos ao HEXA."')
    else:
        tecnico = "Scaloni"
        msg = (f'  "Buenos dias, {nome}. Você está pronto para isso."',
               f'  "Vi cada treino. A decisão está tomada: você é titular."',
               f'  "Argentina campeã novamente. Depende de você também."')


    print()
    digitar(f"  Mensagem do técnico {tecnico}:")
    print()
    for m in msg:
        digitar(m, delay=0.04)
        time.sleep(0.6)


    time.sleep
    print()
    linha()
    digitar(colorir(f"  ⚽  ESCALAÇÃO TITULAR — {seu_time.upper()}  ⚽", cor_seu))
    print()


    for i, jogador in enumerate(titulares):
        pos = POSICOES_BASE[i] if i < len(POSICOES_BASE) else "   "
        c_pos = cor_da_posicao(pos)
        estrela = f" 🌟 (VOCÊ — CAMISA {numero}!)" if jogador == nome else ""
        time.sleep(0.1)
        digitar(
            "    " + colorir(f"[{pos}]", c_pos) +
            colorir(f"  {jogador}{estrela}", cor_seu),
            delay=0.02
        )


    print()
    linha()
    digitar(f"  Você chega ao vestiário e vê sua camisa {numero} pendurada.")
    time.sleep(0.5)


    if seu_time == "Brasil":
        digitar(colorir("  Verde e amarela. Coração apertando.", C_AMARELO))
    else:
        digitar(colorir("  Albiceleste. Azul e branco. Um sonho.", C_AZUL))


    time.sleep(0.8)
    digitar(f"  Logo você enfrentará {adversario}... na FINAL DA COPA DO MUNDO.")
    time.sleep(1.5)


    desenhar_arte(f"""
      ESTÁDIO METLIFE — NEW YORK/NEW JERSEY
      ══════════════════════════════════════
      {colorir("  O   O   O   O   O   O  ", cor_seu)} {colorir("  O   O   O   O   O   O  ", cor_adv)}
      {colorir(" /|\\ /|\\ /|\\ /|\\ /|\\ /|\\ ", cor_seu)} {colorir(" /|\\ /|\\ /|\\ /|\\ /|\\ /|\\ ", cor_adv)}  ← TORCIDA
      {colorir(" / \\ / \\ / \\ / \\ / \\ / \\ ", cor_seu)} {colorir(" / \\ / \\ / \\ / \\ / \\ / \\ ", cor_adv)}  (90.000 pessoas)


      ┌──────────────────────────────────┐
      │ {colorir("  O    O    O    O    O  ", cor_seu)}        │
      │ {colorir(" /|\\  /|\\  /|\\  /|\\  /|\\ ", cor_seu)}        │  ← COMPANHEIROS
      │ {colorir(" / \\  / \\  / \\  / \\  / \\ ", cor_seu)}        │
      │                                  │
      │        {colorir("O  ← VOCÊ (Estreia!)", cor_seu)}      │
      │       {colorir("/|\\", cor_seu)}                        │
      │       {colorir("/ \\", cor_seu)}                        │
      └──────────────────────────────────┘
    """)
    input_digitado("  >>> Pressione ENTER para começar a FINAL... <<<")
    print()


linha("█", 56, C_VERDE)
digitar(colorir("█" + "  COPA DO MUNDO 2026 — O JOGO  ".center(54) + "█", C_VERDE), delay=0.01)
linha("█", 56, C_VERDE)
print()


while True:
    nome = input_digitado("  Qual é o seu nome, jogador? ").strip()
    if nome:
        break
    digitar(colorir("  ⚠ Por favor, digite um nome para continuar.", C_VERMELHO))
    print()


while True:
    numero = input_digitado("  Qual número de camisa você quer usar? (1-99) ").strip()
    if numero.isdigit() and 1 <= int(numero) <= 99:
        break
    digitar(colorir("  ⚠ Número inválido! Digite um número entre 1 e 99.", C_VERMELHO))
    print()


print()
linha()
digitar("  Em qual posição você joga?")
print()
digitar("    " + colorir("[ 1 ]", C_AMARELO + C_BOLD) + colorir(" Goleiro     ", C_AMARELO) + colorir("(GOL)", C_AMARELO))
digitar("    " + colorir("[ 2 ]", C_AZUL + C_BOLD) + colorir(" Defensor    ", C_AZUL) + colorir("(ZAG/LAT)", C_AZUL))
digitar("    " + colorir("[ 3 ]", C_ROXO + C_BOLD) + colorir(" Meio-Campo  ", C_ROXO) + colorir("(MEI/VOL)", C_ROXO))
digitar("    " + colorir("[ 4 ]", C_VERMELHO + C_BOLD) + colorir(" Atacante    ", C_VERMELHO) + colorir("(ATA)", C_VERMELHO))
print()


while True:
    pos_escolha = input_digitado(colorir("  ▶ Escolha de 1 a 4: ", C_BRANCO)).strip()
    if pos_escolha in ("1", "2", "3", "4"):
        break
    digitar(colorir("  ⚠ Opção inválida! Digite apenas 1, 2, 3 ou 4.", C_VERMELHO))
    print()


idx_substituicao = 10
if pos_escolha == "1":
    idx_substituicao = 0
elif pos_escolha == "2":
    idx_substituicao = 2
elif pos_escolha == "3":
    idx_substituicao = 6


print()
linha()
digitar("  Escolha sua seleção:")
print()


while True:
    digitar("    " + colorir("[ 1 ]", C_AMARELO + C_BOLD) + colorir(" Brasil", C_AMARELO))
    digitar("    " + colorir("[ 2 ]", C_AZUL + C_BOLD) + colorir(" Argentina", C_AZUL))
    print()
    time_escolha = input_digitado(colorir("  ▶ Digite 1 ou 2: ", C_BRANCO)).strip()


    if time_escolha == "1":
        seu_time = "Brasil"
        adversario = "Argentina"
        seus_titulares = TITULARES_BRASIL[:]
        adv_titulares = TITULARES_ARGENTINA[:]
        seu_goleiro = "Alisson" if idx_substituicao != 0 else nome
        goleiro_adv = "Emiliano Martínez"
        COR_SEU = C_AMARELO
        COR_ADV = C_AZUL
        seus_titulares[idx_substituicao] = nome
        seus_batedores = [nome, "Vinícius Júnior", "Raphinha", "Neymar",
                          "Lucas Paquetá", "Gabriel Martinelli", "Casemiro",
                          "Bruno Guimarães", "Matheus Cunha", "Marquinhos", "Danilo"]
        adv_batedores = ["Lionel Messi", "Lautaro Martínez", "Julián Álvarez",
                         "Mac Allister", "De Paul", "Garnacho", "Enzo Fernández",
                         "Nico González", "Mastantuono", "Molina", "Otamendi"]
        break
    elif time_escolha == "2":
        seu_time = "Argentina"
        adversario = "Brasil"
        seus_titulares = TITULARES_ARGENTINA[:]
        adv_titulares = TITULARES_BRASIL[:]
        seu_goleiro = "Emiliano Martínez" if idx_substituicao != 0 else nome
        goleiro_adv = "Alisson"
        COR_SEU = C_AZUL
        COR_ADV = C_AMARELO
        seus_titulares[idx_substituicao] = nome
        seus_batedores = [nome, "Lionel Messi", "Lautaro Martínez", "Julián Álvarez",
                          "Mac Allister", "De Paul", "Garnacho", "Enzo Fernández",
                          "Nico González", "Mastantuono", "Molina"]
        adv_batedores = ["Vinícius Júnior", "Raphinha", "Neymar", "Lucas Paquetá",
                         "Gabriel Martinelli", "Casemiro", "Bruno Guimarães",
                         "Matheus Cunha", "Marquinhos", "Danilo", "Endrick"]
        break
    else:
        digitar(colorir("  ⚠ Opção inválida! Digite apenas 1 ou 2.", C_VERMELHO))
        print()


cena_escalacao(nome, numero, seu_time, adversario, seus_titulares,
               goleiro_adv, COR_SEU, COR_ADV)


linha()
digitar(colorir(f"  ✅ {nome} está em campo pelo {seu_time}!", COR_SEU))
digitar(f"  🏆 A FINAL DA COPA DO MUNDO contra a {adversario} começou!")
time.sleep(1)


linha()
digitar("  ⏱ 88 MINUTOS — PLACAR: 1 x 1")
time.sleep(0.5)


craque_adv = adv_batedores[0]


if pos_escolha == "1":
    digitar(f"  Contra-ataque mortal da {adversario}! A zaga falhou!")
    time.sleep(0.5)
    digitar(f"  {craque_adv} sai cara a cara com você, {nome}!")
    time.sleep(0.5)
    digitar(f"  Ele arma o chute... É a defesa da sua vida!")


    escolha_acao = escolher_lado(f"\n  Para qual lado você pula para defender o chute de {craque_adv}?")
    boneco_goleiro(nome, escolha_acao, COR_SEU)
    digitar(f"  {craque_adv} bate firme na bola...")
    time.sleep(1.5)


    if escolha_acao == "esquerda":
        cena_defesa(nome, COR_SEU)
        digitar(colorir(f"  MILAGRE DE {nome.upper()}!!! Espalmou no reflexo puro!", C_VERDE))
        time.sleep(0.8)
        digitar(f"  Você lança a bola rápido, armando o contra-ataque pro {seu_time}...")
        time.sleep(1.2)
        cena_gol("Ataque do seu time", COR_SEU, "G O L  DA  V I T Ó R I A !")
        sucesso_tempo_normal = True
    else:
        cena_gol(craque_adv, COR_ADV)
        digitar(colorir(f"  GOOOL da {adversario}... {craque_adv} tirou de você.", C_VERMELHO))
        time.sleep(1)
        digitar("  Mas espere... O BANDEIRINHA DEU IMPEDIMENTO!!!")
        time.sleep(1.2)
        colorir_var = colorir("  O VAR CONFIRMA! GOL ANULADO! Que alívio...", C_AMARELO)
        digitar(colorir_var)
        sucesso_tempo_normal = False


elif pos_escolha == "2":
    digitar(f"  Último escanteio do jogo para o {seu_time}!")
    time.sleep(0.5)
    digitar(f"  Você ({nome}) é forte no jogo aéreo e vai pra área tentar o milagre.")
    time.sleep(0.5)
    digitar(f"  A bola viaja na área, você se livra da marcação...")


    escolha_acao = escolher_lado("\n  Para qual lado você tenta cabecear?")
    boneco_jogada(nome, escolha_acao, COR_SEU, "CABECEIO")
    digitar(f"  {nome} sobe mais alto que todo mundo...")
    time.sleep(1.5)


    if escolha_acao == "direita":
        cena_gol(nome, COR_SEU)
        digitar(colorir(f"  GOLAÇOOOOOOOO!!! Testa firme pro fundo do gol!", C_VERDE))
        sucesso_tempo_normal = True
    else:
        cena_trave()
        digitar(colorir(f"  NA TRAVE! O goleiro {goleiro_adv} já estava batido!", C_VERMELHO))
        sucesso_tempo_normal = False


elif pos_escolha == "3":
    digitar(f"  Falta perigosa na entrada da área para o {seu_time}.")
    time.sleep(0.5)
    digitar(f"  {nome}, o cérebro do time, pega a bola. A barreira está se formando...")
    time.sleep(0.5)
    digitar(f"  O goleiro {goleiro_adv} orienta a zaga. É agora ou nunca.")


    escolha_acao = escolher_lado("\n  Para qual canto você vai bater a falta?")


    cena_barreira(nome, goleiro_adv, escolha_acao, COR_SEU, COR_ADV)
    time.sleep(1.5)


    if escolha_acao == "direita":
        cena_gol(nome, COR_SEU)
        digitar(colorir(f"  GOLAÇOOOOOOOO!!! No ângulo, onde a coruja dorme!", C_VERDE))
        sucesso_tempo_normal = True
    else:
        boneco_goleiro(goleiro_adv, "esquerda", COR_ADV)
        digitar(colorir(f"  {goleiro_adv} VOOU E DEFENDEU!!! Que defesa espetacular!", C_VERMELHO))
        sucesso_tempo_normal = False


else:  # pos_escolha == "4"
    digitar(f"  {nome} recebe na área, dribla o adversário e é derrubado... PÊNALTI!")
    time.sleep(0.5)
    digitar(f"  O árbitro aponta para a marca da cal. É a chance de decidir o jogo agora!")


    escolha_acao = escolher_lado("\n  Para onde você bate o pênalti decisivo?")
    boneco_jogada(nome, escolha_acao, COR_SEU, "PÊNALTI")
    digitar(f"  {nome} corre em direção à bola...")
    time.sleep(1.5)


    if escolha_acao == "direita":
        cena_gol(nome, COR_SEU)
        digitar(colorir(f"  GOLAÇOOOOOOOO!!! {nome} desloca o goleiro com perfeição!", C_VERDE))
        sucesso_tempo_normal = True
    else:
        cena_trave()
        digitar(colorir(f"  NA TRAVE! Que crueldade! A bola explode no poste.", C_VERMELHO))
        sucesso_tempo_normal = False


if sucesso_tempo_normal:
    time.sleep(1.5)
    linha("═", 56, C_AMARELO)
    desenhar_arte(colorir("""
  ██████████████████████████████████████████████████████
         \\O/   \\O/   \\O/   \\O/   \\O/
          |     |     |     |     |    O JOGO ACABOU!!!
         / \\   / \\   / \\   / \\   / \\
  ██████████████████████████████████████████████████████
    """, COR_SEU))
    digitar(f"  O ÁRBITRO APITA! FIM DE JOGO!!! {seu_time} 2 x 1 {adversario}!")
    time.sleep(1.5)
    if seu_time == "Brasil":
        digitar(colorir(f"  🇧🇷 O BRASIL É HEXACAMPEÃO DO MUNDO!!! 🇧🇷", C_AMARELO))
        time.sleep(0.8)
        digitar(f"  Você foi o herói absoluto do título aos 88 minutos!")
        digitar(f"  Seus companheiros pulam em cima de você! O estádio vai abaixo!")
        time.sleep(1.2)
        digitar(colorir(f"  Feriado nacional é decretado imediatamente no Brasil!", C_VERDE))
        digitar(colorir(f"  Você acaba de se tornar uma LENDA IMORTAL da nação brasileira!", C_AMARELO))
    else:
        digitar(colorir(f"  🇦🇷 A ARGENTINA É CAMPEÃ DO MUNDO!!! 🇦🇷", C_AZUL))
        time.sleep(0.8)
        digitar(f"  Você consagrou a vitória heróica aos 88 minutos!")
        digitar(f"  Você se consagra para sempre na história, adorado por todo o seu país!")


    print()
    linha("═")
    digitar("  Obrigado por jogar!  ⚽  Copa do Mundo 2026")
    linha("═")
    sys.exit()


else:
    linha()
    time.sleep(1.5)
    digitar(f"  O árbitro apita o final do tempo normal e da prorrogação.")
    digitar(f"  O placar termina empatado em 1 a 1.")
    digitar(colorir("  🏆  A FINAL VAI PARA A DISPUTA DE PÊNALTIS!!!", C_AMARELO))


linha()
digitar("  ⚽⚽⚽  DISPUTA DE PÊNALTIS — FINAL DA COPA  ⚽⚽⚽")
linha()
time.sleep(1.5)


seus_gols = 0
gols_adv = 0


padrao_chute_adv = ["esquerda", "direita", "esquerda", "direita", "esquerda",
                    "direita", "esquerda", "direita", "esquerda", "direita"]
padrao_pulo_adv = ["direita", "esquerda", "direita", "esquerda", "direita",
                   "esquerda", "direita", "esquerda", "direita", "esquerda"]


rodada = 0
morte_subita = False


while True:
    if not morte_subita and rodada < 5:
        cobrancas_restantes = 5 - rodada
        if (seus_gols + cobrancas_restantes < gols_adv or
                gols_adv + cobrancas_restantes < seus_gols):
            break


    campo_ascii(seu_time, seus_gols, adversario, gols_adv)
    linha("-")


    if morte_subita:
        digitar(colorir(f"  🔁 MORTE SÚBITA — Rodada {rodada + 1}", C_AMARELO))
    else:
        digitar(f"  📋 Rodada {rodada + 1} de 5")
    linha("-")


    idx_seu = rodada % len(seus_batedores)
    batedor = seus_batedores[idx_seu]


    print()
    digitar(colorir(f"  🔵 Seu batedor: {batedor}", COR_SEU))
    if batedor == nome:
        digitar(colorir(f"  ⭐ É VOCÊ, {nome}! A chance de ser herói!", C_AMARELO))


    escolha = escolher_lado("\n  Para onde você quer bater?")
    boneco_jogada(batedor, escolha, COR_SEU, "PÊNALTI")
    digitar(f"  {batedor} corre para a bola...")
    time.sleep(1.5)


    pulo_goleiro = padrao_pulo_adv[rodada % len(padrao_pulo_adv)]


    if escolha != pulo_goleiro:
        cena_gol(batedor, COR_SEU)
        seus_gols += 1
    else:
        cena_defesa(goleiro_adv, COR_ADV)


    linha("-")
    digitar(f"  PLACAR PÊNALTIS: {seu_time} {seus_gols} x {gols_adv} {adversario}")
    linha("-")
    time.sleep(1.5)


    idx_adv = rodada % len(adv_batedores)
    cobrador = adv_batedores[idx_adv]


    print()
    digitar(colorir(f"  🔴 Batedor adversário: {cobrador}", COR_ADV))
    digitar(f"  Agora você controla o goleiro {seu_goleiro}!")


    escolha_goleiro = escolher_lado("\n  Para qual lado você pula?")
    lado_chute_adv = padrao_chute_adv[rodada % len(padrao_chute_adv)]
    boneco_jogada(cobrador, lado_chute_adv, COR_ADV, "PÊNALTI")
    digitar(f"  {cobrador} corre para a bola...")
    time.sleep(1.5)


    if escolha_goleiro == lado_chute_adv:
        cena_defesa(seu_goleiro, COR_SEU)
    else:
        cena_gol(cobrador, COR_ADV)
        gols_adv += 1


    linha("-")
    digitar(f"  PLACAR PÊNALTIS: {seu_time} {seus_gols} x {gols_adv} {adversario}")
    linha("-")
    time.sleep(1.5)


    rodada += 1


    if not morte_subita:
        if rodada >= 5:
            if seus_gols != gols_adv:
                break
            else:
                linha()
                digitar(colorir("  ⚡ Empatados após 5 cobranças!", C_AMARELO))
                digitar(colorir("  🔁 MORTE SÚBITA! Quem errar agora, perde.", C_VERMELHO))
                morte_subita = True
    else:
        if seus_gols != gols_adv:
            break


campo_ascii(seu_time, seus_gols, adversario, gols_adv)
linha("═")


if seus_gols > gols_adv:
    desenhar_arte(colorir("""
  ██████████████████████████████████████████████████████
               \\O/   \\O/   \\O/   \\O/
                |     |     |     |     CAMPEÕES!!!
               / \\   / \\   / \\   / \\
  ██████████████████████████████████████████████████████
    """, COR_SEU))
    digitar(colorir(f"  🏆 {seu_time.upper()} É CAMPEÃO DA COPA DO MUNDO 2026!!!", C_AMARELO))
    time.sleep(0.8)
    digitar(f"  Apesar do sufoco no tempo normal, {nome} solta o grito de campeão!")
    time.sleep(0.8)
    digitar("  A torcida invade o gramado, confete por todo lado...")
    time.sleep(1)
    digitar(f"  {nome} levanta o troféu. Lágrimas no rosto.")
else:
    desenhar_arte(colorir("""
  😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢
           O      O      O      O
          /|\\    /|\\    /|\\    /|\\    
          / \\    / \\    / \\    / \\
  😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢😢
    """, COR_SEU))
    digitar(colorir("  Seu time perdeu a final nos pênaltis...", C_VERMELHO))
    time.sleep(0.8)
    digitar(colorir(f"  {adversario} é campeão do mundo.", COR_ADV))
    time.sleep(0.8)
    digitar(f"  O lance falhado no tempo normal vai assombrar {nome} por um tempo.")
    time.sleep(1)
    digitar("  A dor é imensa. Mas a carreira não acaba aqui.")


linha("═")
print()
digitar("  Obrigado por jogar!  ⚽  Copa do Mundo 2026")
linha("═")


