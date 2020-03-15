# Boj 11004
import sys

N, K = map(int, sys.stdin.readline().split(' '))
print(sorted(map(int, sys.stdin.readline().split(' ')))[K -1])