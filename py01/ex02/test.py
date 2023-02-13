from vector import Vector

v1 = Vector([[1.0, 2.0, 1.0]])
v2 = Vector([[1.0], [2.0], [3.0]])
v4 = Vector([[0.0], [2.0], [1.0]])
v3 = Vector([[0.0, 3.0, 5.0]])
t1 = v1.T()
tt1 = t1.T()

print(v1.shape, v1.values)
print(t1.shape, t1.values)
print(tt1.shape, tt1.values)
print(v2.shape, v2.values)
print(v3.shape, v3.values)
print(f"dot product : {v1.dot(v3)}")
print(f"dot product : {v2.dot(v4)}")
s1 = v1 + v3
s2 = v2 + v4
print(f"Sum of v1 v3 : {s1.values}")
print(f"Sum of v2 v4 : {s2.values}")

ss1 = v1 - v3
ss2 = v1.__rsub__(v3)
print("dif of v1 v3", ss1)
print("dif of v3 v1", ss2)
ss3 = v2 - v4
ss4 = v2.__rsub__(v4)
print("dif of v2 v4", ss3)
print("dif of v4 v2", ss4)


d1 = v1 / 2
d2 = v2 / 2
print("v1 / 2", d1)
print("v2 / 2", d2)


m1 = v1 * 2
m2 = 2 * v2
print("v1 * 2", m1)
print("2 * v2", m2)

print(Vector((10, 16)).shape, Vector((10, 16)))
print(Vector(3).shape, Vector(3))
print(Vector(0).shape, Vector(0))
print(Vector((10, 10)).shape, Vector((10, 10)))
print(Vector((10, 3)))


