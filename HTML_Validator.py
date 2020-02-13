#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    s = _extract_tags(html)
    if len(s) < 2:
        return False
    #print(s)
    left = 0
    right = len(s)-1
    while (left < right):
        open = s[left]
        close = s[right]
        if open[1:-1] != close[2:-1]:
            return False
        right -= 1
        left += 1
    return True

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    s=[]
    for i in range(len(html)):
        temp = ''
        symbol = html[i]
        if symbol == '<' :
            while symbol != '>':
                temp += symbol
                i = i+1
                symbol = html[i]
            temp += '>'
            s.append(temp)
    return s
