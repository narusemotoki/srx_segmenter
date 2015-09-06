import os
import unittest

import srx_segmenter


class SegmenterTest(unittest.TestCase):
    def setUp(self):
        srx_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'segment.srx')
        self.rules = srx_segmenter.parse(srx_filepath)

    def test_ja(self):
        table = [
            {
                'expect': (
                    ["おはよう。", "こんにちは。"],
                    ["", "", ""]
                ),
                'source': ("おはよう。こんにちは。")
            },
        ]

        for test in table:
            segmenter = srx_segmenter.SrxSegmenter(self.rules['Japanese'], test['source'])
            self.assertEqual(test['expect'], segmenter.extract())
