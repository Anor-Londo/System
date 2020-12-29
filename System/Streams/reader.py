import sys
print(f'Got this: {input()}')
data = sys.stdin.readline()[:-1]
print(f'The meaning of life is {data} {int(data) * 2}')
