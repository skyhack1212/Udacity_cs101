# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if letter == 'z':
        return letter_list[0]
    else:
        for le in letter_list:
            if le == letter:
                index = letter_list.index(letter)
                return letter_list[index+1]

print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
