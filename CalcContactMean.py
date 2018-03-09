#! /usr/bin/env python

with open('24_249_contacts_high.dat') as f:
    content = f.readlines()

    total = 0
    for line in content:
        if line[0] != "#":
            line = line.split()
            total += int(line[2])
print total

with open('24_249_high_total.dat','w') as o:
    o.writelines(str(total))
