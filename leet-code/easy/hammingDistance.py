'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

'''
Steps for solving
1. convert from int to binary string - don't flip
2. get substring of binary strings
3. compare strings to each other and increment
'''
def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    def intToBinary(binary):
        binaryStr = ""

        while(True):
        	if (binary % 2 == 0):
        		binaryStr = "0" + binaryStr
        	else:
        		binaryStr = "1" + binaryStr
        	
        	binary = binary // 2 # integer division
        	if (binary == 0):
        		break
        return binaryStr

    binaryX = intToBinary(x)
    binaryY = intToBinary(y)
    hamDist = 0

    if len(binaryX) > len(binaryY):
    	diff = len(binaryX) - len(binaryY)
    	for _ in range(diff): # underscore means var doesn't matter
    		binaryY = "0" + binaryY

    if len(binaryX) < len(binaryY):
    	diff = len(binaryY) - len(binaryX)
    	for _ in range(diff):
    		binaryX = "0" + binaryX

    print("X String : {}".format(binaryX))
    print("Y String : {}".format(binaryY))

    for i in range(len(binaryX)):
    	if binaryX[i:i+1] != binaryY[i:i+1]:
    		hamDist += 1

    print ("HamDist : {}".format(hamDist))
    return hamDist


if __name__ == '__main__':
    hammingDistance(1, 4)



