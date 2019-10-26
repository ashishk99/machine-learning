"""
Mike wants to go fishing this weekend to nearby lake. His neighbour Alice (is the one Mike was hoping to ask out since long time) is also planing to go to the same spot for fishing this weekend. The probability that it will rain this weekend is P1 . There are two possible ways to reach the fishing spot (bus or train). The probability that Mike will take the bus is Pmb and that Alice will take the bus is Pab . Travel plans of both are independent of each other and rain.
What is the probability Prs that Mike and Alice meet each other only (should not meet in bus or train) in a romantic setup (on a lake in rain)?
Input constraints
(0<=P1<=1),(0<=Pmb<=1) ,(0<=Pab<=1) 
Input format
FIrst line: Pmb
Second line: Pab
Third line: P1
Output format
Prs, rounded up to six decimal places.
"""



result = 0.00000
fn = float(input())
sn = float(input())
tn = float(input())
result = ((1-fn)*sn) + (fn*(2/tn))
print('%.6f'%result)