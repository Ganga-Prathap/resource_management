# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdminResourcesAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAdminResourcesAPITestCase::test_case body'] = {
    'resources': [
        {
            'description': 'description-0',
            'link': 'https://link-0',
            'resource_id': 1,
            'resource_name': 'resource_name-0',
            'thumbnail': 'https://thumbnail-0'
        },
        {
            'description': 'description-1',
            'link': 'https://link-1',
            'resource_id': 2,
            'resource_name': 'resource_name-1',
            'thumbnail': 'https://thumbnail-1'
        }
    ],
    'total_resources': 2
}

snapshots['TestCase01GetAdminResourcesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '337',
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
