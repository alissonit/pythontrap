import requests
import json
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        api_cep = "https://viacep.com.br/ws/"
        path = func(*args, **kwargs)
        response = requests.get(api_cep+path)

        return response.content
    return wrapper

@decorator
def find_cep(cep, re_format):
    """
    :param cep: number of the CEP.
    :param re_format: CEP return format (json|xml|PIPED)
    :info: https://viacep.com.br/
    """
    path = f"{cep}/{re_format}"
    return path

@decorator
def get_cep(uf, city, place, re_format):

    """
    :param UF: state abbreviation.
    :param city: city's name.
    :param place: place to be found.
    """
    path = f"{uf}/{city}/{place}/{re_format}/"

    return path 

if __name__ == "__main__":
    
    print(get_cep.__name__) #functools wraps
    print(get_cep.__doc__) #functools wraps

    re_format = "xml"
    consult_cep = get_cep(uf="SP", city="Santo Andre", place="Centro", re_format="json")
    all_cep = json.loads(consult_cep)

    for cep in all_cep:
        info_cep = find_cep(cep=cep['cep'], re_format=re_format)
        print(info_cep)