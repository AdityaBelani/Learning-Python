digits={0,1,2,3,7,8,9}
print(digits) #{0, 1, 2, 3, 7, 8, 9}

digits2=digits.copy()
print(digits2) #{0, 1, 2, 3, 7, 8, 9}

digits.update({4,5,6})
print(digits) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
