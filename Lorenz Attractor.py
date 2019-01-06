def Lorenz(state, t):
    x = state[0]
    y = state[1]
    z = state[2]
    #sigma = 10.0
    #rho = 26.0
    #beta = 8.0/3
    #xd = x + t * (sigma * (y-x))
    #yd = y + t * ((rho-z)*x - y)
    #zd = z + t * (x*y - beta*z)
    sigma = -5.5
    rho = 3.5
    beta = -1
    xd = x + t * y
    yd = y + t * z
    zd = z + t * (-sigma*x - rho*y - z + beta*(x*x*x))
    return [xd, yd, zd]

import bpy
import bmesh

mesh = bpy.data.meshes.new("mesh")
obj = bpy.data.objects.new("Lorenz", mesh)


scene = bpy.context.scene
scene.objects.link(obj)
scene.objects.active = obj
obj.select = True

mesh = bpy.context.object.data
bm = bmesh.new()

state0 = [0.1, 0.0, 0.0]
time = 0.008
state = Lorenz(state0, time)

temp_vert = bm.verts.new([0.1, 0.0, 0.0])

for i in range(0, 50000):
    temp = temp_vert
    state = Lorenz(state, time)
    temp_vert = bm.verts.new(state)
    bm.edges.new((temp, temp_vert))

bm.to_mesh(mesh)
bm.free()
