number = input()
count = 0

for i in number:
    
    if i.isdigit():
        count += int(i)
        
print(count)