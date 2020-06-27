# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetResourceItemsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetResourceItemsAPITestCase::test_case body'] = {
    'items': [
        {
            'description': 'description-0',
            'item_id': 1,
            'link': 'https://link0',
            'resource_name': 'resource_name-0',
            'title': 'title-0'
        },
        {
            'description': 'description-1',
            'item_id': 2,
            'link': 'https://link1',
            'resource_name': 'resource_name-0',
            'title': 'title-1'
        }
    ],
    'total_items': 2
}

snapshots['TestCase01GetResourceItemsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '287',
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
