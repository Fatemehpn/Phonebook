from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

@app.route("/contacts", methods=["GET"])
def get_contacts():
    return jsonify(load_contacts())

@app.route("/contacts", methods=["POST"])
def add_contact():
    contacts = load_contacts()
    data = request.json
    for contact in contacts:
        if contact["phone"] == data["phone"]:
            return jsonify({"error": f"Number already exists under {contact['name']}"}), 400
    contacts.append({"name": data["name"], "phone": data["phone"]})
    save_contacts(contacts)
    return jsonify({"success": True})

@app.route("/contacts/<phone>", methods=["DELETE"])
def remove_contact(phone):
    contacts = load_contacts()
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            return jsonify({"success": True})
    return jsonify({"error": "Contact not found"}), 404

@app.route("/contacts/<phone>", methods=["PUT"])
def edit_contact(phone):
    contacts = load_contacts()
    data = request.json
    for contact in contacts:
        if contact["phone"] == phone:
            if "phone" in data:
                for other in contacts:
                    if other["phone"] == data["phone"] and other != contact:
                        return jsonify({"error": f"Number already exists under {other['name']}"}), 400
            contact["name"] = data.get("name", contact["name"])
            contact["phone"] = data.get("phone", contact["phone"])
            save_contacts(contacts)
            return jsonify({"success": True})
    return jsonify({"error": "Contact not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)