# import math
# # attmpt 1
# def downToZero(n):
#     moves = 0
#     def isPrime(targ):
#         for num in range(2, int(math.sqrt(targ)) + 1):
#             if targ % num == 0:
#                 return int(num)
#         return 0
#     getMinFactors = lambda targ, divisor: targ / divisor
#     def lookOneStepAhead(k, trial):
#         pth_1 = k 
#         pth_1 -= 1
#         divis = isPrime(pth_1)
#         if divis:
#             print(pth_1, divis)
#             option = max(getMinFactors(pth_1, divis), divis)
#         else:
#             option = pth_1
#         trial_divis = isPrime(trial)
#         if trial_divis:
#             trial_option = max(getMinFactors(k, trial_divis), trial_divis)
#             return trial_option < option
#         else:
#             return trial - 1 < option

#     while n != 0:
#         print(n)
#         divisor = isPrime(n)
#         if not divisor:
#             n -= 1
#             moves += 1
#             continue
#         candidate = max(getMinFactors(n, divisor), divisor)
#         print(candidate)
#         if lookOneStepAhead(n, candidate):
#             n = int(candidate)
#         else:
#             n -= 1
#         moves += 1
#     return moves
    
import math


# attmpt 2 , split at every choice

def downToZero(n):
    getMinFactors = lambda targ, divisor: targ / divisor
    track = 0
    initial = "split_0"
    routes = {initial: [n, 0]}
    def isPrime(targ):
        for num in range(2, int(math.sqrt(targ)) + 1):
            if targ % num == 0:
                return int(num)
        return 0
    def choose_move(idx, cur_n, alt=False, routes=routes):
        if idx not in routes:
            routes[idx] = tuple(cur_n, 0)
        temp = isPrime(routes[idx][0])
        if temp:
            track += 1
            choose_move(f"split_{track}", routes[idx][0], alt=True)
            comp = max(getMinFactors(routes[idx][0], temp), temp)
            routes[idx][0] = comp
        if alt:
            routes[idx][0] -= 1
    while True:
        choose_move(routes[initial], routes[initial][0])
        for key in routes.keys():
            routes[key][1] += 1
        for _, v in routes.items():
            if v[0] == 0:
                return v[1]
print(downToZero(94))

        
