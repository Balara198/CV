import random

def bejon(sansz):
    return random.random()<sansz

avg = [[0,0] for i in range(6000)]

for idx in range(1000):

    pont = 36
    dupla_pont = 0.1
    xp_bonus = 1.3
    xp = 0
    i = 0
    perc = []
    pont_to_xp = 11.875

    while True:
        if xp >= 10000:
            break
        if not i%10:
            pont += 1
        if pont > 0:
            pont -= 1-bejon(dupla_pont)
            xp += pont_to_xp*xp_bonus
        perc.append((pont,xp))
        i += 1
    for i, elem in enumerate(perc):
        #avg[i] = (avg[i]*idx+elem[1])/(idx+1)
        avg[i][0] = (avg[i][1]*avg[i][0]+elem[1])/(avg[i][1]+1)
        avg[i][1] += 1
        
    
for i, elem in enumerate(avg):
    if not i%10:
        print(f"{i}. perc:  {elem[0]}")

