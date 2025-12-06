

def part1():
    with open("input.txt", "r") as file:
        problems = [(line.split()) for line in file]
        answer = 0
        for i in range(len(problems[0])):
            for j in range(len(problems)-1):
                value = int(problems[j][i])
                if j == 0:
                    current_total = value
                    continue
                
                if problems[-1][i] == "*":
                    current_total = value * current_total
                else:
                    current_total = value + current_total
            answer += current_total
        print(answer)


