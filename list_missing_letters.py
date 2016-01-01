def list_missing_letters(string):
	alphabet = "abcdefghijklmnopqrstuvwxz"
	missing_letters = sorted(set(alphabet) - set(string.lower()))
	print ''.join(missing_letters)

list_missing_letters(raw_input("Enter text to know which letters it misses from being pangram: "))
