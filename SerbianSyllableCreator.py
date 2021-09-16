#! python3

# .......................................................WELCOME TO SYLLABLE CREATOR.................................................

# This program lists splits the word into its syllables. Works best in Serbian!

# ...................................................................................................................................

# Many variables in the program have the "_str" or "_list" sufixes. These tell a value type the variable will finally evaluate to. 
# For example, "word_str" evaluates to a string, but the word_list evaluates to the list..
#  - in this case, the list containing str characters of the word_str. 

# ...................................................................................................................................

#vowels and consonants list

vowels_list = ['a', 'e', 'i', 'o', 'u'] 
consonants_list = ['b', 'c', 'č','ć', 'd', 'đ', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 't', 'v', 'w', 'x', 'y', 'z', 'ž']

#the main code

while True:

    #prompts the user to enter the new word

    word_str = ''
    word_str = input('Enter your word here: ').lower()
    
    #makes neccesary lists and variables

    word_list = list(word_str)
    
    lastLetter_index = len(word_list)-1
    lastLetter_str = word_list[lastLetter_index]

    lastLetter1_index = len(word_list)-2
    lastLetter1_str = word_list[lastLetter1_index]

    lastLetter2_index = len(word_list)-3
    lastLetter2_str = word_list[lastLetter2_index]

    listSemiSyllables_str = []
    listSemiSyllables_list = []

    finalList = []                                              #the final list of all syllables belonging to the word entered.

    # this creates a list of syllable like structures, made from the word the user has provided the program with. 
    # these will later be used to derive real syllables. 

    for i in range (len(word_list)):
        if word_list[i] in vowels_list:

            semiSyllable_list = word_list[0:i+1]
            semiSyllable_str = ''.join(semiSyllable_list) #prebacuje 

            listSemiSyllables_str.append(semiSyllable_str)
            listSemiSyllables_list.append(semiSyllable_list)
    
    # this is the formula for real syllable creation

    for i in range (len(listSemiSyllables_str)):
        if i != 0:                                              #derives all the syllables in a word except the first one
            motherSyllable_str = listSemiSyllables_str[i]
            previousSyllable_str = listSemiSyllables_str[i-1]
            motherSyllable_list = list(motherSyllable_str)
            previousSyllable_list = list(previousSyllable_str)
            for x in previousSyllable_list:
                motherSyllable_list.remove(x)
                newSyllable_str = ''.join(motherSyllable_list)
            finalList.append(newSyllable_str)
        else:                                                   #derives the first syllable
            prviSlog = ''.join(listSemiSyllables_list[0])
            finalList.insert(0, prviSlog)

    # In some instances, the last(final) syllable ommits either the last letter or the several ending letters. 
    # This part of the code corrects that.
 
    finalSyllable_str = finalList[len(finalList)-1]
    finalSylllableCorrection_str = finalList[len(finalList)-1] + lastLetter_str
    finalSyllableCorrection1_str = finalList[len(finalList)-1] + lastLetter1_str + lastLetter_str
    finalSyllableCorrection2_str = finalList[len(finalList)-1] + lastLetter2_str + lastLetter1_str + lastLetter_str

    if (lastLetter_str in consonants_list) and (lastLetter1_str in consonants_list) and (lastLetter2_str in consonants_list):
        finalList.remove(finalSyllable_str)
        finalList.append(finalSyllableCorrection2_str)

    elif (lastLetter_str in consonants_list) and (lastLetter1_str in consonants_list) :
        finalList.remove(finalSyllable_str)
        finalList.append(finalSyllableCorrection1_str)
    
    elif lastLetter_str in consonants_list:
        finalList.remove(finalSyllable_str)
        finalList.append(finalSylllableCorrection_str)
    
    #The program finally prints the results in a nice, clean and formatted way. 

    allSlogovi = '  |  '.join(finalList)
    
    print ('\n')
    print ('REČ PO SLOGOVIMA'.center(50))
    print ('..........................................................'.center(50))
    print (allSlogovi.center(50))
    print ('..........................................................\n\n'.center(50))