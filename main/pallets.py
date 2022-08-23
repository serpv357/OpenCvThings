SOME_PALETTE = ['#080000','#201A0B','#432817','#492910',  
             '#234309','#5D4F1E','#9C6B20','#A9220F',
             '#2B347C','#2B7409','#D0CA40','#E8A077',
             '#6A94AB','#D5C4B3','#FCE76E','#FCFAE2']

def convertHexStringsToBGR(hexStrings):
  ret_list = []
  for string in hexStrings:
    ret_list.append(tuple(int(string[i:i+2],16) for i in (4, 2, 0)))
  return ret_list