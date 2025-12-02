

dial = 50
code = 0
prev_dial = 0

with open("inputdesember1.txt", "r") as file:
    for l in file:
        prev_dial = dial 
        direction = l[0]
        num = int(l[1:])
        code += num // 100
        num = num % 100
        
        if(direction == "R"): 
            dial = (dial + num) % 100
            
            if((dial < prev_dial) and (dial != 0)):
                code += 1
        
        if(direction == "L"):
            dial = dial - num
            
            if(dial < 0):
                if(prev_dial != 0):
                    code += 1
                dial = (100 + dial)
                
        if(dial == 0):
                code += 1
            
print(code)
            
    
