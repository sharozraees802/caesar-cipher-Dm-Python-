def encrypt(sentence):
   result = []
   for letter in sentence:
       Letter = ord(letter) - 20
       result.append(Letter)

   print("This is you Encrypted message!")

   for numbers in result:
       print(numbers, end='')
       print(" ",end='')

   print()
   decrypt(result)

def decrypt(result):
    end_string = ''

    for numbers in result:
        letter = int(numbers)
        letter = letter + 20
        letter = chr(letter)
        end_string = end_string + letter


    print("you decrypted message is:")
    print(end_string)

def main():
    s = open("dm_project.txt", 'r')
    f = s.read()
    encrypt(f)

if __name__ == '__main__':
    main()