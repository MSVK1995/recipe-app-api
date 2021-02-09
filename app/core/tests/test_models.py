from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_w_email_success(self):
        """Test to create a new user with email and checking if successful"""
        test_mail = "test@email.com"
        test_password = "test@1234"
        user = get_user_model().objects.create_user(
            email=test_mail,
            password=test_password
        )
        self.assertEqual(user.email, test_mail)
        self.assertTrue(user.check_password(test_password))

    def test_new_user_email_normalized(self):
        """Test the email for new user normalized"""
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user with no email raising error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "admin@test.com",
            "admin@123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
