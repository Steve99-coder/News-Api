import unittest
from app.model import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("1234","Bbc","Australia's national carrier Qantas will require future international travelers to prove they have been vaccinated","https://www.bbc.com/news/business","Business","English","UK")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

