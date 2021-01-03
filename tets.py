from atlatl.lib.auth import create_app

test_response = {
    "id": "563419",
    "name": "test app",
    "website": None,
    "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
    "client_id": "TWhM-tNSuncnqN7DBJmoyeLnk6K3iJJ71KKXxgL1hPM",
    "client_secret": "ZEaFUFmF0umgBX1qKJDjaU99Q31lDkOU8NutzTOoliw",
    "vapid_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M=",
}


def test_stab():
    return test_response


create_app("test", "test_app", test=True, stab=test_stab)