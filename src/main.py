from core.energy_core import EnergyCore

from observer.shield import Shield
from observer.lights import Lights
from observer.panel import Panel


core = EnergyCore()

shield = Shield()

lights = Lights()

panel = Panel()

core.add_observer(shield)

core.add_observer(lights)

core.add_observer(panel)

core.reduce_energy(30)

core.reduce_energy(50)