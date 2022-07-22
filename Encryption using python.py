print ("Select the action you want to perform(A or B)")
print ("A-ROT-7 cipher")
print ("B-polyalphabetic cipher")
print ("C-Vigenere cipher")
print ("D-Ceasar Cipher")
option=input("Enter your option(A , B , C , D) :-")


if option == 'A':                          #ROT-7 rotation
    message=input("Enter a message ")                   #hello
    alphabet="abcdefghijklmnopqerstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}|?/.,<\>"
    encrypt=""
    key=5
    for i in message:
        position=alphabet.find(i)
        newposition=(position+5)%26
        encrypt+=alphabet[newposition]
    print(encrypt)    

elif option == "B":
    message=input(print("Enter a message: "))
    message=message.lower()

    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    password=input("Enter a password: ")
    password=password.lower()

    ciphertext=''
    password=password*len(message)
    count=0
    for letter in message:
        if letter in alphabet:
            shift=alphabet.index(password[count])
            letterindex=alphabet.index(letter)
            cipherletter=alphabet[(shift+letterindex)%26]
            ciphertext+=cipherletter  
        else:
            ciphertext+=letter    
        count+=1
    print(ciphertext)

elif option == "C":

    def generateKey(string, key): 
      key = list(key) 
      if len(string) == len(key): 
        return(key) 
      else: 
        for i in range(len(string) -len(key)): 
          key.append(key[i % len(key)]) 
      return("" . join(key)) 
  
    def encryption(string, key): 
      encrypt_text = [] 
      for i in range(len(string)): 
        x = (ord(string[i]) +ord(key[i])) % 26
        x += ord('A') 
        encrypt_text.append(chr(x)) 
      return("" . join(encrypt_text)) 
    def decryption(encrypt_text, key): 
      orig_text = [] 
      for i in range(len(encrypt_text)): 
        x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
      return("" . join(orig_text)) 
    if __name__ == "__main__": 
      string = input("Enter the message: ")
      keyword = input("Enter the keyword: ")
      key = generateKey(string, keyword) 
      encrypt_text = encryption(string,key) 
      print("Encrypted message:", encrypt_text) 
      print("Decrypted message:", decryption(encrypt_text, key)) 
elif option == "D":
    x=input("Enter a string: ")
    alpha="abcdefghijklmnopqerstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}|?/.,<\>"
    enc=""                                          #encrypted text storage variale
    for i in x:
        posit=alpha.find(i)
        newposit=(posit+2)%26
        enc+=alpha[newposit]
    print(enc)    
    exit()