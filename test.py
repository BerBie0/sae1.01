def permutation(s):
   if len(s) == 1:
     return [s]

   perm_list = [] # resulting list
   for a in s:
     remaining_elements = [x for x in s if x != a]
     z = permutation(remaining_elements) # permutations of sublist

     for t in z:
       print([t])
       perm_list.append([a]+t)

   return perm_list

print(permutation([1,2,3]))