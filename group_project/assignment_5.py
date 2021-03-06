def positions(a_string, first_word, second_word, third_word):
    
    if first_word in a_string:
        pos1 = a_string.find(first_word)
    else:
        pos1 = "-"
    
    if second_word in a_string:
        pos2 = a_string.find(second_word)
    else:
        pos2 = "-"
    
    if third_word in a_string:
        pos3 = a_string.find(third_word)
    else:
        pos3 = "-"
    
    
    return "{},{},{}".format(str(pos1),str(pos2),str(pos3))
    
 
print (positions("Python is good. Python is Wise. I like Python", 'Python', 'Wise', 'like' ))

def test_three_occurrences():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'like') == "0,26,34"


def test_two_occurrences_missing_third():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'Ruby') == "0,26,-"


def test_two_occurrences_missing_first():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Ruby', 'Wise', 'like') == "-,26,34"


def test_one_occurrence_first_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Javascript', 'Ruby') == "0,-,-"


def test_one_occurrence_second_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'like', 'Ruby') == "-,34,-"


def test_one_occurrence_third_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'Ruby', 'Wise') == "-,-,26"
