#! /usr/bin/env python

import math

def pow10(value, pow):
    return value * math.pow(10, pow)

k_a = input("k_a ")
if type(k_a) == tuple:
    k_a = [str(item) for item in k_a]
    k_a = float('.'.join(k_a))
else:
    k_a = float(k_a)

k_a_10 = float(input("k_a_10 "))

se_a = input("se_a ")
if type(se_a) == tuple:
    se_a = [str(item) for item in se_a]
    se_a = float('.'.join(se_a))
else:
    se_a = float(se_a)

se_a_10 = float(input("se_a_10 "))

k_d = input("k_d ")
if type(k_d) == tuple:
    k_d = [str(item) for item in k_d]
    k_d = float('.'.join(k_d))
else:
    k_d = float(k_d)

k_d_10 = -float(input("k_d_10 "))

se_d = input("se_d ")
if type(se_d) == tuple:
    se_d = [str(item) for item in se_d]
    se_d = float('.'.join(se_d))
else:
    se_d = float(se_d)

se_d_10 = -float(input("se_d_10 "))

KD = input("K_D ")
if type(KD) == tuple:
    KD = [str(item) for item in KD]
    KD = float('.'.join(KD))
else:
    KD = float(KD)

# k_a = 94
# k_a_10 = 0
# se_a = 2.7
# se_a_10 = 0
#
# k_d = 85
# k_d_10 = 0
# se_d = 2.5
# se_d_10 = 0
#
# KD = 9.0

k_a = pow10(k_a, k_a_10)
se_a = pow10(se_a, se_a_10)

k_d = pow10(k_d, k_d_10)
se_d = pow10(se_d, se_d_10)

first = math.pow((se_a / k_a), 2)
second = math.pow((se_d / k_d), 2)

sum = first + second

se = math.sqrt(sum) * 100

out = (KD / 100) * se

print(out)


# print("((" +str(se_a) + "*10^" + str(se_a_10) + "/" + str(k_a) + "*10^" + str(k_a_10) + ")^2" + " + (" + str(se_d) + "*10^" + str(se_d_10) + "/" + str(k_d) + "*10^" + str(k_d_10) + ")^2")

# print(se)

