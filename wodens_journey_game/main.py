"""
- Corregir que siempre se está dando golpes críticos.
- Corregir que no se pasa bien de un efecto elemental a otro.
- Corregir que no se toman bien los valores para los efectos.
- En la función de efecto y ataque se deben de estar pasando los valores erradamente.
"""

from Battle.Battle import Battle


def main():
    print("*** Stats de batalla ***")

    print(" ")

    hero_name = input("Nombre del heroe: ")
    hero_life = int(input("PS del heroe: "))
    hero_damage = int(input("PD del heroe: "))
    hero_elemental_damage = int(input("PD Elemental del heroe: "))
    hero_critic_damage = int(input("PD Crítico del heroe: "))
    hero_critic_prob = int(input("Probabilidad de golpe crítico del heroe: "))
    hero_miss_prob = int(input("Probabilidad de fallar del heroe: "))

    print(" ")

    enemy_name = input("Nombre del enemy: ")
    enemy_life = int(input("PS del enemy: "))
    enemy_damage = int(input("PD del enemy: "))
    enemy_elemental_damage = int(input("PD Elemental del enemy: "))
    enemy_critic_damage = int(input("PD Crítico del enemy: "))
    enemy_critic_prob = int(input("Probabilidad de golpe crítico del enemy: "))
    enemy_miss_prob = int(input("Probabilidad de fallar del enemy: "))

    battle = Battle(
        hero_name,
        hero_life,
        hero_damage,
        hero_elemental_damage,
        hero_critic_damage,
        hero_critic_prob,
        hero_miss_prob,
        enemy_name,
        enemy_life,
        enemy_damage,
        enemy_elemental_damage,
        enemy_critic_damage,
        enemy_critic_prob,
        enemy_miss_prob
    )

    battle.battle_start()


if __name__ == "__main__":
    main()
