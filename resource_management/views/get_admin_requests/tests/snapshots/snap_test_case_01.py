# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdminRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAdminRequestsAPITestCase::test_case body'] = {
    'requests': [
        {
            'access_level': 'READ',
            'due_date_time': '2020-06-27T09:06:11Z',
            'item_name': 'title-0',
            'profile_pic': 'profile_pic-0',
            'request_id': 1,
            'resource_name': 'resource_name-0',
            'username': 'username-0'
        }
    ],
    'total_requests': 2
}

snapshots['TestCase01GetAdminRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '237',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
