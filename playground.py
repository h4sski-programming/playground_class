from character import Character

npc_01 = Character('npc_01', 10, [10, 10])

print(npc_01.position)
npc_01.move([2, -4])
print(npc_01.position)

print(npc_01.distance_to([14, 3]))

npc_01.take_dmg(2)
print(npc_01.alive)

a = ['1', '2', '3']
b = [1, 2, 3]
c = zip(a, b)
print(c)