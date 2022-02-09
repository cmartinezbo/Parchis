# Libraries
from random import randint
from os import system
from time import sleep
from termcolor import colored


def clear():
    system('cls')


def dices():
    enter = input(f'\nPresione ENTER para lanzar los dados')
    dice_1 = 0
    dice_2 = 0
    total_dice = 0

    if enter == "":
        print('Lanzando dados...')
        sleep(1.5)
        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        total_dice = dice_1 + dice_2
    return dice_1, dice_2, total_dice


def dices_desarrollador():
    dice_1 = int(input('Digite el valor del primer dado: '))
    dice_2 = int(input('Digite el valor del segundo dado: '))
    total_dice = dice_1 + dice_2

    return dice_1, dice_2, total_dice


def show_dices(d1, d2, td):
    print(f'\nDice #1: {d1}\nDice #2: {d2}\nTotal Dices: {td}\n')


def board():
    return 68


def player_1():
    piece_1 = 0

    return piece_1


def player_2():
    piece_2 = 0

    return piece_2


def exit_jail(dice_1, dice_2, total_dices):
    if total_dices == 5 or dice_1 == 5 or dice_2 == 5:
        return True
    else:
        return False


def save_place():
    return [1, 8, 13, 18, 25, 30, 35, 42, 47, 52, 59, 64]


def check_jail_p1(p1):
    if p1 == 0:
        return True
    else:
        return False


def check_jail_p2(p2):
    if p2 == 0:
        return True
    else:
        return False


def move_pieces(piece, dice):
    piece += dice
    return piece


def check_pairs(d1, d2):
    if d1 == d2:
        return True
    else:
        return False


def p1_jail(p1):
    p1 = 0
    return p1


def p1_start(p1):
    p1 = 1
    return p1


'''
def p2_start(p2):
    p2 = 35
    return p2


def p2_jail(p2):
    p2 = 100
    return p2
'''


def check_same_place(p1, p2):
    if p1 == p2:
        return True
    else:
        return False


def check_goal(piece, goal):
    if piece == goal:
        return True
    else:
        return False


def remaining_1(p1, goal_1):
    if p1 >= goal_1:
        return 72 - p1
    else:
        return None


def remaining_2(p2, goal_2):
    if p2 >= goal_2:
        return 38 - p2
    else:
        return None


def dev_players(player, p1, p2):
    ganador = 0

    # Asigna las metas para los jugadores
    p1_goal = 60
    p2_goal = 26

    # Asigna inicio para los jugadores
    p1_begin = 1
    p2_begin = 35

    # Asigna cárcel para los jugadores
    p1_prison = 0
    p2_prison = 0

    vueltas = 0

    # Faltantes Meta
    rp1 = remaining_1(p1, p1_goal)
    rp2 = remaining_2(p2, p2_goal)

    # Tira y asigna dados
    d1, d2, td = dices()

    # Muestra resultado dados
    show_dices(d1, d2, td)

    # Muestra posición ficha según el jugador antes de avanzar

    if player == 'Jugador 1':
        if p1 < p1_goal:
            print(f'Before moving, your position is: {p1}')
        else:
            print(f'Positions Remaining: {rp1}')
    elif player == 'Jugador 2':
        if not vueltas:
            print(f'Before moving, your position is: {p2}')
        elif vueltas:
            if p2 < p2_goal:
                print(f'Before moving, your position is: {p2}')
            else:
                print(f'Positions Remaining: {rp2}')

    # Revisa si la ficha está en la cárcel según el jugador
    if player == 'Jugador 1':
        if check_jail_p1(p1):
            # Revisa si la ficha puede salir de la cárcel
            if exit_jail(d1, d2, td):
                p1 = p1_begin  # Mueve la ficha al inicio
                if check_same_place(p1, p2):  # Si hay alguien en el inicio se lo come
                    p2 = p2_prison
                else:
                    pass  # Pasa turno
            else:
                pass
        else:
            # Revisa si está en la etapa final
            if p1 >= p1_goal:
                if td == rp1:  # Si el total de de dados es igual al remaining, gana
                    print(f'{player}, has ganado, ez win, gg no team')
                    ganador = 1
                elif td > rp1:  # Si el total de dados es mayor, analiza cada dado
                    if d1 <= rp1:
                        p1 += d1
                        if d1 == rp1:  # Si el total de de dados es igual al remaining, gana
                            print(f'{player}, has ganado, ez win, gg no team')
                            ganador = 1
                    elif d2 <= rp1:
                        p1 += d2
                        if d2 == rp1:  # Si el total de de dados es igual al remaining, gana
                            print(f'{player}, has ganado, ez win, gg no team')
                            ganador = 1
                    else:
                        pass  # Pasa turno
                else:  # Mueve los dados libremente
                    p1 += td
            else:
                p1 += td

    elif 'Jugador 2':
        if check_jail_p2(p2):
            # Revisa si la ficha puede salir de la cárcel
            if exit_jail(d1, d2, td):
                p2 = p2_begin  # Mueve la ficha al inicio
                if check_same_place(p1, p2):  # Si hay alguien en el inicio se lo come
                    p1 = p1_prison
                else:
                    pass  # Pasa turno
            else:
                pass
        else:
            # Revisa si está en la etapa final
            if vueltas:

                if p2 >= p2_goal:
                    if td == rp2:  # Si el total de de dados es igual al remaining, gana
                        print(f'{player}, has ganado, ez win, gg no team')
                        ganador = 1
                    elif td > rp2:  # Si el total de dados es mayor, analiza cada dado
                        if d1 <= rp2:
                            p2 += d1
                            if d1 == rp2:  # Si el total de de dados es igual al remaining, gana
                                print(f'{player}, has ganado, ez win, gg no team')
                                ganador = 1
                        elif d2 <= rp2:
                            p2 += d2
                            if d2 == rp2:  # Si el total de de dados es igual al remaining, gana
                                print(f'{player}, has ganado, ez win, gg no team')
                                ganador = 1
                        else:
                            pass  # Pasa turno
                    else:  # Mueve los dados libremente
                        p2 += td
            else:
                p2 += td

    if p2 > 68:
        vueltas = 1
        p2 -= 68

    rp1 = remaining_1(p1, p1_goal)
    rp2 = remaining_2(p2, p2_goal)

    # Muestra posición ficha según el jugador despues de avanzar
    if player == 'Jugador 1':
        if p1 < p1_goal:
            print(f'After moving, your position is: {p1}')
        else:
            print(f'Positions Remaining: {rp1}')
    elif player == 'Jugador 2':
        if not vueltas:
            print(f'After moving, your position is: {p2}')
        elif vueltas:
            if p2 < p2_goal:
                print(f'After moving, your position is: {p2}')
            else:
                print(f'Positions Remaining: {rp2}')

    return p1, p2, ganador


def dev_desarrollador(player, p1, p2):
    ganador = 0

    # Asigna las metas para los jugadores
    p1_goal = 60
    p2_goal = 26

    # Asigna inicio para los jugadores
    p1_begin = 1
    p2_begin = 35

    # Asigna cárcel para los jugadores
    p1_prison = 0
    p2_prison = 0

    vueltas = 0

    # Faltantes Meta
    rp1 = remaining_1(p1, p1_goal)
    rp2 = remaining_2(p2, p2_goal)

    # Tira y asigna dados
    d1, d2, td = dices_desarrollador()

    # Muestra resultado dados
    show_dices(d1, d2, td)

    # Muestra posición ficha según el jugador antes de avanzar

    if player == 'Jugador 1':
        if p1 < p1_goal:
            print(f'Before moving, your position is: {p1}')
        else:
            print(f'Positions Remaining: {rp1}')
    elif player == 'Jugador 2':
        if not vueltas:
            print(f'Before moving, your position is: {p2}')
        elif vueltas:
            if p2 < p2_goal:
                print(f'Before moving, your position is: {p2}')
            else:
                print(f'Positions Remaining: {rp2}')

    # Revisa si la ficha está en la cárcel según el jugador
    if player == 'Jugador 1':
        if check_jail_p1(p1):
            # Revisa si la ficha puede salir de la cárcel
            if exit_jail(d1, d2, td):
                p1 = p1_begin  # Mueve la ficha al inicio
                if check_same_place(p1, p2):  # Si hay alguien en el inicio se lo come
                    p2 = p2_prison
                else:
                    pass  # Pasa turno
            else:
                pass
        else:
            # Revisa si está en la etapa final
            if p1 >= p1_goal:
                if td == rp1:  # Si el total de de dados es igual al remaining, gana
                    print(f'{player}, has ganado, ez win, gg no team')
                    ganador = 1
                elif td > rp1:  # Si el total de dados es mayor, analiza cada dado
                    if d1 <= rp1:
                        p1 += d1
                        if d1 == rp1:  # Si el total de de dados es igual al remaining, gana
                            print(f'{player}, has ganado, ez win, gg no team')
                            ganador = 1
                    elif d2 <= rp1:
                        p1 += d2
                        if d2 == rp1:  # Si el total de de dados es igual al remaining, gana
                            print(f'{player}, has ganado, ez win, gg no team')
                            ganador = 1
                    else:
                        pass  # Pasa turno
                else:  # Mueve los dados libremente
                    p1 += td
            else:
                p1 += td

    elif 'Jugador 2':
        if check_jail_p2(p2):
            # Revisa si la ficha puede salir de la cárcel
            if exit_jail(d1, d2, td):
                p2 = p2_begin  # Mueve la ficha al inicio
                if check_same_place(p1, p2):  # Si hay alguien en el inicio se lo come
                    p1 = p1_prison
                else:
                    pass  # Pasa turno
            else:
                pass
        else:
            # Revisa si está en la etapa final
            if vueltas:

                if p2 >= p2_goal:
                    if td == rp2:  # Si el total de de dados es igual al remaining, gana
                        print(f'{player}, has ganado, ez win, gg no team')
                        ganador = 1
                    elif td > rp2:  # Si el total de dados es mayor, analiza cada dado
                        if d1 <= rp2:
                            p2 += d1
                            if d1 == rp2:  # Si el total de de dados es igual al remaining, gana
                                print(f'{player}, has ganado, ez win, gg no team')
                                ganador = 1
                        elif d2 <= rp2:
                            p2 += d2
                            if d2 == rp2:  # Si el total de de dados es igual al remaining, gana
                                print(f'{player}, has ganado, ez win, gg no team')
                                ganador = 1
                        else:
                            pass  # Pasa turno
                    else:  # Mueve los dados libremente
                        p2 += td
            else:
                p2 += td

    if p2 > 68:
        vueltas = 1
        p2 -= 68

    rp1 = remaining_1(p1, p1_goal)
    rp2 = remaining_2(p2, p2_goal)

    # Muestra posición ficha según el jugador despues de avanzar
    if player == 'Jugador 1':
        if p1 < p1_goal:
            print(f'After moving, your position is: {p1}')
        else:
            print(f'Positions Remaining: {rp1}')
    elif player == 'Jugador 2':
        if not vueltas:
            print(f'After moving, your position is: {p2}')
        elif vueltas:
            if p2 < p2_goal:
                print(f'After moving, your position is: {p2}')
            else:
                print(f'Positions Remaining: {rp2}')

    return p1, p2, ganador


def partida_rapida():
    players = ['Jugador 1', 'Jugador 2']

    # Asigna fichas jugadores
    p1 = player_1()
    p2 = player_2()

    while True:
        for i in players:
            print(f'\n{i}')
            p1, p2, ganador = dev_players(i, p1, p2)
            if ganador == 1:
                break


def modo_desarrollador():
    players = ['Jugador 1', 'Jugador 2']

    # Asigna fichas jugadores
    p1 = player_1()
    p2 = player_2()

    while True:
        for i in players:
            print(f'\n{i}')
            p1, p2, ganador = dev_desarrollador(i, p1, p2)
            if ganador == 1:
                break


def main():
    print(colored("BIENVENIDO AL PARQUÉS ULTIMATE\n{:^31}".format("made by Cristian\n"), "cyan"))

    opcion = int(input("¿Qué modo desea utulizar? ¿Partida rápida [1] ó Modo desarrollador [2]? "))

    if opcion == 1:
        partida_rapida()
    else:
        modo_desarrollador()

main()