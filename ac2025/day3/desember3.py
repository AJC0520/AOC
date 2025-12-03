def part1():
    with open("input.txt", "r") as file:
        banks = file.readlines()
        total = 0
        for bank in banks:
            bank_list = [int(battery) for battery in bank.strip()]
            if(len(bank_list) == 1):
                continue
            
            index_largest = bank_list.index(max(bank_list[:len(bank_list)-1]))
            largest =  str(bank_list[index_largest])
            next_largest = str(max(bank_list[index_largest:]))
            
            bank_largest = largest + next_largest
            total += int(bank_largest)
        print(total)
    

    
def part2():
    with open("input.txt", "r") as file:
        banks = file.readlines()
        total = 0
        for bank in banks:
            bank_list = [int(battery) for battery in bank.strip()]

            setup = ""
            while len(setup) < 12:
                range_of_interest = len(bank_list) - 12 + len(setup) + 1
                index_largest = bank_list.index(max(bank_list[:range_of_interest]))
                largest = bank_list[index_largest]  
                setup += str(largest)
                bank_list = bank_list[index_largest+1:]
            total += int(setup)
        print(total)

part2()

