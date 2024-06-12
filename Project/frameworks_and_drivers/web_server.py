from flask import Flask, jsonify
from interface_adapters.controllers.user_controller import UserController
from use_cases.get_user import GetUser
from frameworks_and_drivers.database.user_repository import UserRepository

app = Flask(__name__)

user_repository = UserRepository()
get_user_use_case = GetUser(user_repository)
user_controller = UserController(get_user_use_case)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_controller.get_user(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run()