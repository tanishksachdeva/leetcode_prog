# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

# Example:

# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
 

# Note:

# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution1:
    def findWords(self, words: List[str]) -> List[str]:
        dict_map  = {1 : 'qwertyuiop',
                    2: 'asdfghjkl',
                    3 : "zxcvbnm"}
        output =[] 
        for w in words:
            for key in dict_map:
                print(list(w))
                print(list(dict_map[key]))
                if(all(x in list(dict_map[key]) for x in list(w.lower()))):
                    #if(all(x in test_list for x in sub_list)):
                    print('in')
                    output.append(w)
        return output
        
#---------------------------------------


class Solution2:
    def findWords(self, words: List[str]) -> List[str]:
            
        res = []
        for i in range(len(words)):
            if(check(words[i])):
                res.append(words[i])
        
        return (res)

def check(word):
    row1 = "qwertyuiopQWERTYUIOP"
    row2 = "asdfghjklASDFGHJKL"
    row3 = "zxcvbnmZXCVBNM"

    if(word[0] in row1):
        for i in word:
            if(i not in row1):
                return False
        return True
    if(word[0] in row2):
        for i in word:
            if(i not in row2):
                return False
        return True
    if(word[0] in row3):
        for i in word:
            if(i not in row3):
                return False
        return True    