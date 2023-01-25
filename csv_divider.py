
import sys

def main():
    if sys.argv[2] == '-t':
        with open(sys.argv[3],'r') as csv:
            print(len(csv.readlines()))
            sys.exit()
    if len(sys.argv) != 4:
        print('Usage: csv_divider.py [option] <input_path> <output_path> <number_of_files>')
        print('option: -d divide csv file into n files')
        print('option: -t test')
        sys.exit(1)
    
    
    with open(sys.argv[2],'r') as csv:
        tmp = []
        lines = csv.readlines()
        size = len(lines)
        divisor = int(len(lines)/int(sys.argv[4]))
        j = 0
        k = 1
        for i in range(0, size):
            tmp.append(lines[i])
            if j > divisor or i == size -1:
                j = 0
                with open(sys.argv[3] + '_' + str(k) + '.csv', 'w') as output:
                    output.writelines(lines)
                    tmp = []
                    k += 1
            
            j += 1


if __name__ == '__main__':
    main()
