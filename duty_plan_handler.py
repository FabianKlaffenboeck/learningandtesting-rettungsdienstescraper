import requests

from data_objects import Duty


def get_own_duties(credentials):
    data = {
        'year': '',
        'month': '',
        'dateDescendingSort': 'true',
        'max': '30',
        'orgUnit': '',
        'withSubOrgs': 'on',
        'form.event.onsubmit': 'searchForm',
    }

    response = requests.post(
        'https://dienstplan.o.roteskreuz.at/StaffPortal/duties/data/load.json',
        cookies={'PHPSESSID': credentials[0]},
        headers=credentials[1],
        data=data,
    )

    return response.json()['data']


def parse_duties_json(data_json):
    duties = []

    for value in data_json:
        other_entities = list(value['allocationInfo'].values())[0]
        duties.append(
            Duty(
                uid=value['guid'],
                from_data=value['begin'],
                duty_type=other_entities[0].split(" ")[1],
                to_data=value['end'],
                duration=value['duration'],
                other_person=other_entities[1:]
            )
        )

    return duties
