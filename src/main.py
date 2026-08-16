"""
Desafio Técnico - LabTIME 2026

Simulação interativa de uma nave espacial utilizando os padrões
de projeto Observer, State e Decorator.

Comandos disponíveis:

- reduzir_energia
- tomar_dano
- mudar_funcao
- trabalhar
- equipar_arma
- adicionar_modificador
- atirar
"""

from core.energy_core import EnergyCore

from observer.shield import Shield
from observer.lights import Lights
from observer.panel import Panel

from crew.crew_member import CrewMember
from crew.gunner import Gunner
from crew.engineer import Engineer

from ship.spaceship import Spaceship

from weapons.laser import Laser
from weapons.missile import Missile

from weapons.fire import FireDamage
from weapons.armor import ArmorPenetration


def show_menu():
    print("""
==============================
LABTIME - NAVE ESPACIAL
==============================

Observer:
reduzir_energia <valor>
tomar_dano <valor>

State:
mudar_funcao <operador|mecanico>
trabalhar

Decorator:
equipar_arma <laser|misseis>
adicionar_modificador <fogo|perfuracao>
atirar

Outros:
ajuda
sair
""")


core = EnergyCore()

core.add_observer(Shield())
core.add_observer(Lights())
core.add_observer(Panel())

crew = CrewMember(Gunner())

ship = Spaceship()

show_menu()

while True:

    command = input("> ").strip().lower()

    if not command:
        continue

    if command == "sair":
        print("Encerrando o programa...")
        break

    if command == "ajuda":
        show_menu()
        continue

    parts = command.split()

    action = parts[0]

    if action == "reduzir_energia":

        if len(parts) < 2:
            print("Informe um valor.")
            continue

        try:
            value = int(parts[1])
            core.reduce_energy(value)

        except ValueError:
            print("Digite um número válido.")
        
    elif action == "tomar_dano":

        if len(parts) < 2:
            print("Informe um valor.")
            continue

        try:
            damage = int(parts[1])

            core.take_damage(damage)

        except ValueError:
            print("Digite um número válido.")

    elif action == "mudar_funcao":

        if len(parts) < 2:
            print("Informe uma função.")
            continue

        role = parts[1]

        if role == "operador":
            crew.set_state(Gunner())
            print("Função alterada para operador.")

        elif role == "mecanico":
            crew.set_state(Engineer())
            print("Função alterada para mecânico.")

        else:
            print("Função inválida.")

    elif action == "trabalhar":

        crew.work()

    elif action == "equipar_arma":

        if len(parts) < 2:
            print("Informe uma arma.")
            continue

        weapon = parts[1]

        if weapon == "laser":
            ship.equip_weapon(Laser())
            print("Laser equipado.")

        elif weapon == "misseis":
            ship.equip_weapon(Missile())
            print("Enxame de mísseis equipado.")

        else:
            print("Arma inválida.")

    elif action == "adicionar_modificador":

        if ship.weapon is None:
            print("Equipe uma arma primeiro.")
            continue

        if len(parts) < 2:
            print("Informe um modificador.")
            continue

        modifier = parts[1]

        if modifier == "fogo":
            ship.add_modifier(FireDamage)
            print("Dano de fogo adicionado.")

        elif modifier == "perfuracao":
            ship.add_modifier(ArmorPenetration)
            print("Perfuração de blindagem adicionada.")

        else:
            print("Modificador inválido.")

    elif action == "atirar":

        print(ship.shoot())

    else:

        print("Comando inválido. Digite 'ajuda' para ver os comandos.")