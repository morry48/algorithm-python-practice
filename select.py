from typing import List

def select_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range((len_numbers)):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers
        
print(select_sort([
    394, 808, 4820, 38, 409, 30, 342
]))

