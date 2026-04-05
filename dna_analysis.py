dna = "ATGCGATAGCTAGCTA"
dna2 = "ATGCGXATBAGCTA"
counts = {
    'A': 0,
    'T': 0, 
    'C': 0,
    'G': 0 }

for base in dna2:
    if base in counts:
        counts[base]+=1
print(counts)    

gc = counts["G"] + counts["C"]
total = len(dna)

gc_content = (gc / total) * 100

print(f"GC Content: {gc_content}%")

num3 = int(input('Enter the first number: '))
num4 = int(input('Enter the second number: '))

if num3 < num4:
    num3, num4 = num4, num3

while num4 != 0:
    num3, num4 = num4, num3 % num4
print(f'The HCF is {num3}.')

    