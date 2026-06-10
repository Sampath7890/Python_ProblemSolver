def highestAltitude(n, arr):
    # Write your logic here
    current_alt = 0 
    highest_alt = 0

    for gain in arr :
        current_alt += gain
        if current_alt > highest_alt :
            highest_alt = current_alt
    return highest_alt  # Placeholder return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)