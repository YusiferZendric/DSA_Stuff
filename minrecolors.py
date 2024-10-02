def minimumRecolors(s: str, k: int) -> int:
    i, j, n = 0, 0, len(s)
    curr, ans = 0, float('inf')

    while j < n:
        if s[j] == 'W':
            curr += 1
        if (j - i + 1) < k:
            j += 1
        else:
            ans = min(ans, curr)
            j += 1
            if s[i] == 'W':
                curr -= 1
            i += 1

    return ans

string = input("Enter your string: ")
K = int(input('Enter the streak you want: '))
a = minimumRecolors(string, K)
print(f"Minimum recolors needed: {a}")