class Sequence:
    transcription_dict = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    enz_dict = {'EcoRI':'GAATTC', 'EcoRV':'GATATC'}
    complement_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    def __init__(self, seq_string):
        self.seq_string = seq_string.upper()

    # Returns RNA sequence
    def transcription(self):
        transcript = ''
        for letter in self.seq_string:
            if letter in 'ATCG':
                transcript += self.transcription_dict[letter]
        return transcript
    
    def restriction(self, enz):
        enz_target = Sequence.enz_dict[enz]
        return self.seq_string.count(enz_target)
    
    def melting_temperature(self):
        G=self.seq_string.count('G')
        C=self.seq_string.count('C')
        A=self.seq_string.count('A')
        T=self.seq_string.count('T')
        return 4*(G+C) + 2*(A+T)
    
    def complement(self):
        complement_sequence=''
        for nucleotide in self.seq_string:
            complement_sequence += self.complement_dict[nucleotide]
        return complement_sequence
    
    def reverse_complement(self):
        return self.complement()[::-1]

unknown_virus = Sequence('AGGAATTCTGCATGTCGAATTCGCT')
print(unknown_virus.seq_string)
print(unknown_virus.transcription())
print('---------------------------------')
known_virus = Sequence('ACGATATCTCATTACTA')
print(known_virus.seq_string)
print(known_virus.transcription())
print('---------------------------------')
print(unknown_virus.restriction('EcoRI'))
print(known_virus.restriction('EcoRI'))
print('---------------------------------')

# Exercise
print('Melting temperature:', known_virus.melting_temperature())
print('Complement sequence:', known_virus.complement())
print('Reverse Complement sequence:', known_virus.reverse_complement())