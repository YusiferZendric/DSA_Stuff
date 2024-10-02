def minimumRecolors(blocks: str, k: int) -> int:
    streaks = []
    for i in range(len(list(blocks))):
        if list(blocks)[i] == "W":
            streaks.append(0)
        elif list(blocks)[i] == "B":
            if i>0:
                try:
                    if streaks[len(streaks)-1]!=0:
                        streaks[len(streaks)-1]+=1
                    else:
                        streaks.append(1)
                except:
                    pass
            else:
                streaks.append(1)
        
    # streaks = [x for x in streaks if x!=0]
    if any(x>k for x in streaks): return 0
    minval = float('inf')
    for t in range(len(streaks)):
        total_sum = 0
        changed = 0
        for i in streaks[t:]:
            if total_sum>=k:
                break
            elif i == 0:
                total_sum+=1
                changed+=1
            else:
                total_sum+=i
        if total_sum >= k:
            minval = min(minval, changed)
    
    return minval


print(minimumRecolors("WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", 15))