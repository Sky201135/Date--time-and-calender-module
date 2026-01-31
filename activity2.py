import random
import time

def getRndomDate(startDate, endDate):
   print("printing random date between", startDate, "and", endDate)
   randomGenerator = random.random()
   dateFormat = "%Y-%m-%d"

   startTime = time.mktime(time.strptime(startDate, dateFormat))
   endTime = time.mktime(time.strptime(endDate, dateFormat))

   randomTime = startTime + randomGenerator * (endTime - startTime)
   randomDate = time.strftime(dateFormat, time.localtime(randomTime))
   return randomDate

print("Random Date =", getRndomDate("2020-01-01", "2020-12-31"))