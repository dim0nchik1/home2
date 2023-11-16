import os 


def alltext(directory):
    result = []
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".txt"):
            with open(file, encoding="utf-8") as f:
                line = f .readlines()
                date = len(line)
                result.append([file, str(date), line])
    result = sorted(result, reverse=True, key=lambda x: x[2])
# #
    for res in result:
        with open('newlille.txt', 'a',encoding="utf-8") as f:
            f.write(res[0] + '\n')
            f.write(f'строк в файле: {res[1]} \n')
            count = 0
            for i in res[2]:
                count += 1
                f.write(f'{count}:{i}\n')
#
alltext(os.getcwd())