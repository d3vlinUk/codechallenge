
def read_file_noncompliant(filename):
    file = open(filename, 'r')
    return file.readlines()