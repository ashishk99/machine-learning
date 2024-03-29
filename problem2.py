﻿"""
Bob has an important meeting tomorrow and he has to reach office on time in morning. His general mode of transport is by car and on a regular day (no car trouble) the probability that he will reach on time is Pot. The probability that he might have car trouble is Pct. If the car runs into trouble he will have to take a train and only 2 trains out of the available N trains will get him to office on time.

What are the chances that he will reach office on time tomorrow?

Input constraints:

0<=Pct<=1
0<=Pot<=1
N>=2

Input format

First line: Pct

Second line: Pot

Third line: N

Output format

Probability he will reach in time, rounded to six decimal digits
"""

result = 0.00000
fn = float(input())
sn = float(input())
tn = float(input())
result = ((1-fn)*sn) + (fn*(2/tn))
print('%.6f'%result)
