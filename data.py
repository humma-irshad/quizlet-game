import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}

source = requests.get('https://opentdb.com/api.php', params = parameters)
question_data = source.json()['results']