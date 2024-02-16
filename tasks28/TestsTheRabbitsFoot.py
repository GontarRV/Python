import unittest
from TheRabbitsFoot import TheRabbitsFoot

class TheRabbitsFootTests(unittest.TestCase):

    def tests_basic_true(self):
        self.assertEqual(TheRabbitsFoot('отдай мою кроличью лапку', True), 'омоюу толл дюиа акчп йрьк')

    def tests_basic_false(self):
        self.assertEqual(TheRabbitsFoot('омоюутоллдюиаакчпйрьк', False), 'отдаймоюкроличьюлапку')

    def tests_eng_true(self):
        self.assertEqual(TheRabbitsFoot('a test proposal to determine the correctness of the work', True),
                                        'apetct tothth eseene sarcew tlmoso ptirsr ronrok')
    
    def tests_eng_false(self):
        self.assertEqual(TheRabbitsFoot('apetct tothth eseene sarcew tlmoso ptirsr ronrok', False), 
                                        'atestprposaltoeterminthecorrctnessothework')
        
if __name__ == '__main__':
    unittest.main()