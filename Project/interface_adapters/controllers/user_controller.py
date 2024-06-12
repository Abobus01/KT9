from use_cases.get_user import GetUser

class UserController:
    def __init__(self, get_user_use_case: GetUser):
        self.get_user_use_case = get_user_use_case

    def get_user(self, user_id: int):
        user = self.get_user_use_case.execute(user_id)
        return {
            "user_id": user.user_id,
            "username": user.username
        }