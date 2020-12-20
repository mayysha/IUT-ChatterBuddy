import spacy
import random
import for_iut_related
import for_simple_convo
import Extract_Word
import machine_learning

nlp = spacy.load('en_core_web_lg')


def bot_answer(question):
    returning = ''
    flag = 0
    flag1 = 0
    flag2 = 0
    extracted_question = Extract_Word.extractor(question)
    print(extracted_question)
    doc = nlp(extracted_question)

    dict = machine_learning.dict

    for dict_question, dict_answer in dict.items():
        if question == dict_question:
            returning = dict_answer
            return returning

    for token in doc:
        if token.text in for_iut_related.keywords:
            returning = for_iut_related.keywords[token.text]
            return returning
            flag = 1
            break

    if flag == 0:
        for token in doc:
            str1 = nlp(token.text)
            for t in for_iut_related.keywords:
                str2 = nlp(t)
                print(str1.similarity(str2))
                if (str1.similarity(str2)) > .5:
                    returning = for_iut_related.keywords[t]
                    return returning
                    flag1 = 1
                    break
            if flag1 == 1:
                break

    if flag1 == 0:
        for key, values in for_simple_convo.intents.items():
            if key in question:
                returning = random.choice(for_simple_convo.intents[key])
                return returning
        for token in doc:
            str1 = nlp(token.text)
            for t in for_simple_convo.intents:
                str2 = nlp(t)
                print(str1.similarity(str2))
                if (str1.similarity(str2)) > .73:
                    returning = random.choice(for_simple_convo.intents[t])
                    return returning
                    flag2 = 1
                    break
            if flag2 == 1:
                break
            else:
                returning = random.choice(for_simple_convo.continuing_answers)
                return returning

    return returning
