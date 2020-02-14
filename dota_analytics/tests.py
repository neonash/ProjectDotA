from django.test import TestCase

from dota_analytics.services import fetchdata_service


class FetchParseDataTest(TestCase):
    """Class to test the UnitTest Case for the Parsing of Data from the Template into View"""

    def test_func_tester(self):
        """Function to test the parsing of Inputted data"""
        test_list = [{'player': 'r1', 'gold': '9000', 'xp': '8897', 'health': '1162', 'level': '14', 'hero_id': '9'}, {'player': 'r2', 'gold': '6633', 'xp': '7179', 'health': '1040', 'level': '12', 'hero_id': '27' }, {'player': 'r3', 'gold': '10232', 'xp': '11261', 'health': '1950', 'level': '15', 'hero_id': '76'}, {'player': 'r4', 'gold': '5053', 'xp': '5073', 'health': '179', 'level': '9', 'hero_id': '26'}, {'player': 'r5', 'gold': '6319', 'xp': '7160', 'health': '0', 'level': '12', 'hero_id': '63'}, {'player': 'd1', 'gold': '12678', 'xp': '11676', 'health': '594', 'level': '16', 'hero_id': '44'}, {'player': 'd2', 'gold': '6683', 'xp': '8200', 'health': '1670', 'level': '13', 'hero_id': '36'}, {'player': 'd3', 'gold': '8032', 'xp': '9487', 'health': '1080', 'level': '14', 'hero_id': '11'}, {'player': 'd4', 'gold': '4794', 'xp': '5069', 'health': '1080', 'level': '9', 'hero_id': '3'}, {'player': 'd5', 'gold': '4225', 'xp': '4661', 'health': '1340', 'level': '9', 'hero_id': '84'}]
        test_matchid = 'nan6wjhp'
        print(type(test_list))
        actual_op = fetchdata_service.formatNewInputMatchData(test_list,test_matchid)
        self.assertEqual(str(actual_op.reset_index(drop=True).loc[0, 'r1_gold']), '9000')