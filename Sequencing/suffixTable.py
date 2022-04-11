def suffixtable (t:str):
   """<<IN>>     t = text
   <<OUT>>       List of Tuples (suffix, offset)
   """
   suffixtable = []
   for i in range(len(t)):
      suffix = t[i:]
      offset = i
      suffixtable.append((suffix,offset))
      
   return suffixtable.sort()
