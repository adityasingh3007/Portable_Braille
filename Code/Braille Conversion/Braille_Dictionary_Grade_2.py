# -*- coding: utf-8 -*-
"""
**************************************************************************************
*                     Braille Dictionary (GRADE 2)
*                  ================================
*  This software is intended to convert english text into braille characters
*  MODULE: Braille_Dictionary_Grade_2
*  Filename: Braille_Dictionary_Grade_2.py
*  Version: 1.0.0  
*  Date: December 8, 2018
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
       

                              GRADE 2 BRAILLE
                        ==========================
    1. It is the the second grade in braille.

    2. Theis includes all the character sets which were there in grade 1.

    3. In addition to those, this has abbreviation, contraction which shortens the
       overall braille characters.

    4. And it has some short notations for most commonly used words as well to represent
       them as a single character.
    
    5. For more visit "http://www.acb.org/tennessee/braille.html"

       
----------------------------------------------------------------------------------------     
"""

class Grade2:
    last_type_modifier=""                       #Variable to keep track of type of character last read
    braille_code=[]                             #List which will hold the braille code after conversion
    #Partial contractions, dot 5,6 raised
    cpartial_56 = {
        "ence" : "e",
        "ong" : "g",
        "ful" : "l",
        "tion" : "n",
        "ness" : "s",
        "ment" : "t",
        "ity" : "y"
        }
    #Partial contractions, dot 6 raised
    cpartial_6={
        "ation" : "n",
        "ally" : "y"
        }
    #Partial contractions, dot 4,6 raised
    cpartial_46={
        "ound" : "d",
        "ance" : "e",
        "sion" : "n",
        "less" : "s",
        "ount" : "t"
        }
    #Whole word contractions, dot 5 rasied
    cwhole_5 = {
        "character" : "(ch)",
        "day" : "d",
        "ever" : "e",
        "father" : "f",
        "here" : "h",
        "know" : "k",
        "lord" : "l",
        "mother" : "m",
        "name" : "n",
        "one" : "o",
        "ought" : "(ou)",
        "part" : "p",
        "question" : "q",
        "right" : "r",
        "some" : "s",
        "there" : "(the)",
        "through" : "(th)",
        "time" : "t",
        "under" : "u",
        "where" : "(wh)",
        "work" : "w",
        "young" : "y"
        }
    #Whole word contractions, dot 4,5 rasied
    cwhole_45= {
        "these" : "(the)",
        "those" : "(th)",
        "upon" : "u",
        "whose" : "(wh)",
        "word" : "w"
        }
    #Whole word contractions, dot 4,5,6 rasied
    cwhole_456= {
        "cannot" : "c",
        "had" : "h",
        "many" : "m",
        "spirit" : "s",
        "their" : "(the)",
        "world" : "w"
        }
    #Abbreviation
    abbr= {
        "about" : "ab",
        "above" : "abv",
        "according" : "ac",
        "across" : "acr",
        "after" : "af",
        "afternoon" : "afn",
        "afterward" : "afw",
        "again" : "ag",
        "against" : "ag(st)",
        "almost" : "alm",
        "already" : "alr",
        "also" : "al",
        "although" : "al(th)",
        "altogether" : "alt",
        "always" : "alw",
        "because" : "(be)c",
        "before" : "(be)f",
        "behind" : "(be)h",
        "below" : "(be)l",
        "beneath" : "(be)n",
        "beside" : "(be)s",
        "between" : "(be)t",
        "beyond" : "(be)y",
        "blind" : "bl",
        "braille" : "brl",
        "children" : "(ch)n",
        "conceive" : "(con)cv",
        "conceiving" : "(con)cvg",
        "could" : "cd",
        "deceive" : "dcv",
        "deceiving" : "dcvg",
        "declare" : "dcl",
        "declaring" : "dclg",
        "either" : "ei",
        "first" : "f(st)",
        "friend" : "fr",
        "good" : "gd",
        "great" : "grt",
        "herself" : "h(er)f",
        "him" : "hm",
        "himself" : "hmf",
        "immediate" : "imm",
        "letter" : "lr",
        "little" : "ll",
        "much" : "m(ch)",
        "must" : "m(st)",
        "myself" : "myf",
        "necessary" : "nec",
        "neither" : "nei",
        "o'clock" : "o'c",
        "oneself" : "(one)f",
        "ourselves" : "(ou)rvs",
        "paid" : "pd",
        "perceive" : "p(er)cv",
        "perceiving" : "p(er)cvg",
        "perhaps" : "p(er)h",
        "quick" : "qk",
        "receive" : "rcv",
        "receiving" : "rcvg",
        "rejoice" : "rjc",
        "rejoicing" : "rjcg",
        "said" : "sd",
        "should" : "(sh)d",
        "such" : "s(ch)",
        "themselves" : "(the)mvs",
        "thyself" : "(th)yf",
        "today" : "td",
        "together" : "tgr",
        "tomorrow" : "tm",
        "tonight" : "tn",
        "would" : "wd",
        "its" : "xs",
        "itself" : "xf",
        "your" : "yr",
        "yourself" : "yrf",
        "yourselves" : "yrvs"
        }
    #Standalone words
    std_aln = {
        "but" : "b",
        "can" : "c",
        "do" : "d",
        "every" : "e",
        "from" : "f",
        "go" : "g",
        "have" : "h",
        "just" : "j",
        "knowledge" : "k",
        "like" : "l",
        "more" : "m",
        "not" : "n",
        "people" : "p",
        "quite" : "q",
        "rather" : "r",
        "so" : "s",
        "that" : "t",
        "us" : "u",
        "very" : "v",
        "it" : "x",
        "you" : "y",
        "as" : "z",
        "child" : "(ch)",
        "shall" : "(sh)",
        "this" : "(th)",
        "which" : "(wh)",
        "out" : "(ou)",
        "will" : "w",
        "be" : ";",
        "enough" : "(en)",
        "to" : "!",
        "were" : "(gg)",
        "his" : "(\"?)",
        "in" : "*",
        "was" : "\"",
        "by" : "\"",
        "still" : "(st)"
        }
    #Main dictionary as per GRADE 2
    Dict = {                               
        "_number": [0, 0, 1, 1, 1, 1],
        "ble": [0, 0, 1, 1, 1, 1],
        "_letter": [0, 0, 0, 0, 1, 1],
        "_p56": [0, 0, 0, 0, 1, 1],
        "_caps": [0, 0, 0, 0, 0, 1],
        "_p6": [0, 0, 0, 0, 0, 1],
        "_decimal": [0, 0, 0, 1, 0, 1],
        "_p46": [0, 0, 0, 1, 0, 1],
        "_w5": [0, 0, 0, 0, 1, 0],
        "_w45": [0, 0, 0, 1, 1, 0],
        "_w456": [0, 0, 0, 1, 1, 1],
        "_space": [0, 0, 0, 0, 0, 0],
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
        "and": [1, 1, 1, 1, 0, 1],
        "for": [1, 1, 1, 1, 1, 1],
        "of": [1, 1, 1, 0, 1, 1],
        "the": [0, 1, 1, 1, 0, 1],
        "with": [0, 1, 1, 1, 1, 1],
        "ch": [1, 0, 0, 0, 0, 1],
        "gh": [1, 1, 0, 0, 0, 1],
        "sh": [1, 0, 0, 1, 0, 1],
        "th": [1, 0, 0, 1, 1, 1],
        "wh": [1, 0, 0, 0, 1, 1],
        "ed": [1, 1, 0, 1, 0, 1],
        "er": [1, 1, 0, 1, 1, 1],
        "ou": [1, 1, 0, 0, 1, 1],
        "ow": [0, 1, 0, 1, 0, 1],
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
        "ea": [0, 1, 0, 0, 0, 0],
        ";": [0, 1, 1, 0, 0, 0],
        "bb": [0, 1, 1, 0, 0, 0],
        "be": [0, 1, 1, 0, 0, 0],
        ":": [0, 1, 0, 0, 1, 0],
        "con": [0, 1, 0, 0, 1, 0],
        "cc": [0, 1, 0, 0, 1, 0],
        ".": [0, 1, 0, 0, 1, 1],
        "$": [0, 1, 0, 0, 1, 1],
        "dis": [0, 1, 0, 0, 1, 1],
        "dd": [0, 1, 0, 0, 1, 1],
        "en": [0, 1, 0, 0, 0, 1],
        "!": [0, 1, 1, 0, 1, 0],
        "ff": [0, 1, 1, 0, 1, 0],
        "()": [0, 1, 1, 0, 1, 1],
        "gg": [0, 1, 1, 0, 1, 1],
        "\"?": [0, 1, 1, 0, 0, 1],
        "*": [0, 0, 1, 0, 1, 0],
        "\"": [0, 0, 1, 0, 1, 1],
        "'": [0, 0, 1, 0, 0, 0],
        "com": [0, 0, 1, 0, 0, 1],
        "-": [0, 0, 1, 0, 0, 1],
        "ing": [0, 0, 1, 1, 0, 1],
        "st": [0, 0, 1, 1, 0, 0],
        "/": [0, 0, 1, 1, 0, 0],
        "ar": [0, 0, 1, 1, 1, 0],
        }

    """
    Constructor Function
    """
    def __init__(self):
        self.last_type_modifier=False
        braille_code=[]
        
    """
    This Function prints all the characters defined in the main dictionary
    present in its parent class
    """
    def show_all(self):
        print("Grade 2.... \n")
        for i,j in self.Dict.items():    
            print(i+"->")
            for n,k in enumerate(self.Dict[i][:3]):
                print(k,self.Dict[i][n+3])
            print("\n")

    """
    This Function prints a particular character in its braille form.
    NOTE: The character should belong to Grade 2.
    """      
    def print_braille1(self,char):
        if(char.isupper()):
            char=char.lower()
        if char in self.Dict:
            for n,i in enumerate(self.Dict[char][:3]):
                print(i,self.Dict[char][n+3])
            print("..")

    """
    This Function checks whether the given word can be shortened or not.
    If it can then it will return the shortened word or else it will simply return the
    given word.
    NOTE: This function doesnt convert the the given string into braille,
          this only sees if it can be be shortened or not.
          If yes then it returns the shortened string.
    """
    def process(self,text):
        m=""                                    #String to store afer shortening the given text
        if (text.isupper() or text.islower() or (text[0].isupper() and text[1:len(text)].islower())):   #Checking if it fits in Grade 2 standards
            char=text.lower()                       
            if char in self.std_aln:                #Checking in standalone dictionary
                #print("Standalone word found")
                """
                   This checks for the type of capatallisation and add the capatallsing
                   letter accordingly
                """
                if(text.isupper()):                 
                    m+="(_caps)(_caps)"
                elif(text[0].isupper()):
                    m+="(_caps)"
                m+=self.std_aln[char]
            elif char in self.abbr:                 #Checking in abbreviation dictionary
                #print("Abbreviation found")
                if(text.isupper()):
                    m+="(_caps)(_caps)"
                elif(text[0].isupper()):
                    m+="(_caps)"
                m+=self.abbr[char]
            elif char in self.cwhole_5 or char in self.cwhole_45 or char in self.cwhole_456:  #Checking in word contraction dictionary
                #print("Whole word contraction found")
                """
                 Now checking which under which type of word contraction,
                 the given word really falls in.
                """
                if char in self.cwhole_5:     #Dot 5 raised word contraction
                    if(text.isupper()):
                        m+="(_caps)(_caps)"
                    elif(text[0].isupper()):
                        m+="(_caps)"
                    m+="(_w5)"+self.cwhole_5[char]
                elif char in self.cwhole_45:     #Dot 4,5 raised word contraction
                    if(text.isupper()):
                        m+="(_caps)(_caps)"
                    elif(text[0].isupper()):
                        m+="(_caps)"
                    m+="(_w45)"+self.cwhole_45[char]
                elif char in self.cwhole_456:       #Dot 4,5,6 raised word contraction
                    if(text.isupper()):
                        m+="(_caps)(_caps)"
                    elif(text[0].isupper()):
                        m+="(_caps)"
                    m+="(_w456)"+self.cwhole_456[char]
            elif char in self.Dict:             #Checking if its directly there in main dictionary
                    m="("+char+")"
            else:
                m=text
        else:
            m=text
        return m

    """
     This function checks for the index of a balanced parenthesis in the passed string
     and returns it in a form of list
    """
    def match_parenthesis(self,string):
        a=[]
        for j in range(0,len(string)):
            i=string[j]
            if i == "(":
                a.append(j)
            elif i == ")":
                a.append(j)
        return a

    """
     This function actually takes the converted string and maps it to its braille
     equivallent.
    """
    def get_braille(self,text):
        code=[]                             #List to store the braille array character by character
        #Check for blanced parenthesis
        flag=self.match_parenthesis(text)        #Checking if parenthesis is there or not
        opt=0
        if(len(flag)!=0):
            opt=1
        else:
            opt=0

        if(opt==0):                             #Simple character by character conversion is there, since parenthesis was not detected
            for i in text:
                if i in self.Dict:
                    code.append(self.Dict[i])
        else:
            """
              Since parethesis was detected. Now the complete string inside the parenthesis should be treated as
              one character and not s individual character.
            """
            substr=[]                           #List to store the string within parenthesis
            m=0
            #This loop will append all substring inside all the parenthesis into the substr list
            while(m<len(flag)-1):
                substr.append(text[flag[m]+1:flag[m+1]]) 
                m+=2
            #now traversing the main converted text character by character
            index=0
            count=0
            while(index<len(text)):
                i=text[index]
                if(i=="("):                 # if found the take the upcoming character as one character until
                                            # parenthesis closed is detected
                    if substr[count] in self.Dict:      #Checking whether the sub-string inside parenthesis is in Main dicitonary or not
                        code.append(self.Dict[substr[count]])
                        count+=1
                    else:                               #if not then again send this word to get it shortened. 
                        char=self.process(substr[count])
                        temp=0
                        for k in range(index,len(text)):
                            if(text[k]==")"):
                                temp=k
                        char+=text[temp+1:len(text)]    #Add the rest of the part of the string to it
                        m=self.get_braille(char)        #Call itself to process the new form.
                        return m                        
                    for j in range(index,len(text)):    #Update the index to ')''s index
                        if(text[j]==")"):
                            index=j
                            break
                else:                     #or simply take the braille from main dictionary
                    code.append(self.Dict[i])
                index+=1
        return code

    """
       This function takes the word first and then process it as per Grade 2.
       If doesnt suit with grade 2 then simply with grade 1.
    """
    def process_word(self,text):
        char=""
        conv_str=self.process(text)
        if(conv_str==text):
            print("The given word cannot be shortened as per GRADE 2 standards.")
            print("Hence, it will be converted as per GRADE 1 standards")
            #Function to call grade 1 conversion
        else:
            print(conv_str)
            char=self.get_braille(conv_str)
        return char
            
            
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
  
Braille=Grade2()                   #Object Created


"""
i="oneself"
print("Given text:" + i)
print("Text after conversion: ")
code=Braille.process_word(i)
print_braille(code)
"""

pre_defined_words=["and", "for", "of", "the", "with", "child", "shall", "this", "which", "out", "ow", "will", "be", "enough", "to", "were", "his", "in", "was", "by", "still", "a", "but", "can", "do", "every", "from", "go", "have", "I", "just", "knowledge", "like", "more", "not", "o", "people", "quite", "rather", "so", "that", "us", "very", "it", "you", "as", "character", "day", "ever", "father", "here", "know", "lord", "mother", "name", "one", "ought", "part", "question", "right", "some", "there", "through", "time", "under", "where", "work", "young", "these", "those", "upon", "whose", "word", "cannot", "had", "many", "spirit", "their", "world", "about", "above", "according", "across", "after", "afternoon", "afterward", "again", "against", "almost", "already", "also", "although", "altogether", "always", "because", "before", "behind", "below", "beneath", "beside", "between", "beyond", "blind", "braille", "children", "conceive", "conceiving", "could", "deceive", "deceiving", "declare", "declaring", "either", "first", "friend", "good", "great", "herself", "him", "himself", "immediate", "letter", "little", "much", "must", "myself", "necessary", "neither", "o'clock", "oneself", "ourselves", "paid", "perceive", "perceiving", "perhaps", "quick", "receive", "receiving", "rejoice", "rejoicing", "said", "should", "such", "themselves", "thyself", "today", "together", "tonight", "would", "its", "itself", "your", "yourself", "yourselves"]


for i in pre_defined_words:
    print("Given text:" + i)
    print("Text after conversion: ")
    code=Braille.process_word(i)
    print_braille(code)


