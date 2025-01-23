
fname = open(r"C:\Users\Mashigo\Python Projects\Word Counter\Python-Word-Counter\Python word counter.txt", "r")
data = fname.read()

# Function to count words
def WordCounter(data):
    Words = data.split()  # Split by whitespace into words
    Num = len(Words)
    return Num

# Function to count lines
def CountLines(data):
    Lines = data.split("\n")  # Split by newline into lines
    Nums = len(Lines)
    return Nums

# Function to count characters
def CountChars(data):
    NumChars = len(data)  # Total number of characters
    return NumChars

# Get counts
Num = WordCounter(data)
Nums = CountLines(data)
NumChars = CountChars(data)

# Print results
print("Number of words in the text file is: " + str(Num))
print("Number of lines in the text file is: " + str(Nums))
print("Number of characters in the text file is: " + str(NumChars))

# Close the file
fname.close()
