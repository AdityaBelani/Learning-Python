digits1={0,1,2,3}
digits2={2,4,5,6}
digits3={0,7,8,9,2}

print(set.union(digits1,digits2,digits3), #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
      set.intersection(digits1,digits2,digits3), #{2}
      set.difference(digits1,digits2,digits3)) #{1, 3}
