def iter_palindrome(s):
	for i in range(0, len(s)/2):
		if s[i] != s[-(i+1)]:
			return False
	return True

print iter_palindrome('')
#>>> True
print iter_palindrome('abab')
#>>> False
print iter_palindrome('abba')
#>>> True
