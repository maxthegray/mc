import random
import time

# connect to minecraft 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for _ in range(10):
    x = random.randint(-120, 120)
    y = random.randint(8, 120)
    z = random.randint(-120, 120)
    mc.player.setTilePos(x, y, z)
    time.sleep(4)

# set x. y, and z variables to represent coordinates
x = 86.7
y = 0.0
z = -43.1

#change the player's position
mc.player.setPos(x, y, z)

