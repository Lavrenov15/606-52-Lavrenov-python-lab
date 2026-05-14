def w_recursive(i):
   
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    
   
    return w_recursive(i-1) * w_recursive(i-2) * ((i-1)**2 / (i+1)**3)

def w_iterative(i):
   
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    w_prev2 = 0.3   # w_{i-2}
    w_prev1 = -1.5  # w_{i-1}
    w_current = 0
    for current_i in range(3, i + 1):
        w_current = w_prev1 * w_prev2 * ((current_i - 1)**2 / (current_i + 1)**3)
        w_prev2, w_prev1 = w_prev1, w_current  
    
    return w_current

print("i\tw_i (рекурсия)\tw_i (итерация)")
print("-" * 45)
for i in range(1, 7):
    rec = w_recursive(i)
    it = w_iterative(i)
    print(f"{i}\t{rec:.6f}\t\t{it:.6f}")
