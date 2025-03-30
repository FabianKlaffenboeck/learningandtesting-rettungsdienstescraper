import requests

from data_objects import Duty, Selve_duty
from collections import defaultdict, OrderedDict
from datetime import datetime


def get_duty_plan_json(credentials,from_date, to_date):
    data = {
        'orgUnitDataGuid': 'ce1489c70eecc69d9c43cc510aa3fc0f646ce68a_2_1551851993_2274',
        'withSubOrgUnits': '1',
        'dateFrom': '' + from_date + 'T00:00:00.000Z',
        'dateTo': '' + to_date + 'T00:00:00.000Z',
        'sortPlan': 'false',
    }

    response = requests.post(
        'https://dienstplan.o.roteskreuz.at/StaffPortal/plan/data/loadPlan.json',
        cookies={'PHPSESSID': credentials[0]},
        headers=credentials[1],
        data=data,
    )

    return response.json()['data']


def parse_duty_plan_json(data_json):
    duties = []

    for key, value in data_json.items():
        duties.append(Duty(key, value['begin'], value['end'], value['additionalInfos']['ressource_name']))

    grouped_by_from_data = defaultdict(list)
    for duty in duties:
        if duty.person_name:
            grouped_by_from_data[duty.from_data].append(duty)

    sorted_grouped_by_from_data = OrderedDict(
        sorted(
            grouped_by_from_data.items(),
            key=lambda item: datetime.strptime(item[0], "%Y-%m-%dT%H:%M:%SZ")  # Parse ISO 8601 date
        )
    )

    return sorted_grouped_by_from_data
