# Dictionary sorting

d = {2:'feb', 1:'jan', 4:'april', 3:'march'}
print(d)

print('########')
print(d.keys())
print(sorted(d.keys()))

for k in sorted(d.keys()):
    print(k, d[k])
