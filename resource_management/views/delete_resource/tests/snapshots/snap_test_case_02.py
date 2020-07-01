# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02DeleteResourceAPITestCase::test_case status'] = 400

snapshots['TestCase02DeleteResourceAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'UNAUTHORIZED_USER',
    'response': 'You are not admin'
}

snapshots['TestCase02DeleteResourceAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '93',
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
