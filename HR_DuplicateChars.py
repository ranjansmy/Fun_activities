# In order to find duplicate characters

from collections import Counter

def find_dup_char(input_char):

	WC = Counter(input_char)
	j = -1
	
	for i in WC.values():
		j = j + 1
		if( i > 1 ):
			print WC.keys()[j],

# Driver program
if __name__ == "__main__":
	input_char = raw_input("Enter the string characters:") 
	find_dup_char(input_char)
