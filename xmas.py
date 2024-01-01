def christmas_tree():
    # Tree star
    try:
        n = int(input("Input your desired height of your Christmas Tree: "))
    except ValueError:
        print("You can only input whole numbers")
        return
    
    if n == 1:
        print("Tree size is too small. Increase the tree size")
        return
    
    i = 0
    while i < n:
        spaces =  n - i - 1
        stars = 2*i + 1
        print (" "*spaces + "*"*stars)
        i += 1

    # Xmas tree truck
    if n <= 2:
        y = 1
        for j in range (1):
            print(" "*(n-1) + "*")
            return
        
    elif n < 5:
        y = 1
        for j in range (1):
            print(" "*(n-y-1) + "*"*(1 + y*2))
            return

    elif n < 8:   
        y = 2
    else:
        y = n//4
    
    for j in range (y):
        print(" "*(n-y-1) + "*"*(1 + y*2))

if __name__ == "__main__":
    christmas_tree()
