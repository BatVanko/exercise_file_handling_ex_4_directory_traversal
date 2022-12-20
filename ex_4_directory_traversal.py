from os import listdir
from os.path import isdir,join

def directory_traversal(path, files_by_extension):
    for element in listdir(path):
        if isdir(join(path,element)):
            directory_traversal(join(path,element), files_by_extension)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(element)

result = {}

directory_traversal('./', result)
output_string = ''
for key,value in sorted(result.items()):
    with open('report.txt','a') as file:
        file.write(f'.{key}\n')
        for w in sorted(value):
            file.write(f'- - - {w}\n')


    # with open('output_string.txt', 'a')


