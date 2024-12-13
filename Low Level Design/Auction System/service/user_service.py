from entities.user import User

class UserService:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.users = {}

    @staticmethod
    def get_instance() -> 'UserService':
        if UserService._instance is None:
            UserService()
        return UserService._instance

    def add_user(self, user: User) -> None:
        self.users[user.id] = user

    def get_user_by_id(self, user_id: str) -> User:
        return self.users[user_id]