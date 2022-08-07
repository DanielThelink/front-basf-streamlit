from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
import re

class SimpleGroupedColorFunc(object):

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

def separe_text_by_group(data : list):

    green_words = []
    yellow_words = []

    for i in data:

        text = i['texto'].lower()
        splited_text = text.split()

        if i['classificacao_nps'] == "Promotor":
            for text in splited_text:
                green_words.append(text)

        elif i['classificacao_nps'] == "Neutro":
            for text in splited_text:
                yellow_words.append(text)

    return {

        '#0DFF00' : green_words,
        '#FFF200' : yellow_words,

    }

def covert_data_text_to_string(data : list) :

    data_to_string = ''

    for i in data:
        for key, value in i.items():
            if key == 'texto':
                data_to_string += ' ' + value
    
    return data_to_string


def draw_word_cloud(data : list):

    text = covert_data_text_to_string(data)
    
    wc = WordCloud(background_color="white", collocations=False).generate(text.lower())

    color_to_words = separe_text_by_group(data)

    default_color = '#92140C'

    grouped_color_func = GroupedColorFunc(color_to_words, default_color)

    wc.recolor(color_func=grouped_color_func)

    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    
    return plt