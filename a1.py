import sys
def main ():

    # open and read sample.txt file from argument; 'r' reads the file
    text = open(sys.argv[1], 'r')
    # input duplicates into 2 dictionaries; use one unordered dictionary for duplicate occurances and the other to count the number of occurances
    duplicates = dict()
    counter  = dict()

    #computation loop for each line in input file
    for line in text:
        #remove trailing and leading string characters
        numb = line.strip()
        #convert string to an integer with base 16 hex
        a = int(numb, base=16)
        #if length of string is greater than 1, string the 0s
        if len(numb)>1:
            numb = numb.lstrip('0')
        #increment the number of occurances and put in collections
        #index the stripped string and index the number of occurances
        duplicates[a] = numb
        counter[a] = counter.get(a,0) +1
        
    #use keys for valued pairs and then sort dictionaries from from the smallest value to the largest value in hex
    keys = sorted(counter.keys(), cmp=None, key=None, reverse=False)

    #if more than one total occurance, go through sorted kets and print key pair
    for key in keys:
        total = counter[key]
        if total > 1:
            print duplicates[key], total        

#figuring out if we are on module directly or imported
if __name__ == '__main__':
    main()
