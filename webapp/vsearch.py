def search4vowels(phrase:str) -> set:   
    """Returns the set of vowels found in 'phrase'""" 
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set:    
    """Retruns the set of 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))

    
