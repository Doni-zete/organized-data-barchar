from bs4 import BeautifulSoup
import re
import os.path

# Open file to read the values

def openFile():
  if os.path.isfile('./input.bin'):
      file = open("./input.bin", "r", encoding='utf-8')
  else:
    # create file if not exist
    createFile = open("./input.bin", "w+", encoding='utf-8')
    createFile.close()
    # after creating the file open it in read mode.
    file = open("./input.bin", "r", encoding='utf-8')
    print("Put the values in the 'input.bin' file!")
  
  soup = BeautifulSoup(file, features="html.parser")
  file.close()
  return soup

def formatValuesToSave(values):
  data = [];
  strValues = '',
  strToSave = '',
  
  for value in values: 
    strValues = str(';'.join(value))
    data.append(strValues)
  strToSave = '\n'.join(data)  
  return strToSave
  
def saveFile(value):
  # Open or create the file to save the values
  file = open("./output.csv", "w", encoding='utf-8')
  file.write(u'\ufeff' + formatValuesToSave(value))
  file.close()
  
def createMatrizFrequency(values, amountUniqueNames):
  dataValues = [str(ele[0][0:4]) for ele in sorted(values)]
  
  # The fields of the titles
  data = [['NAME', 'IMAGE'] + dataValues]
  for i in range(amountUniqueNames):
    data.append([])
    
  return data
  
  
def getUniqueNames(values):
  allNames = [ele[1].upper() for ele in values]
  return dict.fromkeys(list(set(allNames)), 1)

def yearFrequency(values):
  yearCountFrequency = []
  uniqueNamesDict = getUniqueNames(values)
  
  # [year, name]
  for value in values:
    keyName = value[1].upper()
    year = [value[0][0:4], uniqueNamesDict[keyName], keyName]

    # increment the times the current name have apperead.
    uniqueNamesDict[keyName] = uniqueNamesDict[keyName] + 1
    yearCountFrequency.append(year)

  matrizFrequency = createMatrizFrequency(yearCountFrequency, len(uniqueNamesDict))
  
  for index, nameKey in enumerate(sorted(uniqueNamesDict)):
    lastValue = ''
    isSetName = True
    for year in yearCountFrequency:
      if isSetName:
        matrizFrequency[index+1].append(nameKey)
        matrizFrequency[index+1].append('IMG:URL')
        isSetName = False
      
      if year[2] == nameKey:
        lastValue = str(year[1])
        matrizFrequency[index+1].append(lastValue)
      else:
        matrizFrequency[index+1].append(lastValue)
      
  return matrizFrequency
  
def main():
  openedFile = openFile()
  rows = openedFile.find_all('tr')
  data = []
  for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols] # Get rid of empty values  
    if len(cols) > 0:
      # Mudar as cols if len e name 0 e 1
      year = cols[1]
      name = re.sub(r"\([^()]*\)", "", cols[2]).strip()
      data.append([year, name]) 
  
  
  saveFile(yearFrequency(data))
  
  
# Initialize the application
main() 


