

n = 10
key = b"gabe"
key2 = "string".encode()
key3 = b"smoothie"

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8

print(index)
print(index2)
print(index3)


'''
for i in range(n):
    print(hash(key))
    '''