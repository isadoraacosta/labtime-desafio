from weapons.decorator import WeaponDecorator

class FireDamage(WeaponDecorator):

    def shoot(self):
        previous_attack = self.weapon.shoot()

        return previous_attack + "\n+ Dano de fogo"