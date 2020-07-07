outputLinks = []

with open("links.txt", "r") as f:
	inputLinks = f.readlines()

removedLinks = len(inputLinks)
print("Links removed: " + str(removedLinks))

with open("output_links.txt", "w") as f:
	for link in inputLinks:
		if link not in outputLinks:
			removedLinks -= 1
			f.write(link)
			outputLinks.append(link)

print("Links removed: " + str(removedLinks))
