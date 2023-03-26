import mouse

mouse.move(10**5, 10**5)

print(tuple(i/2 for i in mouse.get_position()))
