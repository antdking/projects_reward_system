from django.test import TestCase
from utils import create_teacher_object


class CreateTeacherTestCase(TestCase):
    def test_one_teacher(self):
        user = create_teacher_object("hi", "bye")
        self.assertEqual(user.username, 'hbye')
        self.assertEqual(user.first_name, 'hi')
        self.assertEqual(user.last_name, 'bye')

    def test_two_teacher_diff_name(self):
        user1 = create_teacher_object("hi", "bye")
        user2 = create_teacher_object("foo", "bar")
        self.assertEqual(user1.username, 'hbye')
        self.assertEqual(user1.first_name, 'hi')
        self.assertEqual(user1.last_name, 'bye')

        self.assertEqual(user2.username, 'fbar')
        self.assertEqual(user2.first_name, 'foo')
        self.assertEqual(user2.last_name, 'bar')

    def test_two_teacher_same_name(self):
        user1 = create_teacher_object("hi", "bye")
        user2 = create_teacher_object("hi", "bye")
        self.assertEqual(user1.username, 'hbye')
        self.assertEqual(user1.first_name, 'hi')
        self.assertEqual(user1.last_name, 'bye')

        self.assertEqual(user2.username, 'hbye1')
        self.assertEqual(user2.first_name, 'hi')
        self.assertEqual(user2.last_name, 'bye')

    def test_teacher_is_staff(self):
        user1 = create_teacher_object("hi", "bye")
        user2 = create_teacher_object("foo", "bar", admin=True)
        self.assertEqual(user1.is_staff, False)
        self.assertEqual(user2.is_staff, True)