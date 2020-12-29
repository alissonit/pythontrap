#EXEPLO USANDO MULTIPLOS PARAMETROS E FUNÇÕES
def get_rapper_country_two(rapper, rappers_country, found_rappers=[], message="rapper born in"):
    
    for country, rappers in rappers_country.items():
        if rapper in rappers:
            print(f"{message} {country}: {rapper}")
            found_rappers.append(rapper)

    if rapper not in found_rappers:
        print(f"rapper not found: {rapper}")

if __name__ == '__main__':
    
    rappers_choice = ["L7NNON", "KB", "Trip Lee", "Travis Scott", ["Lecrae", "Projota", "Tupac"], "Don Omar"]

    rappers_country = {"BR":["Hungria", "Kamau", "Projota", "Mano Brown", "Luo", "L7NNON"],
        "US":["Tupac", "Drake", "Eminem", "KB", "Kanye West", "Lecrae", "Travis Scott", "Trip Lee"]}

    for rp in rappers_choice:
        if isinstance(rp, list):
            for rp_one in rp:
                get_rapper_country_two(rp_one, rappers_country, message="[from isinstance] rapper born in")
        else:
            get_rapper_country_two(rp, rappers_country)