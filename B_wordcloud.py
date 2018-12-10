from wordcloud import WordCloud
import matplotlib.pyplot as plt
import Aa_words

def gen_wordcloud(filename, output_png):
    '''
    parameter: string filename and string outfile name (.png format)
    return: None - save a wordcloud png as output_png
    '''
    words = Aa_words.all_words(filename, True)
    text = ''
    for word in words:  # accumulate into big string
        text += ' {}'.format(word)
    wordcloud = WordCloud().generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(output_png)
    plt.close()