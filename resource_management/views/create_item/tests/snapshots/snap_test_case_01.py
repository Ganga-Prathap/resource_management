# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateItemAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateItemAPITestCase::test_case body'] = {
    'response': 'created successfully'
}

snapshots['TestCase01CreateItemAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '36',
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