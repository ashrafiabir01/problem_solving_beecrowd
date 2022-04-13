value =0
pos = 0
for i in range(100):
    inp = int(input())
    if (value<inp):
        value = inp
        pos =i 
print(f"{value}\n{pos+1}")