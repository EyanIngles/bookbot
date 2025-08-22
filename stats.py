
def get_book_text(file_name):
    file_contents = ""
    with open(file_name) as f:
        file_contents = f.read()
    split = file_contents.split()
    length = len(split)
    return length

def get_number_symbols(file_name):
    file_content = {}
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    with open(file_name) as f:
        file = f.read().lower()
        dicti = {}
        for f in file:
           
            if f in dicti:
              
            #increase value by 1 if is true by using f as key value
                dicti[f] = dicti[f]+1
            else:
                dicti[f] =1
        return dicti

def sort_dict(sorting): 
    sorting = sorted(sorting.items(), key=lambda item: item[1])
    new_sort = {}
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    for s in sorting:
        if s[0] in alphabet:
            item = s[1]
            cha = s[0]
            new_sortings = {"char":cha, "num": item}
            new_sort[cha] = new_sortings
        else:
            pass 
    return new_sort 


#prin = get_number_symbols("./books/frankenstein.txt")
#sorting = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894}
#prin = test_idea(sorting)
#print(prin)
