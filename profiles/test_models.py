from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTests(TestCase):

    def setUp(self):
        # Creates a user instance to be associated with a UserProfile
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_userprofile_creation_on_user_creation(self):
        """
        Test that a UserProfile instance is created automatically when a new User is created.
        """
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_userprofile_default_values(self):
        """
        Test that default values can be set on a UserProfile instance.
        """
        profile = UserProfile.objects.get(user=self.user)
        profile.default_full_name = 'Test User'
        profile.default_phone_number = '123456789'
        profile.default_street_address1 = '123 Test Street'
        profile.default_town_or_city = 'Test City'
        profile.default_postcode = 'TEST123'
        profile.default_country = 'US'
        profile.save()

        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_full_name, 'Test User')
        self.assertEqual(updated_profile.default_phone_number, '123456789')
        self.assertEqual(updated_profile.default_street_address1, '123 Test Street')
        self.assertEqual(updated_profile.default_town_or_city, 'Test City')
        self.assertEqual(updated_profile.default_postcode, 'TEST123')
        self.assertEqual(updated_profile.default_country.code, 'US')

    def test_userprofile_str_method(self):
        """
        Test the string representation of the UserProfile model.
        """
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')

    def test_create_or_update_profile_signal_for_update(self):
        """
        Test the signal for updating an existing UserProfile instance when the User instance is saved.
        """
        profile = UserProfile.objects.get(user=self.user)
        profile.default_full_name = 'Updated Name'
        profile.save()

        self.user.save()

        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_full_name, 'Updated Name')