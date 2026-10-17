import json

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name: str, age: int) -> dict:
        user = {
            "id": self.next_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def get_user(self, user_id: int):
        for u in self.users:
            if u["id"] == user_id:
                return u
        return None

    def update_age(self, user_id: int, new_age: int) -> bool:
        user = self.get_user(user_id)
        if user is None:
            return False
        user["age"] = new_age
        return True

    def remove_user(self, user_id: int) -> bool:
        for idx, u in enumerate(self.users):
            if u["id"] == user_id:
                self.users.pop(idx)
                return True
        return False

    def list_users(self):
        return self.users.copy()

    def save_to_json(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)

    def load_from_json(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            loaded_users = json.load(f)
        self.users = loaded_users
        if self.users:
            max_id = max(u["id"] for u in self.users)
            self.next_id = max_id + 1
        else:
            self.next_id = 1


