text = """Reading books offers a unique escape, transporting you to different worlds, times, and perspectives without ever leaving your chair,
fostering empathy and broadening understanding as you connect with diverse characters and complex ideas,
making it a truly enriching activity that sharpens the mind while providing relaxation and endless new discoveries.
"""
para_list = text.split()
print("The length of the paragraph: ",len(text))

palindrome = 0
for word in para_list:
    if word == word[::-1]:
        palindrome += 1

print("The number of palindrome present in the paragraph is ",palindrome)

for i in para_list:
    print(i[::-1], end=" ")