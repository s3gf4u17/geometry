#raw,unassembleddata
v=[]
vt=[]
vn=[]

#final,assembledandpackedresult
vertices=[]

#opentheobjfileandreadthedata
with open('blender/untitled.obj','r') as f:
    line=f.readline()
    while line:
        firstSpace=line.find(" ")
        flag=line[0:firstSpace]
        if flag=="v":
            line=line.replace("v ","")
            line=line.split(" ")
            l=[float(x) for x in line]
            v.append(l)
        elif flag=="vt":
            line=line.replace("vt ","")
            line=line.split(" ")
            l=[float(x) for x in line]
            vt.append(l)
        elif flag=="vn":
            line=line.replace("vn ","")
            line=line.split(" ")
            l=[float(x) for x in line]
            vn.append(l)
        elif flag=="f":
            line=line.replace("f ","")
            line=line.replace("\n","")
            line=line.split(" ")
            faceVertices=[]
            faceNormals=[]
            faceTextures=[]
            for vertex in line:
                l=vertex.split("/")
                position=int(l[0])-1
                faceVertices.append(v[position])
                texture=int(l[1])-1
                faceTextures.append(vt[texture])
                normal=int(l[2])-1
                faceNormals.append(vn[normal])
            triangles_in_face=len(line)-2
            vertex_order=[]
            for i in range(triangles_in_face):
                vertex_order.append(0)
                vertex_order.append(i+1)
                vertex_order.append(i+2)
            for i in vertex_order:
                for x in faceVertices[i]:
                    vertices.append(x)
                for x in faceTextures[i]:
                    vertices.append(x)
                for x in faceVertices[i]:
                    vertices.append(x)
        line=f.readline()
print(vertices)
# """
# eg.0,1,2,3unpackstovertices:[0,1,2,0,2,3]
# """
# foriinrange(triangles_in_face):
# vertex_order.append(0)
# vertex_order.append(i+1)
# vertex_order.append(i+2)

# foriinvertex_order:

# forxinfaceVertices[i]:
# vertices.append(x)
# forxinfaceTextures[i]:
# vertices.append(x)

# forxinfaceNormals[i]:
# vertices.append(x)
# line=f.readline()