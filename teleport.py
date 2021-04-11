import time

# connect to minecraft 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# set x. y, and z variables to represent coordinates
x = 86.7
y = 0.0
z = -43.1

#change the player's position
mc.player.setPos(x, y, z)

