import sys

inputCommand = sys.argv

inputFile = inputCommand[2]
inputContent = ''
with open(inputFile) as f:
  inputContent = f.read()  

def reverseFunction(inputContent,outputFile):
  outputContent = ''
  with open(outputFile, 'w') as f:
    outputContent = f.write(inputContent[::-1])
  return outputContent

def copy(inputContent, outputFile):
  outputContent = ''
  with open(outputFile, 'w') as f:
    outputContent = f.write(inputContent)
  return outputContent

def duplicate_contents(inputFile,str):
  n = int(str)
  for i in range(n):
    with open(inputFile,'a') as f:
      f.write(inputContent)
  return inputFile

def replace_string(inputFile, str1, str2):
  with open(inputFile, 'w') as f:
    f.write(inputContent.replace(str1, str2))
  return inputFile

def fileManipulator(command):
  if command[1] == "reverse" and len(command) == 4:
    return reverseFunction(inputContent, command[3])
  elif command[1] == "copy" and len(command) == 4:
    return copy(inputContent, command[3])
  elif command[1] == "duplicate-contents" and len(command) == 4:
    return duplicate_contents(command[2],command[3])
  elif command[1] == "replace-string" and len(command) == 5:
    return replace_string(command[2],command[3],command[4])
  else:
    return "コマンドが見つかりません"
#print(fileManipulator(inputCommand))
fileManipulator(inputCommand)