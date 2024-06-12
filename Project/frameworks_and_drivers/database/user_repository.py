from entities.user import User

class UserRepository:
    def __init__(self):

        self.users = {
            1: User(1, "JohnDoe"),
            2: User(2, "JaneDoe")
        }

def get_user_by_id(self, user_id: int) -> User:
    return self.users.get(user_id)