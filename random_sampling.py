import random
import csv
import sys

# cv = change vector
short_cv = int('''length of short cv''')
long_cv = int('''length of long cv''')

csv.field_size_limit(sys.maxsize)

def main():
    if sys.argv[1] == '-m':
        # mapping hash to length
        # map: key = length, value = list of hashes
        map = dict()
        hash_len_file = open(sys.argv[2], 'r')
        csvreader = csv.reader(hash_len_file, delimiter=',')
        for row in csvreader:
            if row[1] not in map.keys():
                new_list = list()
                new_list.append(row[0])
                map[row[1]] = new_list
            else:
                map[row[1]].append(row[0])
        hash_len_file.close()

        # random sampling
        # range: short = 1 to short_cv, long = long_cv to max(len of cv)
        num = int(sys.argv[4])/2
        short_sample = []
        is_all_sample_in_map = False
        while not is_all_sample_in_map:
            short_sample = random.sample(range(1, short_cv + 1), num)
            num_of_sample_in_map = 0
            for idx in short_sample:
                if idx in map.keys():
                    num_of_sample_in_map += 1
            if num_of_sample_in_map == num:
                is_all_sample_in_map = True

        num = sys.argv[4] - num
        long_sample = []
        is_all_sample_in_map = False
        while not is_all_sample_in_map:
            long_sample = random.sample(range(1, short_cv + 1), num)
            num_of_sample_in_map = 0
            for idx in long_sample:
                if idx in map.keys():
                    num_of_sample_in_map += 1
            if num_of_sample_in_map == num:
                is_all_sample_in_map = True

        # write to output directory
        if sys.argv[4][-1] != '/':
            sys.argv[4] += '/'
        short_output = open(sys.argv[4]+"short_sample.csv", 'w')
        long_output = open(sys.argv[4]+"long_sample.csv", 'w')
        with open(sys.argv[2],'r') as file:
            csvreader = csv.reader(file, delimiter=' ')
            for row in csvreader:
                if len(row) < 2:
                    continue
                for idx in short_sample:
                    if row[0] in map[idx]:
                        # row[0] = hash, idx = length, row[1] = change vector
                        short_output.write(row[0] + ',' + idx + ',' + row[1])
                        break
                for idx in long_sample:
                    if row[0] in map[idx]:
                        # row[0] = hash, idx = length, row[1] = change vector
                        long_output.write(row[0] + ',' + idx + ',' + row[1])
                        break
        short_output.close()
        long_output.close()
        sys.exit()

    if len(sys.argv) != 5 and (sys.argv[1] != '-m'):
        print('Usage: random_sampling.py [option] <hash_cv_path> <hash_len_path> <output_path> <number_of_sample>')
        print('option: -m merge data of hash_cv and hash_len into one output file')
        print('output_path: path to output directory')
        print('L short change vector will be saved as short_sample.csv in output_path')
        print('L long change vector will be saved as long_sample.csv in output_path')
        sys.exit(1)

if __name__ == '__main__':
    main()