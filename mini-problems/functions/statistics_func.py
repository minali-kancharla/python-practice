numbers = input("Enter numbers separated by commas: ").split(",")

numbers = [int(number) for number in numbers]


print(numbers)

def mean(numbers):
    return (sum(numbers)/len(numbers))

def median(numbers):
    sorted_data = sorted(numbers)
    n = len(sorted_data)
    mid = n//2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else: 
        return sorted_data[mid]

def minimum(numbers):
    return min(numbers) 

def maximum(numbers):
    return max(numbers)

print(mean(numbers))
print(median(numbers))
print(min(numbers))
print(max(numbers))