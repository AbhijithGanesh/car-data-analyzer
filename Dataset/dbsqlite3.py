import pandas as pd
def datareturn():
    file_errors_location = r'A:\Abhijith _files\Abhijith\PythonProjects\1.DJANGO PROJECTS\Pragyaan\Dataset\Book1.xlsx'
    df = pd.read_excel(file_errors_location)
    arr  = []
    df = df.drop('Unnamed: 8', 1)
    df = df.drop('Unnamed: 9', 1)
    df = df.drop('Unnamed: 10', 1)
    a = df.values.tolist()
    for i in df:
        arr.append(i)
    arr.remove(0.01)
    finalarr = []
    finalarr.append(arr)
    finalarr.extend(a)
    finalarr.remove(finalarr[-1])
    return finalarr
print(datareturn())