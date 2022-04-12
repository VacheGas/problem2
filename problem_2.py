


def isvowels(char_check):
	return (char_check.upper() in ['A', 'E', 'I', 'O', 'U'])
def count_vowels() :
	count_vowel = 0
	str_vowels = str(input("Please input string\n"))
	for char_check in str_vowels :
		if isvowels(char_check) == True :
			count_vowel += 1
	return count_vowel
		

print(count_vowels())