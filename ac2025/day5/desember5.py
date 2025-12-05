
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    split_index = lines.index("")
    
    ranges = lines[:split_index]
    ids = lines[split_index + 1:]
    
parsed_ranges = []
for r in ranges:
    range_split = r.split("-")
    parsed_ranges.append((int(range_split[0]),int(range_split[1])))



sorted_ranges = sorted(parsed_ranges)
merged = []
for start, end in sorted_ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

total_ids = sum(end - start + 1 for start, end in merged)
print(f"{total_ids}")
            
        
       
