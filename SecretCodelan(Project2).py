# Take input
st = input("Enter the message: ")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding: ")
coding = True if (coding == "1") else False

# Print coding choice
print(coding)

# If we are encoding the message
if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

# If we are decoding the message
else:
    nwords = []
    for word in words:
        if len(word) >= 6:  # Ensure word is long enough to remove prefixes and suffixes
            stnew = word[3:-3]  # Remove the first 3 and last 3 characters
            if len(stnew) > 1:
                stnew = stnew[-1] + stnew[:-1]  # Move last letter to the beginning
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))



