from django import template



register = template.Library()

@register.filter(name='new_slice')


def new_slice(string,count):
    count_str=1
    result=""
    for i in string:
        if count_str>=count and i==" ":
            result=string[:count_str]
            break

        elif count_str>=count_str and i != " ":
            result=string[:count]

        count_str+=1
    return result
    
    


