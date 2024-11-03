import unireedsolomon as rs
coder = rs.RSCoder(30,24)
c = coder.encode("Hi my name is Meenakshi!")

print(repr(c))
# 'Hello, world!\x8d\x13\xf4\xf9C\x10\xe5'
print(len(c))
print(type(c))
r = c[:2] + "\0"*3 + c[5:] + "\0"

# '\x00\x00\x00lo, world!\x8d\x13\xf4\xf9C\x10\xe5'
print(r.decode("utf-8"))
print(coder.decode(r))
# 'Hello, world!'