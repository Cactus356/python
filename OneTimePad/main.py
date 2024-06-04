import secrets
import string
import math
import random

forbidden_chars = string.digits + string.punctuation + string.whitespace
message = ""
custom_otp = ""
random_otp = ""
hybrid_otp = ""
otp_choice = ""
encrypted_message = ""
otp_input = ""
decrypted_message = ""

print("One-time pad tool v1.0. Created by J.N.")
print("Encrypt and/or decrypt a message using a one-time pad (OTP) that is either random, user defined, or both.")
print("Can also generate a list of OTPs to be used at a later time")
print("All computer RNG is done using secrets.random")


def encrypt():
    global message, custom_otp, random_otp, hybrid_otp, otp_choice
    while True:  # Ref 2 - Enter message to be encrypted
        message = input("\nEnter the message you want to encrypt (letters only, 256 character max), enter 9 to return: ")
        if message == "9":
            break  # Quits Ref2
        elif any(char in forbidden_chars for char in message):  # Checks for forbidden characters in message
            print(f'*** You can only enter letters, please try again ***')
            continue  # Ref2 - Re-enter message
        elif len(message) > 256 or len(message) < 1:  # Checks message against defined max length
            print(f'*** Message needs to be between 1 and 256 characters, please try again ***')
            continue  # Ref2 - Re-enter message
        while True:  # Ref 1 - Pick to either define your own or generate a one-time pad
            otp_length = len(str(message))
            otp_choice = input("\nEnter 1 to use a custom OTP, enter 2 to use a random OTP, enter 3 to use a hybrid OTP, enter 9 to return: ")
            if otp_choice == "1":  # Using a custom OTP
                print(f"\nYour OTP needs to be the same length as your message, which was {otp_length} characters")
                while True:  # Ref 3 - Enter custom OTP
                    custom_otp = input("\nEnter your custom OTP now (letters only), enter 9 to return: ")
                    if custom_otp == "9":
                        break  # Quits Ref3
                    elif any(char in forbidden_chars for char in custom_otp):  # Checks for forbidden characters in OTP
                        print(f'*** You can only enter letters, please try again ***')
                        continue  # Ref3 - Re-enter custom OTP
                    elif len(str(message)) != len(str(custom_otp)):
                        print(f'*** Your OTP length must match your message length, please try again ***')
                        continue  # Ref3 - Re-enter custom OTP
                    else:
                        crypter()
                        print(str.upper(f"\nPlaintext message: {message}"))
                        print(str.upper(f"Your OTP: {custom_otp}"))
                        print(str.upper(f"Encrypted message: " + ''.join(encrypted_message)))
                    break  # Quits Ref3
                break  # Quits Ref1
            elif otp_choice == "2":  # Using a random OTP
                print(f"\nGenerating a random OTP that is {otp_length} characters long.")
                random_otp = str(''.join(secrets.choice(string.ascii_lowercase) for _ in range(otp_length)))
                crypter()
                print(str.upper(f"\nPlaintext message: {message}"))
                print(str.upper(f"Random OTP: {random_otp}"))
                print(str.upper(f"Encrypted message: " + ''.join(encrypted_message)))
                break  # Quits Ref1
            elif otp_choice == "3":  # Using a hybrid random and user generated OTP
                hybrid_random_length = math.floor(otp_length / 2)
                hybrid_user_length = otp_length - hybrid_random_length
                while True:  # Ref11 - Using a hybrid OTP
                    hybrid_random_input = str(''.join(secrets.choice(string.ascii_lowercase) for _ in range(hybrid_random_length)))
                    print(f"\nRandomly generating {hybrid_random_length} of the {otp_length} characters for the OTP")
                    hybrid_user_input = input(f"\nEnter the remaining {hybrid_user_length} characters now, or enter 9 to return: ")
                    if hybrid_user_input == "9":
                        break  # Quits Ref11
                    elif any(char in forbidden_chars for char in hybrid_user_input):  # Checks for forbidden characters in OTP
                        print(f'*** You can only enter letters, please try again ***')
                        continue  # Ref11 - Re-enter custom OTP
                    elif hybrid_user_length != len(str(hybrid_user_input)):
                        print(f'*** Your OTP length must match your message length, please try again ***')
                        continue  # Ref11 - Re-enter custom OTP
                    else:
                        hybrid_otp = ''.join(random.sample(hybrid_user_input + hybrid_random_input, len(message)))
                        crypter()
                        print(str.upper(f"\nPlaintext message: {message}"))
                        print(str.upper(f"Hybrid OTP: {hybrid_otp}"))
                        print(str.upper(f"Encrypted message: " + ''.join(encrypted_message)))
                    break  # Quits Ref11
                break  # Quits Ref1
            elif otp_choice == "9":
                break  # Quits Ref1
            else:
                print("Input not accepted, please try again")
                continue  # Ref1 - Restarts
        break  # Quits Ref2


def crypter():
    global encrypted_message
    message_numerical = [ord(i) - 96 for i in str.lower(message)]  # Turns each character into it's numerical location in the alphabet
    if otp_choice == "1":
        custom_otp_numerical = [ord(i) - 96 for i in str.lower(custom_otp)]  # Turns each character into it's numerical location in the alphabet
        enc_combined_numerical = [message_numerical[i] + custom_otp_numerical[i] - 1 for i in range(len(message_numerical))]  # Adds the OTP to the message and subtracts 1
    elif otp_choice == "2":
        random_otp_numerical = [ord(i) - 96 for i in random_otp]  # Turns each character into it's numerical location in the alphabet
        enc_combined_numerical = [message_numerical[i] + random_otp_numerical[i] - 1 for i in range(len(message_numerical))]  # Adds the OTP to the message and subtracts 1
    else:
        hybrid_otp_numerical = [ord(i) - 96 for i in str.lower(hybrid_otp)]  # Turns each character into it's numerical location in the alphabet
        enc_combined_numerical = [message_numerical[i] + hybrid_otp_numerical[i] - 1 for i in range(len(message_numerical))]  # Adds the OTP to the message and subtracts 1
    for i in range(len(enc_combined_numerical)):  # Checks for needing to "roll over" past Z
        if enc_combined_numerical[i] > 26:  # Finds any entries greater than 26
            enc_combined_numerical[i] = enc_combined_numerical[i] - 26  # If found, replaces entry with 26 less - ie Y + Y = 50, so result is 24
    encrypted_unicode = [enc_combined_numerical[i] + 64 for i in range(len(enc_combined_numerical))]  # Convert back to uppercase unicode for chr()
    encrypted_message = [chr(i) for i in encrypted_unicode]  # Turns each unicode entry back into it's letter


def decrypt():
    global message, otp_input
    while True:  # Ref 21 - Enter message to be decrypted
        message = input("\nEnter your encrypted message (letters only, 1-256 characters), enter 9 to return: ")
        otp_length = len(str(message))
        if message == "9":
            break  # Quits Ref21
        elif any(char in forbidden_chars for char in message):  # Checks for forbidden characters in message
            print(f'*** You can only enter letters, please try again ***')
            continue  # Ref21 - Re-enter message
        elif len(message) > 256 or len(message) < 1:  # Checks message against defined length
            print(f'*** Message needs to be between 1 and 256 characters, please try again ***')
            continue  # Ref21 - Re-enter message
        while True:  # Ref 31 - Enter OTP to decrypt the message
            otp_input = input(f"\nEnter your OTP ({otp_length} characters), enter 9 to return: ")
            if otp_input == "9":
                break  # Quits Ref31
            elif any(char in forbidden_chars for char in otp_input):  # Checks for forbidden characters in OTP
                print(f'*** You can only enter letters, please try again ***')
                continue  # Ref31 - Re-enter OTP
            elif len(str(message)) != len(str(otp_input)):
                print(f'*** Your OTP length must match your message length, please try again ***')
                continue  # Ref31 - Re-enter OTP
            else:
                decrypter()
                print(str.upper(f"\nEncrypted message: {message}"))
                print(str.upper(f"OTP: {otp_input}"))
                print(str.upper(f"Decrypted message: " + ''.join(decrypted_message)))
            break  # Quits Ref31
        break  # Quits Ref21


def decrypter():
    global decrypted_message
    enc_message_numerical = [ord(i) - 96 for i in str.lower(message)]  # Turns each character into it's numerical location in the alphabet
    otp_numerical = [ord(i) - 96 for i in str.lower(otp_input)]  # Turns each character into it's numerical location in the alphabet
    dec_combined_numerical = [enc_message_numerical[i] - otp_numerical[i] + 1 for i in range(len(enc_message_numerical))]  # Adds the OTP to the message and subtracts 1
    for i in range(len(dec_combined_numerical)):  # Checks for needing to "roll over" past Z
        if dec_combined_numerical[i] < 0:  # Finds any negative entries
            dec_combined_numerical[i] = dec_combined_numerical[i] + 26  # If found, replaces entry with 26 more - ie C - E = -2, so result is 24
    decrypted_unicode = [dec_combined_numerical[i] + 64 for i in range(len(dec_combined_numerical))]  # Convert back to uppercase unicode for chr()
    decrypted_message = [chr(i) for i in decrypted_unicode]  # Turns each unicode entry back into it's letter


def otp_generator():
    print("\nNow generating 256 character OTP(s)")
    while True:  # Ref88
        amount = input(f"\nEnter amount of OTPs to generate (1-100), or enter 0 to return: ")
        if any(char in string.ascii_letters + string.punctuation + string.whitespace for char in amount):  # Checks for forbidden characters in message
            print(f'\n*** You can only enter numbers, please try again ***')
            continue  # Ref2 - Re-enter message
        elif amount == "0":
            break  # Quits Ref88
        elif int(amount) < 1 or int(amount) > 100:  # Too short or too long
            print("\nInput out of range, please try again")
            continue  # Back to Ref88
        else:
            for i in range(int(amount)):
                full_random_otp = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(256))
                print(full_random_otp)
                continue


while True:  # Ref99 - Choose to either encrypt or decrypt a message
    encrypt_decrypt = input("\nPress 1 to encrypt a message, press 2 to decrypt a message, 3 to generate a list of OTPs, 9 to quit: ")
    if encrypt_decrypt == "1":
        encrypt()
        continue
    elif encrypt_decrypt == "2":
        decrypt()
        continue
    elif encrypt_decrypt == "3":
        otp_generator()
        continue
    elif encrypt_decrypt == "9":
        break  # Quits Ref99
    else:
        continue  # Restart Ref99
