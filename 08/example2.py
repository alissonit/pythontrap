#EXEMPLO USANDO FUNÇÃO :)
def get_rapper_country(rapper):

    if rapper in rappers_country["BR"]:
            print(f"Rapper BR: {rapper}")
    elif rapper in rappers_country["US"]:
        print(f"Rapper US: {rapper}")
    else:
        print(f"Rapper not found in lists: {rapper}")

if __name__ == '__main__':
    
    rappers_choice = ["L7NNON", "KB", "Trip Lee", "Travis Scott", ["Lecrae", "Projota", "Tupac"], "Don Omar"]

    rappers_country = {"BR":["Hungria", "Kamau", "Projota", "Mano Brown", "Luo", "L7NNON"],
        "US":["Tupac", "Drake", "Eminem", "KB", "Kanye West", "Lecrae", "Travis Scott", "Trip Lee"]}
        
    for rp in rappers_choice:
        if isinstance(rp, list):
            for rp_one in rp:
                get_rapper_country(rp_one)
        else:
            get_rapper_country(rp)