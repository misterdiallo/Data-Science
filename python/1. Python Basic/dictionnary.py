d={
    "alpha": 18354919286,
    "police": 110,
}

print(d["police"])

d["andrea"]=1536513902
d["yacine"]="1536513902"

print(d)
del d['yacine']
print(d)

print("Using Key only")
for key in d:
    print("key:", key, "value:", d[key])

print("Using Key and Value directly")
for k,v in d.items():
    print("key:", k, "value:", v)

print("alpha" in d)
d.clear()
print(d)