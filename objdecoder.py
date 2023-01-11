with open("blender/untitled.obj") as f:
    lines=f.readlines()

v=[]
vn=[]
vt=[]
f=[]
merged=[]

for line in lines:
    linetype=line.split(" ")[0]
    line=line.replace("\n","")
    if linetype=="v":
        v.append([float(element) for element in line.split(" ")[1:]])
    elif linetype=="vt":
        vt.append([float(element) for element in line.split(" ")[1:]])
    elif linetype=="vn":
        vn.append([float(element) for element in line.split(" ")[1:]])
    elif linetype=="f":
        f.append([element.split("/") for element in line.split(" ")[1:]])

f = [item for sublist in f for item in sublist]

for element in f:
    merged.append(v[int(element[0])-1][0])
    merged.append(v[int(element[0])-1][1])
    merged.append(v[int(element[0])-1][2])
    merged.append(vt[int(element[1])-1][0])
    merged.append(vt[int(element[1])-1][1])
    merged.append(vn[int(element[2])-1][0])
    merged.append(vn[int(element[2])-1][1])
    merged.append(vn[int(element[2])-1][2])

### merged
### x, y, z, s, t, nx, ny, nz

print(merged)