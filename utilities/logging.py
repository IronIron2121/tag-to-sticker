# print to console with strong boundaries for clarity
def notif(given_str: str):
	print('\n')
	print('#' + "--"*(len(given_str)//2) + '#\n')
	print(given_str)
	print('\n#' + "--"*(len(given_str)//2) + '#\n')
