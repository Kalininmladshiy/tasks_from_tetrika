import requests


def get_animals():
    animals = []
    cmcontinue_value = ''
    while True:
        payload = {
            "action": "query",
            "cmtitle": "Категория:Животные по алфавиту",
            "cmlimit": 40500,
            "list": "categorymembers",
            "format": "json",
            "cmcontinue": f'{cmcontinue_value}'
        }
        response = requests.get(
            "https://ru.wikipedia.org/w/api.php",
            params=payload,
        )
        response.raise_for_status()
        for categorymember in response.json()['query']['categorymembers']:
            if categorymember['title'].startswith('A'):
                break
            animals.append(categorymember['title'])
        cmcontinue_value = response.json()['continue']['cmcontinue']
        if categorymember['title'].startswith('A'):
            break
    return animals


if __name__ == "__main__":
    count_animals = {}
    for animal in get_animals():
        count_animals[animal[0]] = count_animals.get(animal[0], 0) + 1
    for animal, count in sorted(count_animals.items()):
        print(f'{animal}: {count}')
