# Main game file:
# Projeto Básico de Python, Praticando Uso do Pygame
# Pedra, Papel e Tesoura com Pygame e interface

# 0. Bibliotecas do Projeto
import random
import sys
import pygame

# 1. Inicialização do Pygame
pygame.init()
LARGURA, ALTURA = 1200, 800
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pedra, Papel e Tesoura")
font = pygame.font.SysFont("arial", 28)

# 2. Variáveis do Jogo
opcoes = ["Pedra", "Papel", "Tesoura"]
placar_jogador = 0
placar_pc = 0
resultado = "Clique no botão para jogar!"

# 3. Criar os Botões Centralizados (Largura: 160px, Altura: 60px)
LARGURA_BTN, ALTURA_BTN = 160, 60
POS_Y_BTN = 450

btn_pedra = pygame.Rect(270, POS_Y_BTN, LARGURA_BTN, ALTURA_BTN)
btn_papel = pygame.Rect(520, POS_Y_BTN, LARGURA_BTN, ALTURA_BTN)
btn_tesoura = pygame.Rect(770, POS_Y_BTN, LARGURA_BTN, ALTURA_BTN)


# 4. Função para saber quem ganhou
def jogar(escolha_jogador):
    global placar_jogador, placar_pc, resultado

    escolha_pc = random.choice(opcoes)

    if escolha_jogador == escolha_pc:
        resultado = f"Empate! O adversário escolheu {escolha_pc}."
    elif (
        (escolha_jogador == "Pedra" and escolha_pc == "Tesoura")
        or (escolha_jogador == "Papel" and escolha_pc == "Pedra")
        or (escolha_jogador == "Tesoura" and escolha_pc == "Papel")
    ):
        resultado = f"Ganhou! O adversário escolheu {escolha_pc}."
        placar_jogador += 1
    else:
        resultado = f"Perdeu! O adversário escolheu {escolha_pc}."
        placar_pc += 1


# 5. Loop Principal do Jogo
rodando = True
while rodando:
    screen.fill((30, 30, 30))  # Fundo cinza escuro

    # Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_pedra.collidepoint(event.pos):
                jogar("Pedra")
            elif btn_papel.collidepoint(event.pos):
                jogar("Papel")
            elif btn_tesoura.collidepoint(event.pos):
                jogar("Tesoura")

    # Desenhar o Placar Centralizado
    texto_placar = font.render(
        f"Jogador: {placar_jogador}  |  PC: {placar_pc}", True, (255, 255, 255)
    )
    rect_placar = texto_placar.get_rect(center=(LARGURA // 2, 100))
    screen.blit(texto_placar, rect_placar)

    # Desenhar o Resultado Centralizado
    texto_res = font.render(resultado, True, (255, 215, 0))
    rect_res = texto_res.get_rect(center=(LARGURA // 2, 250))
    screen.blit(texto_res, rect_res)

    # Desenhar os Botões
    pygame.draw.rect(screen, (70, 130, 180), btn_pedra, border_radius=8)
    pygame.draw.rect(screen, (70, 130, 180), btn_papel, border_radius=8)
    pygame.draw.rect(screen, (70, 130, 180), btn_tesoura, border_radius=8)

    # Centralizar Textos Dentro de Cada Botão
    txt_pedra = font.render("Pedra", True, (255, 255, 255))
    txt_papel = font.render("Papel", True, (255, 255, 255))
    txt_tesoura = font.render("Tesoura", True, (255, 255, 255))

    screen.blit(txt_pedra, txt_pedra.get_rect(center=btn_pedra.center))
    screen.blit(txt_papel, txt_papel.get_rect(center=btn_papel.center))
    screen.blit(txt_tesoura, txt_tesoura.get_rect(center=btn_tesoura.center))

    pygame.display.flip()

pygame.quit()
sys.exit()