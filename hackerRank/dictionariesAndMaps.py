import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    phone_book = {}
    for i in range(1, 2 * n + 1, 2):
        name = input_data[i]
        phone = input_data[i+1]
        phone_book[name] = phone
        
    queries = input_data[2 * n + 1:]
    
    for q in queries:
        if q in phone_book:
            print(f"{q}={phone_book[q]}")
        else:
            print("Not found")

if __name__ == "__main__":
    solve()