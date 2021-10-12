
n = 4
m = 6

d = [19, 15, 10, 17]

# print(d)


d = sorted(d)

print(d)


def dd_search(d, target, start, end):

  if start > end:
    return None

  if len(d) == 0:
    return None

  mid = (start + end) // 2

  dd = []
  for i in range(len(d)):
    if d[i] > d[mid]:
      dd.append(d[i] - d[mid])

  print("start : {}, end : {}, mid : {}, dd : {}, sum(dd) :{} ".format(start, end, mid, dd, sum))

  if sum(dd) >= target:
    print("okay")
    return d[mid]

  else:
    return dd_search(d, target, mid+1, end)
  
    

print(dd_search(d, 6, 0, len(d)-1 ))
