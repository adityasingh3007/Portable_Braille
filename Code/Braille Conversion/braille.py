import Braille_Dictionary_Grade_1 as GD1
import string

def get_braille(text):
    braille=GD1.Braille.encode_braille(text)
    print("Given word: " + text)
    print("Braille converted text: ")
    GD1.print_braille(braille)
    print(" ")

ocr="'INSTRUCTIONS TO THE CANDIDATES\n\nDo not write your name anywhere in the answer book.\nBorrowing or lending of calculator, data book, etc. , will not be allowed.\n\nData books and tables which are permitted in the examination hall for reference\nshould be free from handwritten and unauthorized additions.\n\nDo not write on the question paper.\n\nRough works should be done only on the sheet provided at the end of the\n\nanswer booklet.\n\nUse both sides of the paper for answering questions.\n\nAnswers must be legibly written with blue or black ink pens only.\n\nThe answer book contains sufficient pages and no additional sheet will be given.\nMobile Phones, programmable calculators are not allowed inside the examination hall.\nMobile phones possessed by students inside the examination hall will be confiscated\nand shall not be retumed to students.\n\nStudy materials, memory aids, copies of notes or pages of books are not allowed\ninside the examination hall.\n\nStrict silence is expected inside the examination halls.\nCopying or any other malpractice may attract stringent penal'"
ocr_=""
for i in ocr:
    if i=='\n':
        i=" "
    ocr_+=i
ocr_=ocr_[1:len(ocr_)-1]

new_word=""
for j in range(0,len(ocr_)):
    i=ocr_[j]
    if(j==len(ocr_)-1):
        #print(new_word)
        get_braille(new_word)
        new_word=""
    if(i.isalpha() or i in string.punctuation):
        new_word+=i
    elif(len(new_word)!=0):
        #print(new_word)
        get_braille(new_word)
        new_word=""
    else:
        new_word=""
        
        
