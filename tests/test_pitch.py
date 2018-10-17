from app.models import Pitch,User
from app import db
import unittest

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.user_Kev = User(username ='Kev',password ='pineapple', email='kevahere@gmail.com')
        self.new_pitch = Pitch(id=1,
                               title="Milk vendor",
                               pitch_body="Sell milk indoors",
                               body="Sell milk all day everyday",
                               user_id=1,
                               category_id=1,
                               )

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,"Milk vendor")
        self.assertEquals(self.new_pitch.pitch_body,"Sell milk indoors")
        self.assertEquals(self.new_pitch.body,"Sell milk all day everyday")
        self.assertEquals(self.new_pitch.user_id,1)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)