import csv
import sys

def main():
    if sys.argv[1] == '-t':
        with open(sys.argv[2],'r') as csv:
            print(len(csv.readlines()))
            sys.exit()
    if sys.argv[1] == '-m':
        with open(sys.argv[2],'w') as output:
            for i in range(3, int(len(sys.argv))):
                with open(sys.argv[i],'r') as csv:
                    lines = csv.readlines()
                    output.writelines(lines)
            sys.exit()
    if sys.argv[1] == '-n':
        map = dict()
        for i in range(3, int(len(sys.argv))):
            f = open(sys.argv[i], 'r')
            size = f.readlines()
            f.close()
            with open(sys.argv[i],'r') as csv:
                for j in range (0, len(size)):
                    line = size[j]
                    if len(line) < 3:
                        continue
                    
                    tailLength_num = line.split(',')
                    print(tailLength_num[0])
                    if tailLength_num[0] in map:
                        map[tailLength_num[0]] += int(tailLength_num[1])
                    else:
                        map[tailLength_num[0]] = int(tailLength_num[1])
        with open(sys.argv[2],'w') as output:
            for key in map:
                output.write(key + ',' + str(map[key]) + '\n')
        sys.exit()
    if sys.argv[1] == '-l':
        output = open(sys.argv[3], 'w')
        with open(sys.argv[2],'r') as csv:
            csvreader = csv.reader(csv)
            for row in csvreader:
                lst = row.split(',')
                editscript = lst[1].split('|')
                print(lst[1] + ": " + len(editscript))
                output.write(lst[0] + "," + str(len(editscript)) + '\n')
                print(lst[0] + "," + str(len(editscript)))
        output.close()
        sys.exit()
    
    if len(sys.argv) != 4 and (sys.argv[1] != '-m' or sys.argv[1] != '-t'):
        print('Usage: csv_divider.py [option] <input_path> <output_path> <number_of_files>')
        print('option: -m merge csv file into n files')
        print('option: -t test')
        print('option: -l calculate the length of each tail')
        sys.exit(1)
    
    
    with open(sys.argv[1],'r') as csv:
        tmp = []
        lines = csv.readlines()
        size = len(lines)
        divisor = int(len(lines)/int(sys.argv[3]))
        j = 0
        k = 1
        for i in range(0, size):
            tmp.append(lines[i])
            if j > divisor or i == size -1:
                j = 0
                with open(sys.argv[2] + '_' + str(k) + '.csv', 'w') as output:
                    output.writelines(tmp)
                    tmp = []
                    k += 1
            
            j += 1


if __name__ == '__main__':
    main()
