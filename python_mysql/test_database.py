import unittest
from profiles import fetch_by_userhandle, get_connection, get_profile_by_id, fetch_all_profiles, create_profile, update_user_age, delete_profile

class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_connection(self):
        self.assertTrue(self.conn.is_connected())

    def test_get_profile(self):
        result = get_profile_by_id(self.cursor, 2)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Beyonce Knowles")
        self.assertEqual(result[2], "beyonce")

    def test_injection_protection(self):
        """Verify that SQL injection attempts don't bypass security"""
        # Attempt injection
        malicious_input = "' OR '1'='1"   
        # Use the SAFE function
        result = fetch_by_userhandle(self.cursor, malicious_input)   
        # Should find nothing (no user has that literal username)
        self.assertEqual(result, None)   
        # Also test that normal searches still work
        normal_result = fetch_by_userhandle(self.cursor, "beyonce")
        self.assertEqual(len(normal_result), 6) 

    def test_create_update_delete_profile(self):    
        # Create a new profile
        create_profile(self.cursor, 10, "Test User", "testuser", "testuser@example.com", "testpassword", 25)
        self.conn.commit()
        # Verify creation
        result = fetch_by_userhandle(self.cursor, "testuser")
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Test User")
        # Update the profile
        update_user_age(self.cursor, 10, 30)
        self.conn.commit()
        # Verify update
        result = fetch_by_userhandle(self.cursor, "testuser")
        self.assertEqual(result[5], 30)
        # Delete the profile
        delete_profile(self.cursor, 10)
        self.conn.commit()
        # Verify deletion
        result = fetch_by_userhandle(self.cursor, "testuser")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()