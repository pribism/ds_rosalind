#Calculate the Profile Matrix and the Consensus string for a given set of entries

from Fasta_proc import process_fasta, fasta_to_list
import pandas as pd

inp_file = process_fasta('./rosalind_cons (2).txt')
inp_file = fasta_to_list(inp_file)

inp = pd.DataFrame(inp_file)
#print(inp.loc[0].value_counts())

#print(inp[inp == 'A'])
inp['A'] = inp[inp == 'A'].count(1)
inp['C'] = inp[inp == 'C'].count(1)
inp['G'] = inp[inp == 'G'].count(1)
inp['T'] = inp[inp == 'T'].count(1)

print(inp)

prof = inp[['A','C','G','T']].transpose()
print(prof)
print(''.join(map(str,prof.idxmax().tolist())))
#print(prof.set_index(['A: C: G: T:'.split(' ')]))
a = 'A: '+ ' '.join(map(str,prof.loc['A'].tolist()))
c = 'C: '+ ' '.join(map(str,prof.loc['C'].tolist()))
g = 'G: '+ ' '.join(map(str,prof.loc['G'].tolist()))
t = 'T: '+ ' '.join(map(str,prof.loc['T'].tolist()))

print(a)
print(c)
print(g)
print(t)
#prof['Consensus'] = inp[]

#print(inp)

