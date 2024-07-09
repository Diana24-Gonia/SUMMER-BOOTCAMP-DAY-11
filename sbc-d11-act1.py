bubble_sort = ['Q', 'S', 'A', 'M', 'Z', 'R']

print("Original array:", bubble_sort)

n = len(bubble_sort)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if bubble_sort[j] > bubble_sort[j+1]:
            bubble_sort[j], bubble_sort[j+1] = bubble_sort[j+1], bubble_sort[j]
            swapped = True
            print(f"After swap {bubble_sort[j]} and {bubble_sort[j+1]}:", bubble_sort)
    if not swapped:
        break
    
print("Sorted array:", bubble_sort)
