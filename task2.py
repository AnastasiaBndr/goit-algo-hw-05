import random

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    iterations=0
 
    while low <= high:
        iterations+=1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            if mid==len(arr)-1:
                return (iterations,arr[mid])
            else: return (iterations,arr[mid+1])
 
    # якщо елемент не знайдений
    return None

def main():
    size=10
    arr=[]
    for i in range(0,size):
        arr.append(round(random.random(),4))
    arr.sort()
    print(arr)
    print("Write the number you want to find:")
    find=input()
    result = binary_search(arr, float(find))
    
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)