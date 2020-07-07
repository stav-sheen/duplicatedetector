output = []
with open('./file') as f:
    lines = f.readlines()
    for line in lines:
        # Cleaning up spaces and creating [key,value] lists
        line = ''.join(line.split())
        line = line.split('=')

        # Adding relevant keys to output list
        if line[0] != '' and '#' not in line[0]:
            output.append(line[0])

# Finding duplicate keys in output list
seen = {}
dupes = []

for x in output:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

# Output duplicate keys
print("The following keys are defined more than once:")
for key in dupes:
    print(key)
