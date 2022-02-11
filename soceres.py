from robot_soccer_python.simulation2D import simulation2D, init_simulation
from robot_soccer_python.agents import Player, Pose
import time

simulation = simulation2D(
    [Player(Pose(3, 3, 0), 2, 2, 0.2),
    Player(Pose(6, 3, 0), 2, 2, 0.2)],
    shockable=True,
    full_vision=False)

now = time.time()
now2 = time.time()
command1 = (0, 0)
command2 = (0, 0)
while True:
    if time.time() - now > 2:
        command1 = (1 + command1[0], 1 + command1[1])
        command2 = (1 + command2[0], - 1 + command2[1])
        now = time.time()
    if time.time() - now2 < 3:
        simulation.set_commands([command1, command2])
    else:
        simulation.set_commands([command2, command1])
        if time.time() - now2 > 5:
            now2 = time.time()
    init_simulation(simulation)
    player_sensors = simulation.get_sensors()