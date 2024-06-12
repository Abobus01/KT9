from entities.user import User

class GetUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id) 