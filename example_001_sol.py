
n = 5

tool_list = [8, 3, 7, 9 ,2]

m = 3

c_list = [5, 7, 9]


def binary_search(tool_list, target, start, end):

  if start > end :
    print("no")
    return None
  
  mid = (start + end) // 2

  if tool_list[mid] > target:

    return binary_search(tool_list, target, start, mid -1)
    
  elif tool_list[mid] < target:
   
    return binary_search(tool_list, target, mid + 1, end)
    
  
  elif tool_list[mid] == target:

    print("yes")
  else:
    print("no")

tool_list = sorted(tool_list)

print(tool_list)

for i in c_list:
  binary_search(tool_list, i, 0, len(tool_list) -1)
      

