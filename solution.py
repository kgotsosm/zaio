def sum_even_numbers(arr):
    # Store the sum in a variable
    even_sum = 0
    
    # Iterate through the array and add even numbers to the sum
    for num in arr:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum
