import unittest
import regex_exercises


class TestRegexExercises(unittest.TestCase):

    def test_is_hex(self):
        self.assertFalse(regex_exercises.is_hex(""))
        self.assertFalse(regex_exercises.is_hex("X"))
        self.assertTrue(regex_exercises.is_hex("99"))
        self.assertTrue(regex_exercises.is_hex('0123999AADDEEE'))
        self.assertTrue(regex_exercises.is_hex('A24'))
        self.assertFalse(regex_exercises.is_hex('G0123999AADDEEE'))
        self.assertFalse(regex_exercises.is_hex('123XXX'))
        # Bonus points for adding the correct flag to the regular
        # expression to make it work with lower case as well and
        # extending the test.
        # self.assertTrue(regex_exercises.is_hex('a24'))

    def test_has_vowel(self):
        self.assertFalse(regex_exercises.has_vowel(""))
        self.assertTrue(regex_exercises.has_vowel('hello'))
        self.assertFalse(regex_exercises.has_vowel('spryly'))

    def test_split_words(self):
        test_sentence = "A   very, very_strange; sentence. indeed"
        expected = ["A", "very", "very", "strange", "sentence", "indeed"]
        self.assertEqual(regex_exercises.split_words(test_sentence), expected)

    def test_grouped_date(self):
        self.assertEqual(regex_exercises.grouped_date("2019-10-06"), ("2019", "10", "06"))

    def test_sub_digits(self):
        string = '1 AAA o0 99 ANBLD&C4CV 33'
        expected_output = 'X AAA oX XX ANBLD&CXCV XX'
        self.assertEqual(regex_exercises.sub_digits(string), expected_output)

    def test_date_rewrite(self):
        self.assertEqual(regex_exercises.date_rewrite('1/10/2018'), '2018-1-10')
        self.assertEqual(regex_exercises.date_rewrite('12/1/2018'), '2018-12-1')
        self.assertEqual(regex_exercises.date_rewrite('08/12/1974'), '1974-08-12')

    def test_findall_airportcodes(self):
        self.assertEqual(regex_exercises.findall_airportcodes(''), [])
        self.assertEqual(regex_exercises.findall_airportcodes('LAX'), ['LAX'])
        sentence = "This sentence has no aiport codes"
        self.assertEqual(regex_exercises.findall_airportcodes(sentence), [])
        sentence = "This sentence has DEN to DFW via ORD"
        self.assertEqual(regex_exercises.findall_airportcodes(sentence), ['DEN', 'DFW', 'ORD'])
        sentence = "This sentence lOOKs like two but only has LGW"
        self.assertEqual(regex_exercises.findall_airportcodes(sentence), ['LGW'])

    def test_valid_twenty_four_hour_time(self):
        self.assertTrue(regex_exercises.valid_times("00:00"))
        self.assertTrue(regex_exercises.valid_times("12:30"))
        self.assertTrue(regex_exercises.valid_times("23:59"))
        self.assertFalse(regex_exercises.valid_times(""))
        self.assertFalse(regex_exercises.valid_times("foo"))
        self.assertFalse(regex_exercises.valid_times("0000"))
        self.assertFalse(regex_exercises.valid_times("ab:cd"))
        self.assertFalse(regex_exercises.valid_times("23:61"))
        self.assertFalse(regex_exercises.valid_times("24:00"))


if __name__ == '__main__':
    unittest.main()
