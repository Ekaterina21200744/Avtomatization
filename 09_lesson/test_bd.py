from TableUsers import TableUsers


db = TableUsers("postgresql://postgres:0208@localhost:5432/QA")

def test_create_uws():
    user_id = 2411

    db.cleanup_user_ws(user_id)

    db.create_uws(user_id, "test2411@mail.ru", 1)
    new_user = db.get_user_by_id_ws(user_id)

    db.delete_user_ws(user_id)
    assert new_user.user_id == user_id


def test_update_user():

    user_id = 2411

    db.cleanup_user_ws(user_id)
    db.create_uws(user_id, "test2411@mail.ru", 15)

    new_subject_id = db.get_user_by_id_ws(user_id).subject_id
    assert new_subject_id == 15

    db.delete_user_ws(user_id)


def test_delete_user():
    user_id = 2411

    db.cleanup_user_ws(user_id)
    db.create_uws(user_id, "test2411@mail.ru", 1)

    user_before = db.get_user_by_id_ws(user_id)
    assert user_before is not None
    assert user_before.user_email == "test2411@mail.ru"

    db.delete_user_ws(user_id)

    user_after = db.get_user_by_id_ws(user_id)
    assert user_after is None
    