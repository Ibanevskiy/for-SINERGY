def sum_negatives_between_min_max(arr):
    if not arr:
        return 0  # Пустой массив
    
    min_val = min(arr)
    max_val = max(arr)
    min_index = arr.index(min_val)
    max_index = arr.index(max_val)
    
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    
    sum_neg = 0
    for i in range(start + 1, end):
        if arr[i] < 0:
            sum_neg += arr[i]
    
    return sum_neg

# Пример использования
if __name__ == "__main__":
    array = [3, -1, -2, 5, -4, 6, 2]
    result = sum_negatives_between_min_max(array)
    print(f"Сумма отрицательных элементов между min и max: {result}")
