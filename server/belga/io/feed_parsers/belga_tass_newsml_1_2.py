# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.appendsourcefabric.org/superdesk/license

from superdesk.io.registry import register_feed_parser
from .base_belga_newsml_1_2 import BaseBelgaNewsMLOneFeedParser
from superdesk.utc import local_to_utc


class BelgaTASSNewsMLOneFeedParser(BaseBelgaNewsMLOneFeedParser):
    """Feed Parser for Belga specific TASS NewsML."""

    NAME = 'belga_tass_newsml12'
    label = 'Belga specific TASS News ML 1.2 Parser'

    def can_parse(self, xml):
        # TODO clarify version
        return xml.tag == 'NewsML' and xml.get('Version', '1.2') == '1.2'

    def parser_newsmanagement(self, item, manage_el):
        super().parser_newsmanagement(item, manage_el)
        tz = 'Europe/Moscow'
        item['firstcreated'] = local_to_utc(tz, item['firstcreated'])
        item['versioncreated'] = local_to_utc(tz, item['firstcreated'])


register_feed_parser(BelgaTASSNewsMLOneFeedParser.NAME, BelgaTASSNewsMLOneFeedParser())
