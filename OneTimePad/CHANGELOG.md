**Version 1.0 - 6/4/24**
* Initial release
* Encrypts or decrypts messages with a OTP and can generate a list of future OTPs
* Encrypting a message with a OTP
	* 1-256 characters
	* OTP can either be computer generated, user supplied, or a combination of both
 		* Checks length and characters for validity
* Decrypting a message with a OTP
	* 1-256 characters
	* OTP and the encrypted message are user supplied
 		* Checks length and characters for validity
* Prints 3 final lines: The original input (ie plaintext message), the OTP used, and the output (ie encrypted message)
* The OTP generator will create 256 character long OTPs, which the user to save for a future message
