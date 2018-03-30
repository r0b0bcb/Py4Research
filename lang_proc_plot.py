# # # # # # # # # # # #
# Language Processing #
# r0b0bcb             #
# 3/28/18             #
# # # # # # # # # # # #

from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

def count_words(text):
	""" 
	Counts words in string and gives dictionary with words as keys and value as number of repititions.
	Error corrects by changing all letters to lowercase and removing . , ; : ! ? ' "
	"""
	text = text.lower()
	skips = [".", ",", ";", ":", "!", "?", "'", '"']
	for punt in skips:
		text = text.replace(punt, "")

	word_counts = {}
	for word in text.split(" "):
		# Known words
		if word in word_counts:
			word_counts[word] += 1
		# Unknown words
		else:
			word_counts[word] = 1
	return word_counts

def count_words_fast(text):
	""" 
	Counts words in string with collections.counter
	Error corrects by changing all letters to lowercase and removing . , ; : ! ? ' "
	"""
	text = text.lower()
	skips = [".", ",", ";", ":", "!", "?", "'", '"']
	for punt in skips:
		text = text.replace(punt, "")

	word_counts = Counter(text.split(" "))
	return word_counts

def read_book(title_path):
	"""
  Read book, make it into string
  """
	with open(title_path, "r", encoding="utf8") as current_file:
		text = current_file.read()
		text = text.replace("\n", "").replace("\r", "")
	return text

def word_stats(word_counts):
	"""
  Return # unique words and frequencies
  """
	num_unique = len(word_counts)
	counts = word_counts.values()
	return (num_unique, counts)

book_dir = "./Books" #Change to whever ever the folder is stored

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
for language in os.listdir(book_dir):
	if not language.startswith('.'):	#Must be included on mac to avoid dumb .DS_Store files
		for author in os.listdir(book_dir + "/" + language):
			if not author.startswith('.'):
					for title in os.listdir(book_dir + "/" + language + "/" + author):
						if not title.startswith('.'):
							inputfile = book_dir + "/" + language + "/" + author + "/" + title
							print(inputfile)
							text = read_book(inputfile)
							(num_unique, counts) = word_stats(count_words_fast(text))
							stats.loc[title_num] = language, author.capitalize(),title.replace(".txt", ""), sum(counts), num_unique
							title_num += 1

# Plot the book stats relative to language

plt.figure(figsize = (10,10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "1", label = "English", color = "blue")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "2", label = "French", color = "red")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "3", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "4", label = "Portuguese", color = "green")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("# Unique words")
plt.savefig("lang_plot.pdf")
