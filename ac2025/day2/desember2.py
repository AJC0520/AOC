
with open("input.txt", "r") as file:
    invalid_id_total = 0
    
    line = file.readline()
    id_list = line.strip().split(",")
    
    for id in id_list:
        id_range = id.split("-")
        for i in range(int(id_range[0]), int(id_range[1]) + 1):
            s = str(i)
            
            mid = len(s) // 2
            part1 = s[:mid]
            part2 = s[mid:]

            if(part1 == part2):
                invalid_id_total += i
                continue
            
            temp_string = ""
            for digit in s:
                temp_string += digit
                if(temp_string * (len(s) // len(temp_string)) == s and (len(s) // len(temp_string) >= 2)):
                    invalid_id_total += i
                
print(invalid_id_total)

            
            