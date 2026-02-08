import mysql.connector

def get_connection():
    # ⚠️ IMPORTANT: Replace 'password' with YOUR MySQL password
    return mysql.connector.connect(
        host="localhost",
        user="root",
    )

def get_profile_by_id(cursor, profileid):
    print("📱 Fetching profile with ID {} from 'instabook' database...".format(profileid))
    cursor.execute("USE instabook")
    cursor.execute("SELECT * FROM Profiles WHERE profileid = %s", (profileid,))
    result = cursor.fetchone()
    print("   ✅ Fetched profile:", result)
    return result

def fetch_all_profiles(cursor):
    print("📱 Fetching all profiles from 'instabook' database...")
    cursor.execute("USE instabook")
    cursor.execute("SELECT * FROM Profiles")
    results = cursor.fetchall()
    print("   ✅ Fetched profiles:", results)
    return results

def fetch_by_userhandle(cursor, userhandle):
    print("📱 Fetching profile with userhandle '{}' from 'instabook' database...".format(userhandle))
    cursor.execute("USE instabook")
    cursor.execute("SELECT * FROM Profiles WHERE userhandle = %s", (userhandle,))
    result = cursor.fetchone()
    print("   ✅ Fetched profile:", result)
    return result

def create_profile(cursor, profileid, fullname, userhandle, email, password, age):
    print("📱 Creating profile '{}' in 'instabook' database...".format(userhandle))
    cursor.execute("USE instabook")
    cursor.execute("""
        INSERT INTO Profiles (profileid, fullname, userhandle, email, password, age)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (profileid, fullname, userhandle, email, password, age))
    print("   ✅ Created profile for userhandle '{}'".format(userhandle))

def update_user_age(cursor, profileid, new_age):
    print("📱 Updating age for profileid '{}' to {}...".format(profileid, new_age))
    cursor.execute("USE instabook")
    cursor.execute("""
        UPDATE Profiles
        SET age = %s
        WHERE profileid = %s
    """, (new_age, profileid))
    print("   ✅ Updated age for profileid '{}'".format(profileid))

def delete_profile(cursor, profileid):
    print("📱 Deleting profile with ID '{}'...".format(profileid))
    cursor.execute("USE instabook")
    cursor.execute("DELETE FROM Profiles WHERE profileid = %s", (profileid,))
    print("   ✅ Deleted profile with ID '{}'".format(profileid))

def main():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # profile = get_profile_by_id(cursor, profileid=1)
        # print("Profile details:", profile)

        profiles = fetch_all_profiles(cursor)
        print("All profiles:", profiles)
        print("-----\n")

        # create_profile(cursor, 5, 'Shakira', 'shakira', 'shakira@shakira.com', 'password123', 25)
        # print("-----\n")
        # connection.commit()
        # all_profiles = fetch_all_profiles(cursor)

        # update_user_age(cursor, 5, 48)
        # print("-----\n")
        # connection.commit()
        # all_profiles = fetch_all_profiles(cursor)
        # print("All profiles after creation and update:", all_profiles) 

        delete_profile(cursor, 5)
        connection.commit()
        print("-----\n")
        all_profiles = fetch_all_profiles(cursor)
        print("All profiles after deletion:", all_profiles) 

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()