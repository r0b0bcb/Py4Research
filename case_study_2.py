

# Uses def from lang_proc.py

# 1: Check for books named 'Hamlet' then store all in a pandas dataframe 

hamlets = pd.DataFrame(columns=("language", "text"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

# 2: Create Pandas Dataframe to record words and their useage frequency

language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)
data = pd.DataFrame({"word": list(counted_text.keys()), "count": list(counted_text.values())})

# 3: Add two more columns to previous dataframe; one for word length and other for frequency qualifier

data["length"] = data['word'].str.len()
def frequency(count):
    if count == 1:
        return "unique"
    elif count > 10:
         return "frequent"
    else:
         return "infrequent"
data["frequency"] = data['count'].apply(frequency)

# 4: New dataframe that pulls data from previous dataframe

sub_data = pd.DataFrame({
    "language" : language,
    "frequency" : ["frequent", "infrequent", "unique"],
    "mean_word_length" : data.groupby(by = "frequency")["length"].mean(),
    "num_words" : data.groupby(by = "frequency")["count"].size()
})

# 5: Above code is called summarize_text & returns sub_data. 

grouped_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])
# I used "grouped_data=pd.DataFrame({})"
for loop in range (hamlets.shape[0]): #and "(0, len(hamlets))" which gave me an identical output, but datacamp didn't like it.
    language, text = hamlets.iloc[loop]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
   
# 6: Plot the stats

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show()

