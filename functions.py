# reading a file using generator method
def readFile(fileName):
    """
        file reading using genearot method.
        does not load the whole file in RAM at once instead loads one line at a time
        file format should be like this ... a txt file having key value in a single line then new line then key value ...
        'http:/dana-farber.com  12'
        'http:/amazon.com   1234'
    """
    fd = open(fileName, 'r')
    for line in fd:
        key, val = line.split() # splitting on space/tab
        yield (key, val)
    return
    
