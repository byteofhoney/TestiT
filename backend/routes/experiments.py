from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime, timezone
from db import experiments

experiments_bp = Blueprint("experiments", __name__)


@experiments_bp.route("/experiments", methods=["POST"])
def create_experiment():
    data = request.get_json()

    name = data.get("name")
    variants = data.get("variants")

    if not name or not variants:
        return jsonify({"error": "name and variants are required"}), 400

    if len(variants) < 2:
        
        return jsonify({"error": "at least 2 variants required"}), 400

    experiment = {
        "name": name,
        "variants": variants,
        "created_at": datetime.now(timezone.utc),
        "status": "active"
    }

    result = experiments.insert_one(experiment)

    return jsonify(
        {
        "id": str(result.inserted_id),
        "name": name,
        "variants": variants,
        "status": "active"
    } ), 201