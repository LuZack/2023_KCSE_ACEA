
import sys

def main():
    if len(sys.argv) != 4:
        print('Usage: csv_divider.py <input_path> <output_path> <number_of_files>')
        sys.exit(1)
    with open(sys.argv[1],'r') as csv:
        lines = csv.readlines()
        size = len(lines)
        divisor = int(len(lines)/int(sys.argv[3]))
        j = 0
        k = 1
        for i in range(0, size):
            if j > divisor or i == size -1:
                j = 0
                with open(sys.argv[2] + '_' + str(k) + '.csv', 'w') as output:
                    output.writelines(lines[i:i+100])
                    k += 1
            j += 1


if __name__ == '__main__':
    main()