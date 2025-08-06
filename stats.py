
def word_count(path_to_file):
    word_list = get_book_txt(path_to_file).split()
    return word_list



def get_book_txt(path_to_file):
    with open(path_to_file, 'r', encoding="utf-8") as file:
        file_contents = file.read()
        return file_contents


def character_count(file_contents):
    characters = {}
    for char in file_contents:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sorted_list(text):
    character_dih = character_count(text)
    result = []
    for key, value in sorted(character_dih.items(), key=lambda kv: kv[1], reverse=True):
        if key.isalpha():
            result.append((key, value))
    return result


def formatted_text(text):
    result = ""
    for char, count in sorted_list(text):
        result += f"{char}: {count}\n"
    return result


