""" Implement a function
generate_sentences(subjects, predicates, objects)
that takes three lists of strings as parameters. The first argument is a list of words
that can be used as a subject in a sentence, the second { as a predicate, and the third
{ as an object. The function must return a string that contains all the sentences in
the alphabetical order that can be constructed using the provided subjects, predicates
and objects. (Note that the words in the list of subjects are not necessarily in the
alphabetical order, and the same applies to the lists of predicates and objects.) Each
sentence must be ended by "." and the sentences must be separated by " ".
Indicative test cases:
assert generate_sentences(["John", "Mary"], ["hates", "loves"],\
["apples", "bananas"])) == "John hates apples. John hates bananas. \
John loves apples. John loves bananas. Mary hates apples. \
Mary hates bananas. Mary loves apples. Mary loves bananas."
assert generate_sentences(["Vlad", "Hubie"], ["drives"],\
["car", "motorcycle, "bus"])) == "Hubie drives bus. Hubie drives car. \
Hubie drives motorcycle. Vlad drives bus. Vlad drives car. \
Vlad drives motorcycle." """

def generate_sentences(subjects, predicates, objects):
    sentence = []
    for sub in range(len(subjects)):
        for pred in range(len(predicates)):
            for obj in range(len(objects)):
                to_add = subjects[sub] + " " + predicates[pred] + " " + objects[obj] + "."
                sentence.append(to_add)
    sentence.sort()
    result = ""
    for sen in range(len(sentence)):
        result += sentence[sen] + " "
    return result
