import math
import fractions
from fractions import Fraction
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
import copy
import string
import os
from decimal import *

def sieveOfE(theMax):
	currList = range(2, theMax)
	prevSize = len(currList)
	ind = 0
	val = currList[ind]
	currList = [x for x in currList if x == val or x%val != 0]
	currSize = len(currList)
	ind = ind + 1
	while prevSize != currSize:
		prevSize = currSize
		val = currList[ind]
		currList = [x for x in currList if x == val or x%val != 0]
		currSize = len(currList)
		ind = ind + 1

	return currList


def isTruncatable(n, listPrimes):
	digits = [i for i in str(n)]
	for x in range(1, len(digits) + 1):
		print "".join(digits[0:x])
		if int("".join(digits[0:x])) not in listPrimes:
			return False
	for x in range(len(digits) - 1, -1, -1):
		print "".join(digits[x:])
		if int("".join(digits[x:])) not in listPrimes:
			return False
	return True
def isPrime(n):
	for x in range(2, int(n**0.5) + 1):
		if n%x == 0:
			return False
	return True

def euler37():
	primesList = sieveOfE(1000000)
	truncatables = []
	for a in primesList:
		if isTruncatable(a, primesList):
			truncatables = truncatables + [a]
	return truncatables


def euler31(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	else:
		return euler31(n - 1) + euler31(n - 2) + euler31(n - 5) + euler31(n - 10) + euler31(n - 20) + euler31(n - 50) + euler31(n - 100) + euler31(n - 200)


def euler31DP():
	currList = [1, 1]
	for n in range(2, 200):
		if n == 200:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5] + currList[n - 10] + currList[n - 20] + currList[n - 50] + currList[n - 100] + currList[n - 200]]
		elif n >= 100:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5] + currList[n - 10] + currList[n - 20] + currList[n - 50] + currList[n - 100]]
		elif n >= 50:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5] + currList[n - 10] + currList[n - 20] + currList[n - 50]]
		elif n >= 20:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5] + currList[n - 10] + currList[n - 20]]
		elif n >= 10:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5] + currList[n - 10]]
		elif n >= 5:
			currList = currList + [currList[n - 1] + currList[n - 2] + currList[n - 5]]
		elif n >= 2:
			currList = currList + [currList[n - 1] + currList[n - 2]]
		else:
			currList = currList + [currList[n - 1]]
	return currList[len(currList) - 1]

def euler76():
    return numSums(100, range(99, 0, -1), 0)

def euler97():
	return (28433 * pow(2, 7830457, 10000000000) + 1)%10000000000
def sumList(l):
	currVal = 0
	for x in l:
		currVal = currVal + x
	return currVal

def lenConsecSum(n, l):
	theList = [range(x,y) for x in range(0, len(l)) for y in range(x + 2, len(l)) if sumList(l[x:y]) == n]
	rangeMax = 0
	for x in theList:
		currLen = len(x)
		if currLen > rangeMax:
			rangeMax = currLen
	return rangeMax

def euler50():
	primes = sieveOfE(1000000)
	theSum = sumList(primes)
	ind = len(primes) - 1
	while theSum not in primes:
		theSum = theSum - primes[ind]
		ind = ind - 1
	return (ind + 1, theSum)

def existsArithmeticSeq(l):
	if len(l) < 3:
		return []
	else:
		diffs = [abs(x - y) for x in l for y in l if x != y]
		counts = [a for a in diffs if diffs.count(a) >2]
		return counts

def checkPerm(a,b):
    l = [i for i in str(a)]
    li = [int(''.join(x)) for x in permutations(l, len(l))]
    return a + b in li and a + 2*b in li

def euler49():

    fourDig = [x for x in range(1000, 10000)]
    primes = sieveOfE(10000)
    fDigPrimes = set(primes).intersection(set(fourDig))
    curr = []
    for y in range(1, 5000):
        l = [x for x in fDigPrimes if x + y in primes and x + 2*y in primes and checkPerm(x,y)]
        if len(l) != 0:
            curr = curr + [(l, y)]
    return curr

def sumSqDig(n):
	return sumList([int(i)**2 for i in str(n)])

def euler92():
	count = 0
	for x in range(1,10000000):
		y = x
		while y != 1 and y!= 89:
			y = sumSqDig(y)
		if y == 89:
			count = count + 1
	return count

def anyTwo(a,b,c,d, primes):
	l = [a,b,c,d]
	li = [int(str(x) + str(y)) for x in l for y in l if x != y]
	if set(li).issubset(primes):
		return True
	return False

def getDivisors(n):
	divisors = [1]
	for x in range(2, int(n**0.5) + 1):
		if n%x == 0:
			divisors = divisors + [x,n/x]
	return set(divisors)

def isAbundant(n):
	l = getDivisors(n)
	if sumList(l) > n:
		return True
	return False

def euler23():
	abundant = []
	for x in range(1, 28124):
		if isAbundant(x):
			abundant = abundant + [x]
	sums = set([x + y for x in abundant for y in abundant])
	allNums = set(range(1,28124))
	nonSumAb = allNums.difference(sums)
	return sumList(nonSumAb)

def numDig(n):
	return len([i for i in str(n)])

def euler63():
	count =0
	for x in range(1, 10):
		for a in range(1,22):
			if numDig(x**a) == a:
				count = count + 1
	return count

def euler75():
	l = []
	for a in range(1, 375001):
		for b in range(a, 500001):
			c_sq = a**2 + b**2
			c = c_sq**0.5
			if int(c) ** 2 == c_sq:
				l = l + [a + b + c]
	return l

def detRepLen(n):#assuming n has a repeating sequence
    powOfTen = 1
    remainders = []
    count = 0
    while True:
        while powOfTen < n:
            powOfTen = powOfTen * 10
        rem = powOfTen%n
        if rem == 0:
            break
        elif rem in remainders:
            return count
        else:
            remainders = remainders + [rem]
            count = count + 1
            powOfTen = rem
    return -1



def euler26():
    powOf2 = [x for x in range(1, 10) if 2**int(math.log(x, 2)) == x]
    powOf5 = [x for x in range(1, 5) if 5**int(math.log(x, 5)) == x]
    nonRep = set([x * y for x in powOf2 for y in powOf5])
    repSeq = set(range(1,1000)).difference(nonRep)
    maxNum = 0
    currMax = 0
    for x in repSeq:
        curr = detRepLen(x)
        if curr > currMax:
            maxNum = x
            currMax = curr
    return (maxNum, currMax)

def getPrimeFactors(n, primes):
	factors = []
	for x in primes:
		if n == 1:
			break
		if n%x == 0:
			factors = factors + [x]
			while n%x == 0:
				n = n/x
	if n != 1:
		print "More Primes!"
	return factors

def verifyFourConsecPrimes(n, primes):
    s1 = getPrimeFactors(n, primes)
    s2 = getPrimeFactors(n+1, primes)
    s3 = getPrimeFactors(n+2, primes)
    s4 = getPrimeFactors(n+3, primes)
    return len(s1) == 4 and len(s2) == 4 and len(s3) == 4 and len(s4) == 4



def euler47():
    l = sieveOfE(1000000)
    for n in range(1, 1000000):
        if verifyFourConsecPrimes(n, l):
            return n
    return -1

def generateDiag(n):
	count = 0
	l = []
	start = 1
	diff = 2
	while count < n:
		for x in range(0,4):
			start = start + diff
			l = l + [start]
			count = count + 1
		diff = diff + 2
	return l


def euler58():
	primes = sieveOfE(30000000)
	l = generateDiag(15000)
	return float(len(set(l).intersection(set(primes))))/len(l)

def generateTri(n):
        return [x*(x+1)/2 for x in range(1,n)]

def generateSq(n):
        return [x**2 for x in range(1,n)]

def generatePen(n):
        return [x*(3*x - 1)/2 for x in range(1,n)]

def generateHex(n):
        return [x*(2*x - 1) for x in range(1,n)]

def generateHept(n):
        return [x*(5*x - 3)/2 for x in range(1,n)]

def generateOct(n):
        return [x*(3*x - 2) for x in range(1,n)]

def euler44():
	l = generateTri(2500)
	a = [(x,y) for x in l for y in l if x - y in l and x + y in l]
	return a


def euler46(n):
	primes = sieveOfE(n)
	oddComp = set(range(1, n, 2)).difference(set(primes))
	squares = [x**2 for x in range(1,n)]
	primeSq = [x + 2*s for x in primes for s in squares]
	return oddComp.difference(set(primeSq))

def euler50Test(n):
	primes = sieveOfE(1000000)
	currSum = 0
	start = 0
	end = n
	for x in range(0, n):
		currSum = currSum + primes[x]
	if currSum in primes:
		return currSum
	else:
		while end < len(primes):
			if currSum > 1000000:
				break
			currSum = currSum + primes[end]
			currSum = currSum - primes[start]
			start = start + 1
			end = end + 1
			if currSum in primes:
				return currSum
	return -1

def euler50():
	xMax = (0, 0)
	for x in range(505, 550):
                res = euler50Test(x)
		if euler50Test(x) != -1:
			xMax = (x, res)
	return xMax

def replaceDig( n, rep ):
    allReps = []
    i = range(1,10)
    l = [i for i in str(n)]
    combs = [x for x in combinations(range(0, len(l)), rep)]

    for x in combs:
        a = copy.deepcopy(l)
        for p in range(0,10):
            for y in x:
                a[y] = p
            b = [str(i) for i in a]
            allReps = allReps + [int("".join(b))]
    return set(allReps)

def confirm8DigPrimeFam(n, indices, primes):
    l = [i for i in str(n)]
    count = 0
    for x in range(0,10):
        b = copy.copy(l)
        for y in indices:
            b[y] = str(x)
        if int("".join(b)) in primes:
            count = count + 1
    return count == 8

def constructIndices(numDig):
    return permutations(set(range( 0, numDig - 1 )), 2)#the one's place will never allow an 8 dig prime fam


def euler51():
    primes = sieveOfE(1000000)

    currPrimes = [x for x in primes if len(str(x)) == 6]
    for x in currPrimes:
        l = [int(i) for i in str(x)]
        #good = [x for x in combinations(range(0,5),2) if (sumList(l) - l[x[0]] - l[x[1]]) % 3 != 0]
        for indices in good:
            if confirm8DigPrimeFam(x, indices, currPrimes):
                return x
    return -1

def processNum(n):

    singDig = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    doubDigTens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    doubDig = ["twenty","thirty","forty","fifty", "sixty", "seventy", "eighty", "ninety"]
    if n == 0:
        return 0
    if n < 10:
        return len(singDig[n - 1])
    elif n < 20:
        return len(doubDigTens[n - 10])
    else:
        l = [int(i) for i in str(n)]
        print l
        totStr = ""
        if len(l) == 2:
            totStr = totStr + doubDig[l[0] - 2]
            if l[1] == 0:
                return len(totStr)
            else:
                totStr = totStr + singDig[l[1] - 1]
                print totStr
                return len(totStr)
        elif len(l) == 3:
            hPlace = singDig[l[0] - 1] + "hundred"
            other = [str(x) for x in l[1:]]
            if n%100 != 0:
                return len(hPlace) + len('and') + processNum(int("".join(other)))
            else:
                return len(hPlace)
        elif len(l) == 4:
            return len("onethousand")

def euler17():
    curr = 0
    for val in range(1, 1001):
        curr = curr + processNum(val)
    return curr

def constructGraphEdge(edges):#assumes the edges are tuples or lists
    graph = {}
    lnodes = [a for (a,b) in edges]
    rnodes = [b for (a,b) in edges]
    nodes = list(set(lnodes + rnodes))
    for i in nodes:
        curr = []
        l = [x for x in edges if i in x]
        for (a,b) in l:
            if a == i:
                curr = curr + [b]
            else:
                curr = curr + [a]
        graph[i] = list(set(curr))
    return graph

def confirmPPSet(l, primes):
    if len(l) != 4:
        print "......bad, very bad"
        return False
    if set(l).issubset(set(primes)):
        cons = [int(str(a) + str(b)) for a in l for b in l if a != b]
        for x in cons:
            if x not in primes:
                return False
        return True

    else:
        return False


def euler31():
    coins = [1,2,5,10,20,50,100,200]
    allComb = [x for x in combinations_with_replacement(coins, 1)]
    for i in range(2, 41):
        allComb = allComb + [x for x in combinations_with_replacement(coins, i)]
    return allComb
    #return [y for y in allComb if sumList(y) == 200]

def genCubes(n):
    return [x**3 for x in range(1,n)]

def genCubes(a,b):
    return [x**3 for x in range(a,b)]


def euler62():
    c = genCubes(1450, 1650)
    l = []
    cubes = len(c)
    for y in range(1, 12):
        l = l + [[x for x in c if len(str(x)) == y]]
    for p in range(1, cubes):
        num = c[p]
        digs = [i for i in str(num)]
        a = [int("".join(x)) for x in permutations(digs)]
        if len(set(a).intersection(set(l[len(str(num)) - 1]))) == 5:
            return num
    return -1


def euler54():

    l = [["8C", "TS", "KC", "9H", "4S", "7D", "2S", "5D", "3S", "AC"],
    ["5C", "AD", "5D", "AC", "9C", "7C", "5H", "8D", "TD", "KS"],
    ["3H", "7H", "6S", "KC", "JS", "QH", "TD", "JC", "2D", "8S"],
    ["TH", "8H", "5C", "QS", "TC", "9H", "4D", "JC", "KS", "JS"],
    ["7C", "5H", "KC", "QH", "JD", "AS", "KH", "4C", "AD", "4S"],
    ["5H", "KS", "9C", "7D", "9H", "8D", "3S", "5D", "5C", "AH"],
    ["6H", "4H", "5C", "3H", "2H", "3S", "QH", "5S", "6S", "AS"],
    ["TD", "8C", "4H", "7C", "TC", "KC", "4C", "3H", "7S", "KS"],
    ["7C", "9C", "6D", "KD", "3H", "4C", "QS", "QC", "AC", "KH"],
    ["JC", "6S", "5H", "2H", "2D", "KD", "9D", "7C", "AS", "JS"],
    ["AD", "QH", "TH", "9D", "8H", "TS", "6D", "3S", "AS", "AC"],
    ["2H", "4S", "5C", "5S", "TC", "KC", "JD", "6C", "TS", "3C"],
    ["QD", "AS", "6H", "JS", "2C", "3D", "9H", "KC", "4H", "8S"],
    ["KD", "8S", "9S", "7C", "2S", "3S", "6D", "6S", "4H", "KC"],
    ["3C", "8C", "2D", "7D", "4D", "9S", "4S", "QH", "4H", "JD"],
    ["8C", "KC", "7S", "TC", "2D", "TS", "8H", "QD", "AC", "5C"],
    ["3D", "KH", "QD", "6C", "6S", "AD", "AS", "8H", "2H", "QS"],
    ["6S", "8D", "4C", "8S", "6C", "QH", "TC", "6D", "7D", "9D"],
    ["2S", "8D", "8C", "4C", "TS", "9S", "9D", "9C", "AC", "3D"],
    ["3C", "QS", "2S", "4H", "JH", "3D", "2D", "TD", "8S", "9H"],
    ["5H", "QS", "8S", "6D", "3C", "8C", "JD", "AS", "7H", "7D"],
    ["6H", "TD", "9D", "AS", "JH", "6C", "QC", "9S", "KD", "JC"],
    ["AH", "8S", "QS", "4D", "TH", "AC", "TS", "3C", "3D", "5C"],
    ["5S", "4D", "JS", "3D", "8H", "6C", "TS", "3S", "AD", "8C"],
    ["6D", "7C", "5D", "5H", "3S", "5C", "JC", "2H", "5S", "3D"],
    ["5H", "6H", "2S", "KS", "3D", "5D", "JD", "7H", "JS", "8H"],
    ["KH", "4H", "AS", "JS", "QS", "QC", "TC", "6D", "7C", "KS"],
    ["3D", "QS", "TS", "2H", "JS", "4D", "AS", "9S", "JC", "KD"],
    ["QD", "5H", "4D", "5D", "KH", "7H", "3D", "JS", "KD", "4H"],
    ["2C", "9H", "6H", "5C", "9D", "6C", "JC", "2D", "TH", "9S"],
    ["7D", "6D", "AS", "QD", "JH", "4D", "JS", "7C", "QS", "5C"],
    ["3H", "KH", "QD", "AD", "8C", "8H", "3S", "TH", "9D", "5S"],
    ["AH", "9S", "4D", "9D", "8S", "4H", "JS", "3C", "TC", "8D"],
    ["2C", "KS", "5H", "QD", "3S", "TS", "9H", "AH", "AD", "8S"],
    ["5C", "7H", "5D", "KD", "9H", "4D", "3D", "2D", "KS", "AD"],
    ["KS", "KC", "9S", "6D", "2C", "QH", "9D", "9H", "TS", "TC"],
    ["9C", "6H", "5D", "QH", "4D", "AD", "6D", "QC", "JS", "KH"],
    ["9S", "3H", "9D", "JD", "5C", "4D", "9H", "AS", "TC", "QH"],
    ["2C", "6D", "JC", "9C", "3C", "AD", "9S", "KH", "9D", "7D"],
    ["KC", "9C", "7C", "JC", "JS", "KD", "3H", "AS", "3C", "7D"],
    ["QD", "KH", "QS", "2C", "3S", "8S", "8H", "9H", "9C", "JC"],
    ["QH", "8D", "3C", "KC", "4C", "4H", "6D", "AD", "9H", "9D"],
    ["3S", "KS", "QS", "7H", "KH", "7D", "5H", "5D", "JD", "AD"],
    ["2H", "2C", "6H", "TH", "TC", "7D", "8D", "4H", "8C", "AS"],
    ["4S", "2H", "AC", "QC", "3S", "6D", "TH", "4D", "4C", "KH"],
    ["4D", "TC", "KS", "AS", "7C", "3C", "6D", "2D", "9H", "6C"],
    ["8C", "TD", "5D", "QS", "2C", "7H", "4C", "9C", "3H", "9H"],
    ["5H", "JH", "TS", "7S", "TD", "6H", "AD", "QD", "8H", "8S"],
    ["5S", "AD", "9C", "8C", "7C", "8D", "5H", "9D", "8S", "2S"],
    ["4H", "KH", "KS", "9S", "2S", "KC", "5S", "AD", "4S", "7D"],
    ["QS", "9C", "QD", "6H", "JS", "5D", "AC", "8D", "2S", "AS"],
    ["KH", "AC", "JC", "3S", "9D", "9S", "3C", "9C", "5S", "JS"],
    ["AD", "3C", "3D", "KS", "3S", "5C", "9C", "8C", "TS", "4S"],
    ["JH", "8D", "5D", "6H", "KD", "QS", "QD", "3D", "6C", "KC"],
    ["8S", "JD", "6C", "3S", "8C", "TC", "QC", "3C", "QH", "JS"],
    ["KC", "JC", "8H", "2S", "9H", "9C", "JH", "8S", "8C", "9S"],
    ["8S", "2H", "QH", "4D", "QC", "9D", "KC", "AS", "TH", "3C"],
    ["8S", "6H", "TH", "7C", "2H", "6S", "3C", "3H", "AS", "7S"],
    ["QH", "5S", "JS", "4H", "5H", "TS", "8H", "AH", "AC", "JC"],
    ["9D", "8H", "2S", "4S", "TC", "JC", "3C", "7H", "3H", "5C"],
    ["3D", "AD", "3C", "3S", "4C", "QC", "AS", "5D", "TH", "8C"],
    ["6S", "9D", "4C", "JS", "KH", "AH", "TS", "JD", "8H", "AD"],
    ["4C", "6S", "9D", "7S", "AC", "4D", "3D", "3S", "TC", "JD"],
    ["AD", "7H", "6H", "4H", "JH", "KC", "TD", "TS", "7D", "6S"],
    ["8H", "JH", "TC", "3S", "8D", "8C", "9S", "2C", "5C", "4D"],
    ["2C", "9D", "KC", "QH", "TH", "QS", "JC", "9C", "4H", "TS"],
    ["QS", "3C", "QD", "8H", "KH", "4H", "8D", "TD", "8S", "AC"],
    ["7C", "3C", "TH", "5S", "8H", "8C", "9C", "JD", "TC", "KD"],
    ["QC", "TC", "JD", "TS", "8C", "3H", "6H", "KD", "7C", "TD"],
    ["JH", "QS", "KS", "9C", "6D", "6S", "AS", "9H", "KH", "6H"],
    ["2H", "4D", "AH", "2D", "JH", "6H", "TD", "5D", "4H", "JD"],
    ["KD", "8C", "9S", "JH", "QD", "JS", "2C", "QS", "5C", "7C"],
    ["4S", "TC", "7H", "8D", "2S", "6H", "7S", "9C", "7C", "KC"],
    ["8C", "5D", "7H", "4S", "TD", "QC", "8S", "JS", "4H", "KS"],
    ["AD", "8S", "JH", "6D", "TD", "KD", "7C", "6C", "2D", "7D"],
    ["JC", "6H", "6S", "JS", "4H", "QH", "9H", "AH", "4C", "3C"],
    ["6H", "5H", "AS", "7C", "7S", "3D", "KH", "KC", "5D", "5C"],
    ["JC", "3D", "TD", "AS", "4D", "6D", "6S", "QH", "JD", "KS"],
    ["8C", "7S", "8S", "QH", "2S", "JD", "5C", "7H", "AH", "QD"],
    ["8S", "3C", "6H", "6C", "2C", "8D", "TD", "7D", "4C", "4D"],
    ["5D", "QH", "KH", "7C", "2S", "7H", "JS", "6D", "QC", "QD"],
    ["AD", "6C", "6S", "7D", "TH", "6H", "2H", "8H", "KH", "4H"],
    ["KS", "JS", "KD", "5D", "2D", "KH", "7D", "9C", "8C", "3D"],
    ["9C", "6D", "QD", "3C", "KS", "3S", "7S", "AH", "JD", "2D"],
    ["AH", "QH", "AS", "JC", "8S", "8H", "4C", "KC", "TH", "7D"],
    ["JC", "5H", "TD", "7C", "5D", "KD", "4C", "AD", "8H", "JS"],
    ["KC", "2H", "AC", "AH", "7D", "JH", "KH", "5D", "7S", "6D"],
    ["9S", "5S", "9C", "6H", "8S", "TD", "JD", "9H", "6C", "AC"],
    ["7D", "8S", "6D", "TS", "KD", "7H", "AC", "5S", "7C", "5D"],
    ["AH", "QC", "JC", "4C", "TC", "8C", "2H", "TS", "2C", "7D"],
    ["KD", "KC", "6S", "3D", "7D", "2S", "8S", "3H", "5S", "5C"],
    ["8S", "5D", "8H", "4C", "6H", "KC", "3H", "7C", "5S", "KD"],
    ["JH", "8C", "3D", "3C", "6C", "KC", "TD", "7H", "7C", "4C"],
    ["JC", "KC", "6H", "TS", "QS", "TD", "KS", "8H", "8C", "9S"],
    ["6C", "5S", "9C", "QH", "7D", "AH", "KS", "KC", "9S", "2C"],
    ["4D", "4S", "8H", "TD", "9C", "3S", "7D", "9D", "AS", "TH"],
    ["6S", "7D", "3C", "6H", "5D", "KD", "2C", "5C", "9D", "9C"],
    ["2H", "KC", "3D", "AD", "3H", "QD", "QS", "8D", "JC", "4S"],
    ["8C", "3H", "9C", "7C", "AD", "5D", "JC", "9D", "JS", "AS"],
    ["5D", "9H", "5C", "7H", "6S", "6C", "QC", "JC", "QD", "9S"],
    ["JC", "QS", "JH", "2C", "6S", "9C", "QC", "3D", "4S", "TC"],
    ["4H", "5S", "8D", "3D", "4D", "2S", "KC", "2H", "JS", "2C"],
    ["TD", "3S", "TH", "KD", "4D", "7H", "JH", "JS", "KS", "AC"],
    ["7S", "8C", "9S", "2D", "8S", "7D", "5C", "AD", "9D", "AS"],
    ["8C", "7H", "2S", "6C", "TH", "3H", "4C", "3S", "8H", "AC"],
    ["KD", "5H", "JC", "8H", "JD", "2D", "4H", "TD", "JH", "5C"],
    ["3D", "AS", "QH", "KS", "7H", "JD", "8S", "5S", "6D", "5H"],
    ["9S", "6S", "TC", "QS", "JC", "5C", "5D", "9C", "TH", "8C"],
    ["5H", "3S", "JH", "9H", "2S", "2C", "6S", "7S", "AS", "KS"],
    ["8C", "QD", "JC", "QS", "TC", "QC", "4H", "AC", "KH", "6C"],
    ["TC", "5H", "7D", "JH", "4H", "2H", "8D", "JC", "KS", "4D"],
    ["5S", "9C", "KH", "KD", "9H", "5C", "TS", "3D", "7D", "2D"],
    ["5H", "AS", "TC", "4D", "8C", "2C", "TS", "9D", "3H", "8D"],
    ["6H", "8D", "2D", "9H", "JD", "6C", "4S", "5H", "5S", "6D"],
    ["AD", "9C", "JC", "7D", "6H", "9S", "6D", "JS", "9H", "3C"],
    ["AD", "JH", "TC", "QS", "4C", "5D", "9S", "7C", "9C", "AH"],
    ["KD", "6H", "2H", "TH", "8S", "QD", "KS", "9D", "9H", "AS"],
    ["4H", "8H", "8D", "5H", "6C", "AH", "5S", "AS", "AD", "8S"],
    ["QS", "5D", "4S", "2H", "TD", "KS", "5H", "AC", "3H", "JC"],
    ["9C", "7D", "QD", "KD", "AC", "6D", "5H", "QH", "6H", "5S"],
    ["KC", "AH", "QH", "2H", "7D", "QS", "3H", "KS", "7S", "JD"],
    ["6C", "8S", "3H", "6D", "KS", "QD", "5D", "5C", "8H", "TC"],
    ["9H", "4D", "4S", "6S", "9D", "KH", "QC", "4H", "6C", "JD"],
    ["TD", "2D", "QH", "4S", "6H", "JH", "KD", "3C", "QD", "8C"],
    ["4S", "6H", "7C", "QD", "9D", "AS", "AH", "6S", "AD", "3C"],
    ["2C", "KC", "TH", "6H", "8D", "AH", "5C", "6D", "8S", "5D"],
    ["TD", "TS", "7C", "AD", "JC", "QD", "9H", "3C", "KC", "7H"],
    ["5D", "4D", "5S", "8H", "4H", "7D", "3H", "JD", "KD", "2D"],
    ["JH", "TD", "6H", "QS", "4S", "KD", "5C", "8S", "7D", "8H"],
    ["AC", "3D", "AS", "8C", "TD", "7H", "KH", "5D", "6C", "JD"],
    ["9D", "KS", "7C", "6D", "QH", "TC", "JD", "KD", "AS", "KC"],
    ["JH", "8S", "5S", "7S", "7D", "AS", "2D", "3D", "AD", "2H"],
    ["2H", "5D", "AS", "3C", "QD", "KC", "6H", "9H", "9S", "2C"],
    ["9D", "5D", "TH", "4C", "JH", "3H", "8D", "TC", "8H", "9H"],
    ["6H", "KD", "2C", "TD", "2H", "6C", "9D", "2D", "JS", "8C"],
    ["KD", "7S", "3C", "7C", "AS", "QH", "TS", "AD", "8C", "2S"],
    ["QS", "8H", "6C", "JS", "4C", "9S", "QC", "AD", "TD", "TS"],
    ["2H", "7C", "TS", "TC", "8C", "3C", "9H", "2D", "6D", "JC"],
    ["TC", "2H", "8D", "JH", "KS", "6D", "3H", "TD", "TH", "8H"],
    ["9D", "TD", "9H", "QC", "5D", "6C", "8H", "8C", "KC", "TS"],
    ["2H", "8C", "3D", "AH", "4D", "TH", "TC", "7D", "8H", "KC"],
    ["TS", "5C", "2D", "8C", "6S", "KH", "AH", "5H", "6H", "KC"],
    ["5S", "5D", "AH", "TC", "4C", "JD", "8D", "6H", "8C", "6C"],
    ["KC", "QD", "3D", "8H", "2D", "JC", "9H", "4H", "AD", "2S"],
    ["TD", "6S", "7D", "JS", "KD", "4H", "QS", "2S", "3S", "8C"],
    ["4C", "9H", "JH", "TS", "3S", "4H", "QC", "5S", "9S", "9C"],
    ["2C", "KD", "9H", "JS", "9S", "3H", "JC", "TS", "5D", "AC"],
    ["AS", "2H", "5D", "AD", "5H", "JC", "7S", "TD", "JS", "4C"],
    ["2D", "4S", "8H", "3D", "7D", "2C", "AD", "KD", "9C", "TS"],
    ["7H", "QD", "JH", "5H", "JS", "AC", "3D", "TH", "4C", "8H"],
    ["6D", "KH", "KC", "QD", "5C", "AD", "7C", "2D", "4H", "AC"],
    ["3D", "9D", "TC", "8S", "QD", "2C", "JC", "4H", "JD", "AH"],
    ["6C", "TD", "5S", "TC", "8S", "AH", "2C", "5D", "AS", "AC"],
    ["TH", "7S", "3D", "AS", "6C", "4C", "7H", "7D", "4H", "AH"],
    ["5C", "2H", "KS", "6H", "7S", "4H", "5H", "3D", "3C", "7H"],
    ["3C", "9S", "AC", "7S", "QH", "2H", "3D", "6S", "3S", "3H"],
    ["2D", "3H", "AS", "2C", "6H", "TC", "JS", "6S", "9C", "6C"],
    ["QH", "KD", "QD", "6D", "AC", "6H", "KH", "2C", "TS", "8C"],
    ["8H", "7D", "3S", "9H", "5D", "3H", "4S", "QC", "9S", "5H"],
    ["2D", "9D", "7H", "6H", "3C", "8S", "5H", "4D", "3S", "4S"],
    ["KD", "9S", "4S", "TC", "7S", "QC", "3S", "8S", "2H", "7H"],
    ["TC", "3D", "8C", "3H", "6C", "2H", "6H", "KS", "KD", "4D"],
    ["KC", "3D", "9S", "3H", "JS", "4S", "8H", "2D", "6C", "8S"],
    ["6H", "QS", "6C", "TC", "QD", "9H", "7D", "7C", "5H", "4D"],
    ["TD", "9D", "8D", "6S", "6C", "TC", "5D", "TS", "JS", "8H"],
    ["4H", "KC", "JD", "9H", "TC", "2C", "6S", "5H", "8H", "AS"],
    ["JS", "9C", "5C", "6S", "9D", "JD", "8H", "KC", "4C", "6D"],
    ["4D", "8D", "8S", "6C", "7C", "6H", "7H", "8H", "5C", "KC"],
    ["TC", "3D", "JC", "6D", "KS", "9S", "6H", "7S", "9C", "2C"],
    ["6C", "3S", "KD", "5H", "TS", "7D", "9H", "9S", "6H", "KH"],
    ["3D", "QD", "4C", "6H", "TS", "AC", "3S", "5C", "2H", "KD"],
    ["4C", "AS", "JS", "9S", "7C", "TS", "7H", "9H", "JC", "KS"],
    ["4H", "8C", "JD", "3H", "6H", "AD", "9S", "4S", "5S", "KS"],
    ["4C", "2C", "7D", "3D", "AS", "9C", "2S", "QS", "KC", "6C"],
    ["8S", "5H", "3D", "2S", "AC", "9D", "6S", "3S", "4D", "TD"],
    ["QD", "TH", "7S", "TS", "3D", "AC", "7H", "6C", "5D", "QC"],
    ["TC", "QD", "AD", "9C", "QS", "5C", "8D", "KD", "3D", "3C"],
    ["9D", "8H", "AS", "3S", "7C", "8S", "JD", "2D", "8D", "KC"],
    ["4C", "TH", "AC", "QH", "JS", "8D", "7D", "7S", "9C", "KH"],
    ["9D", "8D", "4C", "JH", "2C", "2S", "QD", "KD", "TS", "4H"],
    ["4D", "6D", "5D", "2D", "JH", "3S", "8S", "3H", "TC", "KH"],
    ["AD", "4D", "2C", "QS", "8C", "KD", "JH", "JD", "AH", "5C"],
    ["5C", "6C", "5H", "2H", "JH", "4H", "KS", "7C", "TC", "3H"],
    ["3C", "4C", "QC", "5D", "JH", "9C", "QD", "KH", "8D", "TC"],
    ["3H", "9C", "JS", "7H", "QH", "AS", "7C", "9H", "5H", "JC"],
    ["2D", "5S", "QD", "4S", "3C", "KC", "6S", "6C", "5C", "4C"],
    ["5D", "KH", "2D", "TS", "8S", "9C", "AS", "9S", "7C", "4C"],
    ["7C", "AH", "8C", "8D", "5S", "KD", "QH", "QS", "JH", "2C"],
    ["8C", "9D", "AH", "2H", "AC", "QC", "5S", "8H", "7H", "2C"],
    ["QD", "9H", "5S", "QS", "QC", "9C", "5H", "JC", "TH", "4H"],
    ["6C", "6S", "3H", "5H", "3S", "6H", "KS", "8D", "AC", "7S"],
    ["AC", "QH", "7H", "8C", "4S", "KC", "6C", "3D", "3S", "TC"],
    ["9D", "3D", "JS", "TH", "AC", "5H", "3H", "8S", "3S", "TC"],
    ["QD", "KH", "JS", "KS", "9S", "QC", "8D", "AH", "3C", "AC"],
    ["5H", "6C", "KH", "3S", "9S", "JH", "2D", "QD", "AS", "8C"],
    ["6C", "4D", "7S", "7H", "5S", "JC", "6S", "9H", "4H", "JH"],
    ["AH", "5S", "6H", "9S", "AD", "3S", "TH", "2H", "9D", "8C"],
    ["4C", "8D", "9H", "7C", "QC", "AD", "4S", "9C", "KC", "5S"],
    ["9D", "6H", "4D", "TC", "4C", "JH", "2S", "5D", "3S", "AS"],
    ["2H", "6C", "7C", "KH", "5C", "AD", "QS", "TH", "JD", "8S"],
    ["3S", "4S", "7S", "AH", "AS", "KC", "JS", "2S", "AD", "TH"],
    ["JS", "KC", "2S", "7D", "8C", "5C", "9C", "TS", "5H", "9D"],
    ["7S", "9S", "4D", "TD", "JH", "JS", "KH", "6H", "5D", "2C"],
    ["JD", "JS", "JC", "TH", "2D", "3D", "QD", "8C", "AC", "5H"],
    ["7S", "KH", "5S", "9D", "5D", "TD", "4S", "6H", "3C", "2D"],
    ["4S", "5D", "AC", "8D", "4D", "7C", "AD", "AS", "AH", "9C"],
    ["6S", "TH", "TS", "KS", "2C", "QC", "AH", "AS", "3C", "4S"],
    ["2H", "8C", "3S", "JC", "5C", "7C", "3H", "3C", "KH", "JH"],
    ["7S", "3H", "JC", "5S", "6H", "4C", "2S", "4D", "KC", "7H"],
    ["4D", "7C", "4H", "9S", "8S", "6S", "AD", "TC", "6C", "JC"],
    ["KH", "QS", "3S", "TC", "4C", "8H", "8S", "AC", "3C", "TS"],
    ["QD", "QS", "TH", "3C", "TS", "7H", "7D", "AH", "TD", "JC"],
    ["TD", "JD", "QC", "4D", "9S", "7S", "TS", "AD", "7D", "AC"],
    ["AH", "7H", "4S", "6D", "7C", "2H", "9D", "KS", "JC", "TD"],
    ["7C", "AH", "JD", "4H", "6D", "QS", "TS", "2H", "2C", "5C"],
    ["TC", "KC", "8C", "9S", "4C", "JS", "3C", "JC", "6S", "AH"],
    ["AS", "7D", "QC", "3D", "5S", "JC", "JD", "9D", "TD", "KH"],
    ["TH", "3C", "2S", "6H", "AH", "AC", "5H", "5C", "7S", "8H"],
    ["QC", "2D", "AC", "QD", "2S", "3S", "JD", "QS", "6S", "8H"],
    ["KC", "4H", "3C", "9D", "JS", "6H", "3S", "8S", "AS", "8C"],
    ["7H", "KC", "7D", "JD", "2H", "JC", "QH", "5S", "3H", "QS"],
    ["9H", "TD", "3S", "8H", "7S", "AC", "5C", "6C", "AH", "7C"],
    ["8D", "9H", "AH", "JD", "TD", "QS", "7D", "3S", "9C", "8S"],
    ["AH", "QH", "3C", "JD", "KC", "4S", "5S", "5D", "TD", "KS"],
    ["9H", "7H", "6S", "JH", "TH", "4C", "7C", "AD", "5C", "2D"],
    ["7C", "KD", "5S", "TC", "9D", "6S", "6C", "5D", "2S", "TH"],
    ["KC", "9H", "8D", "5H", "7H", "4H", "QC", "3D", "7C", "AS"],
    ["6S", "8S", "QC", "TD", "4S", "5C", "TH", "QS", "QD", "2S"],
    ["8S", "5H", "TH", "QC", "9H", "6S", "KC", "7D", "7C", "5C"],
    ["7H", "KD", "AH", "4D", "KH", "5C", "4S", "2D", "KC", "QH"],
    ["6S", "2C", "TD", "JC", "AS", "4D", "6C", "8C", "4H", "5S"],
    ["JC", "TC", "JD", "5S", "6S", "8D", "AS", "9D", "AD", "3S"],
    ["6D", "6H", "5D", "5S", "TC", "3D", "7D", "QS", "9D", "QD"],
    ["4S", "6C", "8S", "3S", "7S", "AD", "KS", "2D", "7D", "7C"],
    ["KC", "QH", "JC", "AC", "QD", "5D", "8D", "QS", "7H", "7D"],
    ["JS", "AH", "8S", "5H", "3D", "TD", "3H", "4S", "6C", "JH"],
    ["4S", "QS", "7D", "AS", "9H", "JS", "KS", "6D", "TC", "5C"],
    ["2D", "5C", "6H", "TC", "4D", "QH", "3D", "9H", "8S", "6C"],
    ["6D", "7H", "TC", "TH", "5S", "JD", "5C", "9C", "KS", "KD"],
    ["8D", "TD", "QH", "6S", "4S", "6C", "8S", "KC", "5C", "TC"],
    ["5S", "3D", "KS", "AC", "4S", "7D", "QD", "4C", "TH", "2S"],
    ["TS", "8H", "9S", "6S", "7S", "QH", "3C", "AH", "7H", "8C"],
    ["4C", "8C", "TS", "JS", "QC", "3D", "7D", "5D", "7S", "JH"],
    ["8S", "7S", "9D", "QC", "AC", "7C", "6D", "2H", "JH", "KC"],
    ["JS", "KD", "3C", "6S", "4S", "7C", "AH", "QC", "KS", "5H"],
    ["KS", "6S", "4H", "JD", "QS", "TC", "8H", "KC", "6H", "AS"],
    ["KH", "7C", "TC", "6S", "TD", "JC", "5C", "7D", "AH", "3S"],
    ["3H", "4C", "4H", "TC", "TH", "6S", "7H", "6D", "9C", "QH"],
    ["7D", "5H", "4S", "8C", "JS", "4D", "3D", "8S", "QH", "KC"],
    ["3H", "6S", "AD", "7H", "3S", "QC", "8S", "4S", "7S", "JS"],
    ["3S", "JD", "KH", "TH", "6H", "QS", "9C", "6C", "2D", "QD"],
    ["4S", "QH", "4D", "5H", "KC", "7D", "6D", "8D", "TH", "5S"],
    ["TD", "AD", "6S", "7H", "KD", "KH", "9H", "5S", "KC", "JC"],
    ["3H", "QC", "AS", "TS", "4S", "QD", "KS", "9C", "7S", "KC"],
    ["TS", "6S", "QC", "6C", "TH", "TC", "9D", "5C", "5D", "KD"],
    ["JS", "3S", "4H", "KD", "4C", "QD", "6D", "9S", "JC", "9D"],
    ["8S", "JS", "6D", "4H", "JH", "6H", "6S", "6C", "KS", "KH"],
    ["AC", "7D", "5D", "TC", "9S", "KH", "6S", "QD", "6H", "AS"],
    ["AS", "7H", "6D", "QH", "8D", "TH", "2S", "KH", "5C", "5H"],
    ["4C", "7C", "3D", "QC", "TC", "4S", "KH", "8C", "2D", "JS"],
    ["6H", "5D", "7S", "5H", "9C", "9H", "JH", "8S", "TH", "7H"],
    ["AS", "JS", "2S", "QD", "KH", "8H", "4S", "AC", "8D", "8S"],
    ["3H", "4C", "TD", "KD", "8C", "JC", "5C", "QS", "2D", "JD"],
    ["TS", "7D", "5D", "6C", "2C", "QS", "2H", "3C", "AH", "KS"],
    ["4S", "7C", "9C", "7D", "JH", "6C", "5C", "8H", "9D", "QD"],
    ["2S", "TD", "7S", "6D", "9C", "9S", "QS", "KH", "QH", "5C"],
    ["JC", "6S", "9C", "QH", "JH", "8D", "7S", "JS", "KH", "2H"],
    ["8D", "5H", "TH", "KC", "4D", "4S", "3S", "6S", "3D", "QS"],
    ["2D", "JD", "4C", "TD", "7C", "6D", "TH", "7S", "JC", "AH"],
    ["QS", "7S", "4C", "TH", "9D", "TS", "AD", "4D", "3H", "6H"],
    ["2D", "3H", "7D", "JD", "3D", "AS", "2S", "9C", "QC", "8S"],
    ["4H", "9H", "9C", "2C", "7S", "JH", "KD", "5C", "5D", "6H"],
    ["TC", "9H", "8H", "JC", "3C", "9S", "8D", "KS", "AD", "KC"],
    ["TS", "5H", "JD", "QS", "QH", "QC", "8D", "5D", "KH", "AH"],
    ["5D", "AS", "8S", "6S", "4C", "AH", "QC", "QD", "TH", "7H"],
    ["3H", "4H", "7D", "6S", "4S", "9H", "AS", "8H", "JS", "9D"],
    ["JD", "8C", "2C", "9D", "7D", "5H", "5S", "9S", "JC", "KD"],
    ["KD", "9C", "4S", "QD", "AH", "7C", "AD", "9D", "AC", "TD"],
    ["6S", "4H", "4S", "9C", "8D", "KS", "TC", "9D", "JH", "7C"],
    ["5S", "JC", "5H", "4S", "QH", "AC", "2C", "JS", "2S", "9S"],
    ["8C", "5H", "AS", "QD", "AD", "5C", "7D", "8S", "QC", "TD"],
    ["JC", "4C", "8D", "5C", "KH", "QS", "4D", "6H", "2H", "2C"],
    ["TH", "4S", "2D", "KC", "3H", "QD", "AC", "7H", "AD", "9D"],
    ["KH", "QD", "AS", "8H", "TH", "KC", "8D", "7S", "QH", "8C"],
    ["JC", "6C", "7D", "8C", "KH", "AD", "QS", "2H", "6S", "2D"],
    ["JC", "KH", "2D", "7D", "JS", "QC", "5H", "4C", "5D", "AD"],
    ["TS", "3S", "AD", "4S", "TD", "2D", "TH", "6S", "9H", "JH"],
    ["9H", "2D", "QS", "2C", "4S", "3D", "KH", "AS", "AC", "9D"],
    ["KH", "6S", "8H", "4S", "KD", "7D", "9D", "TS", "QD", "QC"],
    ["JH", "5H", "AH", "KS", "AS", "AD", "JC", "QC", "5S", "KH"],
    ["5D", "7D", "6D", "KS", "KD", "3D", "7C", "4D", "JD", "3S"],
    ["AC", "JS", "8D", "5H", "9C", "3H", "4H", "4D", "TS", "2C"],
    ["6H", "KS", "KH", "9D", "7C", "2S", "6S", "8S", "2H", "3D"],
    ["6H", "AC", "JS", "7S", "3S", "TD", "8H", "3H", "4H", "TH"],
    ["9H", "TC", "QC", "KC", "5C", "KS", "6H", "4H", "AC", "8S"],
    ["TC", "7D", "QH", "4S", "JC", "TS", "6D", "6C", "AC", "KH"],
    ["QH", "7D", "7C", "JH", "QS", "QD", "TH", "3H", "5D", "KS"],
    ["3D", "5S", "8D", "JS", "4C", "2C", "KS", "7H", "9C", "4H"],
    ["5H", "8S", "4H", "TD", "2C", "3S", "QD", "QC", "3H", "KC"],
    ["QC", "JS", "KD", "9C", "AD", "5S", "9D", "7D", "7H", "TS"],
    ["8C", "JC", "KH", "7C", "7S", "6C", "TS", "2C", "QD", "TH"],
    ["5S", "9D", "TH", "3C", "7S", "QH", "8S", "9C", "2H", "5H"],
    ["5D", "9H", "6H", "2S", "JS", "KH", "3H", "7C", "2H", "5S"],
    ["JD", "5D", "5S", "2C", "TC", "2S", "6S", "6C", "3C", "8S"],
    ["4D", "KH", "8H", "4H", "2D", "KS", "3H", "5C", "2S", "9H"],
    ["3S", "2D", "TD", "7H", "8S", "6H", "JD", "KC", "9C", "8D"],
    ["6S", "QD", "JH", "7C", "9H", "5H", "8S", "8H", "TH", "TD"],
    ["QS", "7S", "TD", "7D", "TS", "JC", "KD", "7C", "3C", "2C"],
    ["3C", "JD", "8S", "4H", "2D", "2S", "TD", "AS", "4D", "AC"],
    ["AH", "KS", "6C", "4C", "4S", "7D", "8C", "9H", "6H", "AS"],
    ["5S", "3C", "9S", "2C", "QS", "KD", "4D", "4S", "AC", "5D"],
    ["2D", "TS", "2C", "JS", "KH", "QH", "5D", "8C", "AS", "KC"],
    ["KD", "3H", "6C", "TH", "8S", "7S", "KH", "6H", "9S", "AC"],
    ["6H", "7S", "6C", "QS", "AH", "2S", "2H", "4H", "5D", "5H"],
    ["5H", "JC", "QD", "2C", "2S", "JD", "AS", "QC", "6S", "7D"],
    ["6C", "TC", "AS", "KD", "8H", "9D", "2C", "7D", "JH", "9S"],
    ["2H", "4C", "6C", "AH", "8S", "TD", "3H", "TH", "7C", "TS"],
    ["KD", "4S", "TS", "6C", "QH", "8D", "9D", "9C", "AH", "7D"],
    ["6D", "JS", "5C", "QD", "QC", "9C", "5D", "8C", "2H", "KD"],
    ["3C", "QH", "JH", "AD", "6S", "AH", "KC", "8S", "6D", "6H"],
    ["3D", "7C", "4C", "7S", "5S", "3S", "6S", "5H", "JC", "3C"],
    ["QH", "7C", "5H", "3C", "3S", "8C", "TS", "4C", "KD", "9C"],
    ["QD", "3S", "7S", "5H", "7H", "QH", "JC", "7C", "8C", "KD"],
    ["3C", "KD", "KH", "2S", "4C", "TS", "AC", "6S", "2C", "7C"],
    ["2C", "KH", "3C", "4C", "6H", "4D", "5H", "5S", "7S", "QD"],
    ["4D", "7C", "8S", "QD", "TS", "9D", "KS", "6H", "KD", "3C"],
    ["QS", "4D", "TS", "7S", "4C", "3H", "QD", "8D", "9S", "TC"],
    ["TS", "QH", "AC", "6S", "3C", "9H", "9D", "QS", "8S", "6H"],
    ["3S", "7S", "5D", "4S", "JS", "2D", "6C", "QH", "6S", "TH"],
    ["4C", "4H", "AS", "JS", "5D", "3D", "TS", "9C", "AC", "8S"],
    ["6S", "9C", "7C", "3S", "5C", "QS", "AD", "AS", "6H", "3C"],
    ["9S", "8C", "7H", "3H", "6S", "7C", "AS", "9H", "JD", "KH"],
    ["3D", "3H", "7S", "4D", "6C", "7C", "AC", "2H", "9C", "TH"],
    ["4H", "5S", "3H", "AC", "TC", "TH", "9C", "9H", "9S", "8D"],
    ["8D", "9H", "5H", "4D", "6C", "2H", "QD", "6S", "5D", "3S"],
    ["4C", "5C", "JD", "QS", "4D", "3H", "TH", "AC", "QH", "8C"],
    ["QC", "5S", "3C", "7H", "AD", "4C", "KS", "4H", "JD", "6D"],
    ["QS", "AH", "3H", "KS", "9H", "2S", "JS", "JH", "5H", "2H"],
    ["2H", "5S", "TH", "6S", "TS", "3S", "KS", "3C", "5H", "JS"],
    ["2D", "9S", "7H", "3D", "KC", "JH", "6D", "7D", "JS", "TD"],
    ["AC", "JS", "8H", "2C", "8C", "JH", "JC", "2D", "TH", "7S"],
    ["5D", "9S", "8H", "2H", "3D", "TC", "AH", "JC", "KD", "9C"],
    ["9D", "QD", "JC", "2H", "6D", "KH", "TS", "9S", "QH", "TH"],
    ["2C", "8D", "4S", "JD", "5H", "3H", "TH", "TC", "9C", "KC"],
    ["AS", "3D", "9H", "7D", "4D", "TH", "KH", "2H", "7S", "3H"],
    ["4H", "7S", "KS", "2S", "JS", "TS", "8S", "2H", "QD", "8D"],
    ["5S", "6H", "JH", "KS", "8H", "2S", "QC", "AC", "6S", "3S"],
    ["JC", "AS", "AD", "QS", "8H", "6C", "KH", "4C", "4D", "QD"],
    ["2S", "3D", "TS", "TD", "9S", "KS", "6S", "QS", "5C", "8D"],
    ["3C", "6D", "4S", "QC", "KC", "JH", "QD", "TH", "KH", "AD"],
    ["9H", "AH", "4D", "KS", "2S", "8D", "JH", "JC", "7C", "QS"],
    ["2D", "6C", "TH", "3C", "8H", "QD", "QH", "2S", "3S", "KS"],
    ["6H", "5D", "9S", "4C", "TS", "TD", "JS", "QD", "9D", "JD"],
    ["5H", "8H", "KH", "8S", "KS", "7C", "TD", "AD", "4S", "KD"],
    ["2C", "7C", "JC", "5S", "AS", "6C", "7D", "8S", "5H", "9C"],
    ["6S", "QD", "9S", "TS", "KH", "QS", "5S", "QH", "3C", "KC"],
    ["7D", "3H", "3C", "KD", "5C", "AS", "JH", "7H", "6H", "JD"],
    ["9D", "5C", "9H", "KC", "8H", "KS", "4S", "AD", "4D", "2S"],
    ["3S", "JD", "QD", "8D", "2S", "7C", "5S", "6S", "5H", "TS"],
    ["6D", "9S", "KC", "TD", "3S", "6H", "QD", "JD", "5C", "8D"],
    ["5H", "9D", "TS", "KD", "8D", "6H", "TD", "QC", "4C", "7D"],
    ["6D", "4S", "JD", "9D", "AH", "9S", "AS", "TD", "9H", "QD"],
    ["2D", "5S", "2H", "9C", "6H", "9S", "TD", "QC", "7D", "TC"],
    ["3S", "2H", "KS", "TS", "2C", "9C", "8S", "JS", "9D", "7D"],
    ["3C", "KC", "6D", "5D", "6C", "6H", "8S", "AS", "7S", "QS"],
    ["JH", "9S", "2H", "8D", "4C", "8H", "9H", "AD", "TH", "KH"],
    ["QC", "AS", "2S", "JS", "5C", "6H", "KD", "3H", "7H", "2C"],
    ["QD", "8H", "2S", "8D", "3S", "6D", "AH", "2C", "TC", "5C"],
    ["JD", "JS", "TS", "8S", "3H", "5D", "TD", "KC", "JC", "6H"],
    ["6S", "QS", "TC", "3H", "5D", "AH", "JC", "7C", "7D", "4H"],
    ["7C", "5D", "8H", "9C", "2H", "9H", "JH", "KH", "5S", "2C"],
    ["9C", "7H", "6S", "TH", "3S", "QC", "QD", "4C", "AC", "JD"],
    ["2H", "5D", "9S", "7D", "KC", "3S", "QS", "2D", "AS", "KH"],
    ["2S", "4S", "2H", "7D", "5C", "TD", "TH", "QH", "9S", "4D"],
    ["6D", "3S", "TS", "6H", "4H", "KS", "9D", "8H", "5S", "2D"],
    ["9H", "KS", "4H", "3S", "5C", "5D", "KH", "6H", "6S", "JS"],
    ["KC", "AS", "8C", "4C", "JC", "KH", "QC", "TH", "QD", "AH"],
    ["6S", "KH", "9S", "2C", "5H", "TC", "3C", "7H", "JC", "4D"],
    ["JD", "4S", "6S", "5S", "8D", "7H", "7S", "4D", "4C", "2H"],
    ["7H", "9H", "5D", "KH", "9C", "7C", "TS", "TC", "7S", "5H"],
    ["4C", "8D", "QC", "TS", "4S", "9H", "3D", "AD", "JS", "7C"],
    ["8C", "QS", "5C", "5D", "3H", "JS", "AH", "KC", "4S", "9D"],
    ["TS", "JD", "8S", "QS", "TH", "JH", "KH", "2D", "QD", "JS"],
    ["JD", "QC", "5D", "6S", "9H", "3S", "2C", "8H", "9S", "TS"],
    ["2S", "4C", "AD", "7H", "JC", "5C", "2D", "6D", "4H", "3D"],
    ["7S", "JS", "2C", "4H", "8C", "AD", "QD", "9C", "3S", "TD"],
    ["JD", "TS", "4C", "6H", "9H", "7D", "QD", "6D", "3C", "AS"],
    ["AS", "7C", "4C", "6S", "5D", "5S", "5C", "JS", "QC", "4S"],
    ["KD", "6S", "9S", "7C", "3C", "5S", "7D", "JH", "QD", "JS"],
    ["4S", "7S", "JH", "2C", "8S", "5D", "7H", "3D", "QH", "AD"],
    ["TD", "6H", "2H", "8D", "4H", "2D", "7C", "AD", "KH", "5D"],
    ["TS", "3S", "5H", "2C", "QD", "AH", "2S", "5C", "KH", "TD"],
    ["KC", "4D", "8C", "5D", "AS", "6C", "2H", "2S", "9H", "7C"],
    ["KD", "JS", "QC", "TS", "QS", "KH", "JH", "2C", "5D", "AD"],
    ["3S", "5H", "KC", "6C", "9H", "3H", "2H", "AD", "7D", "7S"],
    ["7S", "JS", "JH", "KD", "8S", "7D", "2S", "9H", "7C", "2H"],
    ["9H", "2D", "8D", "QC", "6S", "AD", "AS", "8H", "5H", "6C"],
    ["2S", "7H", "6C", "6D", "7D", "8C", "5D", "9D", "JC", "3C"],
    ["7C", "9C", "7H", "JD", "2H", "KD", "3S", "KH", "AD", "4S"],
    ["QH", "AS", "9H", "4D", "JD", "KS", "KD", "TS", "KH", "5H"],
    ["4C", "8H", "5S", "3S", "3D", "7D", "TD", "AD", "7S", "KC"],
    ["JS", "8S", "5S", "JC", "8H", "TH", "9C", "4D", "5D", "KC"],
    ["7C", "5S", "9C", "QD", "2C", "QH", "JS", "5H", "8D", "KH"],
    ["TD", "2S", "KS", "3D", "AD", "KC", "7S", "TC", "3C", "5D"],
    ["4C", "2S", "AD", "QS", "6C", "9S", "QD", "TH", "QH", "5C"],
    ["8C", "AD", "QS", "2D", "2S", "KC", "JD", "KS", "6C", "JC"],
    ["8D", "4D", "JS", "2H", "5D", "QD", "7S", "7D", "QH", "TS"],
    ["6S", "7H", "3S", "8C", "8S", "9D", "QS", "8H", "6C", "9S"],
    ["4S", "TC", "2S", "5C", "QD", "4D", "QS", "6D", "TH", "6S"],
    ["3S", "5C", "9D", "6H", "8D", "4C", "7D", "TC", "7C", "TD"],
    ["AH", "6S", "AS", "7H", "5S", "KD", "3H", "5H", "AC", "4C"],
    ["8D", "8S", "AH", "KS", "QS", "2C", "AD", "6H", "7D", "5D"],
    ["6H", "9H", "9S", "2H", "QS", "8S", "9C", "5D", "2D", "KD"],
    ["TS", "QC", "5S", "JH", "7D", "7S", "TH", "9S", "9H", "AC"],
    ["7H", "3H", "6S", "KC", "4D", "6D", "5C", "4S", "QD", "TS"],
    ["TD", "2S", "7C", "QD", "3H", "JH", "9D", "4H", "7S", "7H"],
    ["KS", "3D", "4H", "5H", "TC", "2S", "AS", "2D", "6D", "7D"],
    ["8H", "3C", "7H", "TD", "3H", "AD", "KC", "TH", "9C", "KH"],
    ["TC", "4C", "2C", "9S", "9D", "9C", "5C", "2H", "JD", "3C"],
    ["3H", "AC", "TS", "5D", "AD", "8D", "6H", "QC", "6S", "8C"],
    ["2S", "TS", "3S", "JD", "7H", "8S", "QH", "4C", "5S", "8D"],
    ["AC", "4S", "6C", "3C", "KH", "3D", "7C", "2D", "8S", "2H"],
    ["4H", "6C", "8S", "TH", "2H", "4S", "8H", "9S", "3H", "7S"],
    ["7C", "4C", "9C", "2C", "5C", "AS", "5D", "KD", "4D", "QH"],
    ["9H", "4H", "TS", "AS", "7D", "8D", "5D", "9S", "8C", "2H"],
    ["QC", "KD", "AC", "AD", "2H", "7S", "AS", "3S", "2D", "9S"],
    ["2H", "QC", "8H", "TC", "6D", "QD", "QS", "5D", "KH", "3C"],
    ["TH", "JD", "QS", "4C", "2S", "5S", "AD", "7H", "3S", "AS"],
    ["7H", "JS", "3D", "6C", "3S", "6D", "AS", "9S", "AC", "QS"],
    ["9C", "TS", "AS", "8C", "TC", "8S", "6H", "9D", "8D", "6C"],
    ["4D", "JD", "9C", "KC", "7C", "6D", "KS", "3S", "8C", "AS"],
    ["3H", "6S", "TC", "8D", "TS", "3S", "KC", "9S", "7C", "AS"],
    ["8C", "QC", "4H", "4S", "8S", "6C", "3S", "TC", "AH", "AC"],
    ["4D", "7D", "5C", "AS", "2H", "6S", "TS", "QC", "AD", "TC"],
    ["QD", "QC", "8S", "4S", "TH", "3D", "AH", "TS", "JH", "4H"],
    ["5C", "2D", "9S", "2C", "3H", "3C", "9D", "QD", "QH", "7D"],
    ["KC", "9H", "6C", "KD", "7S", "3C", "4D", "AS", "TC", "2D"],
    ["3D", "JS", "4D", "9D", "KS", "7D", "TH", "QC", "3H", "3C"],
    ["8D", "5S", "2H", "9D", "3H", "8C", "4C", "4H", "3C", "TH"],
    ["JC", "TH", "4S", "6S", "JD", "2D", "4D", "6C", "3D", "4C"],
    ["TS", "3S", "2D", "4H", "AC", "2C", "6S", "2H", "JH", "6H"],
    ["TD", "8S", "AD", "TC", "AH", "AC", "JH", "9S", "6S", "7S"],
    ["6C", "KC", "4S", "JD", "8D", "9H", "5S", "7H", "QH", "AH"],
    ["KD", "8D", "TS", "JH", "5C", "5H", "3H", "AD", "AS", "JS"],
    ["2D", "4H", "3D", "6C", "8C", "7S", "AD", "5D", "5C", "8S"],
    ["TD", "5D", "7S", "9C", "4S", "5H", "6C", "8C", "4C", "8S"],
    ["JS", "QH", "9C", "AS", "5C", "QS", "JC", "3D", "QC", "7C"],
    ["JC", "9C", "KH", "JH", "QS", "QC", "2C", "TS", "3D", "AD"],
    ["5D", "JH", "AC", "5C", "9S", "TS", "4C", "JD", "8C", "KS"],
    ["KC", "AS", "2D", "KH", "9H", "2C", "5S", "4D", "3D", "6H"],
    ["TH", "AH", "2D", "8S", "JC", "3D", "8C", "QH", "7S", "3S"],
    ["8H", "QD", "4H", "JC", "AS", "KH", "KS", "3C", "9S", "6D"],
    ["9S", "QH", "7D", "9C", "4S", "AC", "7H", "KH", "4D", "KD"],
    ["AH", "AD", "TH", "6D", "9C", "9S", "KD", "KS", "QH", "4H"],
    ["QD", "6H", "9C", "7C", "QS", "6D", "6S", "9D", "5S", "JH"],
    ["AH", "8D", "5H", "QD", "2H", "JC", "KS", "4H", "KH", "5S"],
    ["5C", "2S", "JS", "8D", "9C", "8C", "3D", "AS", "KC", "AH"],
    ["JD", "9S", "2H", "QS", "8H", "5S", "8C", "TH", "5C", "4C"],
    ["QC", "QS", "8C", "2S", "2C", "3S", "9C", "4C", "KS", "KH"],
    ["2D", "5D", "8S", "AH", "AD", "TD", "2C", "JS", "KS", "8C"],
    ["TC", "5S", "5H", "8H", "QC", "9H", "6H", "JD", "4H", "9S"],
    ["3C", "JH", "4H", "9H", "AH", "4S", "2H", "4C", "8D", "AC"],
    ["8S", "TH", "4D", "7D", "6D", "QD", "QS", "7S", "TC", "7C"],
    ["KH", "6D", "2D", "JD", "5H", "JS", "QD", "JH", "4H", "4S"],
    ["9C", "7S", "JH", "4S", "3S", "TS", "QC", "8C", "TC", "4H"],
    ["QH", "9D", "4D", "JH", "QS", "3S", "2C", "7C", "6C", "2D"],
    ["4H", "9S", "JD", "5C", "5H", "AH", "9D", "TS", "2D", "4C"],
    ["KS", "JH", "TS", "5D", "2D", "AH", "JS", "7H", "AS", "8D"],
    ["JS", "AH", "8C", "AD", "KS", "5S", "8H", "2C", "6C", "TH"],
    ["2H", "5D", "AD", "AC", "KS", "3D", "8H", "TS", "6H", "QC"],
    ["6D", "4H", "TS", "9C", "5H", "JS", "JH", "6S", "JD", "4C"],
    ["JH", "QH", "4H", "2C", "6D", "3C", "5D", "4C", "QS", "KC"],
    ["6H", "4H", "6C", "7H", "6S", "2S", "8S", "KH", "QC", "8C"],
    ["3H", "3D", "5D", "KS", "4H", "TD", "AD", "3S", "4D", "TS"],
    ["5S", "7C", "8S", "7D", "2C", "KS", "7S", "6C", "8C", "JS"],
    ["5D", "2H", "3S", "7C", "5C", "QD", "5H", "6D", "9C", "9H"],
    ["JS", "2S", "KD", "9S", "8D", "TD", "TS", "AC", "8C", "9D"],
    ["5H", "QD", "2S", "AC", "8C", "9H", "KS", "7C", "4S", "3C"],
    ["KH", "AS", "3H", "8S", "9C", "JS", "QS", "4S", "AD", "4D"],
    ["AS", "2S", "TD", "AD", "4D", "9H", "JC", "4C", "5H", "QS"],
    ["5D", "7C", "4H", "TC", "2D", "6C", "JS", "4S", "KC", "3S"],
    ["4C", "2C", "5D", "AC", "9H", "3D", "JD", "8S", "QS", "QH"],
    ["2C", "8S", "6H", "3C", "QH", "6D", "TC", "KD", "AC", "AH"],
    ["QC", "6C", "3S", "QS", "4S", "AC", "8D", "5C", "AD", "KH"],
    ["5S", "4C", "AC", "KH", "AS", "QC", "2C", "5C", "8D", "9C"],
    ["8H", "JD", "3C", "KH", "8D", "5C", "9C", "QD", "QH", "9D"],
    ["7H", "TS", "2C", "8C", "4S", "TD", "JC", "9C", "5H", "QH"],
    ["JS", "4S", "2C", "7C", "TH", "6C", "AS", "KS", "7S", "JD"],
    ["JH", "7C", "9H", "7H", "TC", "5H", "3D", "6D", "5D", "4D"],
    ["2C", "QD", "JH", "2H", "9D", "5S", "3D", "TD", "AD", "KS"],
    ["JD", "QH", "3S", "4D", "TH", "7D", "6S", "QS", "KS", "4H"],
    ["TC", "KS", "5S", "8D", "8H", "AD", "2S", "2D", "4C", "JH"],
    ["5S", "JH", "TC", "3S", "2D", "QS", "9D", "4C", "KD", "9S"],
    ["AC", "KH", "3H", "AS", "9D", "KC", "9H", "QD", "6C", "6S"],
    ["9H", "7S", "3D", "5C", "7D", "KC", "TD", "8H", "4H", "6S"],
    ["3C", "7H", "8H", "TC", "QD", "4D", "7S", "6S", "QH", "6C"],
    ["6D", "AD", "4C", "QD", "6C", "5D", "7D", "9D", "KS", "TS"],
    ["JH", "2H", "JD", "9S", "7S", "TS", "KH", "8D", "5D", "8H"],
    ["2D", "9S", "4C", "7D", "9D", "5H", "QD", "6D", "AC", "6S"],
    ["7S", "6D", "JC", "QD", "JH", "4C", "6S", "QS", "2H", "7D"],
    ["8C", "TD", "JH", "KD", "2H", "5C", "QS", "2C", "JS", "7S"],
    ["TC", "5H", "4H", "JH", "QD", "3S", "5S", "5D", "8S", "KH"],
    ["KS", "KH", "7C", "2C", "5D", "JH", "6S", "9C", "6D", "JC"],
    ["5H", "AH", "JD", "9C", "JS", "KC", "2H", "6H", "4D", "5S"],
    ["AS", "3C", "TH", "QC", "6H", "9C", "8S", "8C", "TD", "7C"],
    ["KC", "2C", "QD", "9C", "KH", "4D", "7S", "3C", "TS", "9H"],
    ["9C", "QC", "2S", "TS", "8C", "TD", "9S", "QD", "3S", "3C"],
    ["4D", "9D", "TH", "JH", "AH", "6S", "2S", "JD", "QH", "JS"],
    ["QD", "9H", "6C", "KD", "7D", "7H", "5D", "6S", "8H", "AH"],
    ["8H", "3C", "4S", "2H", "5H", "QS", "QH", "7S", "4H", "AC"],
    ["QS", "3C", "7S", "9S", "4H", "3S", "AH", "KS", "9D", "7C"],
    ["AD", "5S", "6S", "2H", "2D", "5H", "TC", "4S", "3C", "8C"],
    ["QH", "TS", "6S", "4D", "JS", "KS", "JH", "AS", "8S", "6D"],
    ["2C", "8S", "2S", "TD", "5H", "AS", "TC", "TS", "6C", "KC"],
    ["KC", "TS", "8H", "2H", "3H", "7C", "4C", "5S", "TH", "TD"],
    ["KD", "AD", "KH", "7H", "7S", "5D", "5H", "5S", "2D", "9C"],
    ["AD", "9S", "3D", "7S", "8C", "QC", "7C", "9C", "KD", "KS"],
    ["3C", "QC", "9S", "8C", "4D", "5C", "AS", "QD", "6C", "2C"],
    ["2H", "KC", "8S", "JD", "7S", "AC", "8D", "5C", "2S", "4D"],
    ["9D", "QH", "3D", "2S", "TC", "3S", "KS", "3C", "9H", "TD"],
    ["KD", "6S", "AC", "2C", "7H", "5H", "3S", "6C", "6H", "8C"],
    ["QH", "TC", "8S", "6S", "KH", "TH", "4H", "5D", "TS", "4D"],
    ["8C", "JS", "4H", "6H", "2C", "2H", "7D", "AC", "QD", "3D"],
    ["QS", "KC", "6S", "2D", "5S", "4H", "TD", "3H", "JH", "4C"],
    ["7S", "5H", "7H", "8H", "KH", "6H", "QS", "TH", "KD", "7D"],
    ["5H", "AD", "KD", "7C", "KH", "5S", "TD", "6D", "3C", "6C"],
    ["8C", "9C", "5H", "JD", "7C", "KC", "KH", "7H", "2H", "3S"],
    ["7S", "4H", "AD", "4D", "8S", "QS", "TH", "3D", "7H", "5S"],
    ["8D", "TC", "KS", "KD", "9S", "6D", "AD", "JD", "5C", "2S"],
    ["7H", "8H", "6C", "QD", "2H", "6H", "9D", "TC", "9S", "7C"],
    ["8D", "6D", "4C", "7C", "6C", "3C", "TH", "KH", "JS", "JH"],
    ["5S", "3S", "8S", "JS", "9H", "AS", "AD", "8H", "7S", "KD"],
    ["JH", "7C", "2C", "KC", "5H", "AS", "AD", "9C", "9S", "JS"],
    ["AD", "AC", "2C", "6S", "QD", "7C", "3H", "TH", "KS", "KD"],
    ["9D", "JD", "4H", "8H", "4C", "KH", "7S", "TS", "8C", "KC"],
    ["3S", "5S", "2H", "7S", "6H", "7D", "KS", "5C", "6D", "AD"],
    ["5S", "8C", "9H", "QS", "7H", "7S", "2H", "6C", "7D", "TD"],
    ["QS", "5S", "TD", "AC", "9D", "KC", "3D", "TC", "2D", "4D"],
    ["TD", "2H", "7D", "JD", "QD", "4C", "7H", "5D", "KC", "3D"],
    ["4C", "3H", "8S", "KD", "QH", "5S", "QC", "9H", "TC", "5H"],
    ["9C", "QD", "TH", "5H", "TS", "5C", "9H", "AH", "QH", "2C"],
    ["4D", "6S", "3C", "AC", "6C", "3D", "2C", "2H", "TD", "TH"],
    ["AC", "9C", "5D", "QC", "4D", "AD", "8D", "6D", "8C", "KC"],
    ["AD", "3C", "4H", "AC", "8D", "8H", "7S", "9S", "TD", "JC"],
    ["4H", "9H", "QH", "JS", "2D", "TH", "TD", "TC", "KD", "KS"],
    ["5S", "6S", "9S", "8D", "TH", "AS", "KH", "5H", "5C", "8S"],
    ["JD", "2S", "9S", "6S", "5S", "8S", "5D", "7S", "7H", "9D"],
    ["5D", "8C", "4C", "9D", "AD", "TS", "2C", "7D", "KD", "TC"],
    ["8S", "QS", "4D", "KC", "5C", "8D", "4S", "KH", "JD", "KD"],
    ["AS", "5C", "AD", "QH", "7D", "2H", "9S", "7H", "7C", "TC"],
    ["2S", "8S", "JD", "KH", "7S", "6C", "6D", "AD", "5D", "QC"],
    ["9H", "6H", "3S", "8C", "8H", "AH", "TC", "4H", "JS", "TD"],
    ["2C", "TS", "4D", "7H", "2D", "QC", "9C", "5D", "TH", "7C"],
    ["6C", "8H", "QC", "5D", "TS", "JH", "5C", "5H", "9H", "4S"],
    ["2D", "QC", "7H", "AS", "JS", "8S", "2H", "4C", "4H", "8D"],
    ["JS", "6S", "AC", "KD", "3D", "3C", "4S", "7H", "TH", "KC"],
    ["QH", "KH", "6S", "QS", "5S", "4H", "3C", "QD", "3S", "3H"],
    ["7H", "AS", "KH", "8C", "4H", "9C", "5S", "3D", "6S", "TS"],
    ["9C", "7C", "3H", "5S", "QD", "2C", "3D", "AD", "AC", "5H"],
    ["JH", "TD", "2D", "4C", "TS", "3H", "KH", "AD", "3S", "7S"],
    ["AS", "4C", "5H", "4D", "6S", "KD", "JC", "3C", "6H", "2D"],
    ["3H", "6S", "8C", "2D", "TH", "4S", "AH", "QH", "AD", "5H"],
    ["7C", "2S", "9H", "7H", "KC", "5C", "6D", "5S", "3H", "JC"],
    ["3C", "TC", "9C", "4H", "QD", "TD", "JH", "6D", "9H", "5S"],
    ["7C", "6S", "5C", "5D", "6C", "4S", "7H", "9H", "6H", "AH"],
    ["AD", "2H", "7D", "KC", "2C", "4C", "2S", "9S", "7H", "3S"],
    ["TH", "4C", "8S", "6S", "3S", "AD", "KS", "AS", "JH", "TD"],
    ["5C", "TD", "4S", "4D", "AD", "6S", "5D", "TC", "9C", "7D"],
    ["8H", "3S", "4D", "4S", "5S", "6H", "5C", "AC", "3H", "3D"],
    ["9H", "3C", "AC", "4S", "QS", "8S", "9D", "QH", "5H", "4D"],
    ["JC", "6C", "5H", "TS", "AC", "9C", "JD", "8C", "7C", "QD"],
    ["8S", "8H", "9C", "JD", "2D", "QC", "QH", "6H", "3C", "8D"],
    ["KS", "JS", "2H", "6H", "5H", "QH", "QS", "3H", "7C", "6D"],
    ["TC", "3H", "4S", "7H", "QC", "2H", "3S", "8C", "JS", "KH"],
    ["AH", "8H", "5S", "4C", "9H", "JD", "3H", "7S", "JC", "AC"],
    ["3C", "2D", "4C", "5S", "6C", "4S", "QS", "3S", "JD", "3D"],
    ["5H", "2D", "TC", "AH", "KS", "6D", "7H", "AD", "8C", "6H"],
    ["6C", "7S", "3C", "JD", "7C", "8H", "KS", "KH", "AH", "6D"],
    ["AH", "7D", "3H", "8H", "8S", "7H", "QS", "5H", "9D", "2D"],
    ["JD", "AC", "4H", "7S", "8S", "9S", "KS", "AS", "9D", "QH"],
    ["7S", "2C", "8S", "5S", "JH", "QS", "JC", "AH", "KD", "4C"],
    ["AH", "2S", "9H", "4H", "8D", "TS", "TD", "6H", "QH", "JD"],
    ["4H", "JC", "3H", "QS", "6D", "7S", "9C", "8S", "9D", "8D"],
    ["5H", "TD", "4S", "9S", "4C", "8C", "8D", "7H", "3H", "3D"],
    ["QS", "KH", "3S", "2C", "2S", "3C", "7S", "TD", "4S", "QD"],
    ["7C", "TD", "4D", "5S", "KH", "AC", "AS", "7H", "4C", "6C"],
    ["2S", "5H", "6D", "JD", "9H", "QS", "8S", "2C", "2H", "TD"],
    ["2S", "TS", "6H", "9H", "7S", "4H", "JC", "4C", "5D", "5S"],
    ["2C", "5H", "7D", "4H", "3S", "QH", "JC", "JS", "6D", "8H"],
    ["4C", "QH", "7C", "QD", "3S", "AD", "TH", "8S", "5S", "TS"],
    ["9H", "TC", "2S", "TD", "JC", "7D", "3S", "3D", "TH", "QH"],
    ["7D", "4C", "8S", "5C", "JH", "8H", "6S", "3S", "KC", "3H"],
    ["JC", "3H", "KH", "TC", "QH", "TH", "6H", "2C", "AC", "5H"],
    ["QS", "2H", "9D", "2C", "AS", "6S", "6C", "2S", "8C", "8S"],
    ["9H", "7D", "QC", "TH", "4H", "KD", "QS", "AC", "7S", "3C"],
    ["4D", "JH", "6S", "5S", "8H", "KS", "9S", "QC", "3S", "AS"],
    ["JD", "2D", "6S", "7S", "TC", "9H", "KC", "3H", "7D", "KD"],
    ["2H", "KH", "7C", "4D", "4S", "3H", "JS", "QD", "7D", "KC"],
    ["4C", "JC", "AS", "9D", "3C", "JS", "6C", "8H", "QD", "4D"],
    ["AH", "JS", "3S", "6C", "4C", "3D", "JH", "6D", "9C", "9H"],
    ["9H", "2D", "8C", "7H", "5S", "KS", "6H", "9C", "2S", "TC"],
    ["6C", "8C", "AD", "7H", "6H", "3D", "KH", "AS", "5D", "TH"],
    ["KS", "8C", "3S", "TS", "8S", "4D", "5S", "9S", "6C", "4H"],
    ["9H", "4S", "4H", "5C", "7D", "KC", "2D", "2H", "9D", "JH"],
    ["5C", "JS", "TC", "9D", "9H", "5H", "7S", "KH", "JC", "6S"],
    ["7C", "9H", "8H", "4D", "JC", "KH", "JD", "2H", "TD", "TC"],
    ["8H", "6C", "2H", "2C", "KH", "6H", "9D", "QS", "QH", "5H"],
    ["AC", "7D", "2S", "3D", "QD", "JC", "2D", "8D", "JD", "JH"],
    ["2H", "JC", "2D", "7H", "2C", "3C", "8D", "KD", "TD", "4H"],
    ["3S", "4H", "6D", "8D", "TS", "3H", "TD", "3D", "6H", "TH"],
    ["JH", "JC", "3S", "AC", "QH", "9H", "7H", "8S", "QC", "2C"],
    ["7H", "TD", "QS", "4S", "8S", "9C", "2S", "5D", "4D", "2H"],
    ["3D", "TS", "3H", "2S", "QC", "8H", "6H", "KC", "JC", "KS"],
    ["5D", "JD", "7D", "TC", "8C", "6C", "9S", "3D", "8D", "AC"],
    ["8H", "6H", "JH", "6C", "5D", "8D", "8S", "4H", "AD", "2C"],
    ["9D", "4H", "2D", "2C", "3S", "TS", "AS", "TC", "3C", "5D"],
    ["4D", "TH", "5H", "KS", "QS", "6C", "4S", "2H", "3D", "AD"],
    ["5C", "KC", "6H", "2C", "5S", "3C", "4D", "2D", "9H", "9S"],
    ["JD", "4C", "3H", "TH", "QH", "9H", "5S", "AH", "8S", "AC"],
    ["7D", "9S", "6S", "2H", "TD", "9C", "4H", "8H", "QS", "4C"],
    ["3C", "6H", "5D", "4H", "8C", "9C", "KC", "6S", "QD", "QS"],
    ["3S", "9H", "KD", "TC", "2D", "JS", "8C", "6S", "4H", "4S"],
    ["2S", "4C", "8S", "QS", "6H", "KH", "3H", "TH", "8C", "5D"],
    ["2C", "KH", "5S", "3S", "7S", "7H", "6C", "9D", "QD", "8D"],
    ["8H", "KS", "AC", "2D", "KH", "TS", "6C", "JS", "KC", "7H"],
    ["9C", "KS", "5C", "TD", "QC", "AH", "6C", "5H", "9S", "7C"],
    ["5D", "4D", "3H", "4H", "6S", "7C", "7S", "AH", "QD", "TD"],
    ["2H", "7D", "QC", "6S", "TC", "TS", "AH", "7S", "9D", "3H"],
    ["TH", "5H", "QD", "9S", "KS", "7S", "7C", "6H", "8C", "TD"],
    ["TH", "2D", "4D", "QC", "5C", "7D", "JD", "AH", "9C", "4H"],
    ["4H", "3H", "AH", "8D", "6H", "QC", "QH", "9H", "2H", "2C"],
    ["2D", "AD", "4C", "TS", "6H", "7S", "TH", "4H", "QS", "TD"],
    ["3C", "KD", "2H", "3H", "QS", "JD", "TC", "QC", "5D", "8H"],
    ["KS", "JC", "QD", "TH", "9S", "KD", "8D", "8C", "2D", "9C"],
    ["3C", "QD", "KD", "6D", "4D", "8D", "AH", "AD", "QC", "8S"],
    ["8H", "3S", "9D", "2S", "3H", "KS", "6H", "4C", "7C", "KC"],
    ["TH", "9S", "5C", "3D", "7D", "6H", "AC", "7S", "4D", "2C"],
    ["5C", "3D", "JD", "4D", "2D", "6D", "5H", "9H", "4C", "KH"],
    ["AS", "7H", "TD", "6C", "2H", "3D", "QD", "KS", "4C", "4S"],
    ["JC", "3C", "AC", "7C", "JD", "JS", "8H", "9S", "QC", "5D"],
    ["JD", "6S", "5S", "2H", "AS", "8C", "7D", "5H", "JH", "3D"],
    ["8D", "TC", "5S", "9S", "8S", "3H", "JC", "5H", "7S", "AS"],
    ["5C", "TD", "3D", "7D", "4H", "8D", "7H", "4D", "5D", "JS"],
    ["QS", "9C", "KS", "TD", "2S", "8S", "5C", "2H", "4H", "AS"],
    ["TH", "7S", "4H", "7D", "3H", "JD", "KD", "5D", "2S", "KC"],
    ["JD", "7H", "4S", "8H", "4C", "JS", "6H", "QH", "5S", "4H"],
    ["2C", "QS", "8C", "5S", "3H", "QC", "2S", "6C", "QD", "AD"],
    ["8C", "3D", "JD", "TC", "4H", "2H", "AD", "5S", "AC", "2S"],
    ["5D", "2C", "JS", "2D", "AD", "9D", "3D", "4C", "4S", "JH"],
    ["8D", "5H", "5D", "6H", "7S", "4D", "KS", "9D", "TD", "JD"],
    ["3D", "6D", "9C", "2S", "AS", "7D", "5S", "5C", "8H", "JD"],
    ["7C", "8S", "3S", "6S", "5H", "JD", "TC", "AD", "7H", "7S"],
    ["2S", "9D", "TS", "4D", "AC", "8D", "6C", "QD", "JD", "3H"],
    ["9S", "KH", "2C", "3C", "AC", "3D", "5H", "6H", "8D", "5D"],
    ["KS", "3D", "2D", "6S", "AS", "4C", "2S", "7C", "7H", "KH"],
    ["AC", "2H", "3S", "JC", "5C", "QH", "4D", "2D", "5H", "7S"],
    ["TS", "AS", "JD", "8C", "6H", "JC", "8S", "5S", "2C", "5D"],
    ["7S", "QH", "7H", "6C", "QC", "8H", "2D", "7C", "JD", "2S"],
    ["2C", "QD", "2S", "2H", "JC", "9C", "5D", "2D", "JD", "JH"],
    ["7C", "5C", "9C", "8S", "7D", "6D", "8D", "6C", "9S", "JH"],
    ["2C", "AD", "6S", "5H", "3S", "KS", "7S", "9D", "KH", "4C"],
    ["7H", "6C", "2C", "5C", "TH", "9D", "8D", "3S", "QC", "AH"],
    ["5S", "KC", "6H", "TC", "5H", "8S", "TH", "6D", "3C", "AH"],
    ["9C", "KD", "4H", "AD", "TD", "9S", "4S", "7D", "6H", "5D"],
    ["7H", "5C", "5H", "6D", "AS", "4C", "KD", "KH", "4H", "9D"],
    ["3C", "2S", "5C", "6C", "JD", "QS", "2H", "9D", "7D", "3H"],
    ["AC", "2S", "6S", "7S", "JS", "QD", "5C", "QS", "6H", "AD"],
    ["5H", "TH", "QC", "7H", "TC", "3S", "7C", "6D", "KC", "3D"],
    ["4H", "3D", "QC", "9S", "8H", "2C", "3S", "JC", "KS", "5C"],
    ["4S", "6S", "2C", "6H", "8S", "3S", "3D", "9H", "3H", "JS"],
    ["4S", "8C", "4D", "2D", "8H", "9H", "7D", "9D", "AH", "TS"],
    ["9S", "2C", "9H", "4C", "8D", "AS", "7D", "3D", "6D", "5S"],
    ["6S", "4C", "7H", "8C", "3H", "5H", "JC", "AH", "9D", "9C"],
    ["2S", "7C", "5S", "JD", "8C", "3S", "3D", "4D", "7D", "6S"],
    ["3C", "KC", "4S", "5D", "7D", "3D", "JD", "7H", "3H", "4H"],
    ["9C", "9H", "4H", "4D", "TH", "6D", "QD", "8S", "9S", "7S"],
    ["2H", "AC", "8S", "4S", "AD", "8C", "2C", "AH", "7D", "TC"],
    ["TS", "9H", "3C", "AD", "KS", "TC", "3D", "8C", "8H", "JD"],
    ["QC", "8D", "2C", "3C", "7D", "7C", "JD", "9H", "9C", "6C"],
    ["AH", "6S", "JS", "JH", "5D", "AS", "QC", "2C", "JD", "TD"],
    ["9H", "KD", "2H", "5D", "2D", "3S", "7D", "TC", "AH", "TS"],
    ["TD", "8H", "AS", "5D", "AH", "QC", "AC", "6S", "TC", "5H"],
    ["KS", "4S", "7H", "4D", "8D", "9C", "TC", "2H", "6H", "3H"],
    ["3H", "KD", "4S", "QD", "QH", "3D", "8H", "8C", "TD", "7S"],
    ["8S", "JD", "TC", "AH", "JS", "QS", "2D", "KH", "KS", "4D"],
    ["3C", "AD", "JC", "KD", "JS", "KH", "4S", "TH", "9H", "2C"],
    ["QC", "5S", "JS", "9S", "KS", "AS", "7C", "QD", "2S", "JD"],
    ["KC", "5S", "QS", "3S", "2D", "AC", "5D", "9H", "8H", "KS"],
    ["6H", "9C", "TC", "AD", "2C", "6D", "5S", "JD", "6C", "7C"],
    ["QS", "KH", "TD", "QD", "2C", "3H", "8S", "2S", "QC", "AH"],
    ["9D", "9H", "JH", "TC", "QH", "3C", "2S", "JS", "5C", "7H"],
    ["6C", "3S", "3D", "2S", "4S", "QD", "2D", "TH", "5D", "2C"],
    ["2D", "6H", "6D", "2S", "JC", "QH", "AS", "7H", "4H", "KH"],
    ["5H", "6S", "KS", "AD", "TC", "TS", "7C", "AC", "4S", "4H"],
    ["AD", "3C", "4H", "QS", "8C", "9D", "KS", "2H", "2D", "4D"],
    ["4S", "9D", "6C", "6D", "9C", "AC", "8D", "3H", "7H", "KD"],
    ["JC", "AH", "6C", "TS", "JD", "6D", "AD", "3S", "5D", "QD"],
    ["JC", "JH", "JD", "3S", "7S", "8S", "JS", "QC", "3H", "4S"],
    ["JD", "TH", "5C", "2C", "AD", "JS", "7H", "9S", "2H", "7S"],
    ["8D", "3S", "JH", "4D", "QC", "AS", "JD", "2C", "KC", "6H"],
    ["2C", "AC", "5H", "KD", "5S", "7H", "QD", "JH", "AH", "2D"],
    ["JC", "QH", "8D", "8S", "TC", "5H", "5C", "AH", "8C", "6C"],
    ["3H", "JS", "8S", "QD", "JH", "3C", "4H", "6D", "5C", "3S"],
    ["6D", "4S", "4C", "AH", "5H", "5S", "3H", "JD", "7C", "8D"],
    ["8H", "AH", "2H", "3H", "JS", "3C", "7D", "QC", "4H", "KD"],
    ["6S", "2H", "KD", "5H", "8H", "2D", "3C", "8S", "7S", "QD"],
    ["2S", "7S", "KC", "QC", "AH", "TC", "QS", "6D", "4C", "8D"],
    ["5S", "9H", "2C", "3S", "QD", "7S", "6C", "2H", "7C", "9D"],
    ["3C", "6C", "5C", "5S", "JD", "JC", "KS", "3S", "5D", "TS"],
    ["7C", "KS", "6S", "5S", "2S", "2D", "TC", "2H", "5H", "QS"],
    ["AS", "7H", "6S", "TS", "5H", "9S", "9D", "3C", "KD", "2H"],
    ["4S", "JS", "QS", "3S", "4H", "7C", "2S", "AC", "6S", "9D"],
    ["8C", "JH", "2H", "5H", "7C", "5D", "QH", "QS", "KH", "QC"],
    ["3S", "TD", "3H", "7C", "KC", "8D", "5H", "8S", "KH", "8C"],
    ["4H", "KH", "JD", "TS", "3C", "7H", "AS", "QC", "JS", "5S"],
    ["AH", "9D", "2C", "8D", "4D", "2D", "6H", "6C", "KC", "6S"],
    ["2S", "6H", "9D", "3S", "7H", "4D", "KH", "8H", "KD", "3D"],
    ["9C", "TC", "AC", "JH", "KH", "4D", "JD", "5H", "TD", "3S"],
    ["7S", "4H", "9D", "AS", "4C", "7D", "QS", "9S", "2S", "KH"],
    ["3S", "8D", "8S", "KS", "8C", "JC", "5C", "KH", "2H", "5D"],
    ["8S", "QH", "2C", "4D", "KC", "JS", "QC", "9D", "AC", "6H"],
    ["8S", "8C", "7C", "JS", "JD", "6S", "4C", "9C", "AC", "4S"],
    ["QH", "5D", "2C", "7D", "JC", "8S", "2D", "JS", "JH", "4C"],
    ["JS", "4C", "7S", "TS", "JH", "KC", "KH", "5H", "QD", "4S"],
    ["QD", "8C", "8D", "2D", "6S", "TD", "9D", "AC", "QH", "5S"],
    ["QH", "QC", "JS", "3D", "3C", "5C", "4H", "KH", "8S", "7H"],
    ["7C", "2C", "5S", "JC", "8S", "3H", "QC", "5D", "2H", "KC"],
    ["5S", "8D", "KD", "6H", "4H", "QD", "QH", "6D", "AH", "3D"],
    ["7S", "KS", "6C", "2S", "4D", "AC", "QS", "5H", "TS", "JD"],
    ["7C", "2D", "TC", "5D", "QS", "AC", "JS", "QC", "6C", "KC"],
    ["2C", "KS", "4D", "3H", "TS", "8S", "AD", "4H", "7S", "9S"],
    ["QD", "9H", "QH", "5H", "4H", "4D", "KH", "3S", "JC", "AD"],
    ["4D", "AC", "KC", "8D", "6D", "4C", "2D", "KH", "2C", "JD"],
    ["2C", "9H", "2D", "AH", "3H", "6D", "9C", "7D", "TC", "KS"],
    ["8C", "3H", "KD", "7C", "5C", "2S", "4S", "5H", "AS", "AH"],
    ["TH", "JD", "4H", "KD", "3H", "TC", "5C", "3S", "AC", "KH"],
    ["6D", "7H", "AH", "7S", "QC", "6H", "2D", "TD", "JD", "AS"],
    ["JH", "5D", "7H", "TC", "9S", "7D", "JC", "AS", "5S", "KH"],
    ["2H", "8C", "AD", "TH", "6H", "QD", "KD", "9H", "6S", "6C"],
    ["QH", "KC", "9D", "4D", "3S", "JS", "JH", "4H", "2C", "9H"],
    ["TC", "7H", "KH", "4H", "JC", "7D", "9S", "3H", "QS", "7S"],
    ["AD", "7D", "JH", "6C", "7H", "4H", "3S", "3H", "4D", "QH"],
    ["JD", "2H", "5C", "AS", "6C", "QC", "4D", "3C", "TC", "JH"],
    ["AC", "JD", "3H", "6H", "4C", "JC", "AD", "7D", "7H", "9H"],
    ["4H", "TC", "TS", "2C", "8C", "6S", "KS", "2H", "JD", "9S"],
    ["4C", "3H", "QS", "QC", "9S", "9H", "6D", "KC", "9D", "9C"],
    ["5C", "AD", "8C", "2C", "QH", "TH", "QD", "JC", "8D", "8H"],
    ["QC", "2C", "2S", "QD", "9C", "4D", "3S", "8D", "JH", "QS"],
    ["9D", "3S", "2C", "7S", "7C", "JC", "TD", "3C", "TC", "9H"],
    ["3C", "TS", "8H", "5C", "4C", "2C", "6S", "8D", "7C", "4H"],
    ["KS", "7H", "2H", "TC", "4H", "2C", "3S", "AS", "AH", "QS"],
    ["8C", "2D", "2H", "2C", "4S", "4C", "6S", "7D", "5S", "3S"],
    ["TH", "QC", "5D", "TD", "3C", "QS", "KD", "KC", "KS", "AS"],
    ["4D", "AH", "KD", "9H", "KS", "5C", "4C", "6H", "JC", "7S"],
    ["KC", "4H", "5C", "QS", "TC", "2H", "JC", "9S", "AH", "QH"],
    ["4S", "9H", "3H", "5H", "3C", "QD", "2H", "QC", "JH", "8H"],
    ["5D", "AS", "7H", "2C", "3D", "JH", "6H", "4C", "6S", "7D"],
    ["9C", "JD", "9H", "AH", "JS", "8S", "QH", "3H", "KS", "8H"],
    ["3S", "AC", "QC", "TS", "4D", "AD", "3D", "AH", "8S", "9H"],
    ["7H", "3H", "QS", "9C", "9S", "5H", "JH", "JS", "AH", "AC"],
    ["8D", "3C", "JD", "2H", "AC", "9C", "7H", "5S", "4D", "8H"],
    ["7C", "JH", "9H", "6C", "JS", "9S", "7H", "8C", "9D", "4H"],
    ["2D", "AS", "9S", "6H", "4D", "JS", "JH", "9H", "AD", "QD"],
    ["6H", "7S", "JH", "KH", "AH", "7H", "TD", "5S", "6S", "2C"],
    ["8H", "JH", "6S", "5H", "5S", "9D", "TC", "4C", "QC", "9S"],
    ["7D", "2C", "KD", "3H", "5H", "AS", "QD", "7H", "JS", "4D"],
    ["TS", "QH", "6C", "8H", "TH", "5H", "3C", "3H", "9C", "9D"],
    ["AD", "KH", "JS", "5D", "3H", "AS", "AC", "9S", "5C", "KC"],
    ["2C", "KH", "8C", "JC", "QS", "6D", "AH", "2D", "KC", "TC"],
    ["9D", "3H", "2S", "7C", "4D", "6D", "KH", "KS", "8D", "7D"],
    ["9H", "2S", "TC", "JH", "AC", "QC", "3H", "5S", "3S", "8H"],
    ["3S", "AS", "KD", "8H", "4C", "3H", "7C", "JH", "QH", "TS"],
    ["7S", "6D", "7H", "9D", "JH", "4C", "3D", "3S", "6C", "AS"],
    ["4S", "2H", "2C", "4C", "8S", "5H", "KC", "8C", "QC", "QD"],
    ["3H", "3S", "6C", "QS", "QC", "2D", "6S", "5D", "2C", "9D"],
    ["2H", "8D", "JH", "2S", "3H", "2D", "6C", "5C", "7S", "AD"],
    ["9H", "JS", "5D", "QH", "8S", "TS", "2H", "7S", "6S", "AD"],
    ["6D", "QC", "9S", "7H", "5H", "5C", "7D", "KC", "JD", "4H"],
    ["QC", "5S", "9H", "9C", "4D", "6S", "KS", "2S", "4C", "7C"],
    ["9H", "7C", "4H", "8D", "3S", "6H", "5C", "8H", "JS", "7S"],
    ["2D", "6H", "JS", "TD", "4H", "4D", "JC", "TH", "5H", "KC"],
    ["AC", "7C", "8D", "TH", "3H", "9S", "2D", "4C", "KC", "4D"],
    ["KD", "QS", "9C", "7S", "3D", "KS", "AD", "TS", "4C", "4H"],
    ["QH", "9C", "8H", "2S", "7D", "KS", "7H", "5D", "KD", "4C"],
    ["9C", "2S", "2H", "JC", "6S", "6C", "TC", "QC", "JH", "5C"],
    ["7S", "AC", "8H", "KC", "8S", "6H", "QS", "JC", "3D", "6S"],
    ["JS", "2D", "JH", "8C", "4S", "6H", "8H", "6D", "5D", "AD"],
    ["6H", "7D", "2S", "4H", "9H", "7C", "AS", "AC", "8H", "5S"],
    ["3C", "JS", "4S", "6D", "5H", "2S", "QH", "6S", "9C", "2C"],
    ["3D", "5S", "6S", "9S", "4C", "QS", "8D", "QD", "8S", "TC"],
    ["9C", "3D", "AH", "9H", "5S", "2C", "7D", "AD", "JC", "3S"],
    ["7H", "TC", "AS", "3C", "6S", "6D", "7S", "KH", "KC", "9H"],
    ["3S", "TC", "8H", "6S", "5H", "JH", "8C", "7D", "AC", "2S"],
    ["QD", "9D", "9C", "3S", "JC", "8C", "KS", "8H", "5D", "4D"],
    ["JS", "AH", "JD", "6D", "9D", "8C", "9H", "9S", "8H", "3H"],
    ["2D", "6S", "4C", "4D", "8S", "AD", "4S", "TC", "AH", "9H"],
    ["TS", "AC", "QC", "TH", "KC", "6D", "4H", "7S", "8C", "2H"],
    ["3C", "QD", "JS", "9D", "5S", "JC", "AH", "2H", "TS", "9H"],
    ["3H", "4D", "QH", "5D", "9C", "5H", "7D", "4S", "JC", "3S"],
    ["8S", "TH", "3H", "7C", "2H", "JD", "JS", "TS", "AC", "8D"],
    ["9C", "2H", "TD", "KC", "JD", "2S", "8C", "5S", "AD", "2C"],
    ["3D", "KD", "7C", "5H", "4D", "QH", "QD", "TC", "6H", "7D"],
    ["7H", "2C", "KC", "5S", "KD", "6H", "AH", "QC", "7S", "QH"],
    ["6H", "5C", "AC", "5H", "2C", "9C", "2D", "7C", "TD", "2S"],
    ["4D", "9D", "AH", "3D", "7C", "JD", "4H", "8C", "4C", "KS"],
    ["TH", "3C", "JS", "QH", "8H", "4C", "AS", "3D", "QS", "QC"],
    ["4D", "7S", "5H", "JH", "6D", "7D", "6H", "JS", "KH", "3C"],
    ["QD", "8S", "7D", "2H", "2C", "7C", "JC", "2S", "5H", "8C"],
    ["QH", "8S", "9D", "TC", "2H", "AD", "7C", "8D", "QD", "6S"],
    ["3S", "7C", "AD", "9H", "2H", "9S", "JD", "TS", "4C", "2D"],
    ["3S", "AS", "4H", "QC", "2C", "8H", "8S", "7S", "TD", "TC"],
    ["JH", "TH", "TD", "3S", "4D", "4H", "5S", "5D", "QS", "2C"],
    ["8C", "QD", "QH", "TC", "6D", "4S", "9S", "9D", "4H", "QC"],
    ["8C", "JS", "9D", "6H", "JD", "3H", "AD", "6S", "TD", "QC"],
    ["KC", "8S", "3D", "7C", "TD", "7D", "8D", "9H", "4S", "3S"],
    ["6C", "4S", "3D", "9D", "KD", "TC", "KC", "KS", "AC", "5S"],
    ["7C", "6S", "QH", "3D", "JS", "KD", "6H", "6D", "2D", "8C"],
    ["JD", "2S", "5S", "4H", "8S", "AC", "2D", "6S", "TS", "5C"],
    ["5H", "8C", "5S", "3C", "4S", "3D", "7C", "8D", "AS", "3H"],
    ["AS", "TS", "7C", "3H", "AD", "7D", "JC", "QS", "6C", "6H"],
    ["3S", "9S", "4C", "AC", "QH", "5H", "5D", "9H", "TS", "4H"],
    ["6C", "5C", "7H", "7S", "TD", "AD", "JD", "5S", "2H", "2S"],
    ["7D", "6C", "KC", "3S", "JD", "8D", "8S", "TS", "QS", "KH"],
    ["8S", "QS", "8D", "6C", "TH", "AC", "AH", "2C", "8H", "9S"],
    ["7H", "TD", "KH", "QH", "8S", "3D", "4D", "AH", "JD", "AS"],
    ["TS", "3D", "2H", "JC", "2S", "JH", "KH", "6C", "QC", "JS"],
    ["KC", "TH", "2D", "6H", "7S", "2S", "TC", "8C", "9D", "QS"],
    ["3C", "9D", "6S", "KH", "8H", "6D", "5D", "TH", "2C", "2H"],
    ["6H", "TC", "7D", "AD", "4D", "8S", "TS", "9H", "TD", "7S"],
    ["JS", "6D", "JD", "JC", "2H", "AC", "6C", "3D", "KH", "8D"],
    ["KH", "JD", "9S", "5D", "4H", "4C", "3H", "7S", "QS", "5C"],
    ["4H", "JD", "5D", "3S", "3C", "4D", "KH", "QH", "QS", "7S"],
    ["JD", "TS", "8S", "QD", "AH", "4C", "6H", "3S", "5S", "2C"],
    ["QS", "3D", "JD", "AS", "8D", "TH", "7C", "6S", "QC", "KS"],
    ["7S", "2H", "8C", "QC", "7H", "AC", "6D", "2D", "TH", "KH"],
    ["5S", "6C", "7H", "KH", "7D", "AH", "8C", "5C", "7S", "3D"],
    ["3C", "KD", "AD", "7D", "6C", "4D", "KS", "2D", "8C", "4S"],
    ["7C", "8D", "5S", "2D", "2S", "AH", "AD", "2C", "9D", "TD"],
    ["3C", "AD", "4S", "KS", "JH", "7C", "5C", "8C", "9C", "TH"],
    ["AS", "TD", "4D", "7C", "JD", "8C", "QH", "3C", "5H", "9S"],
    ["3H", "9C", "8S", "9S", "6S", "QD", "KS", "AH", "5H", "JH"],
    ["QC", "9C", "5S", "4H", "2H", "TD", "7D", "AS", "8C", "9D"],
    ["8C", "2C", "9D", "KD", "TC", "7S", "3D", "KH", "QC", "3C"],
    ["4D", "AS", "4C", "QS", "5S", "9D", "6S", "JD", "QH", "KS"],
    ["6D", "AH", "6C", "4C", "5H", "TS", "9H", "7D", "3D", "5S"],
    ["QS", "JD", "7C", "8D", "9C", "AC", "3S", "6S", "6C", "KH"],
    ["8H", "JH", "5D", "9S", "6D", "AS", "6S", "3S", "QC", "7H"],
    ["QD", "AD", "5C", "JH", "2H", "AH", "4H", "AS", "KC", "2C"],
    ["JH", "9C", "2C", "6H", "2D", "JS", "5D", "9H", "KC", "6D"],
    ["7D", "9D", "KD", "TH", "3H", "AS", "6S", "QC", "6H", "AD"],
    ["JD", "4H", "7D", "KC", "3H", "JS", "3C", "TH", "3D", "QS"],
    ["4C", "3H", "8C", "QD", "5H", "6H", "AS", "8H", "AD", "JD"],
    ["TH", "8S", "KD", "5D", "QC", "7D", "JS", "5S", "5H", "TS"],
    ["7D", "KC", "9D", "QS", "3H", "3C", "6D", "TS", "7S", "AH"],
    ["7C", "4H", "7H", "AH", "QC", "AC", "4D", "5D", "6D", "TH"],
    ["3C", "4H", "2S", "KD", "8H", "5H", "JH", "TC", "6C", "JD"],
    ["4S", "8C", "3D", "4H", "JS", "TD", "7S", "JH", "QS", "KD"],
    ["7C", "QC", "KD", "4D", "7H", "6S", "AD", "TD", "TC", "KH"],
    ["5H", "9H", "KC", "3H", "4D", "3D", "AD", "6S", "QD", "6H"],
    ["TH", "7C", "6H", "TS", "QH", "5S", "2C", "KC", "TD", "6S"],
    ["7C", "4D", "5S", "JD", "JH", "7D", "AC", "KD", "KH", "4H"],
    ["7D", "6C", "8D", "8H", "5C", "JH", "8S", "QD", "TH", "JD"],
    ["8D", "7D", "6C", "7C", "9D", "KD", "AS", "5C", "QH", "JH"],
    ["9S", "2C", "8C", "3C", "4C", "KS", "JH", "2D", "8D", "4H"],
    ["7S", "6C", "JH", "KH", "8H", "3H", "9D", "2D", "AH", "6D"],
    ["4D", "TC", "9C", "8D", "7H", "TD", "KS", "TH", "KD", "3C"],
    ["JD", "9H", "8D", "QD", "AS", "KD", "9D", "2C", "2S", "9C"],
    ["8D", "3H", "5C", "7H", "KS", "5H", "QH", "2D", "8C", "9H"],
    ["2D", "TH", "6D", "QD", "6C", "KC", "3H", "3S", "AD", "4C"],
    ["4H", "3H", "JS", "9D", "3C", "TC", "5H", "QH", "QC", "JC"],
    ["3D", "5C", "6H", "3S", "3C", "JC", "5S", "7S", "2S", "QH"],
    ["AC", "5C", "8C", "4D", "5D", "4H", "2S", "QD", "3C", "3H"],
    ["2C", "TD", "AH", "9C", "KD", "JS", "6S", "QD", "4C", "QC"],
    ["QS", "8C", "3S", "4H", "TC", "JS", "3H", "7C", "JC", "AD"],
    ["5H", "4D", "9C", "KS", "JC", "TD", "9S", "TS", "8S", "9H"],
    ["QD", "TS", "7D", "AS", "AC", "2C", "TD", "6H", "8H", "AH"],
    ["6S", "AD", "8C", "4S", "9H", "8D", "9D", "KH", "8S", "3C"],
    ["QS", "4D", "2D", "7S", "KH", "JS", "JC", "AD", "4C", "3C"],
    ["QS", "9S", "7H", "KC", "TD", "TH", "5H", "JS", "AC", "JH"],
    ["6D", "AC", "2S", "QS", "7C", "AS", "KS", "6S", "KH", "5S"],
    ["6D", "8H", "KH", "3C", "QS", "2H", "5C", "9C", "9D", "6C"],
    ["JS", "2C", "4C", "6H", "7D", "JC", "AC", "QD", "TD", "3H"],
    ["4H", "QC", "8H", "JD", "4C", "KD", "KS", "5C", "KC", "7S"],
    ["6D", "2D", "3H", "2S", "QD", "5S", "7H", "AS", "TH", "6S"],
    ["AS", "6D", "8D", "2C", "8S", "TD", "8H", "QD", "JC", "AH"],
    ["9C", "9H", "2D", "TD", "QH", "2H", "5C", "TC", "3D", "8H"],
    ["KC", "8S", "3D", "KH", "2S", "TS", "TC", "6S", "4D", "JH"],
    ["9H", "9D", "QS", "AC", "KC", "6H", "5D", "4D", "8D", "AH"],
    ["9S", "5C", "QS", "4H", "7C", "7D", "2H", "8S", "AD", "JS"],
    ["3D", "AC", "9S", "AS", "2C", "2D", "2H", "3H", "JC", "KH"],
    ["7H", "QH", "KH", "JD", "TC", "KS", "5S", "8H", "4C", "8D"],
    ["2H", "7H", "3S", "2S", "5H", "QS", "3C", "AS", "9H", "KD"],
    ["AD", "3D", "JD", "6H", "5S", "9C", "6D", "AC", "9S", "3S"],
    ["3D", "5D", "9C", "2D", "AC", "4S", "2S", "AD", "6C", "6S"],
    ["QC", "4C", "2D", "3H", "6S", "KC", "QH", "QD", "2H", "JH"],
    ["QC", "3C", "8S", "4D", "9S", "2H", "5C", "8H", "QS", "QD"],
    ["6D", "KD", "6S", "7H", "3S", "KH", "2H", "5C", "JC", "6C"],
    ["3S", "9S", "TC", "6S", "8H", "2D", "AD", "7S", "8S", "TS"],
    ["3C", "6H", "9C", "3H", "5C", "JC", "8H", "QH", "TD", "QD"],
    ["3C", "JS", "QD", "5D", "TD", "2C", "KH", "9H", "TH", "AS"],
    ["9S", "TC", "JD", "3D", "5C", "5H", "AD", "QH", "9H", "KC"],
    ["TC", "7H", "4H", "8H", "3H", "TD", "6S", "AC", "7C", "2S"],
    ["QS", "9D", "5D", "3C", "JC", "KS", "4D", "6C", "JH", "2S"],
    ["9S", "6S", "3C", "7H", "TS", "4C", "KD", "6D", "3D", "9C"],
    ["2D", "9H", "AH", "AC", "7H", "2S", "JH", "3S", "7C", "QC"],
    ["QD", "9H", "3C", "2H", "AC", "AS", "8S", "KD", "8C", "KH"],
    ["2D", "7S", "TD", "TH", "6D", "JD", "8D", "4D", "2H", "5S"],
    ["8S", "QH", "KD", "JD", "QS", "JH", "4D", "KC", "5H", "3S"],
    ["3C", "KH", "QC", "6D", "8H", "3S", "AH", "7D", "TD", "2D"],
    ["5S", "9H", "QH", "4S", "6S", "6C", "6D", "TS", "TH", "7S"],
    ["6C", "4C", "6D", "QS", "JS", "9C", "TS", "3H", "8D", "8S"],
    ["JS", "5C", "7S", "AS", "2C", "AH", "2H", "AD", "5S", "TC"],
    ["KD", "6C", "9C", "9D", "TS", "2S", "JC", "4H", "2C", "QD"],
    ["QS", "9H", "TC", "3H", "KC", "KS", "4H", "3C", "AD", "TH"],
    ["KH", "9C", "2H", "KD", "9D", "TC", "7S", "KC", "JH", "2D"],
    ["7C", "3S", "KC", "AS", "8C", "5D", "9C", "9S", "QH", "3H"],
    ["2D", "8C", "TD", "4C", "2H", "QC", "5D", "TC", "2C", "7D"],
    ["KS", "4D", "6C", "QH", "TD", "KH", "5D", "7C", "AD", "8D"],
    ["2S", "9S", "8S", "4C", "8C", "3D", "6H", "QD", "7C", "7H"],
    ["6C", "8S", "QH", "5H", "TS", "5C", "3C", "4S", "2S", "2H"],
    ["8S", "6S", "2H", "JC", "3S", "3H", "9D", "8C", "2S", "7H"],
    ["QC", "2C", "8H", "9C", "AC", "JD", "4C", "4H", "6S", "3S"],
    ["3H", "3S", "7D", "4C", "9S", "5H", "8H", "JC", "3D", "TC"],
    ["QH", "2S", "2D", "9S", "KD", "QD", "9H", "AD", "6D", "9C"],
    ["8D", "2D", "KS", "9S", "JC", "4C", "JD", "KC", "4S", "TH"],
    ["KH", "TS", "6D", "4D", "5C", "KD", "5H", "AS", "9H", "AD"],
    ["QD", "JS", "7C", "6D", "5D", "5C", "TH", "5H", "QH", "QS"],
    ["9D", "QH", "KH", "5H", "JH", "4C", "4D", "TC", "TH", "6C"],
    ["KH", "AS", "TS", "9D", "KD", "9C", "7S", "4D", "8H", "5S"],
    ["KH", "AS", "2S", "7D", "9D", "4C", "TS", "TH", "AH", "7C"],
    ["KS", "4D", "AC", "8S", "9S", "8D", "TH", "QH", "9D", "5C"],
    ["5D", "5C", "8C", "QS", "TC", "4C", "3D", "3S", "2C", "8D"],
    ["9D", "KS", "2D", "3C", "KC", "4S", "8C", "KH", "6C", "JC"],
    ["8H", "AH", "6H", "7D", "7S", "QD", "3C", "4C", "6C", "KC"],
    ["3H", "2C", "QH", "8H", "AS", "7D", "4C", "8C", "4H", "KC"],
    ["QD", "5S", "4H", "2C", "TD", "AH", "JH", "QH", "4C", "8S"],
    ["3H", "QS", "5S", "JS", "8H", "2S", "9H", "9C", "3S", "2C"],
    ["6H", "TS", "7S", "JC", "QD", "AC", "TD", "KC", "5S", "3H"],
    ["QH", "AS", "QS", "7D", "JC", "KC", "2C", "4C", "5C", "5S"],
    ["QH", "3D", "AS", "JS", "4H", "8D", "7H", "JC", "2S", "9C"],
    ["5D", "4D", "2S", "4S", "9D", "9C", "2D", "QS", "8H", "7H"],
    ["6D", "7H", "3H", "JS", "TS", "AC", "2D", "JH", "7C", "8S"],
    ["JH", "5H", "KC", "3C", "TC", "5S", "9H", "4C", "8H", "9D"],
    ["8S", "KC", "5H", "9H", "AD", "KS", "9D", "KH", "8D", "AH"],
    ["JC", "2H", "9H", "KS", "6S", "3H", "QC", "5H", "AH", "9C"],
    ["5C", "KH", "5S", "AD", "6C", "JC", "9H", "QC", "9C", "TD"],
    ["5S", "5D", "JC", "QH", "2D", "KS", "8H", "QS", "2H", "TS"],
    ["JH", "5H", "5S", "AH", "7H", "3C", "8S", "AS", "TD", "KH"],
    ["6H", "3D", "JD", "2C", "4C", "KC", "7S", "AH", "6C", "JH"],
    ["4C", "KS", "9D", "AD", "7S", "KC", "7D", "8H", "3S", "9C"],
    ["7H", "5C", "5H", "3C", "8H", "QC", "3D", "KH", "6D", "JC"],
    ["2D", "4H", "5D", "7D", "QC", "AD", "AH", "9H", "QH", "8H"],
    ["KD", "8C", "JS", "9D", "3S", "3C", "2H", "5D", "6D", "2S"],
    ["8S", "6S", "TS", "3C", "6H", "8D", "5S", "3H", "TD", "6C"],
    ["KS", "3D", "JH", "9C", "7C", "9S", "QS", "5S", "4H", "6H"],
    ["7S", "6S", "TH", "4S", "KC", "KD", "3S", "JC", "JH", "KS"],
    ["7C", "3C", "2S", "6D", "QH", "2C", "7S", "5H", "8H", "AH"],
    ["KC", "8D", "QD", "6D", "KH", "5C", "7H", "9D", "3D", "9C"],
    ["6H", "2D", "8S", "JS", "9S", "2S", "6D", "KC", "7C", "TC"],
    ["KD", "9C", "JH", "7H", "KC", "8S", "2S", "7S", "3D", "6H"],
    ["4H", "9H", "2D", "4C", "8H", "7H", "5S", "8S", "2H", "8D"],
    ["AD", "7C", "3C", "7S", "5S", "4D", "9H", "3D", "JC", "KH"],
    ["5D", "AS", "7D", "6D", "9C", "JC", "4C", "QH", "QS", "KH"],
    ["KD", "JD", "7D", "3D", "QS", "QC", "8S", "6D", "JS", "QD"],
    ["6S", "8C", "5S", "QH", "TH", "9H", "AS", "AC", "2C", "JD"],
    ["QC", "KS", "QH", "7S", "3C", "4C", "5C", "KC", "5D", "AH"],
    ["6C", "4H", "9D", "AH", "2C", "3H", "KD", "3D", "TS", "5C"],
    ["TD", "8S", "QS", "AS", "JS", "3H", "KD", "AC", "4H", "KS"],
    ["7D", "5D", "TS", "9H", "4H", "4C", "9C", "2H", "8C", "QC"],
    ["2C", "7D", "9H", "4D", "KS", "4C", "QH", "AD", "KD", "JS"],
    ["QD", "AD", "AH", "KH", "9D", "JS", "9H", "JC", "KD", "JD"],
    ["8S", "3C", "4S", "TS", "7S", "4D", "5C", "2S", "6H", "7C"],
    ["JS", "7S", "5C", "KD", "6D", "QH", "8S", "TD", "2H", "6S"],
    ["QH", "6C", "TC", "6H", "TD", "4C", "9D", "2H", "QC", "8H"],
    ["3D", "TS", "4D", "2H", "6H", "6S", "2C", "7H", "8S", "6C"],
    ["9H", "9D", "JD", "JH", "3S", "AH", "2C", "6S", "3H", "8S"],
    ["2C", "QS", "8C", "5S", "3H", "2S", "7D", "3C", "AD", "4S"],
    ["5C", "QC", "QH", "AS", "TS", "4S", "6S", "4C", "5H", "JS"],
    ["JH", "5C", "TD", "4C", "6H", "JS", "KD", "KH", "QS", "4H"],
    ["TC", "KH", "JC", "4D", "9H", "9D", "8D", "KC", "3C", "8H"],
    ["2H", "TC", "8S", "AD", "9S", "4H", "TS", "7H", "2C", "5C"],
    ["4H", "2S", "6C", "5S", "KS", "AH", "9C", "7C", "8H", "KD"],
    ["TS", "QH", "TD", "QS", "3C", "JH", "AH", "2C", "8D", "7D"],
    ["5D", "KC", "3H", "5S", "AC", "4S", "7H", "QS", "4C", "2H"],
    ["3D", "7D", "QC", "KH", "JH", "6D", "6C", "TD", "TH", "KD"],
    ["5S", "8D", "TH", "6C", "9D", "7D", "KH", "8C", "9S", "6D"],
    ["JD", "QS", "7S", "QC", "2S", "QH", "JC", "4S", "KS", "8D"],
    ["7S", "5S", "9S", "JD", "KD", "9C", "JC", "AD", "2D", "7C"],
    ["4S", "5H", "AH", "JH", "9C", "5D", "TD", "7C", "2D", "6S"],
    ["KC", "6C", "7H", "6S", "9C", "QD", "5S", "4H", "KS", "TD"],
    ["6S", "8D", "KS", "2D", "TH", "TD", "9H", "JD", "TS", "3S"],
    ["KH", "JS", "4H", "5D", "9D", "TC", "TD", "QC", "JD", "TS"],
    ["QS", "QD", "AC", "AD", "4C", "6S", "2D", "AS", "3H", "KC"],
    ["4C", "7C", "3C", "TD", "QS", "9C", "KC", "AS", "8D", "AD"],
    ["KC", "7H", "QC", "6D", "8H", "6S", "5S", "AH", "7S", "8C"],
    ["3S", "AD", "9H", "JC", "6D", "JD", "AS", "KH", "6S", "JH"],
    ["AD", "3D", "TS", "KS", "7H", "JH", "2D", "JS", "QD", "AC"],
    ["9C", "JD", "7C", "6D", "TC", "6H", "6C", "JC", "3D", "3S"],
    ["QC", "KC", "3S", "JC", "KD", "2C", "8D", "AH", "QS", "TS"],
    ["AS", "KD", "3D", "JD", "8H", "7C", "8C", "5C", "QD", "6C"]]

    count = 0
    for x in l:

         hand1 = x[0:5]
         hand2 = x[5:]
         if compareHands(hand1, hand2) == 1:
             count = count + 1
    return count

def isSuccessive(l):
    for i in range(0, len(l) - 1):
        if l[i] + 1 != l[i + 1]:
            return False
    return True

def processHand(h):
    suit = ["S","D","C","H"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = [x[1] for x in h]
    ranks = [x[0] for x in h]
    l = []
    for y in ranks:
        if y == "T":
            l = l + [10]
        elif y == "J":
            l = l + [11]
        elif y == "Q":
            l = l + [12]
        elif y == "K":
            l = l + [13]
        elif y == "A":
            l = l + [14]
        else:
            l = l + [int(y)]
    return l

def isStraight(h):
    suit = ["S","D","C","H"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = [x[1] for x in h]
    ranks = [x[0] for x in h]
    l = []
    for y in ranks:
        if y == "T":
            l = l + [10]
        elif y == "J":
            l = l + [11]
        elif y == "Q":
            l = l + [12]
        elif y == "K":
            l = l + [13]
        elif y == "A":
            l = l + ["A"]
        else:
            l = l + [int(y)]
    if "A" in l:
        l1 = [x for x in l if x != "A"] + [1]
        l2 = [x for x in l if x != "A"] + [14]
        l1.sort()
        l2.sort()

        if isSuccessive(l1) or isSuccessive(l2):
            return True
        else:
            return False
    else:
        l.sort()
        return isSuccessive(l)

def isFlush(h):
    if len(set([x[1] for x in h])) == 1:
        return True
    return False

def isRoyal(h):#since here it's already both a straight and a flush, all I have to do is check for the Ace and the King.
    ranks = [x[0] for x in h]
    if "A" in ranks and "K" in ranks:
        return True
    return False

def detHandRank(h):#0 for high card, 1 for a pair, 2 for 2 pair, 3 for a set, 4 = straight, 5 = flush, 6 = FH, 7 = 4 of a kind, 8 = SF, 9 = RF
    if len(h) != 5:
        print "wtf..."
        return -1

    suit = ["S","D","C", "H"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    suits = [x[1] for x in h]
    ranks = [x[0] for x in h]

    if len(set(ranks)) == len(ranks):#will either be only a high card, or some kind of straight or flush
        straight = isStraight(h)
        flush = isFlush(h)
        if straight and flush:
            royal = isRoyal(h)
            if royal:
                return 9
            else:
                return 8
        elif straight and not flush:
            return 4
        elif not straight and flush:#flush
            return 5
        else:
            return 0#just a high card
    else:#not a straight or flush or high card, could be any kind of pair, 2 pair, or set or a full house, or 4 of a kind
        curr = len(set(ranks))
        if curr == 1:
            return 7#must be 4 of a kind
        elif curr == 2:#full house
            return 6
        elif curr == 3:#set or 2 pair
            counts = [ranks.count(x) for x in ranks]
            if max(counts) == 3:
                return 3
            else:#2 pair
                return 2
        elif curr == 4:#just a pair
            return 1
        else:
            print "bad, very bad"

def compareHands(h1, h2):
    h1Rank = detHandRank(h1)
    h2Rank = detHandRank(h2)
    if h1Rank > h2Rank:
        return 1
    elif h1Rank == h2Rank:
        return compareSameRank(h1,h2, h1Rank)
    return 0

def compareSameRank(h1, h2, rank):#0 for high card, 1 for a pair, 2 for 2 pair, 3 for a set, 4 = straight, 5 = flush, 6 = FH, 7 = 4 of a kind, 8 = SF, 9 = RF
    l1 = processHand(h1)
    l2 = processHand(h2)

    if rank == 0:
        return compHighCard(l1, l2)
    elif rank == 1:#pair
        paired1 = [x for x in l1 if l1.count(x) == 2]
        paired2 = [x for x in l2 if l2.count(x) == 2]
        if max(paired1) != max(paired2):
            return compHighCard(paired1, paired2)
        nonP1 = list(set(l1).difference(set(paired1)))
        nonP2 = list(set(l2).difference(set(paired2)))
        return compHighCard(nonP1, nonP2)
    elif rank == 2:
        paired1 = [x for x in l1 if l1.count(x) == 2]
        paired2 = [x for x in l2 if l2.count(x) == 2]
        if max(paired1) != max(paired2):
            return compHighCard(paired1, paired2)
        else:
            lower1 = list(set(l1).difference(set([max(paired1)])))
            lower2 = list(set(l2).difference(set([max(paired2)])))
            if max(lower1) != max(lower2):
                return compHighCard(lower1, lower2)
            else:
                nonP1 = list(set(l1).difference(set(lower1)))
                nonP2 = list(set(l2).difference(set(lower2)))
                return compHighCard(nonP1, nonP2)
    elif rank == 3:
        set1 = [x for x in l1 if l1.count(x) == 3]
        set2 = [x for x in l2 if l2.count(x) == 3]
        if max(set1) != max(set2):
            return compHighCard(set1, set2)
        else:
            nonS1 = list(set(l1).difference(set(set1)))
            nonS2 = list(set(l2).difference(set(set2)))
            return compHighCard(nonS1, nonS2)
    elif rank == 4:
        if max(l1) > max(l2) and max(l1) != 14 and max(l2) != 14:
            return 1
        elif max(l1) < max(l2) and max(l1) != 14 and max(l2) != 14:
            return 0
        else:#there's an ace
            max1 = 14
            max2 = 14
            if 5 in l1:
                max1 = 5
            if 5 in l2:
                max2 = 5
            if max1 > max2:
                return 1
            return 0

    elif rank == 5:
        if max(l1) > max(l2):
            return 1
        return 0
    elif rank == 6:

        set1 = [x for x in l1 if l1.count(x) == 3]
        set2 = [x for x in l2 if l2.count(x) == 3]
        paired1 = [x for x in l1 if l1.count(x) == 2]
        paired2 = [x for x in l2 if l2.count(x) == 2]

        if max(set1) != max(set2):
            return compHighCard(set1, set2)
        elif max(paired1) != max(paired2):
            return compHighCard(paired1, paired2)
        else:
            print "equal full houses???.....should never happen"

    elif rank == 7:
        quad1 = [x for x in l1 if l1.count(x) == 4]
        quad2 = [x for x in l2 if l2.count(x) == 4]
        return compHighCard(set1, set2)
    elif rank == 8:
        max1 = max(l1)
        max2 = max(l2)
        if max1 == 14:
            max1 = 5
        if max2 == 14:
            max2 = 5
        if max1 > max2:
            return 1
        elif max2 > max1:
            return 0
        else:
            print "2 equivalent straight flushes..."
    else:
        print "should never have 2 equivalent royal flushes"




def compHighCard(l1, l2):
    if max(l1) > max(l2):
        return 1
    elif max(l2) > max(l1):
        return 0
    else:
        print "should be going in here"
        newL1 = list(set(l1).difference(set([max(l1)])))
        newL2 = list(set(l2).difference(set([max(l2)])))
        print newL1
        print newL2
        return compHighCard(newL1, newL2)

def euler99():
    l = [(519432,525806),
    (632382,518061),
    (78864,613712),
    (466580,530130),
    (780495,510032),
    (525895,525320),
    (15991,714883),
    (960290,502358),
    (760018,511029),
    (166800,575487),
    (210884,564478),
    (555151,523163),
    (681146,515199),
    (563395,522587),
    (738250,512126),
    (923525,503780),
    (595148,520429),
    (177108,572629),
    (750923,511482),
    (440902,532446),
    (881418,505504),
    (422489,534197),
    (979858,501616),
    (685893,514935),
    (747477,511661),
    (167214,575367),
    (234140,559696),
    (940238,503122),
    (728969,512609),
    (232083,560102),
    (900971,504694),
    (688801,514772),
    (189664,569402),
    (891022,505104),
    (445689,531996),
    (119570,591871),
    (821453,508118),
    (371084,539600),
    (911745,504251),
    (623655,518600),
    (144361,582486),
    (352442,541775),
    (420726,534367),
    (295298,549387),
    (6530,787777),
    (468397,529976),
    (672336,515696),
    (431861,533289),
    (84228,610150),
    (805376,508857),
    (444409,532117),
    (33833,663511),
    (381850,538396),
    (402931,536157),
    (92901,604930),
    (304825,548004),
    (731917,512452),
    (753734,511344),
    (51894,637373),
    (151578,580103),
    (295075,549421),
    (303590,548183),
    (333594,544123),
    (683952,515042),
    (60090,628880),
    (951420,502692),
    (28335,674991),
    (714940,513349),
    (343858,542826),
    (549279,523586),
    (804571,508887),
    (260653,554881),
    (291399,549966),
    (402342,536213),
    (408889,535550),
    (40328,652524),
    (375856,539061),
    (768907,510590),
    (165993,575715),
    (976327,501755),
    (898500,504795),
    (360404,540830),
    (478714,529095),
    (694144,514472),
    (488726,528258),
    (841380,507226),
    (328012,544839),
    (22389,690868),
    (604053,519852),
    (329514,544641),
    (772965,510390),
    (492798,527927),
    (30125,670983),
    (895603,504906),
    (450785,531539),
    (840237,507276),
    (380711,538522),
    (63577,625673),
    (76801,615157),
    (502694,527123),
    (597706,520257),
    (310484,547206),
    (944468,502959),
    (121283,591152),
    (451131,531507),
    (566499,522367),
    (425373,533918),
    (40240,652665),
    (39130,654392),
    (714926,513355),
    (469219,529903),
    (806929,508783),
    (287970,550487),
    (92189,605332),
    (103841,599094),
    (671839,515725),
    (452048,531421),
    (987837,501323),
    (935192,503321),
    (88585,607450),
    (613883,519216),
    (144551,582413),
    (647359,517155),
    (213902,563816),
    (184120,570789),
    (258126,555322),
    (502546,527130),
    (407655,535678),
    (401528,536306),
    (477490,529193),
    (841085,507237),
    (732831,512408),
    (833000,507595),
    (904694,504542),
    (581435,521348),
    (455545,531110),
    (873558,505829),
    (94916,603796),
    (720176,513068),
    (545034,523891),
    (246348,557409),
    (556452,523079),
    (832015,507634),
    (173663,573564),
    (502634,527125),
    (250732,556611),
    (569786,522139),
    (216919,563178),
    (521815,525623),
    (92304,605270),
    (164446,576167),
    (753413,511364),
    (11410,740712),
    (448845,531712),
    (925072,503725),
    (564888,522477),
    (7062,780812),
    (641155,517535),
    (738878,512100),
    (636204,517828),
    (372540,539436),
    (443162,532237),
    (571192,522042),
    (655350,516680),
    (299741,548735),
    (581914,521307),
    (965471,502156),
    (513441,526277),
    (808682,508700),
    (237589,559034),
    (543300,524025),
    (804712,508889),
    (247511,557192),
    (543486,524008),
    (504383,526992),
    (326529,545039),
    (792493,509458),
    (86033,609017),
    (126554,589005),
    (579379,521481),
    (948026,502823),
    (404777,535969),
    (265767,554022),
    (266876,553840),
    (46631,643714),
    (492397,527958),
    (856106,506581),
    (795757,509305),
    (748946,511584),
    (294694,549480),
    (409781,535463),
    (775887,510253),
    (543747,523991),
    (210592,564536),
    (517119,525990),
    (520253,525751),
    (247926,557124),
    (592141,520626),
    (346580,542492),
    (544969,523902),
    (506501,526817),
    (244520,557738),
    (144745,582349),
    (69274,620858),
    (292620,549784),
    (926027,503687),
    (736320,512225),
    (515528,526113),
    (407549,535688),
    (848089,506927),
    (24141,685711),
    (9224,757964),
    (980684,501586),
    (175259,573121),
    (489160,528216),
    (878970,505604),
    (969546,502002),
    (525207,525365),
    (690461,514675),
    (156510,578551),
    (659778,516426),
    (468739,529945),
    (765252,510770),
    (76703,615230),
    (165151,575959),
    (29779,671736),
    (928865,503569),
    (577538,521605),
    (927555,503618),
    (185377,570477),
    (974756,501809),
    (800130,509093),
    (217016,563153),
    (365709,540216),
    (774508,510320),
    (588716,520851),
    (631673,518104),
    (954076,502590),
    (777828,510161),
    (990659,501222),
    (597799,520254),
    (786905,509727),
    (512547,526348),
    (756449,511212),
    (869787,505988),
    (653747,516779),
    (84623,609900),
    (839698,507295),
    (30159,670909),
    (797275,509234),
    (678136,515373),
    (897144,504851),
    (989554,501263),
    (413292,535106),
    (55297,633667),
    (788650,509637),
    (486748,528417),
    (150724,580377),
    (56434,632490),
    (77207,614869),
    (588631,520859),
    (611619,519367),
    (100006,601055),
    (528924,525093),
    (190225,569257),
    (851155,506789),
    (682593,515114),
    (613043,519275),
    (514673,526183),
    (877634,505655),
    (878905,505602),
    (1926,914951),
    (613245,519259),
    (152481,579816),
    (841774,507203),
    (71060,619442),
    (865335,506175),
    (90244,606469),
    (302156,548388),
    (399059,536557),
    (478465,529113),
    (558601,522925),
    (69132,620966),
    (267663,553700),
    (988276,501310),
    (378354,538787),
    (529909,525014),
    (161733,576968),
    (758541,511109),
    (823425,508024),
    (149821,580667),
    (269258,553438),
    (481152,528891),
    (120871,591322),
    (972322,501901),
    (981350,501567),
    (676129,515483),
    (950860,502717),
    (119000,592114),
    (392252,537272),
    (191618,568919),
    (946699,502874),
    (289555,550247),
    (799322,509139),
    (703886,513942),
    (194812,568143),
    (261823,554685),
    (203052,566221),
    (217330,563093),
    (734748,512313),
    (391759,537328),
    (807052,508777),
    (564467,522510),
    (59186,629748),
    (113447,594545),
    (518063,525916),
    (905944,504492),
    (613922,519213),
    (439093,532607),
    (445946,531981),
    (230530,560399),
    (297887,549007),
    (459029,530797),
    (403692,536075),
    (855118,506616),
    (963127,502245),
    (841711,507208),
    (407411,535699),
    (924729,503735),
    (914823,504132),
    (333725,544101),
    (176345,572832),
    (912507,504225),
    (411273,535308),
    (259774,555036),
    (632853,518038),
    (119723,591801),
    (163902,576321),
    (22691,689944),
    (402427,536212),
    (175769,572988),
    (837260,507402),
    (603432,519893),
    (313679,546767),
    (538165,524394),
    (549026,523608),
    (61083,627945),
    (898345,504798),
    (992556,501153),
    (369999,539727),
    (32847,665404),
    (891292,505088),
    (152715,579732),
    (824104,507997),
    (234057,559711),
    (730507,512532),
    (960529,502340),
    (388395,537687),
    (958170,502437),
    (57105,631806),
    (186025,570311),
    (993043,501133),
    (576770,521664),
    (215319,563513),
    (927342,503628),
    (521353,525666),
    (39563,653705),
    (752516,511408),
    (110755,595770),
    (309749,547305),
    (374379,539224),
    (919184,503952),
    (990652,501226),
    (647780,517135),
    (187177,570017),
    (168938,574877),
    (649558,517023),
    (278126,552016),
    (162039,576868),
    (658512,516499),
    (498115,527486),
    (896583,504868),
    (561170,522740),
    (747772,511647),
    (775093,510294),
    (652081,516882),
    (724905,512824),
    (499707,527365),
    (47388,642755),
    (646668,517204),
    (571700,522007),
    (180430,571747),
    (710015,513617),
    (435522,532941),
    (98137,602041),
    (759176,511070),
    (486124,528467),
    (526942,525236),
    (878921,505604),
    (408313,535602),
    (926980,503640),
    (882353,505459),
    (566887,522345),
    (3326,853312),
    (911981,504248),
    (416309,534800),
    (392991,537199),
    (622829,518651),
    (148647,581055),
    (496483,527624),
    (666314,516044),
    (48562,641293),
    (672618,515684),
    (443676,532187),
    (274065,552661),
    (265386,554079),
    (347668,542358),
    (31816,667448),
    (181575,571446),
    (961289,502320),
    (365689,540214),
    (987950,501317),
    (932299,503440),
    (27388,677243),
    (746701,511701),
    (492258,527969),
    (147823,581323),
    (57918,630985),
    (838849,507333),
    (678038,515375),
    (27852,676130),
    (850241,506828),
    (818403,508253),
    (131717,587014),
    (850216,506834),
    (904848,504529),
    (189758,569380),
    (392845,537217),
    (470876,529761),
    (925353,503711),
    (285431,550877),
    (454098,531234),
    (823910,508003),
    (318493,546112),
    (766067,510730),
    (261277,554775),
    (421530,534289),
    (694130,514478),
    (120439,591498),
    (213308,563949),
    (854063,506662),
    (365255,540263),
    (165437,575872),
    (662240,516281),
    (289970,550181),
    (847977,506933),
    (546083,523816),
    (413252,535113),
    (975829,501767),
    (361540,540701),
    (235522,559435),
    (224643,561577),
    (736350,512229),
    (328303,544808),
    (35022,661330),
    (307838,547578),
    (474366,529458),
    (873755,505819),
    (73978,617220),
    (827387,507845),
    (670830,515791),
    (326511,545034),
    (309909,547285),
    (400970,536363),
    (884827,505352),
    (718307,513175),
    (28462,674699),
    (599384,520150),
    (253565,556111),
    (284009,551093),
    (343403,542876),
    (446557,531921),
    (992372,501160),
    (961601,502308),
    (696629,514342),
    (919537,503945),
    (894709,504944),
    (892201,505051),
    (358160,541097),
    (448503,531745),
    (832156,507636),
    (920045,503924),
    (926137,503675),
    (416754,534757),
    (254422,555966),
    (92498,605151),
    (826833,507873),
    (660716,516371),
    (689335,514746),
    (160045,577467),
    (814642,508425),
    (969939,501993),
    (242856,558047),
    (76302,615517),
    (472083,529653),
    (587101,520964),
    (99066,601543),
    (498005,527503),
    (709800,513624),
    (708000,513716),
    (20171,698134),
    (285020,550936),
    (266564,553891),
    (981563,501557),
    (846502,506991),
    (334,1190800),
    (209268,564829),
    (9844,752610),
    (996519,501007),
    (410059,535426),
    (432931,533188),
    (848012,506929),
    (966803,502110),
    (983434,501486),
    (160700,577267),
    (504374,526989),
    (832061,507640),
    (392825,537214),
    (443842,532165),
    (440352,532492),
    (745125,511776),
    (13718,726392),
    (661753,516312),
    (70500,619875),
    (436952,532814),
    (424724,533973),
    (21954,692224),
    (262490,554567),
    (716622,513264),
    (907584,504425),
    (60086,628882),
    (837123,507412),
    (971345,501940),
    (947162,502855),
    (139920,584021),
    (68330,621624),
    (666452,516038),
    (731446,512481),
    (953350,502619),
    (183157,571042),
    (845400,507045),
    (651548,516910),
    (20399,697344),
    (861779,506331),
    (629771,518229),
    (801706,509026),
    (189207,569512),
    (737501,512168),
    (719272,513115),
    (479285,529045),
    (136046,585401),
    (896746,504860),
    (891735,505067),
    (684771,514999),
    (865309,506184),
    (379066,538702),
    (503117,527090),
    (621780,518717),
    (209518,564775),
    (677135,515423),
    (987500,501340),
    (197049,567613),
    (329315,544673),
    (236756,559196),
    (357092,541226),
    (520440,525733),
    (213471,563911),
    (956852,502490),
    (702223,514032),
    (404943,535955),
    (178880,572152),
    (689477,514734),
    (691351,514630),
    (866669,506128),
    (370561,539656),
    (739805,512051),
    (71060,619441),
    (624861,518534),
    (261660,554714),
    (366137,540160),
    (166054,575698),
    (601878,519990),
    (153445,579501),
    (279899,551729),
    (379166,538691),
    (423209,534125),
    (675310,515526),
    (145641,582050),
    (691353,514627),
    (917468,504026),
    (284778,550976),
    (81040,612235),
    (161699,576978),
    (616394,519057),
    (767490,510661),
    (156896,578431),
    (427408,533714),
    (254849,555884),
    (737217,512182),
    (897133,504851),
    (203815,566051),
    (270822,553189),
    (135854,585475),
    (778805,510111),
    (784373,509847),
    (305426,547921),
    (733418,512375),
    (732087,512448),
    (540668,524215),
    (702898,513996),
    (628057,518328),
    (640280,517587),
    (422405,534204),
    (10604,746569),
    (746038,511733),
    (839808,507293),
    (457417,530938),
    (479030,529064),
    (341758,543090),
    (620223,518824),
    (251661,556451),
    (561790,522696),
    (497733,527521),
    (724201,512863),
    (489217,528217),
    (415623,534867),
    (624610,518548),
    (847541,506953),
    (432295,533249),
    (400391,536421),
    (961158,502319),
    (139173,584284),
    (421225,534315),
    (579083,521501),
    (74274,617000),
    (701142,514087),
    (374465,539219),
    (217814,562985),
    (358972,540995),
    (88629,607424),
    (288597,550389),
    (285819,550812),
    (538400,524385),
    (809930,508645),
    (738326,512126),
    (955461,502535),
    (163829,576343),
    (826475,507891),
    (376488,538987),
    (102234,599905),
    (114650,594002),
    (52815,636341),
    (434037,533082),
    (804744,508880),
    (98385,601905),
    (856620,506559),
    (220057,562517),
    (844734,507078),
    (150677,580387),
    (558697,522917),
    (621751,518719),
    (207067,565321),
    (135297,585677),
    (932968,503404),
    (604456,519822),
    (579728,521462),
    (244138,557813),
    (706487,513800),
    (711627,513523),
    (853833,506674),
    (497220,527562),
    (59428,629511),
    (564845,522486),
    (623621,518603),
    (242689,558077),
    (125091,589591),
    (363819,540432),
    (686453,514901),
    (656813,516594),
    (489901,528155),
    (386380,537905),
    (542819,524052),
    (243987,557841),
    (693412,514514),
    (488484,528271),
    (896331,504881),
    (336730,543721),
    (728298,512647),
    (604215,519840),
    (153729,579413),
    (595687,520398),
    (540360,524240),
    (245779,557511),
    (924873,503730),
    (509628,526577),
    (528523,525122),
    (3509,847707),
    (522756,525555),
    (895447,504922),
    (44840,646067),
    (45860,644715),
    (463487,530404),
    (398164,536654),
    (894483,504959),
    (619415,518874),
    (966306,502129),
    (990922,501212),
    (835756,507474),
    (548881,523618),
    (453578,531282),
    (474993,529410),
    (80085,612879),
    (737091,512193),
    (50789,638638),
    (979768,501620),
    (792018,509483),
    (665001,516122),
    (86552,608694),
    (462772,530469),
    (589233,520821),
    (891694,505072),
    (592605,520594),
    (209645,564741),
    (42531,649269),
    (554376,523226),
    (803814,508929),
    (334157,544042),
    (175836,572970),
    (868379,506051),
    (658166,516520),
    (278203,551995),
    (966198,502126),
    (627162,518387),
    (296774,549165),
    (311803,547027),
    (843797,507118),
    (702304,514032),
    (563875,522553),
    (33103,664910),
    (191932,568841),
    (543514,524006),
    (506835,526794),
    (868368,506052),
    (847025,506971),
    (678623,515342),
    (876139,505726),
    (571997,521984),
    (598632,520198),
    (213590,563892),
    (625404,518497),
    (726508,512738),
    (689426,514738),
    (332495,544264),
    (411366,535302),
    (242546,558110),
    (315209,546555),
    (797544,509219),
    (93889,604371),
    (858879,506454),
    (124906,589666),
    (449072,531693),
    (235960,559345),
    (642403,517454),
    (720567,513047),
    (705534,513858),
    (603692,519870),
    (488137,528302),
    (157370,578285),
    (63515,625730),
    (666326,516041),
    (619226,518883),
    (443613,532186),
    (597717,520257),
    (96225,603069),
    (86940,608450),
    (40725,651929),
    (460976,530625),
    (268875,553508),
    (270671,553214),
    (363254,540500),
    (384248,538137),
    (762889,510892),
    (377941,538833),
    (278878,551890),
    (176615,572755),
    (860008,506412),
    (944392,502967),
    (608395,519571),
    (225283,561450),
    (45095,645728),
    (333798,544090),
    (625733,518476),
    (995584,501037),
    (506135,526853),
    (238050,558952),
    (557943,522972),
    (530978,524938),
    (634244,517949),
    (177168,572616),
    (85200,609541),
    (953043,502630),
    (523661,525484),
    (999295,500902),
    (840803,507246),
    (961490,502312),
    (471747,529685),
    (380705,538523),
    (911180,504275),
    (334149,544046),
    (478992,529065),
    (325789,545133),
    (335884,543826),
    (426976,533760),
    (749007,511582),
    (667067,516000),
    (607586,519623),
    (674054,515599),
    (188534,569675),
    (565185,522464),
    (172090,573988),
    (87592,608052),
    (907432,504424),
    (8912,760841),
    (928318,503590),
    (757917,511138),
    (718693,513153),
    (315141,546566),
    (728326,512645),
    (353492,541647),
    (638429,517695),
    (628892,518280),
    (877286,505672),
    (620895,518778),
    (385878,537959),
    (423311,534113),
    (633501,517997),
    (884833,505360),
    (883402,505416),
    (999665,500894),
    (708395,513697),
    (548142,523667),
    (756491,511205),
    (987352,501340),
    (766520,510705),
    (591775,520647),
    (833758,507563),
    (843890,507108),
    (925551,503698),
    (74816,616598),
    (646942,517187),
    (354923,541481),
    (256291,555638),
    (634470,517942),
    (930904,503494),
    (134221,586071),
    (282663,551304),
    (986070,501394),
    (123636,590176),
    (123678,590164),
    (481717,528841),
    (423076,534137),
    (866246,506145),
    (93313,604697),
    (783632,509880),
    (317066,546304),
    (502977,527103),
    (141272,583545),
    (71708,618938),
    (617748,518975),
    (581190,521362),
    (193824,568382),
    (682368,515131),
    (352956,541712),
    (351375,541905),
    (505362,526909),
    (905165,504518),
    (128645,588188),
    (267143,553787),
    (158409,577965),
    (482776,528754),
    (628896,518282),
    (485233,528547),
    (563606,522574),
    (111001,595655),
    (115920,593445),
    (365510,540237),
    (959724,502374),
    (938763,503184),
    (930044,503520),
    (970959,501956),
    (913658,504176),
    (68117,621790),
    (989729,501253),
    (567697,522288),
    (820427,508163),
    (54236,634794),
    (291557,549938),
    (124961,589646),
    (403177,536130),
    (405421,535899),
    (410233,535417),
    (815111,508403),
    (213176,563974),
    (83099,610879),
    (998588,500934),
    (513640,526263),
    (129817,587733),
    (1820,921851),
    (287584,550539),
    (299160,548820),
    (860621,506386),
    (529258,525059),
    (586297,521017),
    (953406,502616),
    (441234,532410),
    (986217,501386),
    (781938,509957),
    (461247,530595),
    (735424,512277),
    (146623,581722),
    (839838,507288),
    (510667,526494),
    (935085,503327),
    (737523,512167),
    (303455,548204),
    (992779,501145),
    (60240,628739),
    (939095,503174),
    (794368,509370),
    (501825,527189),
    (459028,530798),
    (884641,505363),
    (512287,526364),
    (835165,507499),
    (307723,547590),
    (160587,577304),
    (735043,512300),
    (493289,527887),
    (110717,595785),
    (306480,547772),
    (318593,546089),
    (179810,571911),
    (200531,566799),
    (314999,546580),
    (197020,567622),
    (301465,548487),
    (237808,559000),
    (131944,586923),
    (882527,505449),
    (468117,530003),
    (711319,513541),
    (156240,578628),
    (965452,502162),
    (992756,501148),
    (437959,532715),
    (739938,512046),
    (614249,519196),
    (391496,537356),
    (62746,626418),
    (688215,514806),
    (75501,616091),
    (883573,505412),
    (558824,522910),
    (759371,511061),
    (173913,573489),
    (891351,505089),
    (727464,512693),
    (164833,576051),
    (812317,508529),
    (540320,524243),
    (698061,514257),
    (69149,620952),
    (471673,529694),
    (159092,577753),
    (428134,533653),
    (89997,606608),
    (711061,513557),
    (779403,510081),
    (203327,566155),
    (798176,509187),
    (667688,515963),
    (636120,517833),
    (137410,584913),
    (217615,563034),
    (556887,523038),
    (667229,515991),
    (672276,515708),
    (325361,545187),
    (172115,573985),
    (13846,725685)]

    currSum = 0
    maxDig = 0
    highestInd = 0
    maxDigs = []
    for x in range(0,1000):
        dig = int(l[x][1] * math.log(l[x][0], 10)) + 1
        #if dig > maxDig:
            #maxDig = dig
            #highestInd = x + 1
        if dig == 3005316:
            maxDigs = maxDigs + [x + 1]
    return maxDigs

def euler79():
    l = [319,
    680,
    180,
    690,
    129,
    620,
    762,
    689,
    762,
    318,
    368,
    710,
    720,
    710,
    629,
    168,
    160,
    689,
    716,
    731,
    736,
    729,
    316,
    729,
    729,
    710,
    769,
    290,
    719,
    680,
    318,
    389,
    162,
    289,
    162,
    718,
    729,
    319,
    790,
    680,
    890,
    362,
    319,
    760,
    316,
    729,
    380,
    319,
    728,
    716]
    distinct = list(set(l))
    for x0 in set(range(0,10)).difference(set([4,5])):
        for x1 in set(range(0,10)).difference(set([4,5])):
            for x2 in set(range(0,10)).difference(set([4,5])):
                for x3 in set(range(0,10)).difference(set([4,5])):
                    for x4 in set(range(0,10)).difference(set([4,5])):
                        for x5 in set(range(0,10)).difference(set([4,5])):
                            for x6 in set(range(0,10)).difference(set([4,5])):
                                for x7 in set(range(0,10)).difference(set([4,5])):
                                    num = int(str(x0) + str(x1)+ str(x2)+ str(x3)+ str(x4)+ str(x5)+ str(x6)+ str(x7))
                                    if satisfiesList(num, l):
                                        return num
    return -1


def satisfiesList(n, l):
    ln = [i for i in str(n)]
    for x in l:
        l1 = [i for i in str(x)]
        if not listContainsList(l1, ln):
            return False
    return True

def listContainsList(l1, l2):#assumes smaller list on the left
    ind = -1
    for x in range(0, len(l1)):
        print l1[x]
        if ind != -1 and l1[x] in l2[ind + 1:]:
            ind = ind + l2[ind + 1:].index(l1[x])
        elif ind == -1 and l1[x] in l2[ind + 1:]:
            print  ind
            ind = l2[ind + 1:].index(l1[x])
            print  ind
        else:
            return False
    return True





def buildNums(a, b, l, ind1, ind2):
    s1 = str(a)
    s2 = str(b)
    if ind1 == len(s1) and ind2 == len(s2):
        return l
    elif ind1 == len(s1):
        nextL = []
        for x in l:
            nextL = nextL + [int(str(x)+str(b)[ind2:])]
        return nextL
    elif ind2 == len(s2):
        nextL = []
        for x in l:
            nextL = nextL + [int(str(x)+str(a)[ind1:])]
        return nextL
    else:
        nextL1 = []
        nextL2 = []

        if len(l) == 0:
            nextL1 = [int(str(a)[ind1])]
            nextL2 = [int(str(b)[ind2])]
        else:
            for x in l:
                nextL1 = nextL1 + [int(str(x)+str(a)[ind1])]
            for x in l:
                nextL2 = nextL2 + [int(str(x)+str(b)[ind2])]

        return buildNums(a,b,nextL1, ind1 + 1, ind2) + buildNums(a,b,nextL2, ind1, ind2 + 1)

def euler68():
    s = set(range(1,11))
    l = []
    for a0 in s:
        for a1 in s.difference([a0]):
            for a2 in s.difference([a0, a1]):
                for a3 in s.difference([a0, a1,a2 ]):
                    for a4 in s.difference([a0, a1,a2, a3 ]):
                        for a5 in s.difference([a0, a1,a2, a3, a4 ]):
                            for a6 in s.difference([a0, a1,a2, a3, a4, a5 ]):
                                for a7 in s.difference([a0, a1,a2, a3, a4, a5, a6 ]):
                                    for a8 in s.difference([a0, a1,a2, a3, a4, a5, a6, a7 ]):
                                        for a9 in s.difference([a0, a1,a2, a3, a4, a5, a6, a7, a8 ]):
                                            pentagon = [a0, a1, a2, a3, a4]
                                            if 10 not in pentagon:
                                                if a5 + a0 + a1 == a6 + a1 + a2 and a6 + a1 + a2 == a7 + a2 + a3 and  a7 + a2 + a3 == a8 + a3 + a4 and a8 + a3 + a4 == a9 + a4 + a0 and a9 + a4 + a0 == a5 + a0 + a1:
                                                    l = l + [(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)]
    filtered = []
    for (a0,a1,a2,a3,a4,a5,a6,a7,a8,a9) in l:
        if a5 == min([a5, a6, a7, a8, a9]):
            filtered = filtered + [(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)]

    filteredMax = 0
    for (a0,a1,a2,a3,a4,a5,a6,a7,a8,a9) in filtered:
        strs = [str(a5), str(a0), str(a1), str(a6), str(a1), str(a2), str(a7), str(a2), str(a3), str(a8), str(a3), str(a4), str(a9), str(a4), str(a0)]
        curr = int("".join(strs))
        if curr > filteredMax:
            filteredMax = curr
    return filteredMax



def euler81():
    matrix = [[4445,2697,5115,718,2209,2212,654,4348,3079,6821,7668,3276,8874,4190,3785,2752,9473,7817,9137,496,7338,3434,7152,4355,4552,7917,7827,2460,2350,691,3514,5880,3145,7633,7199,3783,5066,7487,3285,1084,8985,760,872,8609,8051,1134,9536,5750,9716,9371,7619,5617,275,9721,2997,2698,1887,8825,6372,3014,2113,7122,7050,6775,5948,2758,1219,3539,348,7989,2735,9862,1263,8089,6401,9462,3168,2758,3748,5870],
[1096,20,1318,7586,5167,2642,1443,5741,7621,7030,5526,4244,2348,4641,9827,2448,6918,5883,3737,300,7116,6531,567,5997,3971,6623,820,6148,3287,1874,7981,8424,7672,7575,6797,6717,1078,5008,4051,8795,5820,346,1851,6463,2117,6058,3407,8211,117,4822,1317,4377,4434,5925,8341,4800,1175,4173,690,8978,7470,1295,3799,8724,3509,9849,618,3320,7068,9633,2384,7175,544,6583,1908,9983,481,4187,9353,9377],
[9607,7385,521,6084,1364,8983,7623,1585,6935,8551,2574,8267,4781,3834,2764,2084,2669,4656,9343,7709,2203,9328,8004,6192,5856,3555,2260,5118,6504,1839,9227,1259,9451,1388,7909,5733,6968,8519,9973,1663,5315,7571,3035,4325,4283,2304,6438,3815,9213,9806,9536,196,5542,6907,2475,1159,5820,9075,9470,2179,9248,1828,4592,9167,3713,4640,47,3637,309,7344,6955,346,378,9044,8635,7466,5036,9515,6385,9230],
[7206,3114,7760,1094,6150,5182,7358,7387,4497,955,101,1478,7777,6966,7010,8417,6453,4955,3496,107,449,8271,131,2948,6185,784,5937,8001,6104,8282,4165,3642,710,2390,575,715,3089,6964,4217,192,5949,7006,715,3328,1152,66,8044,4319,1735,146,4818,5456,6451,4113,1063,4781,6799,602,1504,6245,6550,1417,1343,2363,3785,5448,4545,9371,5420,5068,4613,4882,4241,5043,7873,8042,8434,3939,9256,2187],
[3620,8024,577,9997,7377,7682,1314,1158,6282,6310,1896,2509,5436,1732,9480,706,496,101,6232,7375,2207,2306,110,6772,3433,2878,8140,5933,8688,1399,2210,7332,6172,6403,7333,4044,2291,1790,2446,7390,8698,5723,3678,7104,1825,2040,140,3982,4905,4160,2200,5041,2512,1488,2268,1175,7588,8321,8078,7312,977,5257,8465,5068,3453,3096,1651,7906,253,9250,6021,8791,8109,6651,3412,345,4778,5152,4883,7505],
[1074,5438,9008,2679,5397,5429,2652,3403,770,9188,4248,2493,4361,8327,9587,707,9525,5913,93,1899,328,2876,3604,673,8576,6908,7659,2544,3359,3883,5273,6587,3065,1749,3223,604,9925,6941,2823,8767,7039,3290,3214,1787,7904,3421,7137,9560,8451,2669,9219,6332,1576,5477,6755,8348,4164,4307,2984,4012,6629,1044,2874,6541,4942,903,1404,9125,5160,8836,4345,2581,460,8438,1538,5507,668,3352,2678,6942],
[4295,1176,5596,1521,3061,9868,7037,7129,8933,6659,5947,5063,3653,9447,9245,2679,767,714,116,8558,163,3927,8779,158,5093,2447,5782,3967,1716,931,7772,8164,1117,9244,5783,7776,3846,8862,6014,2330,6947,1777,3112,6008,3491,1906,5952,314,4602,8994,5919,9214,3995,5026,7688,6809,5003,3128,2509,7477,110,8971,3982,8539,2980,4689,6343,5411,2992,5270,5247,9260,2269,7474,1042,7162,5206,1232,4556,4757],
[510,3556,5377,1406,5721,4946,2635,7847,4251,8293,8281,6351,4912,287,2870,3380,3948,5322,3840,4738,9563,1906,6298,3234,8959,1562,6297,8835,7861,239,6618,1322,2553,2213,5053,5446,4402,6500,5182,8585,6900,5756,9661,903,5186,7687,5998,7997,8081,8955,4835,6069,2621,1581,732,9564,1082,1853,5442,1342,520,1737,3703,5321,4793,2776,1508,1647,9101,2499,6891,4336,7012,3329,3212,1442,9993,3988,4930,7706],
[9444,3401,5891,9716,1228,7107,109,3563,2700,6161,5039,4992,2242,8541,7372,2067,1294,3058,1306,320,8881,5756,9326,411,8650,8824,5495,8282,8397,2000,1228,7817,2099,6473,3571,5994,4447,1299,5991,543,7874,2297,1651,101,2093,3463,9189,6872,6118,872,1008,1779,2805,9084,4048,2123,5877,55,3075,1737,9459,4535,6453,3644,108,5982,4437,5213,1340,6967,9943,5815,669,8074,1838,6979,9132,9315,715,5048],
[3327,4030,7177,6336,9933,5296,2621,4785,2755,4832,2512,2118,2244,4407,2170,499,7532,9742,5051,7687,970,6924,3527,4694,5145,1306,2165,5940,2425,8910,3513,1909,6983,346,6377,4304,9330,7203,6605,3709,3346,970,369,9737,5811,4427,9939,3693,8436,5566,1977,3728,2399,3985,8303,2492,5366,9802,9193,7296,1033,5060,9144,2766,1151,7629,5169,5995,58,7619,7565,4208,1713,6279,3209,4908,9224,7409,1325,8540],
[6882,1265,1775,3648,4690,959,5837,4520,5394,1378,9485,1360,4018,578,9174,2932,9890,3696,116,1723,1178,9355,7063,1594,1918,8574,7594,7942,1547,6166,7888,354,6932,4651,1010,7759,6905,661,7689,6092,9292,3845,9605,8443,443,8275,5163,7720,7265,6356,7779,1798,1754,5225,6661,1180,8024,5666,88,9153,1840,3508,1193,4445,2648,3538,6243,6375,8107,5902,5423,2520,1122,5015,6113,8859,9370,966,8673,2442],
[7338,3423,4723,6533,848,8041,7921,8277,4094,5368,7252,8852,9166,2250,2801,6125,8093,5738,4038,9808,7359,9494,601,9116,4946,2702,5573,2921,9862,1462,1269,2410,4171,2709,7508,6241,7522,615,2407,8200,4189,5492,5649,7353,2590,5203,4274,710,7329,9063,956,8371,3722,4253,4785,1194,4828,4717,4548,940,983,2575,4511,2938,1827,2027,2700,1236,841,5760,1680,6260,2373,3851,1841,4968,1172,5179,7175,3509],
[4420,1327,3560,2376,6260,2988,9537,4064,4829,8872,9598,3228,1792,7118,9962,9336,4368,9189,6857,1829,9863,6287,7303,7769,2707,8257,2391,2009,3975,4993,3068,9835,3427,341,8412,2134,4034,8511,6421,3041,9012,2983,7289,100,1355,7904,9186,6920,5856,2008,6545,8331,3655,5011,839,8041,9255,6524,3862,8788,62,7455,3513,5003,8413,3918,2076,7960,6108,3638,6999,3436,1441,4858,4181,1866,8731,7745,3744,1000],
[356,8296,8325,1058,1277,4743,3850,2388,6079,6462,2815,5620,8495,5378,75,4324,3441,9870,1113,165,1544,1179,2834,562,6176,2313,6836,8839,2986,9454,5199,6888,1927,5866,8760,320,1792,8296,7898,6121,7241,5886,5814,2815,8336,1576,4314,3109,2572,6011,2086,9061,9403,3947,5487,9731,7281,3159,1819,1334,3181,5844,5114,9898,4634,2531,4412,6430,4262,8482,4546,4555,6804,2607,9421,686,8649,8860,7794,6672],
[9870,152,1558,4963,8750,4754,6521,6256,8818,5208,5691,9659,8377,9725,5050,5343,2539,6101,1844,9700,7750,8114,5357,3001,8830,4438,199,9545,8496,43,2078,327,9397,106,6090,8181,8646,6414,7499,5450,4850,6273,5014,4131,7639,3913,6571,8534,9703,4391,7618,445,1320,5,1894,6771,7383,9191,4708,9706,6939,7937,8726,9382,5216,3685,2247,9029,8154,1738,9984,2626,9438,4167,6351,5060,29,1218,1239,4785],
[192,5213,8297,8974,4032,6966,5717,1179,6523,4679,9513,1481,3041,5355,9303,9154,1389,8702,6589,7818,6336,3539,5538,3094,6646,6702,6266,2759,4608,4452,617,9406,8064,6379,444,5602,4950,1810,8391,1536,316,8714,1178,5182,5863,5110,5372,4954,1978,2971,5680,4863,2255,4630,5723,2168,538,1692,1319,7540,440,6430,6266,7712,7385,5702,620,641,3136,7350,1478,3155,2820,9109,6261,1122,4470,14,8493,2095],
[1046,4301,6082,474,4974,7822,2102,5161,5172,6946,8074,9716,6586,9962,9749,5015,2217,995,5388,4402,7652,6399,6539,1349,8101,3677,1328,9612,7922,2879,231,5887,2655,508,4357,4964,3554,5930,6236,7384,4614,280,3093,9600,2110,7863,2631,6626,6620,68,1311,7198,7561,1768,5139,1431,221,230,2940,968,5283,6517,2146,1646,869,9402,7068,8645,7058,1765,9690,4152,2926,9504,2939,7504,6074,2944,6470,7859],
[4659,736,4951,9344,1927,6271,8837,8711,3241,6579,7660,5499,5616,3743,5801,4682,9748,8796,779,1833,4549,8138,4026,775,4170,2432,4174,3741,7540,8017,2833,4027,396,811,2871,1150,9809,2719,9199,8504,1224,540,2051,3519,7982,7367,2761,308,3358,6505,2050,4836,5090,7864,805,2566,2409,6876,3361,8622,5572,5895,3280,441,7893,8105,1634,2929,274,3926,7786,6123,8233,9921,2674,5340,1445,203,4585,3837],
[5759,338,7444,7968,7742,3755,1591,4839,1705,650,7061,2461,9230,9391,9373,2413,1213,431,7801,4994,2380,2703,6161,6878,8331,2538,6093,1275,5065,5062,2839,582,1014,8109,3525,1544,1569,8622,7944,2905,6120,1564,1839,5570,7579,1318,2677,5257,4418,5601,7935,7656,5192,1864,5886,6083,5580,6202,8869,1636,7907,4759,9082,5854,3185,7631,6854,5872,5632,5280,1431,2077,9717,7431,4256,8261,9680,4487,4752,4286],
[1571,1428,8599,1230,7772,4221,8523,9049,4042,8726,7567,6736,9033,2104,4879,4967,6334,6716,3994,1269,8995,6539,3610,7667,6560,6065,874,848,4597,1711,7161,4811,6734,5723,6356,6026,9183,2586,5636,1092,7779,7923,8747,6887,7505,9909,1792,3233,4526,3176,1508,8043,720,5212,6046,4988,709,5277,8256,3642,1391,5803,1468,2145,3970,6301,7767,2359,8487,9771,8785,7520,856,1605,8972,2402,2386,991,1383,5963],
[1822,4824,5957,6511,9868,4113,301,9353,6228,2881,2966,6956,9124,9574,9233,1601,7340,973,9396,540,4747,8590,9535,3650,7333,7583,4806,3593,2738,8157,5215,8472,2284,9473,3906,6982,5505,6053,7936,6074,7179,6688,1564,1103,6860,5839,2022,8490,910,7551,7805,881,7024,1855,9448,4790,1274,3672,2810,774,7623,4223,4850,6071,9975,4935,1915,9771,6690,3846,517,463,7624,4511,614,6394,3661,7409,1395,8127],
[8738,3850,9555,3695,4383,2378,87,6256,6740,7682,9546,4255,6105,2000,1851,4073,8957,9022,6547,5189,2487,303,9602,7833,1628,4163,6678,3144,8589,7096,8913,5823,4890,7679,1212,9294,5884,2972,3012,3359,7794,7428,1579,4350,7246,4301,7779,7790,3294,9547,4367,3549,1958,8237,6758,3497,3250,3456,6318,1663,708,7714,6143,6890,3428,6853,9334,7992,591,6449,9786,1412,8500,722,5468,1371,108,3939,4199,2535],
[7047,4323,1934,5163,4166,461,3544,2767,6554,203,6098,2265,9078,2075,4644,6641,8412,9183,487,101,7566,5622,1975,5726,2920,5374,7779,5631,3753,3725,2672,3621,4280,1162,5812,345,8173,9785,1525,955,5603,2215,2580,5261,2765,2990,5979,389,3907,2484,1232,5933,5871,3304,1138,1616,5114,9199,5072,7442,7245,6472,4760,6359,9053,7876,2564,9404,3043,9026,2261,3374,4460,7306,2326,966,828,3274,1712,3446],
[3975,4565,8131,5800,4570,2306,8838,4392,9147,11,3911,7118,9645,4994,2028,6062,5431,2279,8752,2658,7836,994,7316,5336,7185,3289,1898,9689,2331,5737,3403,1124,2679,3241,7748,16,2724,5441,6640,9368,9081,5618,858,4969,17,2103,6035,8043,7475,2181,939,415,1617,8500,8253,2155,7843,7974,7859,1746,6336,3193,2617,8736,4079,6324,6645,8891,9396,5522,6103,1857,8979,3835,2475,1310,7422,610,8345,7615],
[9248,5397,5686,2988,3446,4359,6634,9141,497,9176,6773,7448,1907,8454,916,1596,2241,1626,1384,2741,3649,5362,8791,7170,2903,2475,5325,6451,924,3328,522,90,4813,9737,9557,691,2388,1383,4021,1609,9206,4707,5200,7107,8104,4333,9860,5013,1224,6959,8527,1877,4545,7772,6268,621,4915,9349,5970,706,9583,3071,4127,780,8231,3017,9114,3836,7503,2383,1977,4870,8035,2379,9704,1037,3992,3642,1016,4303],
[5093,138,4639,6609,1146,5565,95,7521,9077,2272,974,4388,2465,2650,722,4998,3567,3047,921,2736,7855,173,2065,4238,1048,5,6847,9548,8632,9194,5942,4777,7910,8971,6279,7253,2516,1555,1833,3184,9453,9053,6897,7808,8629,4877,1871,8055,4881,7639,1537,7701,2508,7564,5845,5023,2304,5396,3193,2955,1088,3801,6203,1748,3737,1276,13,4120,7715,8552,3047,2921,106,7508,304,1280,7140,2567,9135,5266],
[6237,4607,7527,9047,522,7371,4883,2540,5867,6366,5301,1570,421,276,3361,527,6637,4861,2401,7522,5808,9371,5298,2045,5096,5447,7755,5115,7060,8529,4078,1943,1697,1764,5453,7085,960,2405,739,2100,5800,728,9737,5704,5693,1431,8979,6428,673,7540,6,7773,5857,6823,150,5869,8486,684,5816,9626,7451,5579,8260,3397,5322,6920,1879,2127,2884,5478,4977,9016,6165,6292,3062,5671,5968,78,4619,4763],
[9905,7127,9390,5185,6923,3721,9164,9705,4341,1031,1046,5127,7376,6528,3248,4941,1178,7889,3364,4486,5358,9402,9158,8600,1025,874,1839,1783,309,9030,1843,845,8398,1433,7118,70,8071,2877,3904,8866,6722,4299,10,1929,5897,4188,600,1889,3325,2485,6473,4474,7444,6992,4846,6166,4441,2283,2629,4352,7775,1101,2214,9985,215,8270,9750,2740,8361,7103,5930,8664,9690,8302,9267,344,2077,1372,1880,9550],
[5825,8517,7769,2405,8204,1060,3603,7025,478,8334,1997,3692,7433,9101,7294,7498,9415,5452,3850,3508,6857,9213,6807,4412,7310,854,5384,686,4978,892,8651,3241,2743,3801,3813,8588,6701,4416,6990,6490,3197,6838,6503,114,8343,5844,8646,8694,65,791,5979,2687,2621,2019,8097,1423,3644,9764,4921,3266,3662,5561,2476,8271,8138,6147,1168,3340,1998,9874,6572,9873,6659,5609,2711,3931,9567,4143,7833,8887],
[6223,2099,2700,589,4716,8333,1362,5007,2753,2848,4441,8397,7192,8191,4916,9955,6076,3370,6396,6971,3156,248,3911,2488,4930,2458,7183,5455,170,6809,6417,3390,1956,7188,577,7526,2203,968,8164,479,8699,7915,507,6393,4632,1597,7534,3604,618,3280,6061,9793,9238,8347,568,9645,2070,5198,6482,5000,9212,6655,5961,7513,1323,3872,6170,3812,4146,2736,67,3151,5548,2781,9679,7564,5043,8587,1893,4531],
[5826,3690,6724,2121,9308,6986,8106,6659,2142,1642,7170,2877,5757,6494,8026,6571,8387,9961,6043,9758,9607,6450,8631,8334,7359,5256,8523,2225,7487,1977,9555,8048,5763,2414,4948,4265,2427,8978,8088,8841,9208,9601,5810,9398,8866,9138,4176,5875,7212,3272,6759,5678,7649,4922,5422,1343,8197,3154,3600,687,1028,4579,2084,9467,4492,7262,7296,6538,7657,7134,2077,1505,7332,6890,8964,4879,7603,7400,5973,739],
[1861,1613,4879,1884,7334,966,2000,7489,2123,4287,1472,3263,4726,9203,1040,4103,6075,6049,330,9253,4062,4268,1635,9960,577,1320,3195,9628,1030,4092,4979,6474,6393,2799,6967,8687,7724,7392,9927,2085,3200,6466,8702,265,7646,8665,7986,7266,4574,6587,612,2724,704,3191,8323,9523,3002,704,5064,3960,8209,2027,2758,8393,4875,4641,9584,6401,7883,7014,768,443,5490,7506,1852,2005,8850,5776,4487,4269],
[4052,6687,4705,7260,6645,6715,3706,5504,8672,2853,1136,8187,8203,4016,871,1809,1366,4952,9294,5339,6872,2645,6083,7874,3056,5218,7485,8796,7401,3348,2103,426,8572,4163,9171,3176,948,7654,9344,3217,1650,5580,7971,2622,76,2874,880,2034,9929,1546,2659,5811,3754,7096,7436,9694,9960,7415,2164,953,2360,4194,2397,1047,2196,6827,575,784,2675,8821,6802,7972,5996,6699,2134,7577,2887,1412,4349,4380],
[4629,2234,6240,8132,7592,3181,6389,1214,266,1910,2451,8784,2790,1127,6932,1447,8986,2492,5476,397,889,3027,7641,5083,5776,4022,185,3364,5701,2442,2840,4160,9525,4828,6602,2614,7447,3711,4505,7745,8034,6514,4907,2605,7753,6958,7270,6936,3006,8968,439,2326,4652,3085,3425,9863,5049,5361,8688,297,7580,8777,7916,6687,8683,7141,306,9569,2384,1500,3346,4601,7329,9040,6097,2727,6314,4501,4974,2829],
[8316,4072,2025,6884,3027,1808,5714,7624,7880,8528,4205,8686,7587,3230,1139,7273,6163,6986,3914,9309,1464,9359,4474,7095,2212,7302,2583,9462,7532,6567,1606,4436,8981,5612,6796,4385,5076,2007,6072,3678,8331,1338,3299,8845,4783,8613,4071,1232,6028,2176,3990,2148,3748,103,9453,538,6745,9110,926,3125,473,5970,8728,7072,9062,1404,1317,5139,9862,6496,6062,3338,464,1600,2532,1088,8232,7739,8274,3873],
[2341,523,7096,8397,8301,6541,9844,244,4993,2280,7689,4025,4196,5522,7904,6048,2623,9258,2149,9461,6448,8087,7245,1917,8340,7127,8466,5725,6996,3421,5313,512,9164,9837,9794,8369,4185,1488,7210,1524,1016,4620,9435,2478,7765,8035,697,6677,3724,6988,5853,7662,3895,9593,1185,4727,6025,5734,7665,3070,138,8469,6748,6459,561,7935,8646,2378,462,7755,3115,9690,8877,3946,2728,8793,244,6323,8666,4271],
[6430,2406,8994,56,1267,3826,9443,7079,7579,5232,6691,3435,6718,5698,4144,7028,592,2627,217,734,6194,8156,9118,58,2640,8069,4127,3285,694,3197,3377,4143,4802,3324,8134,6953,7625,3598,3584,4289,7065,3434,2106,7132,5802,7920,9060,7531,3321,1725,1067,3751,444,5503,6785,7937,6365,4803,198,6266,8177,1470,6390,1606,2904,7555,9834,8667,2033,1723,5167,1666,8546,8152,473,4475,6451,7947,3062,3281],
[2810,3042,7759,1741,2275,2609,7676,8640,4117,1958,7500,8048,1757,3954,9270,1971,4796,2912,660,5511,3553,1012,5757,4525,6084,7198,8352,5775,7726,8591,7710,9589,3122,4392,6856,5016,749,2285,3356,7482,9956,7348,2599,8944,495,3462,3578,551,4543,7207,7169,7796,1247,4278,6916,8176,3742,8385,2310,1345,8692,2667,4568,1770,8319,3585,4920,3890,4928,7343,5385,9772,7947,8786,2056,9266,3454,2807,877,2660],
[6206,8252,5928,5837,4177,4333,207,7934,5581,9526,8906,1498,8411,2984,5198,5134,2464,8435,8514,8674,3876,599,5327,826,2152,4084,2433,9327,9697,4800,2728,3608,3849,3861,3498,9943,1407,3991,7191,9110,5666,8434,4704,6545,5944,2357,1163,4995,9619,6754,4200,9682,6654,4862,4744,5953,6632,1054,293,9439,8286,2255,696,8709,1533,1844,6441,430,1999,6063,9431,7018,8057,2920,6266,6799,356,3597,4024,6665],
[3847,6356,8541,7225,2325,2946,5199,469,5450,7508,2197,9915,8284,7983,6341,3276,3321,16,1321,7608,5015,3362,8491,6968,6818,797,156,2575,706,9516,5344,5457,9210,5051,8099,1617,9951,7663,8253,9683,2670,1261,4710,1068,8753,4799,1228,2621,3275,6188,4699,1791,9518,8701,5932,4275,6011,9877,2933,4182,6059,2930,6687,6682,9771,654,9437,3169,8596,1827,5471,8909,2352,123,4394,3208,8756,5513,6917,2056],
[5458,8173,3138,3290,4570,4892,3317,4251,9699,7973,1163,1935,5477,6648,9614,5655,9592,975,9118,2194,7322,8248,8413,3462,8560,1907,7810,6650,7355,2939,4973,6894,3933,3784,3200,2419,9234,4747,2208,2207,1945,2899,1407,6145,8023,3484,5688,7686,2737,3828,3704,9004,5190,9740,8643,8650,5358,4426,1522,1707,3613,9887,6956,2447,2762,833,1449,9489,2573,1080,4167,3456,6809,2466,227,7125,2759,6250,6472,8089],
[3266,7025,9756,3914,1265,9116,7723,9788,6805,5493,2092,8688,6592,9173,4431,4028,6007,7131,4446,4815,3648,6701,759,3312,8355,4485,4187,5188,8746,7759,3528,2177,5243,8379,3838,7233,4607,9187,7216,2190,6967,2920,6082,7910,5354,3609,8958,6949,7731,494,8753,8707,1523,4426,3543,7085,647,6771,9847,646,5049,824,8417,5260,2730,5702,2513,9275,4279,2767,8684,1165,9903,4518,55,9682,8963,6005,2102,6523],
[1998,8731,936,1479,5259,7064,4085,91,7745,7136,3773,3810,730,8255,2705,2653,9790,6807,2342,355,9344,2668,3690,2028,9679,8102,574,4318,6481,9175,5423,8062,2867,9657,7553,3442,3920,7430,3945,7639,3714,3392,2525,4995,4850,2867,7951,9667,486,9506,9888,781,8866,1702,3795,90,356,1483,4200,2131,6969,5931,486,6880,4404,1084,5169,4910,6567,8335,4686,5043,2614,3352,2667,4513,6472,7471,5720,1616],
[8878,1613,1716,868,1906,2681,564,665,5995,2474,7496,3432,9491,9087,8850,8287,669,823,347,6194,2264,2592,7871,7616,8508,4827,760,2676,4660,4881,7572,3811,9032,939,4384,929,7525,8419,5556,9063,662,8887,7026,8534,3111,1454,2082,7598,5726,6687,9647,7608,73,3014,5063,670,5461,5631,3367,9796,8475,7908,5073,1565,5008,5295,4457,1274,4788,1728,338,600,8415,8535,9351,7750,6887,5845,1741,125],
[3637,6489,9634,9464,9055,2413,7824,9517,7532,3577,7050,6186,6980,9365,9782,191,870,2497,8498,2218,2757,5420,6468,586,3320,9230,1034,1393,9886,5072,9391,1178,8464,8042,6869,2075,8275,3601,7715,9470,8786,6475,8373,2159,9237,2066,3264,5000,679,355,3069,4073,494,2308,5512,4334,9438,8786,8637,9774,1169,1949,6594,6072,4270,9158,7916,5752,6794,9391,6301,5842,3285,2141,3898,8027,4310,8821,7079,1307],
[8497,6681,4732,7151,7060,5204,9030,7157,833,5014,8723,3207,9796,9286,4913,119,5118,7650,9335,809,3675,2597,5144,3945,5090,8384,187,4102,1260,2445,2792,4422,8389,9290,50,1765,1521,6921,8586,4368,1565,5727,7855,2003,4834,9897,5911,8630,5070,1330,7692,7557,7980,6028,5805,9090,8265,3019,3802,698,9149,5748,1965,9658,4417,5994,5584,8226,2937,272,5743,1278,5698,8736,2595,6475,5342,6596,1149,6920],
[8188,8009,9546,6310,8772,2500,9846,6592,6872,3857,1307,8125,7042,1544,6159,2330,643,4604,7899,6848,371,8067,2062,3200,7295,1857,9505,6936,384,2193,2190,301,8535,5503,1462,7380,5114,4824,8833,1763,4974,8711,9262,6698,3999,2645,6937,7747,1128,2933,3556,7943,2885,3122,9105,5447,418,2899,5148,3699,9021,9501,597,4084,175,1621,1,1079,6067,5812,4326,9914,6633,5394,4233,6728,9084,1864,5863,1225],
[9935,8793,9117,1825,9542,8246,8437,3331,9128,9675,6086,7075,319,1334,7932,3583,7167,4178,1726,7720,695,8277,7887,6359,5912,1719,2780,8529,1359,2013,4498,8072,1129,9998,1147,8804,9405,6255,1619,2165,7491,1,8882,7378,3337,503,5758,4109,3577,985,3200,7615,8058,5032,1080,6410,6873,5496,1466,2412,9885,5904,4406,3605,8770,4361,6205,9193,1537,9959,214,7260,9566,1685,100,4920,7138,9819,5637,976],
[3466,9854,985,1078,7222,8888,5466,5379,3578,4540,6853,8690,3728,6351,7147,3134,6921,9692,857,3307,4998,2172,5783,3931,9417,2541,6299,13,787,2099,9131,9494,896,8600,1643,8419,7248,2660,2609,8579,91,6663,5506,7675,1947,6165,4286,1972,9645,3805,1663,1456,8853,5705,9889,7489,1107,383,4044,2969,3343,152,7805,4980,9929,5033,1737,9953,7197,9158,4071,1324,473,9676,3984,9680,3606,8160,7384,5432],
[1005,4512,5186,3953,2164,3372,4097,3247,8697,3022,9896,4101,3871,6791,3219,2742,4630,6967,7829,5991,6134,1197,1414,8923,8787,1394,8852,5019,7768,5147,8004,8825,5062,9625,7988,1110,3992,7984,9966,6516,6251,8270,421,3723,1432,4830,6935,8095,9059,2214,6483,6846,3120,1587,6201,6691,9096,9627,6671,4002,3495,9939,7708,7465,5879,6959,6634,3241,3401,2355,9061,2611,7830,3941,2177,2146,5089,7079,519,6351],
[7280,8586,4261,2831,7217,3141,9994,9940,5462,2189,4005,6942,9848,5350,8060,6665,7519,4324,7684,657,9453,9296,2944,6843,7499,7847,1728,9681,3906,6353,5529,2822,3355,3897,7724,4257,7489,8672,4356,3983,1948,6892,7415,4153,5893,4190,621,1736,4045,9532,7701,3671,1211,1622,3176,4524,9317,7800,5638,6644,6943,5463,3531,2821,1347,5958,3436,1438,2999,994,850,4131,2616,1549,3465,5946,690,9273,6954,7991],
[9517,399,3249,2596,7736,2142,1322,968,7350,1614,468,3346,3265,7222,6086,1661,5317,2582,7959,4685,2807,2917,1037,5698,1529,3972,8716,2634,3301,3412,8621,743,8001,4734,888,7744,8092,3671,8941,1487,5658,7099,2781,99,1932,4443,4756,4652,9328,1581,7855,4312,5976,7255,6480,3996,2748,1973,9731,4530,2790,9417,7186,5303,3557,351,7182,9428,1342,9020,7599,1392,8304,2070,9138,7215,2008,9937,1106,7110],
[7444,769,9688,632,1571,6820,8743,4338,337,3366,3073,1946,8219,104,4210,6986,249,5061,8693,7960,6546,1004,8857,5997,9352,4338,6105,5008,2556,6518,6694,4345,3727,7956,20,3954,8652,4424,9387,2035,8358,5962,5304,5194,8650,8282,1256,1103,2138,6679,1985,3653,2770,2433,4278,615,2863,1715,242,3790,2636,6998,3088,1671,2239,957,5411,4595,6282,2881,9974,2401,875,7574,2987,4587,3147,6766,9885,2965],
[3287,3016,3619,6818,9073,6120,5423,557,2900,2015,8111,3873,1314,4189,1846,4399,7041,7583,2427,2864,3525,5002,2069,748,1948,6015,2684,438,770,8367,1663,7887,7759,1885,157,7770,4520,4878,3857,1137,3525,3050,6276,5569,7649,904,4533,7843,2199,5648,7628,9075,9441,3600,7231,2388,5640,9096,958,3058,584,5899,8150,1181,9616,1098,8162,6819,8171,1519,1140,7665,8801,2632,1299,9192,707,9955,2710,7314],
[1772,2963,7578,3541,3095,1488,7026,2634,6015,4633,4370,2762,1650,2174,909,8158,2922,8467,4198,4280,9092,8856,8835,5457,2790,8574,9742,5054,9547,4156,7940,8126,9824,7340,8840,6574,3547,1477,3014,6798,7134,435,9484,9859,3031,4,1502,4133,1738,1807,4825,463,6343,9701,8506,9822,9555,8688,8168,3467,3234,6318,1787,5591,419,6593,7974,8486,9861,6381,6758,194,3061,4315,2863,4665,3789,2201,1492,4416],
[126,8927,6608,5682,8986,6867,1715,6076,3159,788,3140,4744,830,9253,5812,5021,7616,8534,1546,9590,1101,9012,9821,8132,7857,4086,1069,7491,2988,1579,2442,4321,2149,7642,6108,250,6086,3167,24,9528,7663,2685,1220,9196,1397,5776,1577,1730,5481,977,6115,199,6326,2183,3767,5928,5586,7561,663,8649,9688,949,5913,9160,1870,5764,9887,4477,6703,1413,4995,5494,7131,2192,8969,7138,3997,8697,646,1028],
[8074,1731,8245,624,4601,8706,155,8891,309,2552,8208,8452,2954,3124,3469,4246,3352,1105,4509,8677,9901,4416,8191,9283,5625,7120,2952,8881,7693,830,4580,8228,9459,8611,4499,1179,4988,1394,550,2336,6089,6872,269,7213,1848,917,6672,4890,656,1478,6536,3165,4743,4990,1176,6211,7207,5284,9730,4738,1549,4986,4942,8645,3698,9429,1439,2175,6549,3058,6513,1574,6988,8333,3406,5245,5431,7140,7085,6407],
[7845,4694,2530,8249,290,5948,5509,1588,5940,4495,5866,5021,4626,3979,3296,7589,4854,1998,5627,3926,8346,6512,9608,1918,7070,4747,4182,2858,2766,4606,6269,4107,8982,8568,9053,4244,5604,102,2756,727,5887,2566,7922,44,5986,621,1202,374,6988,4130,3627,6744,9443,4568,1398,8679,397,3928,9159,367,2917,6127,5788,3304,8129,911,2669,1463,9749,264,4478,8940,1109,7309,2462,117,4692,7724,225,2312],
[4164,3637,2000,941,8903,39,3443,7172,1031,3687,4901,8082,4945,4515,7204,9310,9349,9535,9940,218,1788,9245,2237,1541,5670,6538,6047,5553,9807,8101,1925,8714,445,8332,7309,6830,5786,5736,7306,2710,3034,1838,7969,6318,7912,2584,2080,7437,6705,2254,7428,820,782,9861,7596,3842,3631,8063,5240,6666,394,4565,7865,4895,9890,6028,6117,4724,9156,4473,4552,602,470,6191,4927,5387,884,3146,1978,3000],
[4258,6880,1696,3582,5793,4923,2119,1155,9056,9698,6603,3768,5514,9927,9609,6166,6566,4536,4985,4934,8076,9062,6741,6163,7399,4562,2337,5600,2919,9012,8459,1308,6072,1225,9306,8818,5886,7243,7365,8792,6007,9256,6699,7171,4230,7002,8720,7839,4533,1671,478,7774,1607,2317,5437,4705,7886,4760,6760,7271,3081,2997,3088,7675,6208,3101,6821,6840,122,9633,4900,2067,8546,4549,2091,7188,5605,8599,6758,5229],
[7854,5243,9155,3556,8812,7047,2202,1541,5993,4600,4760,713,434,7911,7426,7414,8729,322,803,7960,7563,4908,6285,6291,736,3389,9339,4132,8701,7534,5287,3646,592,3065,7582,2592,8755,6068,8597,1982,5782,1894,2900,6236,4039,6569,3037,5837,7698,700,7815,2491,7272,5878,3083,6778,6639,3589,5010,8313,2581,6617,5869,8402,6808,2951,2321,5195,497,2190,6187,1342,1316,4453,7740,4154,2959,1781,1482,8256],
[7178,2046,4419,744,8312,5356,6855,8839,319,2962,5662,47,6307,8662,68,4813,567,2712,9931,1678,3101,8227,6533,4933,6656,92,5846,4780,6256,6361,4323,9985,1231,2175,7178,3034,9744,6155,9165,7787,5836,9318,7860,9644,8941,6480,9443,8188,5928,161,6979,2352,5628,6991,1198,8067,5867,6620,3778,8426,2994,3122,3124,6335,3918,8897,2655,9670,634,1088,1576,8935,7255,474,8166,7417,9547,2886,5560,3842],
[6957,3111,26,7530,7143,1295,1744,6057,3009,1854,8098,5405,2234,4874,9447,2620,9303,27,7410,969,40,2966,5648,7596,8637,4238,3143,3679,7187,690,9980,7085,7714,9373,5632,7526,6707,3951,9734,4216,2146,3602,5371,6029,3039,4433,4855,4151,1449,3376,8009,7240,7027,4602,2947,9081,4045,8424,9352,8742,923,2705,4266,3232,2264,6761,363,2651,3383,7770,6730,7856,7340,9679,2158,610,4471,4608,910,6241],
[4417,6756,1013,8797,658,8809,5032,8703,7541,846,3357,2920,9817,1745,9980,7593,4667,3087,779,3218,6233,5568,4296,2289,2654,7898,5021,9461,5593,8214,9173,4203,2271,7980,2983,5952,9992,8399,3468,1776,3188,9314,1720,6523,2933,621,8685,5483,8986,6163,3444,9539,4320,155,3992,2828,2150,6071,524,2895,5468,8063,1210,3348,9071,4862,483,9017,4097,6186,9815,3610,5048,1644,1003,9865,9332,2145,1944,2213],
[9284,3803,4920,1927,6706,4344,7383,4786,9890,2010,5228,1224,3158,6967,8580,8990,8883,5213,76,8306,2031,4980,5639,9519,7184,5645,7769,3259,8077,9130,1317,3096,9624,3818,1770,695,2454,947,6029,3474,9938,3527,5696,4760,7724,7738,2848,6442,5767,6845,8323,4131,2859,7595,2500,4815,3660,9130,8580,7016,8231,4391,8369,3444,4069,4021,556,6154,627,2778,1496,4206,6356,8434,8491,3816,8231,3190,5575,1015],
[3787,7572,1788,6803,5641,6844,1961,4811,8535,9914,9999,1450,8857,738,4662,8569,6679,2225,7839,8618,286,2648,5342,2294,3205,4546,176,8705,3741,6134,8324,8021,7004,5205,7032,6637,9442,5539,5584,4819,5874,5807,8589,6871,9016,983,1758,3786,1519,6241,185,8398,495,3370,9133,3051,4549,9674,7311,9738,3316,9383,2658,2776,9481,7558,619,3943,3324,6491,4933,153,9738,4623,912,3595,7771,7939,1219,4405],
[2650,3883,4154,5809,315,7756,4430,1788,4451,1631,6461,7230,6017,5751,138,588,5282,2442,9110,9035,6349,2515,1570,6122,4192,4174,3530,1933,4186,4420,4609,5739,4135,2963,6308,1161,8809,8619,2796,3819,6971,8228,4188,1492,909,8048,2328,6772,8467,7671,9068,2226,7579,6422,7056,8042,3296,2272,3006,2196,7320,3238,3490,3102,37,1293,3212,4767,5041,8773,5794,4456,6174,7279,7054,2835,7053,9088,790,6640],
[3101,1057,7057,3826,6077,1025,2955,1224,1114,6729,5902,4698,6239,7203,9423,1804,4417,6686,1426,6941,8071,1029,4985,9010,6122,6597,1622,1574,3513,1684,7086,5505,3244,411,9638,4150,907,9135,829,981,1707,5359,8781,9751,5,9131,3973,7159,1340,6955,7514,7993,6964,8198,1933,2797,877,3993,4453,8020,9349,8646,2779,8679,2961,3547,3374,3510,1129,3568,2241,2625,9138,5974,8206,7669,7678,1833,8700,4480],
[4865,9912,8038,8238,782,3095,8199,1127,4501,7280,2112,2487,3626,2790,9432,1475,6312,8277,4827,2218,5806,7132,8752,1468,7471,6386,739,8762,8323,8120,5169,9078,9058,3370,9560,7987,8585,8531,5347,9312,1058,4271,1159,5286,5404,6925,8606,9204,7361,2415,560,586,4002,2644,1927,2824,768,4409,2942,3345,1002,808,4941,6267,7979,5140,8643,7553,9438,7320,4938,2666,4609,2778,8158,6730,3748,3867,1866,7181],
[171,3771,7134,8927,4778,2913,3326,2004,3089,7853,1378,1729,4777,2706,9578,1360,5693,3036,1851,7248,2403,2273,8536,6501,9216,613,9671,7131,7719,6425,773,717,8803,160,1114,7554,7197,753,4513,4322,8499,4533,2609,4226,8710,6627,644,9666,6260,4870,5744,7385,6542,6203,7703,6130,8944,5589,2262,6803,6381,7414,6888,5123,7320,9392,9061,6780,322,8975,7050,5089,1061,2260,3199,1150,1865,5386,9699,6501],
[3744,8454,6885,8277,919,1923,4001,6864,7854,5519,2491,6057,8794,9645,1776,5714,9786,9281,7538,6916,3215,395,2501,9618,4835,8846,9708,2813,3303,1794,8309,7176,2206,1602,1838,236,4593,2245,8993,4017,10,8215,6921,5206,4023,5932,6997,7801,262,7640,3107,8275,4938,7822,2425,3223,3886,2105,8700,9526,2088,8662,8034,7004,5710,2124,7164,3574,6630,9980,4242,2901,9471,1491,2117,4562,1130,9086,4117,6698],
[2810,2280,2331,1170,4554,4071,8387,1215,2274,9848,6738,1604,7281,8805,439,1298,8318,7834,9426,8603,6092,7944,1309,8828,303,3157,4638,4439,9175,1921,4695,7716,1494,1015,1772,5913,1127,1952,1950,8905,4064,9890,385,9357,7945,5035,7082,5369,4093,6546,5187,5637,2041,8946,1758,7111,6566,1027,1049,5148,7224,7248,296,6169,375,1656,7993,2816,3717,4279,4675,1609,3317,42,6201,3100,3144,163,9530,4531],
[7096,6070,1009,4988,3538,5801,7149,3063,2324,2912,7911,7002,4338,7880,2481,7368,3516,2016,7556,2193,1388,3865,8125,4637,4096,8114,750,3144,1938,7002,9343,4095,1392,4220,3455,6969,9647,1321,9048,1996,1640,6626,1788,314,9578,6630,2813,6626,4981,9908,7024,4355,3201,3521,3864,3303,464,1923,595,9801,3391,8366,8084,9374,1041,8807,9085,1892,9431,8317,9016,9221,8574,9981,9240,5395,2009,6310,2854,9255],
[8830,3145,2960,9615,8220,6061,3452,2918,6481,9278,2297,3385,6565,7066,7316,5682,107,7646,4466,68,1952,9603,8615,54,7191,791,6833,2560,693,9733,4168,570,9127,9537,1925,8287,5508,4297,8452,8795,6213,7994,2420,4208,524,5915,8602,8330,2651,8547,6156,1812,6271,7991,9407,9804,1553,6866,1128,2119,4691,9711,8315,5879,9935,6900,482,682,4126,1041,428,6247,3720,5882,7526,2582,4327,7725,3503,2631],
[2738,9323,721,7434,1453,6294,2957,3786,5722,6019,8685,4386,3066,9057,6860,499,5315,3045,5194,7111,3137,9104,941,586,3066,755,4177,8819,7040,5309,3583,3897,4428,7788,4721,7249,6559,7324,825,7311,3760,6064,6070,9672,4882,584,1365,9739,9331,5783,2624,7889,1604,1303,1555,7125,8312,425,8936,3233,7724,1480,403,7440,1784,1754,4721,1569,652,3893,4574,5692,9730,4813,9844,8291,9199,7101,3391,8914],
[6044,2928,9332,3328,8588,447,3830,1176,3523,2705,8365,6136,5442,9049,5526,8575,8869,9031,7280,706,2794,8814,5767,4241,7696,78,6570,556,5083,1426,4502,3336,9518,2292,1885,3740,3153,9348,9331,8051,2759,5407,9028,7840,9255,831,515,2612,9747,7435,8964,4971,2048,4900,5967,8271,1719,9670,2810,6777,1594,6367,6259,8316,3815,1689,6840,9437,4361,822,9619,3065,83,6344,7486,8657,8228,9635,6932,4864],
[8478,4777,6334,4678,7476,4963,6735,3096,5860,1405,5127,7269,7793,4738,227,9168,2996,8928,765,733,1276,7677,6258,1528,9558,3329,302,8901,1422,8277,6340,645,9125,8869,5952,141,8141,1816,9635,4025,4184,3093,83,2344,2747,9352,7966,1206,1126,1826,218,7939,2957,2729,810,8752,5247,4174,4038,8884,7899,9567,301,5265,5752,7524,4381,1669,3106,8270,6228,6373,754,2547,4240,2313,5514,3022,1040,9738],
[2265,8192,1763,1369,8469,8789,4836,52,1212,6690,5257,8918,6723,6319,378,4039,2421,8555,8184,9577,1432,7139,8078,5452,9628,7579,4161,7490,5159,8559,1011,81,478,5840,1964,1334,6875,8670,9900,739,1514,8692,522,9316,6955,1345,8132,2277,3193,9773,3923,4177,2183,1236,6747,6575,4874,6003,6409,8187,745,8776,9440,7543,9825,2582,7381,8147,7236,5185,7564,6125,218,7991,6394,391,7659,7456,5128,5294],
[2132,8992,8160,5782,4420,3371,3798,5054,552,5631,7546,4716,1332,6486,7892,7441,4370,6231,4579,2121,8615,1145,9391,1524,1385,2400,9437,2454,7896,7467,2928,8400,3299,4025,7458,4703,7206,6358,792,6200,725,4275,4136,7390,5984,4502,7929,5085,8176,4600,119,3568,76,9363,6943,2248,9077,9731,6213,5817,6729,4190,3092,6910,759,2682,8380,1254,9604,3011,9291,5329,9453,9746,2739,6522,3765,5634,1113,5789],
[5304,5499,564,2801,679,2653,1783,3608,7359,7797,3284,796,3222,437,7185,6135,8571,2778,7488,5746,678,6140,861,7750,803,9859,9918,2425,3734,2698,9005,4864,9818,6743,2475,132,9486,3825,5472,919,292,4411,7213,7699,6435,9019,6769,1388,802,2124,1345,8493,9487,8558,7061,8777,8833,2427,2238,5409,4957,8503,3171,7622,5779,6145,2417,5873,5563,5693,9574,9491,1937,7384,4563,6842,5432,2751,3406,7981]]
    dp = [[0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,000,0000,0000,0000,000,0000,0000,000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,00,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000],
[0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000],
[0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,00,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,000,0000,0000,0000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,00,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000]]

    dp[79][79] = matrix[79][79]
    for x in range(78, -1, -1):
        dp[79][x] = matrix[79][x] + dp[79][x+1]
    for x in range(78, -1, -1):
        dp[x][79] = matrix[x][79] + dp[x+1][79]
    for x in range(78, -1, -1):
        for y in range(78, -1, -1):
            dp[x][y] = matrix[x][y] + min(dp[x+1][y], dp[x][y+1])
    return dp

def euler82():
    matrix = [[4445,2697,5115,718,2209,2212,654,4348,3079,6821,7668,3276,8874,4190,3785,2752,9473,7817,9137,496,7338,3434,7152,4355,4552,7917,7827,2460,2350,691,3514,5880,3145,7633,7199,3783,5066,7487,3285,1084,8985,760,872,8609,8051,1134,9536,5750,9716,9371,7619,5617,275,9721,2997,2698,1887,8825,6372,3014,2113,7122,7050,6775,5948,2758,1219,3539,348,7989,2735,9862,1263,8089,6401,9462,3168,2758,3748,5870],
[1096,20,1318,7586,5167,2642,1443,5741,7621,7030,5526,4244,2348,4641,9827,2448,6918,5883,3737,300,7116,6531,567,5997,3971,6623,820,6148,3287,1874,7981,8424,7672,7575,6797,6717,1078,5008,4051,8795,5820,346,1851,6463,2117,6058,3407,8211,117,4822,1317,4377,4434,5925,8341,4800,1175,4173,690,8978,7470,1295,3799,8724,3509,9849,618,3320,7068,9633,2384,7175,544,6583,1908,9983,481,4187,9353,9377],
[9607,7385,521,6084,1364,8983,7623,1585,6935,8551,2574,8267,4781,3834,2764,2084,2669,4656,9343,7709,2203,9328,8004,6192,5856,3555,2260,5118,6504,1839,9227,1259,9451,1388,7909,5733,6968,8519,9973,1663,5315,7571,3035,4325,4283,2304,6438,3815,9213,9806,9536,196,5542,6907,2475,1159,5820,9075,9470,2179,9248,1828,4592,9167,3713,4640,47,3637,309,7344,6955,346,378,9044,8635,7466,5036,9515,6385,9230],
[7206,3114,7760,1094,6150,5182,7358,7387,4497,955,101,1478,7777,6966,7010,8417,6453,4955,3496,107,449,8271,131,2948,6185,784,5937,8001,6104,8282,4165,3642,710,2390,575,715,3089,6964,4217,192,5949,7006,715,3328,1152,66,8044,4319,1735,146,4818,5456,6451,4113,1063,4781,6799,602,1504,6245,6550,1417,1343,2363,3785,5448,4545,9371,5420,5068,4613,4882,4241,5043,7873,8042,8434,3939,9256,2187],
[3620,8024,577,9997,7377,7682,1314,1158,6282,6310,1896,2509,5436,1732,9480,706,496,101,6232,7375,2207,2306,110,6772,3433,2878,8140,5933,8688,1399,2210,7332,6172,6403,7333,4044,2291,1790,2446,7390,8698,5723,3678,7104,1825,2040,140,3982,4905,4160,2200,5041,2512,1488,2268,1175,7588,8321,8078,7312,977,5257,8465,5068,3453,3096,1651,7906,253,9250,6021,8791,8109,6651,3412,345,4778,5152,4883,7505],
[1074,5438,9008,2679,5397,5429,2652,3403,770,9188,4248,2493,4361,8327,9587,707,9525,5913,93,1899,328,2876,3604,673,8576,6908,7659,2544,3359,3883,5273,6587,3065,1749,3223,604,9925,6941,2823,8767,7039,3290,3214,1787,7904,3421,7137,9560,8451,2669,9219,6332,1576,5477,6755,8348,4164,4307,2984,4012,6629,1044,2874,6541,4942,903,1404,9125,5160,8836,4345,2581,460,8438,1538,5507,668,3352,2678,6942],
[4295,1176,5596,1521,3061,9868,7037,7129,8933,6659,5947,5063,3653,9447,9245,2679,767,714,116,8558,163,3927,8779,158,5093,2447,5782,3967,1716,931,7772,8164,1117,9244,5783,7776,3846,8862,6014,2330,6947,1777,3112,6008,3491,1906,5952,314,4602,8994,5919,9214,3995,5026,7688,6809,5003,3128,2509,7477,110,8971,3982,8539,2980,4689,6343,5411,2992,5270,5247,9260,2269,7474,1042,7162,5206,1232,4556,4757],
[510,3556,5377,1406,5721,4946,2635,7847,4251,8293,8281,6351,4912,287,2870,3380,3948,5322,3840,4738,9563,1906,6298,3234,8959,1562,6297,8835,7861,239,6618,1322,2553,2213,5053,5446,4402,6500,5182,8585,6900,5756,9661,903,5186,7687,5998,7997,8081,8955,4835,6069,2621,1581,732,9564,1082,1853,5442,1342,520,1737,3703,5321,4793,2776,1508,1647,9101,2499,6891,4336,7012,3329,3212,1442,9993,3988,4930,7706],
[9444,3401,5891,9716,1228,7107,109,3563,2700,6161,5039,4992,2242,8541,7372,2067,1294,3058,1306,320,8881,5756,9326,411,8650,8824,5495,8282,8397,2000,1228,7817,2099,6473,3571,5994,4447,1299,5991,543,7874,2297,1651,101,2093,3463,9189,6872,6118,872,1008,1779,2805,9084,4048,2123,5877,55,3075,1737,9459,4535,6453,3644,108,5982,4437,5213,1340,6967,9943,5815,669,8074,1838,6979,9132,9315,715,5048],
[3327,4030,7177,6336,9933,5296,2621,4785,2755,4832,2512,2118,2244,4407,2170,499,7532,9742,5051,7687,970,6924,3527,4694,5145,1306,2165,5940,2425,8910,3513,1909,6983,346,6377,4304,9330,7203,6605,3709,3346,970,369,9737,5811,4427,9939,3693,8436,5566,1977,3728,2399,3985,8303,2492,5366,9802,9193,7296,1033,5060,9144,2766,1151,7629,5169,5995,58,7619,7565,4208,1713,6279,3209,4908,9224,7409,1325,8540],
[6882,1265,1775,3648,4690,959,5837,4520,5394,1378,9485,1360,4018,578,9174,2932,9890,3696,116,1723,1178,9355,7063,1594,1918,8574,7594,7942,1547,6166,7888,354,6932,4651,1010,7759,6905,661,7689,6092,9292,3845,9605,8443,443,8275,5163,7720,7265,6356,7779,1798,1754,5225,6661,1180,8024,5666,88,9153,1840,3508,1193,4445,2648,3538,6243,6375,8107,5902,5423,2520,1122,5015,6113,8859,9370,966,8673,2442],
[7338,3423,4723,6533,848,8041,7921,8277,4094,5368,7252,8852,9166,2250,2801,6125,8093,5738,4038,9808,7359,9494,601,9116,4946,2702,5573,2921,9862,1462,1269,2410,4171,2709,7508,6241,7522,615,2407,8200,4189,5492,5649,7353,2590,5203,4274,710,7329,9063,956,8371,3722,4253,4785,1194,4828,4717,4548,940,983,2575,4511,2938,1827,2027,2700,1236,841,5760,1680,6260,2373,3851,1841,4968,1172,5179,7175,3509],
[4420,1327,3560,2376,6260,2988,9537,4064,4829,8872,9598,3228,1792,7118,9962,9336,4368,9189,6857,1829,9863,6287,7303,7769,2707,8257,2391,2009,3975,4993,3068,9835,3427,341,8412,2134,4034,8511,6421,3041,9012,2983,7289,100,1355,7904,9186,6920,5856,2008,6545,8331,3655,5011,839,8041,9255,6524,3862,8788,62,7455,3513,5003,8413,3918,2076,7960,6108,3638,6999,3436,1441,4858,4181,1866,8731,7745,3744,1000],
[356,8296,8325,1058,1277,4743,3850,2388,6079,6462,2815,5620,8495,5378,75,4324,3441,9870,1113,165,1544,1179,2834,562,6176,2313,6836,8839,2986,9454,5199,6888,1927,5866,8760,320,1792,8296,7898,6121,7241,5886,5814,2815,8336,1576,4314,3109,2572,6011,2086,9061,9403,3947,5487,9731,7281,3159,1819,1334,3181,5844,5114,9898,4634,2531,4412,6430,4262,8482,4546,4555,6804,2607,9421,686,8649,8860,7794,6672],
[9870,152,1558,4963,8750,4754,6521,6256,8818,5208,5691,9659,8377,9725,5050,5343,2539,6101,1844,9700,7750,8114,5357,3001,8830,4438,199,9545,8496,43,2078,327,9397,106,6090,8181,8646,6414,7499,5450,4850,6273,5014,4131,7639,3913,6571,8534,9703,4391,7618,445,1320,5,1894,6771,7383,9191,4708,9706,6939,7937,8726,9382,5216,3685,2247,9029,8154,1738,9984,2626,9438,4167,6351,5060,29,1218,1239,4785],
[192,5213,8297,8974,4032,6966,5717,1179,6523,4679,9513,1481,3041,5355,9303,9154,1389,8702,6589,7818,6336,3539,5538,3094,6646,6702,6266,2759,4608,4452,617,9406,8064,6379,444,5602,4950,1810,8391,1536,316,8714,1178,5182,5863,5110,5372,4954,1978,2971,5680,4863,2255,4630,5723,2168,538,1692,1319,7540,440,6430,6266,7712,7385,5702,620,641,3136,7350,1478,3155,2820,9109,6261,1122,4470,14,8493,2095],
[1046,4301,6082,474,4974,7822,2102,5161,5172,6946,8074,9716,6586,9962,9749,5015,2217,995,5388,4402,7652,6399,6539,1349,8101,3677,1328,9612,7922,2879,231,5887,2655,508,4357,4964,3554,5930,6236,7384,4614,280,3093,9600,2110,7863,2631,6626,6620,68,1311,7198,7561,1768,5139,1431,221,230,2940,968,5283,6517,2146,1646,869,9402,7068,8645,7058,1765,9690,4152,2926,9504,2939,7504,6074,2944,6470,7859],
[4659,736,4951,9344,1927,6271,8837,8711,3241,6579,7660,5499,5616,3743,5801,4682,9748,8796,779,1833,4549,8138,4026,775,4170,2432,4174,3741,7540,8017,2833,4027,396,811,2871,1150,9809,2719,9199,8504,1224,540,2051,3519,7982,7367,2761,308,3358,6505,2050,4836,5090,7864,805,2566,2409,6876,3361,8622,5572,5895,3280,441,7893,8105,1634,2929,274,3926,7786,6123,8233,9921,2674,5340,1445,203,4585,3837],
[5759,338,7444,7968,7742,3755,1591,4839,1705,650,7061,2461,9230,9391,9373,2413,1213,431,7801,4994,2380,2703,6161,6878,8331,2538,6093,1275,5065,5062,2839,582,1014,8109,3525,1544,1569,8622,7944,2905,6120,1564,1839,5570,7579,1318,2677,5257,4418,5601,7935,7656,5192,1864,5886,6083,5580,6202,8869,1636,7907,4759,9082,5854,3185,7631,6854,5872,5632,5280,1431,2077,9717,7431,4256,8261,9680,4487,4752,4286],
[1571,1428,8599,1230,7772,4221,8523,9049,4042,8726,7567,6736,9033,2104,4879,4967,6334,6716,3994,1269,8995,6539,3610,7667,6560,6065,874,848,4597,1711,7161,4811,6734,5723,6356,6026,9183,2586,5636,1092,7779,7923,8747,6887,7505,9909,1792,3233,4526,3176,1508,8043,720,5212,6046,4988,709,5277,8256,3642,1391,5803,1468,2145,3970,6301,7767,2359,8487,9771,8785,7520,856,1605,8972,2402,2386,991,1383,5963],
[1822,4824,5957,6511,9868,4113,301,9353,6228,2881,2966,6956,9124,9574,9233,1601,7340,973,9396,540,4747,8590,9535,3650,7333,7583,4806,3593,2738,8157,5215,8472,2284,9473,3906,6982,5505,6053,7936,6074,7179,6688,1564,1103,6860,5839,2022,8490,910,7551,7805,881,7024,1855,9448,4790,1274,3672,2810,774,7623,4223,4850,6071,9975,4935,1915,9771,6690,3846,517,463,7624,4511,614,6394,3661,7409,1395,8127],
[8738,3850,9555,3695,4383,2378,87,6256,6740,7682,9546,4255,6105,2000,1851,4073,8957,9022,6547,5189,2487,303,9602,7833,1628,4163,6678,3144,8589,7096,8913,5823,4890,7679,1212,9294,5884,2972,3012,3359,7794,7428,1579,4350,7246,4301,7779,7790,3294,9547,4367,3549,1958,8237,6758,3497,3250,3456,6318,1663,708,7714,6143,6890,3428,6853,9334,7992,591,6449,9786,1412,8500,722,5468,1371,108,3939,4199,2535],
[7047,4323,1934,5163,4166,461,3544,2767,6554,203,6098,2265,9078,2075,4644,6641,8412,9183,487,101,7566,5622,1975,5726,2920,5374,7779,5631,3753,3725,2672,3621,4280,1162,5812,345,8173,9785,1525,955,5603,2215,2580,5261,2765,2990,5979,389,3907,2484,1232,5933,5871,3304,1138,1616,5114,9199,5072,7442,7245,6472,4760,6359,9053,7876,2564,9404,3043,9026,2261,3374,4460,7306,2326,966,828,3274,1712,3446],
[3975,4565,8131,5800,4570,2306,8838,4392,9147,11,3911,7118,9645,4994,2028,6062,5431,2279,8752,2658,7836,994,7316,5336,7185,3289,1898,9689,2331,5737,3403,1124,2679,3241,7748,16,2724,5441,6640,9368,9081,5618,858,4969,17,2103,6035,8043,7475,2181,939,415,1617,8500,8253,2155,7843,7974,7859,1746,6336,3193,2617,8736,4079,6324,6645,8891,9396,5522,6103,1857,8979,3835,2475,1310,7422,610,8345,7615],
[9248,5397,5686,2988,3446,4359,6634,9141,497,9176,6773,7448,1907,8454,916,1596,2241,1626,1384,2741,3649,5362,8791,7170,2903,2475,5325,6451,924,3328,522,90,4813,9737,9557,691,2388,1383,4021,1609,9206,4707,5200,7107,8104,4333,9860,5013,1224,6959,8527,1877,4545,7772,6268,621,4915,9349,5970,706,9583,3071,4127,780,8231,3017,9114,3836,7503,2383,1977,4870,8035,2379,9704,1037,3992,3642,1016,4303],
[5093,138,4639,6609,1146,5565,95,7521,9077,2272,974,4388,2465,2650,722,4998,3567,3047,921,2736,7855,173,2065,4238,1048,5,6847,9548,8632,9194,5942,4777,7910,8971,6279,7253,2516,1555,1833,3184,9453,9053,6897,7808,8629,4877,1871,8055,4881,7639,1537,7701,2508,7564,5845,5023,2304,5396,3193,2955,1088,3801,6203,1748,3737,1276,13,4120,7715,8552,3047,2921,106,7508,304,1280,7140,2567,9135,5266],
[6237,4607,7527,9047,522,7371,4883,2540,5867,6366,5301,1570,421,276,3361,527,6637,4861,2401,7522,5808,9371,5298,2045,5096,5447,7755,5115,7060,8529,4078,1943,1697,1764,5453,7085,960,2405,739,2100,5800,728,9737,5704,5693,1431,8979,6428,673,7540,6,7773,5857,6823,150,5869,8486,684,5816,9626,7451,5579,8260,3397,5322,6920,1879,2127,2884,5478,4977,9016,6165,6292,3062,5671,5968,78,4619,4763],
[9905,7127,9390,5185,6923,3721,9164,9705,4341,1031,1046,5127,7376,6528,3248,4941,1178,7889,3364,4486,5358,9402,9158,8600,1025,874,1839,1783,309,9030,1843,845,8398,1433,7118,70,8071,2877,3904,8866,6722,4299,10,1929,5897,4188,600,1889,3325,2485,6473,4474,7444,6992,4846,6166,4441,2283,2629,4352,7775,1101,2214,9985,215,8270,9750,2740,8361,7103,5930,8664,9690,8302,9267,344,2077,1372,1880,9550],
[5825,8517,7769,2405,8204,1060,3603,7025,478,8334,1997,3692,7433,9101,7294,7498,9415,5452,3850,3508,6857,9213,6807,4412,7310,854,5384,686,4978,892,8651,3241,2743,3801,3813,8588,6701,4416,6990,6490,3197,6838,6503,114,8343,5844,8646,8694,65,791,5979,2687,2621,2019,8097,1423,3644,9764,4921,3266,3662,5561,2476,8271,8138,6147,1168,3340,1998,9874,6572,9873,6659,5609,2711,3931,9567,4143,7833,8887],
[6223,2099,2700,589,4716,8333,1362,5007,2753,2848,4441,8397,7192,8191,4916,9955,6076,3370,6396,6971,3156,248,3911,2488,4930,2458,7183,5455,170,6809,6417,3390,1956,7188,577,7526,2203,968,8164,479,8699,7915,507,6393,4632,1597,7534,3604,618,3280,6061,9793,9238,8347,568,9645,2070,5198,6482,5000,9212,6655,5961,7513,1323,3872,6170,3812,4146,2736,67,3151,5548,2781,9679,7564,5043,8587,1893,4531],
[5826,3690,6724,2121,9308,6986,8106,6659,2142,1642,7170,2877,5757,6494,8026,6571,8387,9961,6043,9758,9607,6450,8631,8334,7359,5256,8523,2225,7487,1977,9555,8048,5763,2414,4948,4265,2427,8978,8088,8841,9208,9601,5810,9398,8866,9138,4176,5875,7212,3272,6759,5678,7649,4922,5422,1343,8197,3154,3600,687,1028,4579,2084,9467,4492,7262,7296,6538,7657,7134,2077,1505,7332,6890,8964,4879,7603,7400,5973,739],
[1861,1613,4879,1884,7334,966,2000,7489,2123,4287,1472,3263,4726,9203,1040,4103,6075,6049,330,9253,4062,4268,1635,9960,577,1320,3195,9628,1030,4092,4979,6474,6393,2799,6967,8687,7724,7392,9927,2085,3200,6466,8702,265,7646,8665,7986,7266,4574,6587,612,2724,704,3191,8323,9523,3002,704,5064,3960,8209,2027,2758,8393,4875,4641,9584,6401,7883,7014,768,443,5490,7506,1852,2005,8850,5776,4487,4269],
[4052,6687,4705,7260,6645,6715,3706,5504,8672,2853,1136,8187,8203,4016,871,1809,1366,4952,9294,5339,6872,2645,6083,7874,3056,5218,7485,8796,7401,3348,2103,426,8572,4163,9171,3176,948,7654,9344,3217,1650,5580,7971,2622,76,2874,880,2034,9929,1546,2659,5811,3754,7096,7436,9694,9960,7415,2164,953,2360,4194,2397,1047,2196,6827,575,784,2675,8821,6802,7972,5996,6699,2134,7577,2887,1412,4349,4380],
[4629,2234,6240,8132,7592,3181,6389,1214,266,1910,2451,8784,2790,1127,6932,1447,8986,2492,5476,397,889,3027,7641,5083,5776,4022,185,3364,5701,2442,2840,4160,9525,4828,6602,2614,7447,3711,4505,7745,8034,6514,4907,2605,7753,6958,7270,6936,3006,8968,439,2326,4652,3085,3425,9863,5049,5361,8688,297,7580,8777,7916,6687,8683,7141,306,9569,2384,1500,3346,4601,7329,9040,6097,2727,6314,4501,4974,2829],
[8316,4072,2025,6884,3027,1808,5714,7624,7880,8528,4205,8686,7587,3230,1139,7273,6163,6986,3914,9309,1464,9359,4474,7095,2212,7302,2583,9462,7532,6567,1606,4436,8981,5612,6796,4385,5076,2007,6072,3678,8331,1338,3299,8845,4783,8613,4071,1232,6028,2176,3990,2148,3748,103,9453,538,6745,9110,926,3125,473,5970,8728,7072,9062,1404,1317,5139,9862,6496,6062,3338,464,1600,2532,1088,8232,7739,8274,3873],
[2341,523,7096,8397,8301,6541,9844,244,4993,2280,7689,4025,4196,5522,7904,6048,2623,9258,2149,9461,6448,8087,7245,1917,8340,7127,8466,5725,6996,3421,5313,512,9164,9837,9794,8369,4185,1488,7210,1524,1016,4620,9435,2478,7765,8035,697,6677,3724,6988,5853,7662,3895,9593,1185,4727,6025,5734,7665,3070,138,8469,6748,6459,561,7935,8646,2378,462,7755,3115,9690,8877,3946,2728,8793,244,6323,8666,4271],
[6430,2406,8994,56,1267,3826,9443,7079,7579,5232,6691,3435,6718,5698,4144,7028,592,2627,217,734,6194,8156,9118,58,2640,8069,4127,3285,694,3197,3377,4143,4802,3324,8134,6953,7625,3598,3584,4289,7065,3434,2106,7132,5802,7920,9060,7531,3321,1725,1067,3751,444,5503,6785,7937,6365,4803,198,6266,8177,1470,6390,1606,2904,7555,9834,8667,2033,1723,5167,1666,8546,8152,473,4475,6451,7947,3062,3281],
[2810,3042,7759,1741,2275,2609,7676,8640,4117,1958,7500,8048,1757,3954,9270,1971,4796,2912,660,5511,3553,1012,5757,4525,6084,7198,8352,5775,7726,8591,7710,9589,3122,4392,6856,5016,749,2285,3356,7482,9956,7348,2599,8944,495,3462,3578,551,4543,7207,7169,7796,1247,4278,6916,8176,3742,8385,2310,1345,8692,2667,4568,1770,8319,3585,4920,3890,4928,7343,5385,9772,7947,8786,2056,9266,3454,2807,877,2660],
[6206,8252,5928,5837,4177,4333,207,7934,5581,9526,8906,1498,8411,2984,5198,5134,2464,8435,8514,8674,3876,599,5327,826,2152,4084,2433,9327,9697,4800,2728,3608,3849,3861,3498,9943,1407,3991,7191,9110,5666,8434,4704,6545,5944,2357,1163,4995,9619,6754,4200,9682,6654,4862,4744,5953,6632,1054,293,9439,8286,2255,696,8709,1533,1844,6441,430,1999,6063,9431,7018,8057,2920,6266,6799,356,3597,4024,6665],
[3847,6356,8541,7225,2325,2946,5199,469,5450,7508,2197,9915,8284,7983,6341,3276,3321,16,1321,7608,5015,3362,8491,6968,6818,797,156,2575,706,9516,5344,5457,9210,5051,8099,1617,9951,7663,8253,9683,2670,1261,4710,1068,8753,4799,1228,2621,3275,6188,4699,1791,9518,8701,5932,4275,6011,9877,2933,4182,6059,2930,6687,6682,9771,654,9437,3169,8596,1827,5471,8909,2352,123,4394,3208,8756,5513,6917,2056],
[5458,8173,3138,3290,4570,4892,3317,4251,9699,7973,1163,1935,5477,6648,9614,5655,9592,975,9118,2194,7322,8248,8413,3462,8560,1907,7810,6650,7355,2939,4973,6894,3933,3784,3200,2419,9234,4747,2208,2207,1945,2899,1407,6145,8023,3484,5688,7686,2737,3828,3704,9004,5190,9740,8643,8650,5358,4426,1522,1707,3613,9887,6956,2447,2762,833,1449,9489,2573,1080,4167,3456,6809,2466,227,7125,2759,6250,6472,8089],
[3266,7025,9756,3914,1265,9116,7723,9788,6805,5493,2092,8688,6592,9173,4431,4028,6007,7131,4446,4815,3648,6701,759,3312,8355,4485,4187,5188,8746,7759,3528,2177,5243,8379,3838,7233,4607,9187,7216,2190,6967,2920,6082,7910,5354,3609,8958,6949,7731,494,8753,8707,1523,4426,3543,7085,647,6771,9847,646,5049,824,8417,5260,2730,5702,2513,9275,4279,2767,8684,1165,9903,4518,55,9682,8963,6005,2102,6523],
[1998,8731,936,1479,5259,7064,4085,91,7745,7136,3773,3810,730,8255,2705,2653,9790,6807,2342,355,9344,2668,3690,2028,9679,8102,574,4318,6481,9175,5423,8062,2867,9657,7553,3442,3920,7430,3945,7639,3714,3392,2525,4995,4850,2867,7951,9667,486,9506,9888,781,8866,1702,3795,90,356,1483,4200,2131,6969,5931,486,6880,4404,1084,5169,4910,6567,8335,4686,5043,2614,3352,2667,4513,6472,7471,5720,1616],
[8878,1613,1716,868,1906,2681,564,665,5995,2474,7496,3432,9491,9087,8850,8287,669,823,347,6194,2264,2592,7871,7616,8508,4827,760,2676,4660,4881,7572,3811,9032,939,4384,929,7525,8419,5556,9063,662,8887,7026,8534,3111,1454,2082,7598,5726,6687,9647,7608,73,3014,5063,670,5461,5631,3367,9796,8475,7908,5073,1565,5008,5295,4457,1274,4788,1728,338,600,8415,8535,9351,7750,6887,5845,1741,125],
[3637,6489,9634,9464,9055,2413,7824,9517,7532,3577,7050,6186,6980,9365,9782,191,870,2497,8498,2218,2757,5420,6468,586,3320,9230,1034,1393,9886,5072,9391,1178,8464,8042,6869,2075,8275,3601,7715,9470,8786,6475,8373,2159,9237,2066,3264,5000,679,355,3069,4073,494,2308,5512,4334,9438,8786,8637,9774,1169,1949,6594,6072,4270,9158,7916,5752,6794,9391,6301,5842,3285,2141,3898,8027,4310,8821,7079,1307],
[8497,6681,4732,7151,7060,5204,9030,7157,833,5014,8723,3207,9796,9286,4913,119,5118,7650,9335,809,3675,2597,5144,3945,5090,8384,187,4102,1260,2445,2792,4422,8389,9290,50,1765,1521,6921,8586,4368,1565,5727,7855,2003,4834,9897,5911,8630,5070,1330,7692,7557,7980,6028,5805,9090,8265,3019,3802,698,9149,5748,1965,9658,4417,5994,5584,8226,2937,272,5743,1278,5698,8736,2595,6475,5342,6596,1149,6920],
[8188,8009,9546,6310,8772,2500,9846,6592,6872,3857,1307,8125,7042,1544,6159,2330,643,4604,7899,6848,371,8067,2062,3200,7295,1857,9505,6936,384,2193,2190,301,8535,5503,1462,7380,5114,4824,8833,1763,4974,8711,9262,6698,3999,2645,6937,7747,1128,2933,3556,7943,2885,3122,9105,5447,418,2899,5148,3699,9021,9501,597,4084,175,1621,1,1079,6067,5812,4326,9914,6633,5394,4233,6728,9084,1864,5863,1225],
[9935,8793,9117,1825,9542,8246,8437,3331,9128,9675,6086,7075,319,1334,7932,3583,7167,4178,1726,7720,695,8277,7887,6359,5912,1719,2780,8529,1359,2013,4498,8072,1129,9998,1147,8804,9405,6255,1619,2165,7491,1,8882,7378,3337,503,5758,4109,3577,985,3200,7615,8058,5032,1080,6410,6873,5496,1466,2412,9885,5904,4406,3605,8770,4361,6205,9193,1537,9959,214,7260,9566,1685,100,4920,7138,9819,5637,976],
[3466,9854,985,1078,7222,8888,5466,5379,3578,4540,6853,8690,3728,6351,7147,3134,6921,9692,857,3307,4998,2172,5783,3931,9417,2541,6299,13,787,2099,9131,9494,896,8600,1643,8419,7248,2660,2609,8579,91,6663,5506,7675,1947,6165,4286,1972,9645,3805,1663,1456,8853,5705,9889,7489,1107,383,4044,2969,3343,152,7805,4980,9929,5033,1737,9953,7197,9158,4071,1324,473,9676,3984,9680,3606,8160,7384,5432],
[1005,4512,5186,3953,2164,3372,4097,3247,8697,3022,9896,4101,3871,6791,3219,2742,4630,6967,7829,5991,6134,1197,1414,8923,8787,1394,8852,5019,7768,5147,8004,8825,5062,9625,7988,1110,3992,7984,9966,6516,6251,8270,421,3723,1432,4830,6935,8095,9059,2214,6483,6846,3120,1587,6201,6691,9096,9627,6671,4002,3495,9939,7708,7465,5879,6959,6634,3241,3401,2355,9061,2611,7830,3941,2177,2146,5089,7079,519,6351],
[7280,8586,4261,2831,7217,3141,9994,9940,5462,2189,4005,6942,9848,5350,8060,6665,7519,4324,7684,657,9453,9296,2944,6843,7499,7847,1728,9681,3906,6353,5529,2822,3355,3897,7724,4257,7489,8672,4356,3983,1948,6892,7415,4153,5893,4190,621,1736,4045,9532,7701,3671,1211,1622,3176,4524,9317,7800,5638,6644,6943,5463,3531,2821,1347,5958,3436,1438,2999,994,850,4131,2616,1549,3465,5946,690,9273,6954,7991],
[9517,399,3249,2596,7736,2142,1322,968,7350,1614,468,3346,3265,7222,6086,1661,5317,2582,7959,4685,2807,2917,1037,5698,1529,3972,8716,2634,3301,3412,8621,743,8001,4734,888,7744,8092,3671,8941,1487,5658,7099,2781,99,1932,4443,4756,4652,9328,1581,7855,4312,5976,7255,6480,3996,2748,1973,9731,4530,2790,9417,7186,5303,3557,351,7182,9428,1342,9020,7599,1392,8304,2070,9138,7215,2008,9937,1106,7110],
[7444,769,9688,632,1571,6820,8743,4338,337,3366,3073,1946,8219,104,4210,6986,249,5061,8693,7960,6546,1004,8857,5997,9352,4338,6105,5008,2556,6518,6694,4345,3727,7956,20,3954,8652,4424,9387,2035,8358,5962,5304,5194,8650,8282,1256,1103,2138,6679,1985,3653,2770,2433,4278,615,2863,1715,242,3790,2636,6998,3088,1671,2239,957,5411,4595,6282,2881,9974,2401,875,7574,2987,4587,3147,6766,9885,2965],
[3287,3016,3619,6818,9073,6120,5423,557,2900,2015,8111,3873,1314,4189,1846,4399,7041,7583,2427,2864,3525,5002,2069,748,1948,6015,2684,438,770,8367,1663,7887,7759,1885,157,7770,4520,4878,3857,1137,3525,3050,6276,5569,7649,904,4533,7843,2199,5648,7628,9075,9441,3600,7231,2388,5640,9096,958,3058,584,5899,8150,1181,9616,1098,8162,6819,8171,1519,1140,7665,8801,2632,1299,9192,707,9955,2710,7314],
[1772,2963,7578,3541,3095,1488,7026,2634,6015,4633,4370,2762,1650,2174,909,8158,2922,8467,4198,4280,9092,8856,8835,5457,2790,8574,9742,5054,9547,4156,7940,8126,9824,7340,8840,6574,3547,1477,3014,6798,7134,435,9484,9859,3031,4,1502,4133,1738,1807,4825,463,6343,9701,8506,9822,9555,8688,8168,3467,3234,6318,1787,5591,419,6593,7974,8486,9861,6381,6758,194,3061,4315,2863,4665,3789,2201,1492,4416],
[126,8927,6608,5682,8986,6867,1715,6076,3159,788,3140,4744,830,9253,5812,5021,7616,8534,1546,9590,1101,9012,9821,8132,7857,4086,1069,7491,2988,1579,2442,4321,2149,7642,6108,250,6086,3167,24,9528,7663,2685,1220,9196,1397,5776,1577,1730,5481,977,6115,199,6326,2183,3767,5928,5586,7561,663,8649,9688,949,5913,9160,1870,5764,9887,4477,6703,1413,4995,5494,7131,2192,8969,7138,3997,8697,646,1028],
[8074,1731,8245,624,4601,8706,155,8891,309,2552,8208,8452,2954,3124,3469,4246,3352,1105,4509,8677,9901,4416,8191,9283,5625,7120,2952,8881,7693,830,4580,8228,9459,8611,4499,1179,4988,1394,550,2336,6089,6872,269,7213,1848,917,6672,4890,656,1478,6536,3165,4743,4990,1176,6211,7207,5284,9730,4738,1549,4986,4942,8645,3698,9429,1439,2175,6549,3058,6513,1574,6988,8333,3406,5245,5431,7140,7085,6407],
[7845,4694,2530,8249,290,5948,5509,1588,5940,4495,5866,5021,4626,3979,3296,7589,4854,1998,5627,3926,8346,6512,9608,1918,7070,4747,4182,2858,2766,4606,6269,4107,8982,8568,9053,4244,5604,102,2756,727,5887,2566,7922,44,5986,621,1202,374,6988,4130,3627,6744,9443,4568,1398,8679,397,3928,9159,367,2917,6127,5788,3304,8129,911,2669,1463,9749,264,4478,8940,1109,7309,2462,117,4692,7724,225,2312],
[4164,3637,2000,941,8903,39,3443,7172,1031,3687,4901,8082,4945,4515,7204,9310,9349,9535,9940,218,1788,9245,2237,1541,5670,6538,6047,5553,9807,8101,1925,8714,445,8332,7309,6830,5786,5736,7306,2710,3034,1838,7969,6318,7912,2584,2080,7437,6705,2254,7428,820,782,9861,7596,3842,3631,8063,5240,6666,394,4565,7865,4895,9890,6028,6117,4724,9156,4473,4552,602,470,6191,4927,5387,884,3146,1978,3000],
[4258,6880,1696,3582,5793,4923,2119,1155,9056,9698,6603,3768,5514,9927,9609,6166,6566,4536,4985,4934,8076,9062,6741,6163,7399,4562,2337,5600,2919,9012,8459,1308,6072,1225,9306,8818,5886,7243,7365,8792,6007,9256,6699,7171,4230,7002,8720,7839,4533,1671,478,7774,1607,2317,5437,4705,7886,4760,6760,7271,3081,2997,3088,7675,6208,3101,6821,6840,122,9633,4900,2067,8546,4549,2091,7188,5605,8599,6758,5229],
[7854,5243,9155,3556,8812,7047,2202,1541,5993,4600,4760,713,434,7911,7426,7414,8729,322,803,7960,7563,4908,6285,6291,736,3389,9339,4132,8701,7534,5287,3646,592,3065,7582,2592,8755,6068,8597,1982,5782,1894,2900,6236,4039,6569,3037,5837,7698,700,7815,2491,7272,5878,3083,6778,6639,3589,5010,8313,2581,6617,5869,8402,6808,2951,2321,5195,497,2190,6187,1342,1316,4453,7740,4154,2959,1781,1482,8256],
[7178,2046,4419,744,8312,5356,6855,8839,319,2962,5662,47,6307,8662,68,4813,567,2712,9931,1678,3101,8227,6533,4933,6656,92,5846,4780,6256,6361,4323,9985,1231,2175,7178,3034,9744,6155,9165,7787,5836,9318,7860,9644,8941,6480,9443,8188,5928,161,6979,2352,5628,6991,1198,8067,5867,6620,3778,8426,2994,3122,3124,6335,3918,8897,2655,9670,634,1088,1576,8935,7255,474,8166,7417,9547,2886,5560,3842],
[6957,3111,26,7530,7143,1295,1744,6057,3009,1854,8098,5405,2234,4874,9447,2620,9303,27,7410,969,40,2966,5648,7596,8637,4238,3143,3679,7187,690,9980,7085,7714,9373,5632,7526,6707,3951,9734,4216,2146,3602,5371,6029,3039,4433,4855,4151,1449,3376,8009,7240,7027,4602,2947,9081,4045,8424,9352,8742,923,2705,4266,3232,2264,6761,363,2651,3383,7770,6730,7856,7340,9679,2158,610,4471,4608,910,6241],
[4417,6756,1013,8797,658,8809,5032,8703,7541,846,3357,2920,9817,1745,9980,7593,4667,3087,779,3218,6233,5568,4296,2289,2654,7898,5021,9461,5593,8214,9173,4203,2271,7980,2983,5952,9992,8399,3468,1776,3188,9314,1720,6523,2933,621,8685,5483,8986,6163,3444,9539,4320,155,3992,2828,2150,6071,524,2895,5468,8063,1210,3348,9071,4862,483,9017,4097,6186,9815,3610,5048,1644,1003,9865,9332,2145,1944,2213],
[9284,3803,4920,1927,6706,4344,7383,4786,9890,2010,5228,1224,3158,6967,8580,8990,8883,5213,76,8306,2031,4980,5639,9519,7184,5645,7769,3259,8077,9130,1317,3096,9624,3818,1770,695,2454,947,6029,3474,9938,3527,5696,4760,7724,7738,2848,6442,5767,6845,8323,4131,2859,7595,2500,4815,3660,9130,8580,7016,8231,4391,8369,3444,4069,4021,556,6154,627,2778,1496,4206,6356,8434,8491,3816,8231,3190,5575,1015],
[3787,7572,1788,6803,5641,6844,1961,4811,8535,9914,9999,1450,8857,738,4662,8569,6679,2225,7839,8618,286,2648,5342,2294,3205,4546,176,8705,3741,6134,8324,8021,7004,5205,7032,6637,9442,5539,5584,4819,5874,5807,8589,6871,9016,983,1758,3786,1519,6241,185,8398,495,3370,9133,3051,4549,9674,7311,9738,3316,9383,2658,2776,9481,7558,619,3943,3324,6491,4933,153,9738,4623,912,3595,7771,7939,1219,4405],
[2650,3883,4154,5809,315,7756,4430,1788,4451,1631,6461,7230,6017,5751,138,588,5282,2442,9110,9035,6349,2515,1570,6122,4192,4174,3530,1933,4186,4420,4609,5739,4135,2963,6308,1161,8809,8619,2796,3819,6971,8228,4188,1492,909,8048,2328,6772,8467,7671,9068,2226,7579,6422,7056,8042,3296,2272,3006,2196,7320,3238,3490,3102,37,1293,3212,4767,5041,8773,5794,4456,6174,7279,7054,2835,7053,9088,790,6640],
[3101,1057,7057,3826,6077,1025,2955,1224,1114,6729,5902,4698,6239,7203,9423,1804,4417,6686,1426,6941,8071,1029,4985,9010,6122,6597,1622,1574,3513,1684,7086,5505,3244,411,9638,4150,907,9135,829,981,1707,5359,8781,9751,5,9131,3973,7159,1340,6955,7514,7993,6964,8198,1933,2797,877,3993,4453,8020,9349,8646,2779,8679,2961,3547,3374,3510,1129,3568,2241,2625,9138,5974,8206,7669,7678,1833,8700,4480],
[4865,9912,8038,8238,782,3095,8199,1127,4501,7280,2112,2487,3626,2790,9432,1475,6312,8277,4827,2218,5806,7132,8752,1468,7471,6386,739,8762,8323,8120,5169,9078,9058,3370,9560,7987,8585,8531,5347,9312,1058,4271,1159,5286,5404,6925,8606,9204,7361,2415,560,586,4002,2644,1927,2824,768,4409,2942,3345,1002,808,4941,6267,7979,5140,8643,7553,9438,7320,4938,2666,4609,2778,8158,6730,3748,3867,1866,7181],
[171,3771,7134,8927,4778,2913,3326,2004,3089,7853,1378,1729,4777,2706,9578,1360,5693,3036,1851,7248,2403,2273,8536,6501,9216,613,9671,7131,7719,6425,773,717,8803,160,1114,7554,7197,753,4513,4322,8499,4533,2609,4226,8710,6627,644,9666,6260,4870,5744,7385,6542,6203,7703,6130,8944,5589,2262,6803,6381,7414,6888,5123,7320,9392,9061,6780,322,8975,7050,5089,1061,2260,3199,1150,1865,5386,9699,6501],
[3744,8454,6885,8277,919,1923,4001,6864,7854,5519,2491,6057,8794,9645,1776,5714,9786,9281,7538,6916,3215,395,2501,9618,4835,8846,9708,2813,3303,1794,8309,7176,2206,1602,1838,236,4593,2245,8993,4017,10,8215,6921,5206,4023,5932,6997,7801,262,7640,3107,8275,4938,7822,2425,3223,3886,2105,8700,9526,2088,8662,8034,7004,5710,2124,7164,3574,6630,9980,4242,2901,9471,1491,2117,4562,1130,9086,4117,6698],
[2810,2280,2331,1170,4554,4071,8387,1215,2274,9848,6738,1604,7281,8805,439,1298,8318,7834,9426,8603,6092,7944,1309,8828,303,3157,4638,4439,9175,1921,4695,7716,1494,1015,1772,5913,1127,1952,1950,8905,4064,9890,385,9357,7945,5035,7082,5369,4093,6546,5187,5637,2041,8946,1758,7111,6566,1027,1049,5148,7224,7248,296,6169,375,1656,7993,2816,3717,4279,4675,1609,3317,42,6201,3100,3144,163,9530,4531],
[7096,6070,1009,4988,3538,5801,7149,3063,2324,2912,7911,7002,4338,7880,2481,7368,3516,2016,7556,2193,1388,3865,8125,4637,4096,8114,750,3144,1938,7002,9343,4095,1392,4220,3455,6969,9647,1321,9048,1996,1640,6626,1788,314,9578,6630,2813,6626,4981,9908,7024,4355,3201,3521,3864,3303,464,1923,595,9801,3391,8366,8084,9374,1041,8807,9085,1892,9431,8317,9016,9221,8574,9981,9240,5395,2009,6310,2854,9255],
[8830,3145,2960,9615,8220,6061,3452,2918,6481,9278,2297,3385,6565,7066,7316,5682,107,7646,4466,68,1952,9603,8615,54,7191,791,6833,2560,693,9733,4168,570,9127,9537,1925,8287,5508,4297,8452,8795,6213,7994,2420,4208,524,5915,8602,8330,2651,8547,6156,1812,6271,7991,9407,9804,1553,6866,1128,2119,4691,9711,8315,5879,9935,6900,482,682,4126,1041,428,6247,3720,5882,7526,2582,4327,7725,3503,2631],
[2738,9323,721,7434,1453,6294,2957,3786,5722,6019,8685,4386,3066,9057,6860,499,5315,3045,5194,7111,3137,9104,941,586,3066,755,4177,8819,7040,5309,3583,3897,4428,7788,4721,7249,6559,7324,825,7311,3760,6064,6070,9672,4882,584,1365,9739,9331,5783,2624,7889,1604,1303,1555,7125,8312,425,8936,3233,7724,1480,403,7440,1784,1754,4721,1569,652,3893,4574,5692,9730,4813,9844,8291,9199,7101,3391,8914],
[6044,2928,9332,3328,8588,447,3830,1176,3523,2705,8365,6136,5442,9049,5526,8575,8869,9031,7280,706,2794,8814,5767,4241,7696,78,6570,556,5083,1426,4502,3336,9518,2292,1885,3740,3153,9348,9331,8051,2759,5407,9028,7840,9255,831,515,2612,9747,7435,8964,4971,2048,4900,5967,8271,1719,9670,2810,6777,1594,6367,6259,8316,3815,1689,6840,9437,4361,822,9619,3065,83,6344,7486,8657,8228,9635,6932,4864],
[8478,4777,6334,4678,7476,4963,6735,3096,5860,1405,5127,7269,7793,4738,227,9168,2996,8928,765,733,1276,7677,6258,1528,9558,3329,302,8901,1422,8277,6340,645,9125,8869,5952,141,8141,1816,9635,4025,4184,3093,83,2344,2747,9352,7966,1206,1126,1826,218,7939,2957,2729,810,8752,5247,4174,4038,8884,7899,9567,301,5265,5752,7524,4381,1669,3106,8270,6228,6373,754,2547,4240,2313,5514,3022,1040,9738],
[2265,8192,1763,1369,8469,8789,4836,52,1212,6690,5257,8918,6723,6319,378,4039,2421,8555,8184,9577,1432,7139,8078,5452,9628,7579,4161,7490,5159,8559,1011,81,478,5840,1964,1334,6875,8670,9900,739,1514,8692,522,9316,6955,1345,8132,2277,3193,9773,3923,4177,2183,1236,6747,6575,4874,6003,6409,8187,745,8776,9440,7543,9825,2582,7381,8147,7236,5185,7564,6125,218,7991,6394,391,7659,7456,5128,5294],
[2132,8992,8160,5782,4420,3371,3798,5054,552,5631,7546,4716,1332,6486,7892,7441,4370,6231,4579,2121,8615,1145,9391,1524,1385,2400,9437,2454,7896,7467,2928,8400,3299,4025,7458,4703,7206,6358,792,6200,725,4275,4136,7390,5984,4502,7929,5085,8176,4600,119,3568,76,9363,6943,2248,9077,9731,6213,5817,6729,4190,3092,6910,759,2682,8380,1254,9604,3011,9291,5329,9453,9746,2739,6522,3765,5634,1113,5789],
[5304,5499,564,2801,679,2653,1783,3608,7359,7797,3284,796,3222,437,7185,6135,8571,2778,7488,5746,678,6140,861,7750,803,9859,9918,2425,3734,2698,9005,4864,9818,6743,2475,132,9486,3825,5472,919,292,4411,7213,7699,6435,9019,6769,1388,802,2124,1345,8493,9487,8558,7061,8777,8833,2427,2238,5409,4957,8503,3171,7622,5779,6145,2417,5873,5563,5693,9574,9491,1937,7384,4563,6842,5432,2751,3406,7981]]
    dp = [[0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,000,0000,0000,0000,000,0000,0000,000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,00,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,00,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,000,0000],
[0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000],
[0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,000,00,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,000,000,0000,0000,0000,0000,0,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,00,0000,000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,00,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,00,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,00,000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,000,0000,0000,0000,0000],
[0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,00,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000],
[0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,000,0000,000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,000,000,0000,0000,0000,0000,0000,0000,0000,000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000]]

    for x in range(0, 80):
        dp[x][79] = matrix[x][79]
    for x in range(79, -1, -1):
        for y in range(78, -1, -1):
                currSums = []
                currSums = currSums + [dp[x][y+1]]
                for p in range(0,x):

                    currSums = currSums + [calcSumX2D(matrix, p, x,y) + dp[p][y+1]]
                for p in range(x, 80):
                    currSums = currSums + [calcSumX2D(matrix, x, p, y) + dp[p][y+1]]
                dp[x][y] = matrix[x][y] + min(currSums)
    l = []
    for x in range(0,79):
        l = l + [dp[x][0]]
    return min(l)
    #return (matrix, dp)

def calcSumX2D(l,a,b,y):
    currSum = 0
    for x in range(a,b):
        currSum = currSum + l[x][y]
    return currSum

def euler100():

    return [(a,b) for a in range(1,10000) for b in range(1,10000) if (a+b)*(a+b-1) == 2*a*(a-1)]

def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return isPalindrome(s[1:(len(s) - 1)])

def findLimit():
    twos = []
    l = [x**2 for x in range(1, 10**4)]
    for x in range( 0, len(l)) :
        if sumList(l[x:x+2]) > 10**8:
            return l[x + 2]
    return -1

def euler125():
    l = [x**2 for x in range(1, 7073)]
    curr = []
    for x in range( 0, len(l)) :
        for a in range(x + 2, len(l)):
            currSum = sumList(l[x:a])
            if currSum < 10**8 and isPalindrome(str(currSum)):
                curr = curr + [currSum]
    theL = list(set([x for x in curr if x < 10**8]))
    return sumList(theL)

def isHTPandig(n):
    l = [int(i) for i in str(n)]
    pan = range(1, 10)
    l1 = l[0:9]
    l2 = l[(len(l) - 9):len(l)]
    l1.sort()
    l2.sort()
    if  l1 == pan and  l2 == pan:
        return True
    return False
#    if  set(l1) == pan and  set(l2)== pan:
#        return True
#    return False

def euler104():
    n2 = 1
    n1 = 1
    count = 3
    for x in range(0, 1000000):
        temp = n1
        n1 = n2 + n1
        n2 = temp
        if isHTPandig(n1):
            return (count, n1)
        count = count + 1
        print count
    return -1


def prodList(l):
    currProd = 1
    for x in l:
        currProd = currProd*x
    return currProd
#def compTup(a,b):
    #if a[0] != b[0]:
        #return cmp(a[0], b[0])
    #else:
        #return cmp(a[1], b[1])
def comp(a):
    return a[0]
def euler124():
    curr = []
    primes = sieveOfE(100000)
    for n in range(1, 100001):
        l = getPrimeFactors(n, primes)
        curr = curr + [(prodList(l), n)]
    curr.sort(key=comp)
    return curr

def checkPartition(l, primes):
    for x in l:
        if x not in primes:
            return False
    return True

def detInc(n):
    l = [ int(i) for i in str(n) ]
    for x in range(1, len(l)):
            if l[x] < l[x - 1]:
                return False
    return True

def detDec(n):
    l = [ int(i) for i in str(n) ]
    for x in range(1, len(l)):
            if l[x] > l[x - 1]:
                return False
    return True

def findRatio(ind):
    curr = set(range(1, ind + 1))
    inc = []
    dec = []
    for x in curr:
        if detInc(x):
            inc = inc + [x]
    for x in curr:
        if detDec(x):
            dec = dec + [x]
    curr = curr.difference(set(inc))
    curr = curr.difference(set(dec))
    tot = set(inc + dec)
    return float(len(curr))/ind

def sumDigPow(n):
    sumDig = sumList([int(i) for i in str(n)])
    if sumDig != 1 and n > 10:
        if n == sumDig**int(math.log(n, sumDig)):
            print (sumDig, int(math.log(n, sumDig)))
            return True
    return False

def euler119():
    curr = []
    for x in range(3, 10000000):
        if sumDigPow(x):
            curr = curr + [x]
    return curr

def detPrime(n, primes):
    l = [x for x in primes if x < ((n**0.5) + 1)]
    for y in l:
        if n%y == 0:
            return False
    return True

def euler111():
    primes = sieveOfE(10**5)
    currDig = 9
    currL = []
    for x0 in range(0, 10):
        for x1 in range(0, 10):
            for x2 in range(0, 10):
                for x3 in range(0, 10):
                    for x4 in range(0, 10):
                        for x5 in range(0, 10):
                            for x6 in range(0, 10):
                                for x7 in range(0, 10):
                                    for x8 in range(0, 10):
                                        for x9 in range(0, 10):
                                            currNum = int(str(x0) + str(x1)+ str(x2)+ str(x3)+ str(x4)+ str(x5)+ str(x6)+ str(x7) + str(x8) + str(x9))

                                            if str(currDig) in str(currNum) and detPrime(currNum, primes):
                                                currL = currL + [currDig]
    return currL


def getChain(n):
    curr = n
    currL = []
    while curr not in currL:
        if curr > 1000000:
            currL = []
            break
        currL = currL + [curr]
        curr = sumList(getDivisors(curr))
        #print currL
    currL = currL + [curr]
    return currL

def sumDivisors(n):#for all numbers <=n, find the sum of its divisors
    start = [[a, 0] for a in range(0, n + 1)]
    for x in range(1, len(start)):
        for y in range(x, n + 1, x):
            start[y][1] = start[y][1] + x
    return start



def euler95():
    currMax = 0
    currL = []
    for x in range(1, 1000000):
        l = getChain(x)
        currLen = len(l)
        if l[0] == l[len(l) - 1] and currLen > currMax:
            print (l, currMax)
            currMax = currLen
            currL = l
    return currL

def binSearch(l, start, end, target):
    diff = end - start
    curr = start + int(diff/2)
    if l[curr] == target:
        return curr
    elif l[curr] < target:
        return binSearch(l, start, curr, target)
    else:
        return binSearch(l, curr, end, target)

def isBouncy(n):
    l = [int(i) for i in str(n)]
    b = copy.copy(l)
    b.sort()
    if b == l:
        return False
    b.reverse()
    if b == l:
        return False
    return True

def findMin123():
    primes = sieveOfE(1000000)
    x = 0
    while primes[x]**2 < 10**10:
        x = x + 1
    return x

def euler123():
    primes = sieveOfE(1000000)
    l = []
    for x in range(9500, len(primes)):
        curr = primes[x]
        ind = x + 1
        sq = curr**2
        num1 = pow(primes[x] - 1, ind, sq)
        num2 = pow(primes[x] + 1, ind, sq)
        num3 = (num1 + num2)%sq
        if num3 > 10**10:
            return ind
    return -1

def extendedSet(s):
    if 6 in s or 9 in s:
        s = s.union([6,9])
    return s

def checkSquares(s0, s1):
    squares = set([x**2 for x in range(1,10)])
    for x in s0:
        for y in s1:
            if len(squares) == 0:
                return True
            else:
                n1 = int(str(x) + str(y))
                n2 = int(str(y) + str(x))
                squares = squares.difference(set([n1, n2]))
    if len(squares) == 0:
        return True
    return False

def euler90():
    digits = set(range(0,10))
    l = [set(list(x)) for x in combinations(digits, 6)]
    theSets = [(s, extendedSet(s)) for s in l]
    count = 0
    for x in theSets:
        for y in theSets:
            if x != y:
                if checkSquares(x[1], y[1]):
                    count = count + 1
    return count

def euler102():
    l = [[(-340,495),(-153,-910),(835,-947)],
    [(-175,41),(-421,-714),(574,-645)],
    [(-547,712),(-352,579),(951,-786)],
    [(419,-864),(-83,650),(-399,171)],
    [(-429,-89),(-357,-930),(296,-29)],
    [(-734,-702),(823,-745),(-684,-62)],
    [(-971,762),(925,-776),(-663,-157)],
    [(162,570),(628,485),(-807,-896)],
    [(641,91),(-65,700),(887,759)],
    [(215,-496),(46,-931),(422,-30)],
    [(-119,359),(668,-609),(-358,-494)],
    [(440,929),(968,214),(760,-857)],
    [(-700,785),(838,29),(-216,411)],
    [(-770,-458),(-325,-53),(-505,633)],
    [(-752,-805),(349,776),(-799,687)],
    [(323,5),(561,-36),(919,-560)],
    [(-907,358),(264,320),(204,274)],
    [(-728,-466),(350,969),(292,-345)],
    [(940,836),(272,-533),(748,185)],
    [(411,998),(813,520),(316,-949)],
    [(-152,326),(658,-762),(148,-651)],
    [(330,507),(-9,-628),(101,174)],
    [(551,-496),(772,-541),(-702,-45)],
    [(-164,-489),(-90,322),(631,-59)],
    [(673,366),(-4,-143),(-606,-704)],
    [(428,-609),(801,-449),(740,-269)],
    [(453,-924),(-785,-346),(-853,111)],
    [(-738,555),(-181,467),(-426,-20)],
    [(958,-692),(784,-343),(505,-569)],
    [(620,27),(263,54),(-439,-726)],
    [(804,87),(998,859),(871,-78)],
    [(-119,-453),(-709,-292),(-115,-56)],
    [(-626,138),(-940,-476),(-177,-274)],
    [(-11,160),(142,588),(446,158)],
    [(538,727),(550,787),(330,810)],
    [(420,-689),(854,-546),(337,516)],
    [(872,-998),(-607,748),(473,-192)],
    [(653,440),(-516,-985),(808,-857)],
    [(374,-158),(331,-940),(-338,-641)],
    [(137,-925),(-179,771),(734,-715)],
    [(-314,198),(-115,29),(-641,-39)],
    [(759,-574),(-385,355),(590,-603)],
    [(-189,-63),(-168,204),(289,305)],
    [(-182,-524),(-715,-621),(911,-255)],
    [(331,-816),(-833,471),(168,126)],
    [(-514,581),(-855,-220),(-731,-507)],
    [(129,169),(576,651),(-87,-458)],
    [(783,-444),(-881,658),(-266,298)],
    [(603,-430),(-598,585),(368,899)],
    [(43,-724),(962,-376),(851,409)],
    [(-610,-646),(-883,-261),(-482,-881)],
    [(-117,-237),(978,641),(101,-747)],
    [(579,125),(-715,-712),(208,534)],
    [(672,-214),(-762,372),(874,533)],
    [(-564,965),(38,715),(367,242)],
    [(500,951),(-700,-981),(-61,-178)],
    [(-382,-224),(-959,903),(-282,-60)],
    [(-355,295),(426,-331),(-591,655)],
    [(892,128),(958,-271),(-993,274)],
    [(-454,-619),(302,138),(-790,-874)],
    [(-642,601),(-574,159),(-290,-318)],
    [(266,-109),(257,-686),(54,975)],
    [(162,628),(-478,840),(264,-266)],
    [(466,-280),(982,1),(904,-810)],
    [(721,839),(730,-807),(777,981)],
    [(-129,-430),(748,263),(943,96)],
    [(434,-94),(410,-990),(249,-704)],
    [(237,42),(122,-732),(44,-51)],
    [(909,-116),(-229,545),(292,717)],
    [(824,-768),(-807,-370),(-262,30)],
    [(675,58),(332,-890),(-651,791)],
    [(363,825),(-717,254),(684,240)],
    [(405,-715),(900,166),(-589,422)],
    [(-476,686),(-830,-319),(634,-807)],
    [(633,837),(-971,917),(-764,207)],
    [(-116,-44),(-193,-70),(908,809)],
    [(-26,-252),(998,408),(70,-713)],
    [(-601,645),(-462,842),(-644,-591)],
    [(-160,653),(274,113),(-138,687)],
    [(369,-273),(-181,925),(-167,-693)],
    [(-338,135),(480,-967),(-13,-840)],
    [(-90,-270),(-564,695),(161,907)],
    [(607,-430),(869,-713),(461,-469)],
    [(919,-165),(-776,522),(606,-708)],
    [(-203,465),(288,207),(-339,-458)],
    [(-453,-534),(-715,975),(838,-677)],
    [(-973,310),(-350,934),(546,-805)],
    [(-835,385),(708,-337),(-594,-772)],
    [(-14,914),(900,-495),(-627,594)],
    [(833,-713),(-213,578),(-296,699)],
    [(-27,-748),(484,455),(915,291)],
    [(270,889),(739,-57),(442,-516)],
    [(119,811),(-679,905),(184,130)],
    [(-678,-469),(925,553),(612,482)],
    [(101,-571),(-732,-842),(644,588)],
    [(-71,-737),(566,616),(957,-663)],
    [(-634,-356),(90,-207),(936,622)],
    [(598,443),(964,-895),(-58,529)],
    [(847,-467),(929,-742),(91,10)],
    [(-633,829),(-780,-408),(222,-30)],
    [(-818,57),(275,-38),(-746,198)],
    [(-722,-825),(-549,597),(-391,99)],
    [(-570,908),(430,873),(-103,-360)],
    [(342,-681),(512,434),(542,-528)],
    [(297,850),(479,609),(543,-357)],
    [(9,784),(212,548),(56,859)],
    [(-152,560),(-240,-969),(-18,713)],
    [(140,-133),(34,-635),(250,-163)],
    [(-272,-22),(-169,-662),(989,-604)],
    [(471,-765),(355,633),(-742,-118)],
    [(-118,146),(942,663),(547,-376)],
    [(583,16),(162,264),(715,-33)],
    [(-230,-446),(997,-838),(561,555)],
    [(372,397),(-729,-318),(-276,649)],
    [(92,982),(-970,-390),(-922,922)],
    [(-981,713),(-951,-337),(-669,670)],
    [(-999,846),(-831,-504),(7,-128)],
    [(455,-954),(-370,682),(-510,45)],
    [(822,-960),(-892,-385),(-662,314)],
    [(-668,-686),(-367,-246),(530,-341)],
    [(-723,-720),(-926,-836),(-142,757)],
    [(-509,-134),(384,-221),(-873,-639)],
    [(-803,-52),(-706,-669),(373,-339)],
    [(933,578),(631,-616),(770,555)],
    [(741,-564),(-33,-605),(-576,275)],
    [(-715,445),(-233,-730),(734,-704)],
    [(120,-10),(-266,-685),(-490,-17)],
    [(-232,-326),(-457,-946),(-457,-116)],
    [(811,52),(639,826),(-200,147)],
    [(-329,279),(293,612),(943,955)],
    [(-721,-894),(-393,-969),(-642,453)],
    [(-688,-826),(-352,-75),(371,79)],
    [(-809,-979),(407,497),(858,-248)],
    [(-485,-232),(-242,-582),(-81,849)],
    [(141,-106),(123,-152),(806,-596)],
    [(-428,57),(-992,811),(-192,478)],
    [(864,393),(122,858),(255,-876)],
    [(-284,-780),(240,457),(354,-107)],
    [(956,605),(-477,44),(26,-678)],
    [(86,710),(-533,-815),(439,327)],
    [(-906,-626),(-834,763),(426,-48)],
    [(201,-150),(-904,652),(475,412)],
    [(-247,149),(81,-199),(-531,-148)],
    [(923,-76),(-353,175),(-121,-223)],
    [(427,-674),(453,472),(-410,585)],
    [(931,776),(-33,85),(-962,-865)],
    [(-655,-908),(-902,208),(869,792)],
    [(-316,-102),(-45,-436),(-222,885)],
    [(-309,768),(-574,653),(745,-975)],
    [(896,27),(-226,993),(332,198)],
    [(323,655),(-89,260),(240,-902)],
    [(501,-763),(-424,793),(813,616)],
    [(993,375),(-938,-621),(672,-70)],
    [(-880,-466),(-283,770),(-824,143)],
    [(63,-283),(886,-142),(879,-116)],
    [(-964,-50),(-521,-42),(-306,-161)],
    [(724,-22),(866,-871),(933,-383)],
    [(-344,135),(282,966),(-80,917)],
    [(-281,-189),(420,810),(362,-582)],
    [(-515,455),(-588,814),(162,332)],
    [(555,-436),(-123,-210),(869,-943)],
    [(589,577),(232,286),(-554,876)],
    [(-773,127),(-58,-171),(-452,125)],
    [(-428,575),(906,-232),(-10,-224)],
    [(437,276),(-335,-348),(605,878)],
    [(-964,511),(-386,-407),(168,-220)],
    [(307,513),(912,-463),(-423,-416)],
    [(-445,539),(273,886),(-18,760)],
    [(-396,-585),(-670,414),(47,364)],
    [(143,-506),(754,906),(-971,-203)],
    [(-544,472),(-180,-541),(869,-465)],
    [(-779,-15),(-396,890),(972,-220)],
    [(-430,-564),(503,182),(-119,456)],
    [(89,-10),(-739,399),(506,499)],
    [(954,162),(-810,-973),(127,870)],
    [(890,952),(-225,158),(828,237)],
    [(-868,952),(349,465),(574,750)],
    [(-915,369),(-975,-596),(-395,-134)],
    [(-135,-601),(575,582),(-667,640)],
    [(413,890),(-560,-276),(-555,-562)],
    [(-633,-269),(561,-820),(-624,499)],
    [(371,-92),(-784,-593),(864,-717)],
    [(-971,655),(-439,367),(754,-951)],
    [(172,-347),(36,279),(-247,-402)],
    [(633,-301),(364,-349),(-683,-387)],
    [(-780,-211),(-713,-948),(-648,543)],
    [(72,58),(762,-465),(-66,462)],
    [(78,502),(781,-832),(713,836)],
    [(-431,-64),(-484,-392),(208,-343)],
    [(-64,101),(-29,-860),(-329,844)],
    [(398,391),(828,-858),(700,395)],
    [(578,-896),(-326,-604),(314,180)],
    [(97,-321),(-695,185),(-357,852)],
    [(854,839),(283,-375),(951,-209)],
    [(194,96),(-564,-847),(162,524)],
    [(-354,532),(494,621),(580,560)],
    [(419,-678),(-450,926),(-5,-924)],
    [(-661,905),(519,621),(-143,394)],
    [(-573,268),(296,-562),(-291,-319)],
    [(-211,266),(-196,158),(564,-183)],
    [(18,-585),(-398,777),(-581,864)],
    [(790,-894),(-745,-604),(-418,70)],
    [(848,-339),(150,773),(11,851)],
    [(-954,-809),(-53,-20),(-648,-304)],
    [(658,-336),(-658,-905),(853,407)],
    [(-365,-844),(350,-625),(852,-358)],
    [(986,-315),(-230,-159),(21,180)],
    [(-15,599),(45,-286),(-941,847)],
    [(-613,-68),(184,639),(-987,550)],
    [(334,675),(-56,-861),(923,340)],
    [(-848,-596),(960,231),(-28,-34)],
    [(707,-811),(-994,-356),(-167,-171)],
    [(-470,-764),(72,576),(-600,-204)],
    [(379,189),(-542,-576),(585,800)],
    [(440,540),(-445,-563),(379,-334)],
    [(-155,64),(514,-288),(853,106)],
    [(-304,751),(481,-520),(-708,-694)],
    [(-709,132),(594,126),(-844,63)],
    [(723,471),(421,-138),(-962,892)],
    [(-440,-263),(39,513),(-672,-954)],
    [(775,809),(-581,330),(752,-107)],
    [(-376,-158),(335,-708),(-514,578)],
    [(-343,-769),(456,-187),(25,413)],
    [(548,-877),(-172,300),(-500,928)],
    [(938,-102),(423,-488),(-378,-969)],
    [(-36,564),(-55,131),(958,-800)],
    [(-322,511),(-413,503),(700,-847)],
    [(-966,547),(-88,-17),(-359,-67)],
    [(637,-341),(-437,-181),(527,-153)],
    [(-74,449),(-28,3),(485,189)],
    [(-997,658),(-224,-948),(702,-807)],
    [(-224,736),(-896,127),(-945,-850)],
    [(-395,-106),(439,-553),(-128,124)],
    [(-841,-445),(-758,-572),(-489,212)],
    [(633,-327),(13,-512),(952,771)],
    [(-940,-171),(-6,-46),(-923,-425)],
    [(-142,-442),(-817,-998),(843,-695)],
    [(340,847),(-137,-920),(-988,-658)],
    [(-653,217),(-679,-257),(651,-719)],
    [(-294,365),(-41,342),(74,-892)],
    [(690,-236),(-541,494),(408,-516)],
    [(180,-807),(225,790),(494,59)],
    [(707,605),(-246,656),(284,271)],
    [(65,294),(152,824),(442,-442)],
    [(-321,781),(-540,341),(316,415)],
    [(420,371),(-2,545),(995,248)],
    [(56,-191),(-604,971),(615,449)],
    [(-981,-31),(510,592),(-390,-362)],
    [(-317,-968),(913,365),(97,508)],
    [(832,63),(-864,-510),(86,202)],
    [(-483,456),(-636,340),(-310,676)],
    [(981,-847),(751,-508),(-962,-31)],
    [(-157,99),(73,797),(63,-172)],
    [(220,858),(872,924),(866,-381)],
    [(996,-169),(805,321),(-164,971)],
    [(896,11),(-625,-973),(-782,76)],
    [(578,-280),(730,-729),(307,-905)],
    [(-580,-749),(719,-698),(967,603)],
    [(-821,874),(-103,-623),(662,-491)],
    [(-763,117),(661,-644),(672,-607)],
    [(592,787),(-798,-169),(-298,690)],
    [(296,644),(-526,-762),(-447,665)],
    [(534,-818),(852,-120),(57,-379)],
    [(-986,-549),(-329,294),(954,258)],
    [(-133,352),(-660,-77),(904,-356)],
    [(748,343),(215,500),(317,-277)],
    [(311,7),(910,-896),(-809,795)],
    [(763,-602),(-753,313),(-352,917)],
    [(668,619),(-474,-597),(-650,650)],
    [(-297,563),(-701,-987),(486,-902)],
    [(-461,-740),(-657,233),(-482,-328)],
    [(-446,-250),(-986,-458),(-629,520)],
    [(542,-49),(-327,-469),(257,-947)],
    [(121,-575),(-634,-143),(-184,521)],
    [(30,504),(455,-645),(-229,-945)],
    [(-12,-295),(377,764),(771,125)],
    [(-686,-133),(225,-25),(-376,-143)],
    [(-6,-46),(338,270),(-405,-872)],
    [(-623,-37),(582,467),(963,898)],
    [(-804,869),(-477,420),(-475,-303)],
    [(94,41),(-842,-193),(-768,720)],
    [(-656,-918),(415,645),(-357,460)],
    [(-47,-486),(-911,468),(-608,-686)],
    [(-158,251),(419,-394),(-655,-895)],
    [(272,-695),(979,508),(-358,959)],
    [(-776,650),(-918,-467),(-690,-534)],
    [(-85,-309),(-626,167),(-366,-429)],
    [(-880,-732),(-186,-924),(970,-875)],
    [(517,645),(-274,962),(-804,544)],
    [(721,402),(104,640),(478,-499)],
    [(198,684),(-134,-723),(-452,-905)],
    [(-245,745),(239,238),(-826,441)],
    [(-217,206),(-32,462),(-981,-895)],
    [(-51,989),(526,-173),(560,-676)],
    [(-480,-659),(-976,-580),(-727,466)],
    [(-996,-90),(-995,158),(-239,642)],
    [(302,288),(-194,-294),(17,924)],
    [(-943,969),(-326,114),(-500,103)],
    [(-619,163),(339,-880),(230,421)],
    [(-344,-601),(-795,557),(565,-779)],
    [(590,345),(-129,-202),(-125,-58)],
    [(-777,-195),(159,674),(775,411)],
    [(-939,312),(-665,810),(121,855)],
    [(-971,254),(712,815),(452,581)],
    [(442,-9),(327,-750),(61,757)],
    [(-342,869),(869,-160),(390,-772)],
    [(620,601),(565,-169),(-69,-183)],
    [(-25,924),(-817,964),(321,-970)],
    [(-64,-6),(-133,978),(825,-379)],
    [(601,436),(-24,98),(-115,940)],
    [(-97,502),(614,-574),(922,513)],
    [(-125,262),(-946,695),(99,-220)],
    [(429,-721),(719,-694),(197,-558)],
    [(326,689),(-70,-908),(-673,338)],
    [(-468,-856),(-902,-254),(-358,305)],
    [(-358,530),(542,355),(-253,-47)],
    [(-438,-74),(-362,963),(988,788)],
    [(137,717),(467,622),(319,-380)],
    [(-86,310),(-336,851),(918,-288)],
    [(721,395),(646,-53),(255,-425)],
    [(255,175),(912,84),(-209,878)],
    [(-632,-485),(-400,-357),(991,-608)],
    [(235,-559),(992,-297),(857,-591)],
    [(87,-71),(148,130),(647,578)],
    [(-290,-584),(-639,-788),(-21,592)],
    [(386,984),(625,-731),(-993,-336)],
    [(-538,634),(-209,-828),(-150,-774)],
    [(-754,-387),(607,-781),(976,-199)],
    [(412,-798),(-664,295),(709,-537)],
    [(-412,932),(-880,-232),(561,852)],
    [(-656,-358),(-198,-964),(-433,-848)],
    [(-762,-668),(-632,186),(-673,-11)],
    [(-876,237),(-282,-312),(-83,682)],
    [(403,73),(-57,-436),(-622,781)],
    [(-587,873),(798,976),(-39,329)],
    [(-369,-622),(553,-341),(817,794)],
    [(-108,-616),(920,-849),(-679,96)],
    [(290,-974),(234,239),(-284,-321)],
    [(-22,394),(-417,-419),(264,58)],
    [(-473,-551),(69,923),(591,-228)],
    [(-956,662),(-113,851),(-581,-794)],
    [(-258,-681),(413,-471),(-637,-817)],
    [(-866,926),(992,-653),(-7,794)],
    [(556,-350),(602,917),(831,-610)],
    [(188,245),(-906,361),(492,174)],
    [(-720,384),(-818,329),(638,-666)],
    [(-246,846),(890,-325),(-59,-850)],
    [(-118,-509),(620,-762),(-256,15)],
    [(-787,-536),(-452,-338),(-399,813)],
    [(458,560),(525,-311),(-608,-419)],
    [(494,-811),(-825,-127),(-812,894)],
    [(-801,890),(-629,-860),(574,925)],
    [(-709,-193),(-213,138),(-410,-403)],
    [(861,91),(708,-187),(5,-222)],
    [(789,646),(777,154),(90,-49)],
    [(-267,-830),(-114,531),(591,-698)],
    [(-126,-82),(881,-418),(82,652)],
    [(-894,130),(-726,-935),(393,-815)],
    [(-142,563),(654,638),(-712,-597)],
    [(-759,60),(-23,977),(100,-765)],
    [(-305,595),(-570,-809),(482,762)],
    [(-161,-267),(53,963),(998,-529)],
    [(-300,-57),(798,353),(703,486)],
    [(-990,696),(-764,699),(-565,719)],
    [(-232,-205),(566,571),(977,369)],
    [(740,865),(151,-817),(-204,-293)],
    [(94,445),(-768,229),(537,-406)],
    [(861,620),(37,-424),(-36,656)],
    [(390,-369),(952,733),(-464,569)],
    [(-482,-604),(959,554),(-705,-626)],
    [(-396,-615),(-991,108),(272,-723)],
    [(143,780),(535,142),(-917,-147)],
    [(138,-629),(-217,-908),(905,115)],
    [(915,103),(-852,64),(-468,-642)],
    [(570,734),(-785,-268),(-326,-759)],
    [(738,531),(-332,586),(-779,24)],
    [(870,440),(-217,473),(-383,415)],
    [(-296,-333),(-330,-142),(-924,950)],
    [(118,120),(-35,-245),(-211,-652)],
    [(61,634),(153,-243),(838,789)],
    [(726,-582),(210,105),(983,537)],
    [(-313,-323),(758,234),(29,848)],
    [(-847,-172),(-593,733),(-56,617)],
    [(54,255),(-512,156),(-575,675)],
    [(-873,-956),(-148,623),(95,200)],
    [(700,-370),(926,649),(-978,157)],
    [(-639,-202),(719,130),(747,222)],
    [(194,-33),(955,943),(505,114)],
    [(-226,-790),(28,-930),(827,783)],
    [(-392,-74),(-28,714),(218,-612)],
    [(209,626),(-888,-683),(-912,495)],
    [(487,751),(614,933),(631,445)],
    [(-348,-34),(-411,-106),(835,321)],
    [(-689,872),(-29,-800),(312,-542)],
    [(-52,566),(827,570),(-862,-77)],
    [(471,992),(309,-402),(389,912)],
    [(24,520),(-83,-51),(555,503)],
    [(-265,-317),(283,-970),(-472,690)],
    [(606,526),(137,71),(-651,150)],
    [(217,-518),(663,66),(-605,-331)],
    [(-562,232),(-76,-503),(205,-323)],
    [(842,-521),(546,285),(625,-186)],
    [(997,-927),(344,909),(-546,974)],
    [(-677,419),(81,121),(-705,771)],
    [(719,-379),(-944,-797),(784,-155)],
    [(-378,286),(-317,-797),(-111,964)],
    [(-288,-573),(784,80),(-532,-646)],
    [(-77,407),(-248,-797),(769,-816)],
    [(-24,-637),(287,-858),(-927,-333)],
    [(-902,37),(894,-823),(141,684)],
    [(125,467),(-177,-516),(686,399)],
    [(-321,-542),(641,-590),(527,-224)],
    [(-400,-712),(-876,-208),(632,-543)],
    [(-676,-429),(664,-242),(-269,922)],
    [(-608,-273),(-141,930),(687,380)],
    [(786,-12),(498,494),(310,326)],
    [(-739,-617),(606,-960),(804,188)],
    [(384,-368),(-243,-350),(-459,31)],
    [(-550,397),(320,-868),(328,-279)],
    [(969,-179),(853,864),(-110,514)],
    [(910,793),(302,-822),(-285,488)],
    [(-605,-128),(218,-283),(-17,-227)],
    [(16,324),(667,708),(750,3)],
    [(485,-813),(19,585),(71,930)],
    [(-218,816),(-687,-97),(-732,-360)],
    [(-497,-151),(376,-23),(3,315)],
    [(-412,-989),(-610,-813),(372,964)],
    [(-878,-280),(87,381),(-311,69)],
    [(-609,-90),(-731,-679),(150,585)],
    [(889,27),(-162,605),(75,-770)],
    [(448,617),(-988,0),(-103,-504)],
    [(-800,-537),(-69,627),(608,-668)],
    [(534,686),(-664,942),(830,920)],
    [(-238,775),(495,932),(-793,497)],
    [(-343,958),(-914,-514),(-691,651)],
    [(568,-136),(208,359),(728,28)],
    [(286,912),(-794,683),(556,-102)],
    [(-638,-629),(-484,445),(-64,-497)],
    [(58,505),(-801,-110),(872,632)],
    [(-390,777),(353,267),(976,369)],
    [(-993,515),(105,-133),(358,-572)],
    [(964,996),(355,-212),(-667,38)],
    [(-725,-614),(-35,365),(132,-196)],
    [(237,-536),(-416,-302),(312,477)],
    [(-664,574),(-210,224),(48,-925)],
    [(869,-261),(-256,-240),(-3,-698)],
    [(712,385),(32,-34),(916,-315)],
    [(895,-409),(-100,-346),(728,-624)],
    [(-806,327),(-450,889),(-781,-939)],
    [(-586,-403),(698,318),(-939,899)],
    [(557,-57),(-920,659),(333,-51)],
    [(-441,232),(-918,-205),(246,1)],
    [(783,167),(-797,-595),(245,-736)],
    [(-36,-531),(-486,-426),(-813,-160)],
    [(777,-843),(817,313),(-228,-572)],
    [(735,866),(-309,-564),(-81,190)],
    [(-413,645),(101,719),(-719,218)],
    [(-83,164),(767,796),(-430,-459)],
    [(122,779),(-15,-295),(-96,-892)],
    [(462,379),(70,548),(834,-312)],
    [(-630,-534),(124,187),(-737,114)],
    [(-299,-604),(318,-591),(936,826)],
    [(-879,218),(-642,-483),(-318,-866)],
    [(-691,62),(-658,761),(-895,-854)],
    [(-822,493),(687,569),(910,-202)],
    [(-223,784),(304,-5),(541,925)],
    [(-914,541),(737,-662),(-662,-195)],
    [(-622,615),(414,358),(881,-878)],
    [(339,745),(-268,-968),(-280,-227)],
    [(-364,855),(148,-709),(-827,472)],
    [(-890,-532),(-41,664),(-612,577)],
    [(-702,-859),(971,-722),(-660,-920)],
    [(-539,-605),(737,149),(973,-802)],
    [(800,42),(-448,-811),(152,511)],
    [(-933,377),(-110,-105),(-374,-937)],
    [(-766,152),(482,120),(-308,390)],
    [(-568,775),(-292,899),(732,890)],
    [(-177,-317),(-502,-259),(328,-511)],
    [(612,-696),(-574,-660),(132,31)],
    [(-119,563),(-805,-864),(179,-672)],
    [(425,-627),(183,-331),(839,318)],
    [(-711,-976),(-749,152),(-916,261)],
    [(181,-63),(497,211),(262,406)],
    [(-537,700),(-859,-765),(-928,77)],
    [(892,832),(231,-749),(-82,613)],
    [(816,216),(-642,-216),(-669,-912)],
    [(-6,624),(-937,-370),(-344,268)],
    [(737,-710),(-869,983),(-324,-274)],
    [(565,952),(-547,-158),(374,-444)],
    [(51,-683),(645,-845),(515,636)],
    [(-953,-631),(114,-377),(-764,-144)],
    [(-8,470),(-242,-399),(-675,-730)],
    [(-540,689),(-20,47),(-607,590)],
    [(-329,-710),(-779,942),(-388,979)],
    [(123,829),(674,122),(203,563)],
    [(46,782),(396,-33),(386,610)],
    [(872,-846),(-523,-122),(-55,-190)],
    [(388,-994),(-525,974),(127,596)],
    [(781,-680),(796,-34),(-959,-62)],
    [(-749,173),(200,-384),(-745,-446)],
    [(379,618),(136,-250),(-224,970)],
    [(-58,240),(-921,-760),(-901,-626)],
    [(366,-185),(565,-100),(515,688)],
    [(489,999),(-893,-263),(-637,816)],
    [(838,-496),(-316,-513),(419,479)],
    [(107,676),(-15,882),(98,-397)],
    [(-999,941),(-903,-424),(670,-325)],
    [(171,-979),(835,178),(169,-984)],
    [(-609,-607),(378,-681),(184,402)],
    [(-316,903),(-575,-800),(224,983)],
    [(591,-18),(-460,551),(-167,918)],
    [(-756,405),(-117,441),(163,-320)],
    [(456,24),(6,881),(-836,-539)],
    [(-489,-585),(915,651),(-892,-382)],
    [(-177,-122),(73,-711),(-386,591)],
    [(181,724),(530,686),(-131,241)],
    [(737,288),(886,216),(233,33)],
    [(-548,-386),(-749,-153),(-85,-982)],
    [(-835,227),(904,160),(-99,25)],
    [(-9,-42),(-162,728),(840,-963)],
    [(217,-763),(870,771),(47,-846)],
    [(-595,808),(-491,556),(337,-900)],
    [(-134,281),(-724,441),(-134,708)],
    [(-789,-508),(651,-962),(661,315)],
    [(-839,-923),(339,402),(41,-487)],
    [(300,-790),(48,703),(-398,-811)],
    [(955,-51),(462,-685),(960,-717)],
    [(910,-880),(592,-255),(-51,-776)],
    [(-885,169),(-793,368),(-565,458)],
    [(-905,940),(-492,-630),(-535,-988)],
    [(245,797),(763,869),(-82,550)],
    [(-310,38),(-933,-367),(-650,824)],
    [(-95,32),(-83,337),(226,990)],
    [(-218,-975),(-191,-208),(-785,-293)],
    [(-672,-953),(517,-901),(-247,465)],
    [(681,-148),(261,-857),(544,-923)],
    [(640,341),(446,-618),(195,769)],
    [(384,398),(-846,365),(671,815)],
    [(578,576),(-911,907),(762,-859)],
    [(548,-428),(144,-630),(-759,-146)],
    [(710,-73),(-700,983),(-97,-889)],
    [(-46,898),(-973,-362),(-817,-717)],
    [(151,-81),(-125,-900),(-478,-154)],
    [(483,615),(-537,-932),(181,-68)],
    [(786,-223),(518,25),(-306,-12)],
    [(-422,268),(-809,-683),(635,468)],
    [(983,-734),(-694,-608),(-110,4)],
    [(-786,-196),(749,-354),(137,-8)],
    [(-181,36),(668,-200),(691,-973)],
    [(-629,-838),(692,-736),(437,-871)],
    [(-208,-536),(-159,-596),(8,197)],
    [(-3,370),(-686,170),(913,-376)],
    [(44,-998),(-149,-993),(-200,512)],
    [(-519,136),(859,497),(536,434)],
    [(77,-985),(972,-340),(-705,-837)],
    [(-381,947),(250,360),(344,322)],
    [(-26,131),(699,750),(707,384)],
    [(-914,655),(299,193),(406,955)],
    [(-883,-921),(220,595),(-546,794)],
    [(-599,577),(-569,-404),(-704,489)],
    [(-594,-963),(-624,-460),(880,-760)],
    [(-603,88),(-99,681),(55,-328)],
    [(976,472),(139,-453),(-531,-860)],
    [(192,-290),(513,-89),(666,432)],
    [(417,487),(575,293),(567,-668)],
    [(655,711),(-162,449),(-980,972)],
    [(-505,664),(-685,-239),(603,-592)],
    [(-625,-802),(-67,996),(384,-636)],
    [(365,-593),(522,-666),(-200,-431)],
    [(-868,708),(560,-860),(-630,-355)],
    [(-702,785),(-637,-611),(-597,960)],
    [(-137,-696),(-93,-803),(408,406)],
    [(891,-123),(-26,-609),(-610,518)],
    [(133,-832),(-198,555),(708,-110)],
    [(791,617),(-69,487),(696,315)],
    [(-900,694),(-565,517),(-269,-416)],
    [(914,135),(-781,600),(-71,-600)],
    [(991,-915),(-422,-351),(-837,313)],
    [(-840,-398),(-302,21),(590,146)],
    [(62,-558),(-702,-384),(-625,831)],
    [(-363,-426),(-924,-496),(792,-908)],
    [(73,361),(-817,-466),(400,922)],
    [(-626,-164),(-626,860),(-524,286)],
    [(255,26),(-944,809),(-606,986)],
    [(-457,-256),(-103,50),(-867,-871)],
    [(-223,803),(196,480),(612,136)],
    [(-820,-928),(700,780),(-977,721)],
    [(717,332),(53,-933),(-128,793)],
    [(-602,-648),(562,593),(890,702)],
    [(-469,-875),(-527,911),(-475,-222)],
    [(110,-281),(-552,-536),(-816,596)],
    [(-981,654),(413,-981),(-75,-95)],
    [(-754,-742),(-515,894),(-220,-344)],
    [(795,-52),(156,408),(-603,76)],
    [(474,-157),(423,-499),(-807,-791)],
    [(260,688),(40,-52),(702,-122)],
    [(-584,-517),(-390,-881),(302,-504)],
    [(61,797),(665,708),(14,668)],
    [(366,166),(458,-614),(564,-983)],
    [(72,539),(-378,796),(381,-824)],
    [(-485,201),(-588,842),(736,379)],
    [(-149,-894),(-298,705),(-303,-406)],
    [(660,-935),(-580,521),(93,633)],
    [(-382,-282),(-375,-841),(-828,171)],
    [(-567,743),(-100,43),(144,122)],
    [(-281,-786),(-749,-551),(296,304)],
    [(11,-426),(-792,212),(857,-175)],
    [(594,143),(-699,289),(315,137)],
    [(341,596),(-390,107),(-631,-804)],
    [(-751,-636),(-424,-854),(193,651)],
    [(-145,384),(749,675),(-786,517)],
    [(224,-865),(-323,96),(-916,258)],
    [(-309,403),(-388,826),(35,-270)],
    [(-942,709),(222,158),(-699,-103)],
    [(-589,842),(-997,29),(-195,-210)],
    [(264,426),(566,145),(-217,623)],
    [(217,965),(507,-601),(-453,507)],
    [(-206,307),(-982,4),(64,-292)],
    [(676,-49),(-38,-701),(550,883)],
    [(5,-850),(-438,659),(745,-773)],
    [(933,238),(-574,-570),(91,-33)],
    [(-866,121),(-928,358),(459,-843)],
    [(-568,-631),(-352,-580),(-349,189)],
    [(-737,849),(-963,-486),(-662,970)],
    [(135,334),(-967,-71),(-365,-792)],
    [(789,21),(-227,51),(990,-275)],
    [(240,412),(-886,230),(591,256)],
    [(-609,472),(-853,-754),(959,661)],
    [(401,521),(521,314),(929,982)],
    [(-499,784),(-208,71),(-302,296)],
    [(-557,-948),(-553,-526),(-864,793)],
    [(270,-626),(828,44),(37,14)],
    [(-412,224),(617,-593),(502,699)],
    [(41,-908),(81,562),(-849,163)],
    [(165,917),(761,-197),(331,-341)],
    [(-687,314),(799,755),(-969,648)],
    [(-164,25),(578,439),(-334,-576)],
    [(213,535),(874,-177),(-551,24)],
    [(-689,291),(-795,-225),(-496,-125)],
    [(465,461),(558,-118),(-568,-909)],
    [(567,660),(-810,46),(-485,878)],
    [(-147,606),(685,-690),(-774,984)],
    [(568,-886),(-43,854),(-738,616)],
    [(-800,386),(-614,585),(764,-226)],
    [(-518,23),(-225,-732),(-79,440)],
    [(-173,-291),(-689,636),(642,-447)],
    [(-598,-16),(227,410),(496,211)],
    [(-474,-930),(-656,-321),(-420,36)],
    [(-435,165),(-819,555),(540,144)],
    [(-969,149),(828,568),(394,648)],
    [(65,-848),(257,720),(-625,-851)],
    [(981,899),(275,635),(465,-877)],
    [(80,290),(792,760),(-191,-321)],
    [(-605,-858),(594,33),(706,593)],
    [(585,-472),(318,-35),(354,-927)],
    [(-365,664),(803,581),(-965,-814)],
    [(-427,-238),(-480,146),(-55,-606)],
    [(879,-193),(250,-890),(336,117)],
    [(-226,-322),(-286,-765),(-836,-218)],
    [(-913,564),(-667,-698),(937,283)],
    [(872,-901),(810,-623),(-52,-709)],
    [(473,171),(717,38),(-429,-644)],
    [(225,824),(-219,-475),(-180,234)],
    [(-530,-797),(-948,238),(851,-623)],
    [(85,975),(-363,529),(598,28)],
    [(-799,166),(-804,210),(-769,851)],
    [(-687,-158),(885,736),(-381,-461)],
    [(447,592),(928,-514),(-515,-661)],
    [(-399,-777),(-493,80),(-544,-78)],
    [(-884,631),(171,-825),(-333,551)],
    [(191,268),(-577,676),(137,-33)],
    [(212,-853),(709,798),(583,-56)],
    [(-908,-172),(-540,-84),(-135,-56)],
    [(303,311),(406,-360),(-240,811)],
    [(798,-708),(824,59),(234,-57)],
    [(491,693),(-74,585),(-85,877)],
    [(509,-65),(-936,329),(-51,722)],
    [(-122,858),(-52,467),(-77,-609)],
    [(850,760),(547,-495),(-953,-952)],
    [(-460,-541),(890,910),(286,724)],
    [(-914,843),(-579,-983),(-387,-460)],
    [(989,-171),(-877,-326),(-899,458)],
    [(846,175),(-915,540),(-1000,-982)],
    [(-852,-920),(-306,496),(530,-18)],
    [(338,-991),(160,85),(-455,-661)],
    [(-186,-311),(-460,-563),(-231,-414)],
    [(-932,-302),(959,597),(793,748)],
    [(-366,-402),(-788,-279),(514,53)],
    [(-940,-956),(447,-956),(211,-285)],
    [(564,806),(-911,-914),(934,754)],
    [(575,-858),(-277,15),(409,-714)],
    [(848,462),(100,-381),(135,242)],
    [(330,718),(-24,-190),(860,-78)],
    [(479,458),(941,108),(-866,-653)],
    [(212,980),(962,-962),(115,841)],
    [(-827,-474),(-206,881),(323,765)],
    [(506,-45),(-30,-293),(524,-133)],
    [(832,-173),(547,-852),(-561,-842)],
    [(-397,-661),(-708,819),(-545,-228)],
    [(521,51),(-489,852),(36,-258)],
    [(227,-164),(189,465),(-987,-882)],
    [(-73,-997),(641,-995),(449,-615)],
    [(151,-995),(-638,415),(257,-400)],
    [(-663,-297),(-748,537),(-734,198)],
    [(-585,-401),(-81,-782),(-80,-105)],
    [(99,-21),(238,-365),(-704,-368)],
    [(45,416),(849,-211),(-371,-1)],
    [(-404,-443),(795,-406),(36,-933)],
    [(272,-363),(981,-491),(-380,77)],
    [(713,-342),(-366,-849),(643,911)],
    [(-748,671),(-537,813),(961,-200)],
    [(-194,-909),(703,-662),(-601,188)],
    [(281,500),(724,286),(267,197)],
    [(-832,847),(-595,820),(-316,637)],
    [(520,521),(-54,261),(923,-10)],
    [(4,-808),(-682,-258),(441,-695)],
    [(-793,-107),(-969,905),(798,446)],
    [(-108,-739),(-590,69),(-855,-365)],
    [(380,-623),(-930,817),(468,713)],
    [(759,-849),(-236,433),(-723,-931)],
    [(95,-320),(-686,124),(-69,-329)],
    [(-655,518),(-210,-523),(284,-866)],
    [(144,303),(639,70),(-171,269)],
    [(173,-333),(947,-304),(55,40)],
    [(274,878),(-482,-888),(-835,375)],
    [(-982,-854),(-36,-218),(-114,-230)],
    [(905,-979),(488,-485),(-479,114)],
    [(877,-157),(553,-530),(-47,-321)],
    [(350,664),(-881,442),(-220,-284)],
    [(434,-423),(-365,878),(-726,584)],
    [(535,909),(-517,-447),(-660,-141)],
    [(-966,191),(50,353),(182,-642)],
    [(-785,-634),(123,-907),(-162,511)],
    [(146,-850),(-214,814),(-704,25)],
    [(692,1),(521,492),(-637,274)],
    [(-662,-372),(-313,597),(983,-647)],
    [(-962,-526),(68,-549),(-819,231)],
    [(740,-890),(-318,797),(-666,948)],
    [(-190,-12),(-468,-455),(948,284)],
    [(16,478),(-506,-888),(628,-154)],
    [(272,630),(-976,308),(433,3)],
    [(-169,-391),(-132,189),(302,-388)],
    [(109,-784),(474,-167),(-265,-31)],
    [(-177,-532),(283,464),(421,-73)],
    [(650,635),(592,-138),(1,-387)],
    [(-932,703),(-827,-492),(-355,686)],
    [(586,-311),(340,-618),(645,-434)],
    [(-951,736),(647,-127),(-303,590)],
    [(188,444),(903,718),(-931,500)],
    [(-872,-642),(-296,-571),(337,241)],
    [(23,65),(152,125),(880,470)],
    [(512,823),(-42,217),(823,-263)],
    [(180,-831),(-380,886),(607,762)],
    [(722,443),(-149,-216),(-115,759)],
    [(-19,660),(-36,901),(923,231)],
    [(562,-322),(-626,-968),(194,-825)],
    [(204,-920),(938,784),(362,150)],
    [(-410,-266),(-715,559),(-672,124)],
    [(-198,446),(-140,454),(-461,-447)],
    [(83,-346),(830,-493),(-759,-382)],
    [(-881,601),(581,234),(-134,-925)],
    [(-494,914),(-42,899),(235,629)],
    [(-390,50),(956,437),(774,-700)],
    [(-514,514),(44,-512),(-576,-313)],
    [(63,-688),(808,-534),(-570,-399)],
    [(-726,572),(-896,102),(-294,-28)],
    [(-688,757),(401,406),(955,-511)],
    [(-283,423),(-485,480),(-767,908)],
    [(-541,952),(-594,116),(-854,451)],
    [(-273,-796),(236,625),(-626,257)],
    [(-407,-493),(373,826),(-309,297)],
    [(-750,955),(-476,641),(-809,713)],
    [(8,415),(695,226),(-111,2)],
    [(733,209),(152,-920),(401,995)],
    [(921,-103),(-919,66),(871,-947)],
    [(-907,89),(-869,-214),(851,-559)],
    [(-307,748),(524,-755),(314,-711)],
    [(188,897),(-72,-763),(482,103)],
    [(545,-821),(-232,-596),(-334,-754)],
    [(-217,-788),(-820,388),(-200,-662)],
    [(779,160),(-723,-975),(-142,-998)],
    [(-978,-519),(-78,-981),(842,904)],
    [(-504,-736),(-295,21),(-472,-482)],
    [(391,115),(-705,574),(652,-446)],
    [(813,-988),(865,830),(-263,487)],
    [(194,80),(774,-493),(-761,-872)],
    [(-415,-284),(-803,7),(-810,670)],
    [(-484,-4),(881,-872),(55,-852)],
    [(-379,822),(-266,324),(-48,748)],
    [(-304,-278),(406,-60),(959,-89)],
    [(404,756),(577,-643),(-332,658)],
    [(291,460),(125,491),(-312,83)],
    [(311,-734),(-141,582),(282,-557)],
    [(-450,-661),(-981,710),(-177,794)],
    [(328,264),(-787,971),(-743,-407)],
    [(-622,518),(993,-241),(-738,229)],
    [(273,-826),(-254,-917),(-710,-111)],
    [(809,770),(96,368),(-818,725)],
    [(-488,773),(502,-342),(534,745)],
    [(-28,-414),(236,-315),(-484,363)],
    [(179,-466),(-566,713),(-683,56)],
    [(560,-240),(-597,619),(916,-940)],
    [(893,473),(872,-868),(-642,-461)],
    [(799,489),(383,-321),(-776,-833)],
    [(980,490),(-508,764),(-512,-426)],
    [(917,961),(-16,-675),(440,559)],
    [(-812,212),(784,-987),(-132,554)],
    [(-886,454),(747,806),(190,231)],
    [(910,341),(21,-66),(708,725)],
    [(29,929),(-831,-494),(-303,389)],
    [(-103,492),(-271,-174),(-515,529)],
    [(-292,119),(419,788),(247,-951)],
    [(483,543),(-347,-673),(664,-549)],
    [(-926,-871),(-437,337),(162,-877)],
    [(299,472),(-771,5),(-88,-643)],
    [(-103,525),(-725,-998),(264,22)],
    [(-505,708),(550,-545),(823,347)],
    [(-738,931),(59,147),(-156,-259)],
    [(456,968),(-162,889),(132,-911)],
    [(535,120),(968,-517),(-864,-541)],
    [(24,-395),(-593,-766),(-565,-332)],
    [(834,611),(825,-576),(280,629)],
    [(211,-548),(140,-278),(-592,929)],
    [(-999,-240),(-63,-78),(793,573)],
    [(-573,160),(450,987),(529,322)],
    [(63,353),(315,-187),(-461,577)],
    [(189,-950),(-247,656),(289,241)],
    [(209,-297),(397,664),(-805,484)],
    [(-655,452),(435,-556),(917,874)],
    [(253,-756),(262,-888),(-778,-214)],
    [(793,-451),(323,-251),(-401,-458)],
    [(-396,619),(-651,-287),(-668,-781)],
    [(698,720),(-349,742),(-807,546)],
    [(738,280),(680,279),(-540,858)],
    [(-789,387),(530,-36),(-551,-491)],
    [(162,579),(-427,-272),(228,710)],
    [(689,356),(917,-580),(729,217)],
    [(-115,-638),(866,424),(-82,-194)],
    [(411,-338),(-917,172),(227,-29)],
    [(-612,63),(630,-976),(-64,-204)],
    [(-200,911),(583,-571),(682,-579)],
    [(91,298),(396,-183),(788,-955)],
    [(141,-873),(-277,149),(-396,916)],
    [(321,958),(-136,573),(541,-777)],
    [(797,-909),(-469,-877),(988,-653)],
    [(784,-198),(129,883),(-203,399)],
    [(-68,-810),(223,-423),(-467,-512)],
    [(531,-445),(-603,-997),(-841,641)],
    [(-274,-242),(174,261),(-636,-158)],
    [(-574,494),(-796,-798),(-798,99)],
    [(95,-82),(-613,-954),(-753,986)],
    [(-883,-448),(-864,-401),(938,-392)],
    [(913,930),(-542,-988),(310,410)],
    [(506,-99),(43,512),(790,-222)],
    [(724,31),(49,-950),(260,-134)],
    [(-287,-947),(-234,-700),(56,588)],
    [(-33,782),(-144,948),(105,-791)],
    [(548,-546),(-652,-293),(881,-520)],
    [(691,-91),(76,991),(-631,742)],
    [(-520,-429),(-244,-296),(724,-48)],
    [(778,646),(377,50),(-188,56)],
    [(-895,-507),(-898,-165),(-674,652)],
    [(654,584),(-634,177),(-349,-620)],
    [(114,-980),(355,62),(182,975)],
    [(516,9),(-442,-298),(274,-579)],
    [(-238,262),(-431,-896),(506,-850)],
    [(47,748),(846,821),(-537,-293)],
    [(839,726),(593,285),(-297,840)],
    [(634,-486),(468,-304),(-887,-567)],
    [(-864,914),(296,-124),(335,233)],
    [(88,-253),(-523,-956),(-554,803)],
    [(-587,417),(281,-62),(-409,-363)],
    [(-136,-39),(-292,-768),(-264,876)],
    [(-127,506),(-891,-331),(-744,-430)],
    [(778,584),(-750,-129),(-479,-94)],
    [(-876,-771),(-987,-757),(180,-641)],
    [(-777,-694),(411,-87),(329,190)],
    [(-347,-999),(-882,158),(-754,232)],
    [(-105,918),(188,237),(-110,-591)],
    [(-209,703),(-838,77),(838,909)],
    [(-995,-339),(-762,750),(860,472)],
    [(185,271),(-289,173),(811,-300)],
    [(2,65),(-656,-22),(36,-139)],
    [(765,-210),(883,974),(961,-905)],
    [(-212,295),(-615,-840),(77,474)],
    [(211,-910),(-440,703),(-11,859)],
    [(-559,-4),(-196,841),(-277,969)],
    [(-73,-159),(-887,126),(978,-371)],
    [(-569,633),(-423,-33),(512,-393)],
    [(503,143),(-383,-109),(-649,-998)],
    [(-663,339),(-317,-523),(-2,596)],
    [(690,-380),(570,378),(-652,132)],
    [(72,-744),(-930,399),(-525,935)],
    [(865,-983),(115,37),(995,826)],
    [(594,-621),(-872,443),(188,-241)],
    [(-1000,291),(754,234),(-435,-869)],
    [(-868,901),(654,-907),(59,181)],
    [(-868,-793),(-431,596),(-446,-564)],
    [(900,-944),(-680,-796),(902,-366)],
    [(331,430),(943,853),(-851,-942)],
    [(315,-538),(-354,-909),(139,721)],
    [(170,-884),(-225,-818),(-808,-657)],
    [(-279,-34),(-533,-871),(-972,552)],
    [(691,-986),(-800,-950),(654,-747)],
    [(603,988),(899,841),(-630,591)],
    [(876,-949),(809,562),(602,-536)],
    [(-693,363),(-189,495),(738,-1000)],
    [(-383,431),(-633,297),(665,959)],
    [(-740,686),(-207,-803),(188,-520)],
    [(-820,226),(31,-339),(10,121)],
    [(-312,-844),(624,-516),(483,621)],
    [(-822,-529),(69,-278),(800,328)],
    [(834,-82),(-759,420),(811,-264)],
    [(-960,-240),(-921,561),(173,46)],
    [(-324,909),(-790,-814),(-2,-785)],
    [(976,334),(-290,-891),(704,-581)],
    [(150,-798),(689,-823),(237,-639)],
    [(-551,-320),(876,-502),(-622,-628)],
    [(-136,845),(904,595),(-702,-261)],
    [(-857,-377),(-522,-101),(-943,-805)],
    [(-682,-787),(-888,-459),(-752,-985)],
    [(-571,-81),(623,-133),(447,643)],
    [(-375,-158),(72,-387),(-324,-696)],
    [(-660,-650),(340,188),(569,526)],
    [(727,-218),(16,-7),(-595,-988)],
    [(-966,-684),(802,-783),(-272,-194)],
    [(115,-566),(-888,47),(712,180)],
    [(-237,-69),(45,-272),(981,-812)],
    [(48,897),(439,417),(50,325)],
    [(348,616),(180,254),(104,-784)],
    [(-730,811),(-548,612),(-736,790)],
    [(138,-810),(123,930),(65,865)],
    [(-768,-299),(-49,-895),(-692,-418)],
    [(487,-531),(802,-159),(-12,634)],
    [(808,-179),(552,-73),(470,717)],
    [(720,-644),(886,-141),(625,144)],
    [(-485,-505),(-347,-244),(-916,66)],
    [(600,-565),(995,-5),(324,227)],
    [(-771,-35),(904,-482),(753,-303)],
    [(-701,65),(426,-763),(-504,-479)],
    [(409,733),(-823,475),(64,718)],
    [(865,975),(368,893),(-413,-433)],
    [(812,-597),(-970,819),(813,624)],
    [(193,-642),(-381,-560),(545,398)],
    [(711,28),(-316,771),(717,-865)],
    [(-509,462),(809,-136),(786,635)],
    [(618,-49),(484,169),(635,547)],
    [(-747,685),(-882,-496),(-332,82)],
    [(-501,-851),(870,563),(290,570)],
    [(-279,-829),(-509,397),(457,816)],
    [(-508,80),(850,-188),(483,-326)],
    [(860,-100),(360,119),(-205,787)],
    [(-870,21),(-39,-827),(-185,932)],
    [(826,284),(-136,-866),(-330,-97)],
    [(-944,-82),(745,899),(-97,365)],
    [(929,262),(564,632),(-115,632)],
    [(244,-276),(713,330),(-897,-214)],
    [(-890,-109),(664,876),(-974,-907)],
    [(716,249),(816,489),(723,141)],
    [(-96,-560),(-272,45),(-70,645)],
    [(762,-503),(414,-828),(-254,-646)],
    [(909,-13),(903,-422),(-344,-10)],
    [(658,-486),(743,545),(50,674)],
    [(-241,507),(-367,18),(-48,-241)],
    [(886,-268),(884,-762),(120,-486)],
    [(-412,-528),(879,-647),(223,-393)],
    [(851,810),(234,937),(-726,797)],
    [(-999,942),(839,-134),(-996,-189)],
    [(100,979),(-527,-521),(378,800)],
    [(544,-844),(-832,-530),(-77,-641)],
    [(43,889),(31,442),(-934,-503)],
    [(-330,-370),(-309,-439),(173,547)],
    [(169,945),(62,-753),(-542,-597)],
    [(208,751),(-372,-647),(-520,70)],
    [(765,-840),(907,-257),(379,918)],
    [(334,-135),(-689,730),(-427,618)],
    [(137,-508),(66,-695),(78,169)],
    [(-962,-123),(400,-417),(151,969)],
    [(328,689),(666,427),(-555,-642)],
    [(-907,343),(605,-341),(-647,582)],
    [(-667,-363),(-571,818),(-265,-399)],
    [(525,-938),(904,898),(725,692)],
    [(-176,-802),(-858,-9),(780,275)],
    [(580,170),(-740,287),(691,-97)],
    [(365,557),(-375,361),(-288,859)],
    [(193,737),(842,-808),(520,282)],
    [(-871,65),(-799,836),(179,-720)],
    [(958,-144),(744,-789),(797,-48)],
    [(122,582),(662,912),(68,757)],
    [(595,241),(-801,513),(388,186)],
    [(-103,-677),(-259,-731),(-281,-857)],
    [(921,319),(-696,683),(-88,-997)],
    [(775,200),(78,858),(648,768)],
    [(316,821),(-763,68),(-290,-741)],
    [(564,664),(691,504),(760,787)],
    [(694,-119),(973,-385),(309,-760)],
    [(777,-947),(-57,990),(74,19)],
    [(971,626),(-496,-781),(-602,-239)],
    [(-651,433),(11,-339),(939,294)],
    [(-965,-728),(560,569),(-708,-247)]]

    count = 0
    for x in l:
        p1 = x[0]
        p2 = x[1]
        p3 = x[2]

        hasSlope1 = True
        hasSlope2 = True
        hasSlope3 = True
        #note that when it doesn't have slope, it can't have y int
        if p1[0] == p2[0]:
            hasSlope1 = False
        if p2[0] == p3[0]:
            hasSlope2 = False
        if p3[0] == p1[0]:
            hasSlope3 = False

        slope1 = -1
        slope2 = -1
        slope3 = -1
        yint1 = -1
        yint2 = -1
        yint3 = -1


        if hasSlope1:
            slope1 = float((p1[1] - p2[1])/(p1[0] - p2[0]))
            yint1 = p1[1] - slope1*p1[0]

        if hasSlope2:
            slope2 = float((p2[1] - p3[1])/(p2[0] - p3[0]))
            yint2 = p2[1] - slope2*p2[0]

        if hasSlope3:
            slope3 = float((p3[1] - p1[1])/(p3[0] - p1[0]))
            yint3 = p3[1] - slope3*p3[0]

        a = (p3[1] >= (p3[0]*slope1 + yint1))
        b = (p1[1] >= (p1[0]*slope2 + yint2))
        c = (p2[1] >= (p2[0]*slope3 + yint3))

        if not hasSlope1:
            a = p3[0] <= p1[0]
        if not hasSlope2:
            b = p1[0] <= p2[0]
        if not hasSlope3:
            a = p2[0] <= p3[0]

        a0 = (0 >= (0*slope1 + yint1))
        b0 = (0 >= (0*slope2 + yint2))
        c0 = (0 >= (0*slope3 + yint3))

        if not hasSlope1:
            a0 = 0 <= p1[0]
        if not hasSlope2:
            b0 = 0 <= p2[0]
        if not hasSlope3:
            c0 = 0 <= p3[0]

        if a0 == a and b0 == b and c0 == c:
            count = count + 1
    return count

def isDigPerm(a,b):
    l1 = [int(i) for i in str(a)]
    l2 = [int(i) for i in str(b)]
    l1.sort()
    l2.sort()
    return l1 == l2

def phi(n, primes):
    if n in primes:
        return n-1
    factors = getPrimeFactors(n, primes)
    for x in factors:
        n = (n*(x-1))/x
    return n

def isTotientPerm(n, primes):
    curr = phi(n, primes)
    return isDigPerm(n, curr)


def euler72():
    curr = 0
    primes = sieveOfE(1000000)
    for x in range(2, 1000001):
        curr = curr + phi(x, primes)
        print x
    return curr

def euler73():
    count = 0
    for x in range(1,12001):
        for y in range(int(x/3) + 1, int(x/2) + 1):
            if float(y)/x > 1.0/3 and float(y)/x < 1.0/2:
                if fractions.gcd(x,y) == 1:
                    count = count + 1
        print x
    return count

def euler77(n):
    l = sieveOfE(n)
    l1 = [x for x in l if x < n]
    return numPrimeSums(n, l1, 0)

def numPrimeSums(n, l, ind):
    if n == 0:
        return 1
    elif ind > len(l) - 1 and n != 0:
        return 0
    else:
        divs = int(n/l[ind])
        currSum = 0

        #if ind == 2 and n == 7:
            #print "found"
            #print divs

        for x in range(0, divs + 1):
            #print (n - x*l[ind], l, ind + 1, seq + [(x,l[ind])])
            currSum = currSum + numPrimeSums(n - x*l[ind], l, ind + 1)
        return currSum

def euler75():
    squares = [x**2 for x in range(1, 1500000)]
    impCount = 0
    for n in range(1, 1500000):
        count = 0
        impSquares = [x for x in squares if x < n]
        for x in range(0, len(impSquares)):
            for y in range(0,len(impSquares)):
                if squares[x] + squares[y] in squares:
                    z = int(math.sqrt( squares[x] + squares[y] ))
                    if (x + 1) + (y + 1) + z == n:
                        count = count + 1
        if count == 2:
            impCount = impCount + 1
        print n
    return impCount

def euler87():
    l0 = sieveOfE(7100)
    l1 = sieveOfE(400)
    l2 = sieveOfE(100)
    squares = [x**2 for x in l0]
    cubes = [x**3 for x in l1]
    quads = [x**4 for x in l2]

    nums = set([x + y + z for x in squares for y in cubes for z in quads])
    return [x for x in nums if x < 50000000]

def getSqRem(a,n):
    return ((a-1)**n + (a+1)**n)%a**2

def euler120():
    theMax = 0
    for a in range(3, 1001):
        for n in range(1, 1000):
            curr = getSqRem(a,n)
            if curr > theMax:
                theMax = curr
    return theMax



def euler179():
    count = 0
    primes = sieveOfE(10**7)
    adj1 = [x - 1 for x in primes]
    bad = set(primes + adj1)
    good = set(range(1, 10**7 - 1)).difference(bad)
    print len(good)

    #for x in :
        #count = count + len(getDivisors(x)) + 1
        #print x

def confirmPrime(n, primes):
    nums = [x for x in primes if x <= int(n**0.5) + 1]
    for x in nums:
        if n%x == 0:
            return False
    return True

def checkListFive(l):
    if len(l) != 5:
        return False
    for x in l:
        for y in l:
            if x != y:
                if not (isPrime(int(str(x) + str(y))) and isPrime(int(str(y) + str(x)))):
                    return False
    return True

def euler60():
    primes = sieveOfE(10000)
    l = []
    for x in primes:
        for y in primes:
            if x != y:
                if isPrime(int(str(x) + str(y))) and isPrime(int(str(y) + str(x))):
                    l = l + [(x,y)]

    for (a,b) in l:
        if (b,a) in l:
            l.remove((b,a))
    #print l
    counts = []
    for x in primes:
        count = 0
        for (a,b) in l:
            if x == a or x == b:
                count = count + 1
        counts = counts + [(x,count)]

    possible = [i[0] for i in counts if i[1] >= 4]

    pathLenFive = []
    for i in possible:#designate the start of the dfs
    #i = 3
        stack = []
        pathLen = 1
        for (a,b) in l:
            path = [i]
            if i == a:
                path = path + [b]
                stack.append((b, pathLen, path))
            elif i == b:
                path = path + [a]
                stack.append((a, pathLen, path))

        while len(stack) != 0:
            (a,c, currP) = stack.pop()
            if c >= 4:
                if checkListFive(set(currP)):
                    print currP
                    pathLenFive = pathLenFive + [currP]

            else:
                for (x,y) in l:
                    if x == a and ((y,i) in l or (i,y) in l):
                        if y not in currP:
                            stack.append((y, c + 1, currP + [y]))

                    elif y == a and ((x,i) in l or (i,x) in l):
                        if x not in currP:
                            stack.append((x, c + 1, currP + [x]))
    return pathLenFive


def euler61():
    l0 = generateTri(10**4)
    l1 = generateSq(10**4)
    l2 = generatePen(10**4)
    l3 = generateHex(10**4)
    l4 = generateHept(10**4)
    l5 = generateOct(10**4)

    a0 = [x for x in l0 if len(str(x)) == 4]
    a1 = [x for x in l1 if len(str(x)) == 4]
    a2 = [x for x in l2 if len(str(x)) == 4]
    a3 = [x for x in l3 if len(str(x)) == 4]
    a4 = [x for x in l4 if len(str(x)) == 4]
    a5 = [x for x in l5 if len(str(x)) == 4]

    lists = [a0, a1, a2, a3, a4, a5]

    perms = [x for x in permutations(range(0,6))]
    for (a,b,c,d,e,f) in perms:
        curr = []
        for v in lists[a]:
            for w in lists[b]:
                if str(v)[2:] == str(w)[0:2]:
                    for x in lists[c]:
                        if str(w)[2:] == str(x)[0:2]:
                            for y in lists[d]:
                                if str(x)[2:] == str(y)[0:2]:
                                    for z in lists[e]:
                                        if str(y)[2:] == str(z)[0:2]:
                                            for p in lists[f]:
                                                if str(z)[2:] == str(p)[0:2]:
                                                    if str(p)[2:] == str(v)[0:2]:
                                                        return [v,w,x,y,z,p]

    return []



def numSols(n): #number of solutions to 1/x + 1/y = 1/n
    limit = n*(n+1)
    sols = 2#for any n, 1/2n + 1/2n = 1/n and 1/(n+1) + 1/n(n+1) = 1/n
    #print limit
    for x in range(n + 1,limit):
        for y in range(n + 2, 2*n):
            if n*(x + y) <=  x*y:
                if n*(x + y) ==  x*y:
                    print (x,y)
                    sols = sols + 1
                else:
                    break
    return sols

def numSols2(n): #number of solutions to 1/x + 1/y = 1/n
    l = list(getDivisors(n)) + [n]
    li = [x for x in permutations(l, 2)]
    lis = set([float(x)/y for (x,y) in li])
    print lis
    return 2 + len(lis)

#def euler108():

def sumToN(n, l, i, d):
    if i >= len(l):
        if n == 0:
            return 1
        else:
            return 0
    else:
        divs = int(n/l[i])
        currSum = 0
        for x in range(0, divs + 1):
            if (n-x*l[i], i + 1) in d.keys():
                currSum = currSum + d[(n-x*l[i], i + 1)]
            else:
                val = sumToN(n-x*l[i], l, i + 1, d)
                d[(n-x*l[i], i + 1)] = val
                currSum = currSum + val
        return currSum


def euler78():# number of distinct sums of natural numbers that sum to n
    curr = -1
    val = 1
    d = {}
    while curr%1000000 != 0:
        curr = sumToN( val, range(1,val + 1), 0, d)
        print (val, curr)
        val = val + 1
    return val

def numPerm(a,b):
    la = [int(i) for i in str(a)]
    lb = [int(i) for i in str(b)]
    la.sort()
    lb.sort()
    return la == lb

def euler70():
    l = sieveOfE(10**7)
    li = []
    for x in range(10**7, 10**7 - 10000, -1):
        currPhi = phi(x, l)
        if numPerm(x, currPhi):
            li = li + []
        print x
    return li

def sqrtPeriod(n):#determine the length of the period of sqrt(n)
    a0 = int(n**0.5)
    if a0*a0 == n:
        return 0
    prev = (n**0.5 - a0, 1)
    dPrev = -a0
    length = 0
    a = [a0]
    nextFract = (0, 1)

    while nextFract != prev:
        equiv = (n**0.5 + -1*dPrev, (n - dPrev**2)/nextFract[1])
        aNext = int(equiv[0]/equiv[1])
        nextN = -1*dPrev - aNext*equiv[1]
        nextFract = (n**0.5 + nextN, equiv[1])
        dPrev = nextN
        a = a + [aNext]
        length = length + 1
    return a

def euler64():
    num = 0
    for x in range(2, 10001):
        if sqrtPeriod(x)%2 != 0:
            num = num + 1
    return num

def getECon(n):
    l = [2]
    for x in range(1, int(n/3) + 2):
        l = l + [1, 2*x, 1]
    return l[0:n+1]

def eCon(n):#nth convergent of e
    l = getECon(n)
    nextFract = l[len(l) - 1]
    for x in range(len(l) - 1, 0, -1):
        prev = Fraction(1, nextFract)
        nextFract = Fraction(Fraction(l[x - 1], 1) + prev)
    return nextFract

def sumDig(n):
    l = [int(i) for i in str(n)]
    return sumList(l)

def euler65():
    f = eCon(99)
    return sumDig(f.numerator)


def findMinSolCF(D):#compute the continued fraction of sqrt(n)
    a = sqrtPeriod(D)
    a = a + a[1:]
    A = [a[0], a[0]*a[1] + 1]
    B = [1, a[1]]
    ind = 2
    found = False

    for i in range(0, 2):
        if A[i]**2 - D*(B[i]**2) == 1:
            return (A[i], B[i])


    while not found:
        if ind >= len(a):
            a = a + a[1:]

        Anext = a[ind]*A[1] + A[0]
        Bnext = a[ind]*B[1] + B[0]
        A = [A[1]] + [Anext]
        B = [B[1]] + [Bnext]
        ind = ind + 1
        if Anext**2 - D*(Bnext**2) == 1:
            found = True
            return (Anext, Bnext)

def euler66():
    squares = set([x**2 for x in range(1, 1001)])
    l = set(range(1, 1001)).difference(squares)
    print l

    currMax = (0, 0)
    for i in l:
        (a,b) = findMinSolCF(i)
        if a > currMax[0]:
            currMax = (a, i)
    return currMax

def pellsEq(D, numSols):
    a = sqrtPeriod(D)
    a = a + a[1:]
    A = [a[0], a[0]*a[1] + 1]
    B = [1, a[1]]
    ind = 2
    currSols = 0
    sols = []
    for i in range(0, 2):
        if A[i]**2 - D*(B[i]**2) == 1:
            sols = sols + [(A[i], B[i])]
            currSols = currSols + 1

    while currSols < numSols:
        if ind >= len(a):
            a = a + a[1:]

        Anext = a[ind]*A[1] + A[0]
        Bnext = a[ind]*B[1] + B[0]
        A = [A[1]] + [Anext]
        B = [B[1]] + [Bnext]
        ind = ind + 1
        if Anext**2 - D*(Bnext**2) == 1:
            sols = sols + [(Anext, Bnext)]
            currSols = currSols + 1
    return sols


def euler80():
    squares = set([x**2 for x in range(1, 101)])
    l = set(range(1, 101)).difference(squares)
    total = 0

    for x in l:
        l = pellsEq(x, 1000)
        num = l[len(l) - 1][0]*10**100/l[len(l) - 1][1]
        currSum = sumList([int(i) for i in str(num)[0:100]])
        total = total + currSum
        print (x, currSum)
    return total


