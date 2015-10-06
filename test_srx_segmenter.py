import os
import unittest

import srx_segmenter


class SegmenterTest(unittest.TestCase):
    def setUp(self):
        srx_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'segment.srx')
        print(srx_filepath)
        self.rules = srx_segmenter.parse(srx_filepath)

    def test_ja(self):
        table = [
            {
                'expect': (
                    ["おはよう。", "こんにちは。"],
                    ["", "", ""]
                ),
                'source': ("おはよう。こんにちは。"),
                'language': 'Japanese',
            },
            {
                'expect': (
                    ["Hello.", "This is an example."],
                    ["", " ", ""]
                ),
                'source': ("Hello. This is an example."),
                'language': 'English',
            }
        ]

        for test in table:
            segmenter = srx_segmenter.SrxSegmenter(self.rules[test['language']], test['source'])
            self.assertEqual(test['expect'], segmenter.extract())
