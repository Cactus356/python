**Version 1.0 - 2/15/24**
* Initial release
* Uses 7,777 words from the EFF large wordlist (https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) for username and passphrase generation
* Generates username (Optional) comprised of a random word + random four digit number
* Generates password
	* 8 - 128 characters
	* Default characterset, optional user defined sets
 		* Checks to ensure at least one of each character set, whether default or user defined, is in the generated password
* Generates passphrase
	* 3 - 40 words
	* Default 'space' word separator, optional user defined character
	* Optional add a random two digit number after a random word in passphrase
* Both passwords and passphrases can be regenerated with the same settings, or program can restart to the beginning to change parameters
