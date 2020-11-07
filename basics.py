#Rosalind Problem Nr.
#Return The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

def reverse(input):
    putin = ''
    q = 1
    while q <= len(input):
        putin += input[len(input) - q]
        q += 1
    print(putin)

def complementary(dna):
    compl = ''
    code = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in dna:
        compl += code[base]
    print(compl)

reverse('putin')
complementary('AACCT')