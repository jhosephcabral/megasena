import random

nums = int(input("Quando números deseja apostar? : "))

for i in range(1, nums+1):
    print("Número sorteado: ", random.randint(1, 60))