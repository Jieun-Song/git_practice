keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = {}

for i in range(3):
    result[keys[i]] = vals[i]

print(result)

#result = dict(zip(keys, vals))
