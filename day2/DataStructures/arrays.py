# 90% af tiden bruger man lister. Men de er mindre memory effektive
# Når man bruger meget store mængder kan det give performance boost at køre med arrays

from array import array

# Stort set samme funktioner som normalt, men de er type bestemt.
numbers = array("i")
