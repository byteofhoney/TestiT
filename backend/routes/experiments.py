from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime, timezone
from db import experiments, assignments, events
import hashlib

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
    }), 201


@experiments_bp.route("/experiments/<experiment_id>/assign", methods=["GET"])
def assign_variant(experiment_id):
    
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    try:
        experiment = experiments.find_one({"_id": ObjectId(experiment_id)})
    except Exception:
        return jsonify({"error": "invalid experiment id"}), 400

    if not experiment:
        return jsonify({"error": "experiment not found"}), 404

    if experiment["status"] != "active":
        return jsonify({"error": "experiment is not active"}), 400

    existing = assignments.find_one({
        "experiment_id": experiment_id,
        "user_id": user_id
    })

    if existing:
        return jsonify({
            "experiment_id": experiment_id,
            "user_id": user_id,
            "variant": existing["variant"],
            "already_assigned": True
        })

    hash_input = f"{experiment_id}:{user_id}".encode()
    hash_int = int(hashlib.md5(hash_input).hexdigest(), 16)
    variant = experiment["variants"][hash_int % len(experiment["variants"])]

    assignment = {
        "experiment_id": experiment_id,
        "user_id": user_id,
        "variant": variant,
        "assigned_at": datetime.now(timezone.utc)
    }

    assignments.insert_one(assignment)

    return jsonify({
        "experiment_id": experiment_id,
        "user_id": user_id,
        "variant": variant,
        "already_assigned": False
    }), 201


@experiments_bp.route("/experiments/<experiment_id>/event", methods=["POST"])
def log_event(experiment_id):
    data = request.get_json()

    user_id = data.get("user_id")
    event_name = data.get("event")

    if not user_id or not event_name:
        return jsonify({"error": "user_id and event are required"}), 400

    try:
        experiment = experiments.find_one({"_id": ObjectId(experiment_id)})
    except Exception:
        return jsonify({"error": "invalid experiment id"}), 400

    if not experiment:
        return jsonify({"error": "experiment not found"}), 404

    assignment = assignments.find_one({
        "experiment_id": experiment_id,
        "user_id": user_id
    })

    if not assignment:
        return jsonify({"error": "user has no assignment for this experiment"}), 400

    event = {
        "experiment_id": experiment_id,
        "user_id": user_id,
        "variant": assignment["variant"],
        "event": event_name,
        "logged_at": datetime.now(timezone.utc)
    }

    events.insert_one(event)

    return jsonify({
        "experiment_id": experiment_id,
        "user_id": user_id,
        "variant": assignment["variant"],
        "event": event_name,
        "logged": True
    }), 201
    
    
    