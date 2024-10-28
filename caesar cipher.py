alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
          ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("type the shift number :\n"))
def encrypt(plain_text,shift_amount):
    ciper_text=""
    for letter in plain_text:
        position =alphabet.index(letter)
        new_position=position+shift_amount
+        new_letter=alphabet[new_position]
        ciper_text+=new_letter
    print(f"the encoded text is {ciper_text}")
def decrypt(ciper_text,shift_amount):
    plain_text=""
    for letter in ciper_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text+=alphabet[new_position]
    print(f"the decoded text is {plain_text}")
if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(ciper_text=text,shift_amount=shift)
else:
    print("enter the correct option")
    
