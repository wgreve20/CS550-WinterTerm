from Die import Dice


dice1 = Dice(6)

for i in range(15):
	print(dice1.roll())

print('Break')
print(dice1.roll())
print(dice1.roll())