import requests

from data_objects import Selve_duty


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
        duties.append(Selve_duty(value['guid'], value['begin'], value['end'], value['duration'],
                                 list(value['allocationInfo'].values())[0]))

    return duties
