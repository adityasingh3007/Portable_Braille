# -*- coding: utf-8 -*-
"""
**************************************************************************************
*                     Braille Dictionary (GRADE 1)
*                  ================================
*  This software is intended to convert english text into braille characters
*  MODULE: Braille_Dictionary_Grade_1
*  Filename: Braille_Dictionary_Grade_1.py
*  Version: 1.8.0  
*  Date: March 14, 2019
*  
*  Authors: Aditya Kumar Singh and Raj Kumar Bhagat
*  Team Name: Victorious Visionaries
*  Team Members: Aditya Kumar Singh, Raj Kumar Bhagat,
*                Ruphan S, Yash Patel
***************************************************************************************
"""

"""
---------------------------------------------------------------------------------------
                               INSTRUCTIONS
                             =================
    1. Braille is represented in form of 6 raised dots.
       Ex:-
              1-> o o <-4
              2-> o o <-5
              3-> o o <-6
        The dots are represented here with '0' whereas those numbers are dots
        refrence number.
    2. So 'a' is represented as 0 o  where '0' is raised dot and 'o' is normal dot.
                                o o 
                                o o
    3. Now this can be numrically reffered as 1 since only raised dot is at position 1
       In the same way for 'b' we can say [1,2] since only these two dots are raised.

    4. Now here each braille character set is represented in a form of array[] with 
       6 elements in it.

    5. And raised dot is represented by "1". and normal dots are represented with "0".
    
    6. Each element maps to braille character like this :
            [ 1, 2, 3, 4, 5, 6]
       So for 'a' we have [1, 0, 0, 0, 0, 0]
       

                              GRADE 1 BRAILLE
                        ==========================
    1. It is the the first grade in braille.

    2. It is basically contains one-to-one conversion of contractions.

    3. Individual cells cannot represent words or abbreviations in this grade of Braille.

    4. Characters invloved are a-z(with capatalization included), punctutators, numbers.

    5. For more visit "http://www.acb.org/tennessee/braille.html"

       
----------------------------------------------------------------------------------------     
"""

import string                                   #For handling string methods like punctuation()

class Grade1:
    last_type_modifier=""                       #Variable to keep track of type of character last read
    braille_code=[]                             #List which will hold the braille code after conversion
    Dict = {                             #Dictionary for BRAILLE GRADE 1
        "_number": [0, 0, 1, 1, 1, 1],
        "_letter": [0, 0, 0, 0, 1, 1],
        "_caps": [0, 0, 0, 0, 0, 1],
        "_decimal": [0, 0, 0, 1, 0, 1],
        "_space": [0, 0, 0, 1, 0, 1],
        "a": [1, 0, 0, 0, 0, 0],
        "b": [1, 1, 0, 0, 0, 0],
        "c": [1, 0, 0, 1, 0, 0],
        "d": [1, 0, 0, 1, 1, 0],
        "e": [1, 0, 0, 0, 1, 0],
        "f": [1, 1, 0, 1, 0, 0],
        "g": [1, 1, 0, 1, 1, 0],
        "h": [1, 1, 0, 0, 1, 0],
        "i": [0, 1, 0, 1, 0, 0],
        "j": [0, 1, 0, 1, 1, 0],
        "k": [1, 0, 1, 0, 0, 0],
        "l": [1, 1, 1, 0, 0, 0],
        "m": [1, 0, 1, 1, 0, 0],
        "n": [1, 0, 1, 1, 1, 0],
        "o": [1, 0, 1, 0, 1, 0],
        "p": [1, 1, 1, 1, 0, 0],
        "q": [1, 1, 1, 1, 1, 0],
        "r": [1, 1, 1, 0, 1, 0],
        "s": [0, 1, 1, 1, 0, 0],
        "t": [0, 1, 1, 1, 1, 0],
        "u": [1, 0, 1, 0, 0, 1],
        "v": [1, 1, 1, 0, 0, 1],
        "x": [1, 0, 1, 1, 0, 1],
        "y": [1, 0, 1, 1, 1, 1],
        "z": [1, 0, 1, 0, 1, 1],
        "w": [0, 1, 0, 1, 1, 1],
        "1": [1, 0, 0, 0, 0, 0],
        "2": [1, 1, 0, 0, 0, 0],
        "3": [1, 0, 0, 1, 0, 0],
        "4": [1, 0, 0, 1, 1, 0],
        "5": [1, 0, 0, 0, 1, 0],
        "6": [1, 1, 0, 1, 0, 0],
        "7": [1, 1, 0, 1, 1, 0],
        "8": [1, 1, 0, 0, 1, 0],
        "9": [0, 1, 0, 1, 0, 0],
        "0": [0, 1, 0, 1, 1, 0],
        ",": [0, 1, 0, 0, 0, 0],
        ";": [0, 1, 1, 0, 0, 0],
        ":": [0, 1, 0, 0, 1, 0],
        ".": [0, 1, 0, 0, 1, 1],
        "!": [0, 1, 1, 0, 1, 0],
        "()": [0, 1, 1, 0, 1, 1],
        "\"?": [0, 1, 1, 0, 0, 1],
        "*": [0, 0, 1, 0, 1, 0],
        "\"": [0, 0, 1, 0, 1, 1],
        }
    """
    Constructor Function
    """
    def __init__(self):
        self.last_type_modifier=False
        braille_code=[]

    """
    This Function prints all the characters defined in all the dictionaries
    present in its parent class
    """
    def show_all(self):
        print("Grade 1.... \n")
        for i,j in self.Dict.items():    
            print(i+"->")
            for n,k in enumerate(self.Dict[i][:3]):
                print(k,self.Dict[i][n+3])
            print("\n")

    """
    This Function prints a particular character in its braille form.
    NOTE: The character should belong to Grade 1.
    """      
    def print_braille1(self,char):
        if(char.isupper()):
            char=char.lower()
        if char in self.Dict:
            for n,i in enumerate(self.Dict[char][:3]):
                print(i,self.Dict[char][n+3])
            print("..")

    """
    This function encodes the given english word into Braille
    """           
    def decode_grade1(self,word):
        """
          In this function if you want to print the current character which is being
          processed in tis braille form then, uncomment the lines which have print in it.
          Ex: 'print(i)' and 'self.print_braille1("_letter")'
          NOTE: This is helpfull in case of debugging but it also decrease the processing time.
          So better once checked keep those lines in comments.
        """
        #Checking for firstrun
        if(self.last_type_modifier==False):
            if(word[0].isalpha()):
               if(word[0].islower()):
                   self.last_type_modifier="lower"
                   #self.print_braille1("_letter")
                   #self.braille_code.append(self.Dict["_letter"])
               elif(word[0].isupper()):
                   self.last_type_modifier="upper"
            elif(word[0].isnumeric()):
                self.last_type_modifier="num"
                #self.print_braille1("_number")
                self.braille_code.append(self.Dict["_number"])
        m = -1                                  #Variable holding index position for the string word
        while(m<len(word)-1):
            #Update the iterating variable
            m+=1
            #Extracting the character at index m in string word
            i=word[m]
            #Checking for type change
            if(i.islower() and (self.last_type_modifier!="lower")):
                if(self.last_type_modifier=="upper"):
                    self.last_type_modifier="lower"
                else:
                    self.last_type_modifier="lower"
                    #self.print_braille1("_letter")
                    self.braille_code.append(self.Dict["_letter"])
                    
            elif(i.isnumeric() and (self.last_type_modifier!="num")):
                self.last_type_modifier="num"
                #self.print_braille1("_number")
                self.braille_code.append(self.Dict["_number"])
            elif(i.isupper()):
                self.last_type_modifier="upper"
                final_index=len(word)
                if(final_index==1):
                    self.braille_code.append(self.Dict["_caps"])
                    if i.lower() in self.Dict:
                        self.braille_code.append(self.Dict[i.lower()])
                    else:
                        self.braille_code.append([0, 0, 0, 0, 0, 0])
                    return
                flag=0
                while(final_index!=(m+1)):
                    if(word[m:final_index].isupper() and word[m:final_index].isalpha()):
                        #print(word[m:final_index])
                        flag=1
                        #self.print_braille1("_caps")
                        #self.print_braille1("_caps")
                        self.braille_code.append(self.Dict["_caps"])
                        self.braille_code.append(self.Dict["_caps"])
                        for j in word[m:final_index]:
                            #print(j)
                            #self.print_braille1(j)
                            if j.lower() in self.Dict:
                                self.braille_code.append(self.Dict[j.lower()])
                            else:
                                self.braille_code.append([0, 0, 0, 0, 0, 0])
                            
                        break
                    final_index-=1
                m=final_index-1
                if(final_index==len(word)):
                    return
                else:
                    if((not word[m+1].isnumeric()) and flag==1):
                        #self.print_braille1("_caps")
                        #self.print_braille1("_caps")
                        self.braille_code.append(self.Dict["_caps"])
                        self.braille_code.append(self.Dict["_caps"])
                    if(not flag):
                        #self.print_braille1("_caps")
                        self.braille_code.append(self.Dict["_caps"])
                        #print(i)
                        #self.print_braille1(i)
                        if i.lower() in self.Dict:
                            self.braille_code.append(self.Dict[i.lower()])
                        else:
                            self.braille_code.append([0, 0, 0, 0, 0, 0])
                    continue
            elif(i in string.punctuation):
                char=""
                if(i=='(' or i==')'):
                    char="()"
                elif(i=='?'):
                    char="\"?"
                elif(i=='.'):
                    if(m==len(word)-1):
                        char=i
                    else:
                        char="_decimal"
                else:
                    char=i
                if char in self.Dict:
                    self.braille_code.append(self.Dict[char])
                else:
                    self.braille_code.append([0, 0, 0, 0, 0, 0])
                continue
            """Printing the current character"""
            #print(i)
            #self.print_braille1(i)
            self.braille_code.append(self.Dict[i])
            

    """
    This functions start encoding into braille
    """       
    def encode_braille(self,word):
        self.braille_code=[]
        self.decode_grade1(word)
        code=self.braille_code
        return code

"""
    This function prints the converted braille on the screen.
"""
def print_braille(braille):
    #print(braille)
    _len=len(braille)
    for i in range(0,3):
        m=""
        for x in braille:
            m+=str(x[i])+str(x[i+3])
            m+=" "
        print(m)

braille=Grade1()           #Object created

"""
test="asdfghAQWWWopiuytrew"

brl=braille.encode_braille(test)
print("Given word: " + test)
print("Braille converted text: ")
print_braille(brl)
"""






