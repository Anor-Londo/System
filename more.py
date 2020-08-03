"""breaks a line or text file into pages for live viewing"""
def more(text, numlines=15):
    lines = text.splitlines()   # just like sp;it('\n') but without '' in the end
    while lines:
        chunks = lines[:numlines]
        lines = lines[numlines:]
        for line in chunks:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break

if __name__ == 'main':
    import sys                              # if run as a script
    more(open(sys.argv[1]).read(), 10)      # display page by page the contents of the file
                                            # specified in the command line
