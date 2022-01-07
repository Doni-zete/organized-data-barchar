import csv

DUPLICATE_QUANTITY = 2

def openFile():
  with open('output.csv', 'r', newline='', encoding='utf-8') as file:
    data = []
    reader = csv.reader(file,delimiter=';')
    for row in reader:
      data.append(row)
  
    return data 
        
def saveFile(values):
  with open('output_duplicated_year.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(values)

def duplicateData(values):
    data = [[] for _ in values]

    for index, value in enumerate(values):
      for inde, columnData in enumerate(value):
        if inde < 2:
          data[index].append(columnData)
        else:
          for _ in range(DUPLICATE_QUANTITY):
            data[index].append(columnData)

    return data
      
    
def main():
  fileOpened = openFile() 

  saveFile(duplicateData(fileOpened))
  
main()