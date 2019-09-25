def ispalindrome(string):
	position_left = 0
	position_right = len(string) - 1
	
	while position_right >= position_left:
		if not string[position_left] == string[position_right]:
			return False
		position_left += 1
		position_right -= 1
	return True
print(ispalindrome('Shyam')) 
