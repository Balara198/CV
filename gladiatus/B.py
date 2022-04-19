import random

def bejon(sansz):
    return random.random()<sansz

pont = 24
dupla_pont = 0
xp_bonus = 1.6
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
    if not i%10:
        print(f"{elem[1]}".split(".")[0])
