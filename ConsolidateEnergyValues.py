import glob

files = []
for f in glob.glob("*.txt"):
    files.append(f)

data = {}

energies = {}
errors_high = {}
errors_low = {}

for item in files:
    with open(item, 'r') as f:
        content = f.readlines()
        for i in range(len(content)):
            if content[i][0].isalpha():
                line = content[i+1].split()
                line[3] = str(abs(float(line[3])))
                line[4] = str(abs(float(line[4][1:])))
                energies[content[i].strip().replace("/", "")] = line[2:5]
                errors_high = line[3]
                error_low = line[4]
        data[item.replace('.txt','')] = energies
        energies = {}

mutas = []
for key in data.keys():
    for item in data[key]:
        mutas.append(item)

mutas = list(set(mutas))
mutas = sorted(mutas)

print mutas
consolidated = {}
for f in sorted(data.keys()):
    print f
    for muta in mutas:
        if muta in data[f].keys():
            if muta in consolidated.keys():
                consolidated[muta] += data[f][muta]
            else:
                consolidated[muta] = data[f][muta]
        else:
            if muta in consolidated.keys():
                consolidated[muta] += ['', '', '']
            else:
                consolidated[muta] = ['', '', '']

print consolidated

output = ","

for sim in sorted(data.keys()):
    output += sim + ",,,"

output += "\n"

for key in sorted(consolidated.keys()):
    output += key + ","
    output += ",".join(consolidated[key])
    output += "\n"

print output
