# Fetch protein name and sequence from protein fasta file
with open('./files/sequence.fasta', 'r') as my_protein:
    protein_name = my_protein.readline()[1:-1]
    protein_seq = ''
    for line in my_protein:
        protein_seq += line.replace('\n','')

print(f'Protein name: {protein_name}')
print(f'Protein sequence: {protein_seq}')

# Write into file (overwrite)
with open('./files/myfile.txt', 'w') as f:
    f.write('My first line of the file\n') # will create a file if not exists and overwrite from begining
    f.write('My second line of the file\n') # appends to the line form previous commad because it opened one time for both
    lines = ['New line 3\n', 'New line 4\n', 'New line 5\n']
    f.writelines(lines) # this method recieves a list of lines

# Write into file (append)
with open('./files/myfile.txt', 'a' ) as file:
    file.write('The last line from append mode')

# Use CSV module:
import csv
with open('./files/data.csv') as my_csv:
    my_csv_reader = csv.reader(my_csv)
    for row in my_csv_reader:
        print(row)

# Use custom delimeter in csv module
with open('./files/data_semicolon.csv') as my_csv:
    my_csv_reader = csv.reader(my_csv, delimiter=';')  
    for row in my_csv_reader:
        print(row)

# Use sniffer to recognize dialect of csv file
with open('./files/data_semicolon.csv') as my_csv:
    dialect = csv.Sniffer().sniff(open('./files/data_semicolon.csv').read(), ';')
    my_csv_reader = csv.reader(my_csv, delimiter=';', dialect=dialect)  
    for row in my_csv_reader:
        print(row)

# Write into CSV file        
with open('./files/my_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['5', '654', '45', '33.6', '77'])
    writer.writerow(['6', '148', '36', '0.627', '50'])

# Exercise 1
# Its not recommended to use read() method beause the file may be very large and not possible to fetch all data at once

# Exercise 2
# We can use readline() method inside a loop to walk through the file efficiently

# Exercise 3
name = input('Please enter your name:')
with open('./files/my_name.txt', 'w') as new_file:
    new_file.write(name)
print('Please find your name in file: ./files/my_name.txt')

# Exercise 4
# we use 'with' for opening a file to have the auto-close feature

# Exercise 5
# We must close all files after using them to prevent the overusing system resources like RAM and I/O

# Exercise 6
# in 'w' mode everything will be overwritten, by contrast 'a' mode appends new data to the end of file