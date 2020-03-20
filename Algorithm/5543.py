menu = []
for _ in range(5):
    menu.append(int(input()))
    
burger = min(menu[0:3])
soda = min(menu[3:])
print(burger + soda - 50)