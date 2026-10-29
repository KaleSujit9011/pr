dna = input("DNA seq: ").upper()

if not dna or not all(base in "ATGC" for base in dna):
    print("INVALID DNA")
    raise SystemExit

print("len dna:", len(dna))
print("GC : {:.2f}%".format((dna.count("G") + dna.count("C")) / len(dna) * 100))

motif = input("motif : ").upper()

positions = []
for i in range(len(dna) - len(motif) + 1):
    if dna[i:i + len(motif)] == motif:
        positions.append(i + 1)
print("position:", positions)

complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
print("reverse complement:", "".join(complement[base] for base in reversed(dna)))

start = dna.find("ATG")
orf = None

if start != -1:
    for i in range(start + 3, len(dna) - 2, 3):
        if dna[i:i + 3] in {"TAA", "TAG", "TGA"}:
            orf = dna[start:i + 3]
            break
print("code region:", orf if orf else "No ORF found")
