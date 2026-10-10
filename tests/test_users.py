from toolbelt.users import add_user, connect, find_user


def test_find_existing_user():
    conn = connect()
    add_user(conn, "alice", "alice@example.com")
    assert find_user(conn, "alice")[1] == "alice"


def test_find_missing_user():
    conn = connect()
    assert find_user(conn, "bob") is None
