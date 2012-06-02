#!/usr/bin/env python
# 3***00
numbers = [6,5,1987]
multnumbers = []
for number in numbers:
  #print number * numbers[0]
  multnumbers.append(number * numbers[0])
  multnumbers.append(number * numbers[1])
  multnumbers.append(number * numbers[2])

nodupNumbers = list(set(multnumbers))

productListSum = 0
for number in nodupNumbers:
  productListSum += number

catNumbers = 651987
answer = ((productListSum * catNumbers * (25*12)) / 549932400) * 2600
print "answer"
print answer

#find product of the productlist sum * the new integer * <the number of meetings in 25 years>
#divide by 549932400
#multiply that by 2600
