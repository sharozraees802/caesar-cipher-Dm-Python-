def encrypt(sentence):
   result = []
   for letter in sentence:
       Letter = ord(letter) - 20
       result.append(Letter)

   # print(result)
   print("This is you Encrypted message!")
   for numbers in result:
       print(numbers, end='')
       print(" ",end='')

   print()
   decrypt(result)


def decrypt(result):
    end_string = ''
    for numbers in result:
        l = int(numbers)
        l = l + 20
        l = chr(l)
        end_string = end_string + l

    print("you decrypted message is:")
    print(end_string)

def main():
    strings = input("inpute a sentence that you want encrypted: ")
    encrypt(strings)




if __name__ == '__main__':
   main()
