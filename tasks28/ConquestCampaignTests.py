import unittest
import ConquestCampaign

class ConquestCampaignTests(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(ConquestCampaign.ConquestCampaign(1,1,1,(1,1)), 1)

    def tests_repeats_troops(self):
        self.assertEqual(ConquestCampaign.ConquestCampaign(3,4,3,(2,2,3,4,2,2)), 3)

    def tests_lot_of_troops(self):
        self.assertEqual(ConquestCampaign.ConquestCampaign(10,10,5,(1,2,4,3,6,8,5,6,9,1)), 8)

if __name__ == '__main__':
    unittest.main()