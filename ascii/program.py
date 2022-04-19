import os,time
os.system('cls')
filenames = ['elso.txt','masodik.txt']
frames = []

for name in filenames:
    with open(name,'r',encoding='utf8') as f:
        frames.append(f.readlines())
for i in range(10):       
    for frame in frames:
        print(''.join(frame))
        time.sleep(1)
        os.system('cls')