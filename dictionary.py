import json
from difflib import get_close_matches


# data = json.load(open("076 data.json"))

def dict_collector():
    """
    Collecting and converting the file 
    containing the json format datatype
    to a dictionary datatype.
    """
    data = json.load(
        open(
            "076 data.json"
        )
    )

    return data


if __name__ == '__main__':
    dictionary = dict_collector()


def translate_word(search, dictionary):
    """
    returns the search parameter of the function
    as the key and brings out the corresponding
    pair.
    If keyError, the phrase 'What you searched does not exist'
    returns.

    --- search = 'a string'
    --- dictionary = a func
    """

    search = search.lower().strip()
    close_match = get_close_matches(
        search, dictionary.keys(),
        n=5, cutoff=0.8
    )

    if search in dictionary:
        word_searched = dictionary[search]
    elif close_match:
        try_again = input(
            f'Do you mean {close_match[0]} instead?\n(y/n): '
        )
        if try_again.lower() == "y":
            return dictionary[close_match[0]]

        elif try_again.lower() == 'n':
            return "opps! word doesn't exist"

        else:
            return "Invalid entry, Try one of this: (y/n)"

    else:
        word_searched = "What you searched does not exist"

    return word_searched


search = input("What word do you want to search:\n")


if __name__ == '__main__':
    translate_word = translate_word(search, dictionary)


def looping_desc(word):

    num = 0
    if isinstance(word, list):
        for items in translate_word:
            num += 1
            print(f"{num}: {items}")
    else:
        print(word)


if __name__ == '__main__':
    looping_desc(translate_word)
