import random
import csv
import sys
import os

# cv = change vector
short_cv = int('''length of short change vectors''')
long_cv = int('''length of long change vectors''')

csv.field_size_limit(sys.maxsize)

def main():
    if sys.argv[1] == '-m':
        # mapping hash to length
        # dict: key = length, value = list of hashes
        '''
        short_map has change vectors where the length of each change vector is less than or equal to short_cv
        '''
        short_map = dict()
        '''
        long_map has change vectors where the length of each change vector is biger than or equal to long_cv
        '''
        long_map = dict()

        # dict: key = hash, value = length
        total_data = dict()
        hash_len_file = open(sys.argv[3], 'r')
        csvreader = csv.reader(hash_len_file, delimiter=',')
        for row in csvreader:
            if len(row) < 2:
                continue
            total_data[row[0]] = row[1]
            if row[1] not in short_map.keys() and int(row[1]) <= short_cv:
                new_list = list()
                new_list.append(row[0])
                short_map[row[1]] = new_list
            elif int(row[1]) <= short_cv:
                short_map[row[1]].append(row[0])
            elif row[1] not in long_map.keys() and int(row[1]) >= long_cv:
                new_list = list()
                new_list.append(row[0])
                long_map[row[1]] = new_list
            elif int(row[1]) >= long_cv:
                long_map[row[1]].append(row[0])

        hash_len_file.close()

        # random sampling
        num = int(int(sys.argv[5])/2)
        print('Processing ' + str(num) + ' short sample change vectors...')
        short_key = random.sample(list(short_map.keys()), num)
        short_sample = list()
        for key in short_key:
            short_sample.append(random.choice(short_map[key]))

        num = int(sys.argv[5]) - num
        print('Processing ' + str(num) + ' long sample change vectors...')
        long_key = random.sample(list(long_map.keys()), num)
        long_sample = list()
        for key in long_key:
            long_sample.append(random.choice(long_map[key]))

        # write to output directory
        print('Writing to output directory...')
        if sys.argv[4][-1] != '/':
            sys.argv[4] += '/'
        if not os.path.exists(sys.argv[4]):
            os.makedirs(sys.argv[4])
        short_output = open(sys.argv[4]+"short_sample.csv", 'w')
        long_output = open(sys.argv[4]+"long_sample.csv", 'w')

        with open(sys.argv[2],'r') as file:
            csvreader = csv.reader(file, delimiter=' ')
            for row in csvreader:
                if len(row) < 2:
                    continue
                for hash in short_sample:
                    if row[0] == hash:
                        # row[0] = hash, idx = length, row[1] = change vector
                        short_output.write(row[0] + ',' + total_data[row[0]] + ',' + row[1] + '\n')
                        break
                for hash in long_sample:
                    if row[0] == hash:
                        # row[0] = hash, idx = length, row[1] = change vector
                        long_output.write(row[0] + ',' + total_data[row[0]] + ',' + row[1] + '\n')
                        break
        short_output.close()
        long_output.close()
        sys.exit()

    if len(sys.argv) != 5 and (sys.argv[1] != '-m'):
        print('Usage: random_sampling.py [option] <hash_cv_path> <hash_len_path> <output_path> <number_of_sample>')
        print('option: -m merge data of hash_cv and hash_len into one output file')
        print('hash_cv_path: path to file which contains pair of hash and change vector')
        print('hash_len_path: path to file which contains pair of hash and length of change vector(output of csv_divider.py with option -l)')
        print('output_path: path to output directory')
        print('L short change vector will be saved as short_sample.csv in output_path')
        print('L long change vector will be saved as long_sample.csv in output_path')
        print ('number_of_sample: number of total sample to be taken')
        print('L e.g. 1000 will take random 500 short and 500 long change vectors')
        sys.exit(1)

if __name__ == '__main__':
    main()