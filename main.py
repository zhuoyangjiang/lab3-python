# Author: zhuoyangjiang zfj5038@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 7
# Breakout: 

def sum_n(n):
    if n <= 0:
        return n
    
    return n + sum_n(n-1)

def print_n(s, n):
    if n <= 0:
        return
    
    print_n(s,n-1)
    print(s)

def run():
    #print("Enter an int:",end= '')
    n = int(input("Enter an int:"))
    print(f"sum is {sum_n(n)}.")

    s = input("Enter a string:")
    print_n(s,n)
    
if __name__ == "__main__":
    run()