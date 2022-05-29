from database.user.repository import create_user


def initial_seed():
    create_user(
        name="Admin admin",
        username="admin",
        password="admin",
        email="admin@admin.com",
        phone="16999999999",
    )
