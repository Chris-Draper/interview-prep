'''
Given a string, you need to reverse the order of characters in each word 
within a sentence while still reserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will 
not be any extra space in the string.

-----------------------

Game Plan
1. Need for loop to iterate and find spaces
2. Need var for reversed string
3. Need method that takes in spliced string and reverse string var
4. Need to reverse string
5. For loop ends once interated over string

------------------------

You missed the edge case where the last word doesn't have a space
You just need to add in the spaces yourself after each reversed word to preserve white space

-------------------------

Jesus your solution is too long. Apparently you can do this in one line?
Time to spend the next day figuring out how the one liner from leet code works
'''

def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        def switchChars(str, strRev, currChar, prevChar):
            while(currChar > prevChar):
                strRev += str[currChar - 1:currChar]
                currChar += -1
            print("Switched chars : {}".format(strRev))
            return strRev

        print("Og string : {}".format(s))
        strRev = ""
        prevChar = 0
        for i in range(len(s)):
            if s[i:i+1] == " ":
                currChar = i
                strRev = switchChars(s, strRev, currChar, prevChar)
                strRev += " "
                prevChar = i + 1
        currChar = len(s)
        strRev = switchChars(s, strRev, currChar, prevChar)
        print("Reversed String : |{}|".format(strRev))
        return strRev

if __name__ == '__main__':
    reverseWords("Let's take the Leetcode contest")