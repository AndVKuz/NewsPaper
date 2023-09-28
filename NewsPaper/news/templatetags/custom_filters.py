from django import template


register = template.Library()


unwanted_words = ['База', 'помидор', 'огурец', 'чеснок']

@register.filter()
def censor(value):
    text = value.split()
    for i, word in enumerate(text):
        print(word)
        if word in unwanted_words:
            text[i] = word[0] + '****'
        return ' '.join(text)
