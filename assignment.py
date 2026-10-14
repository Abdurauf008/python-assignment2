def classify(value):

    if value < 208:
        return "Below range"
    elif value <= 212:
        return "In range"
    else: 
        return "Above range"
    

def calculate_average(total,count):
        return total/count

total = 0
below_range = 0
in_range = 0
above_range = 0

num_sheets = int(input("Enter the number of paper sheets: "))

for i in range(num_sheets):
    width = int(input("Enter the paper sheet width: "))
    print(classify(width))
    total  += width 
    category = classify(width)

    if category == "Below range":
        below_range += 1
    elif category == "In range":
        in_range += 1
    elif category == "Above range": 
        above_range += 1

average_width = calculate_average(total,num_sheets)
     
print(f"Total width : {total} mm")
print(f"Average width : {average_width} mm")
print(f"Below range : {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")