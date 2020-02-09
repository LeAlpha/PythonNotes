# Generators er memory efficient, og i hver iteration spytter de en ny værdi ud. De beholder derfor
# den begrænsede mængde memory

from sys import getsizeof
value = (x*2 for x in range(10000))
print("Gen: ", getsizeof(value))
value = (x*2 for x in range(1))
print("Gen: ", getsizeof(value))
value = (x*2 for x in range(1000000))
print("Gen: ", getsizeof(value))
