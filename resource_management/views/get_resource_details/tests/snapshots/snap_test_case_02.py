# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetResourceDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetResourceDetailsAPITestCase::test_case body'] = {
    'description': 'description-0',
    'link': 'https://link0',
    'resource_id': 1,
    'resource_name': 'resource_name-0',
    'thumbnail': 'https://thumbnail0'
}

snapshots['TestCase02GetResourceDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '146',
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
