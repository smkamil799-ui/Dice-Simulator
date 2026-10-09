import random
def roll_dice (sides=6):
	return random.randint(1, sides)
rounds = int(input("how many rounds ? "))
target = int(input("target score to reach :"))
total = 0
history = []
round_num = 0
while total < target and round_num < rounds:
      roll = roll_dice()
      total += roll
      round_num += 1
      history.append(roll)
print(f"Rounds played: {round_num}, final score: {total}")
if total >= target:
      print("Target reached!")
else:
      print(f"\nOut of rounds! Final score: {total}")
print(f"Rolls: {history}")



	
	