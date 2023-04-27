import unittest
from Console_Text import Get_Time
from weather_report import get_weather

class TestDOT(unittest.TestCase):

    def testWeatherNotif(self):
        #test weather API
        self.assertIsNotNone(get_weather())

    def testConsole_text(self):
        #test output for console text
        self.assertIsNotNone(Get_Time())
        
"""
---------------------------------------------------
MANUAL TESTING :

    testSetUp:
        expected_output: *link to Austin weather details*
                         "use $ to chat with me
                            use < to tell me what to do!"
    
    testGreeting:
        Input: $hey Dot!
        expected_output: Hi everybody! ＼(^o^)／

    testBotWeather:
        input: $what is today's weather?
        expected_output: *Brief image describing today's 
                         weather in Austin and a link to further details*

    testUnknownCommandsResponse:
        input: *anything not in the command list"
        expected_output: "hmm I don't know that one"
        
---------------------------------------------------
"""

if __name__ == '__main__':
    unittest.main()
