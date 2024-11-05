from flask import Blueprint, request, jsonify
from services.mutant_service import Mutante
from schemas.dna_schema import DNASchema

mutant_bp = Blueprint('mutant', __name__)

@mutant_bp.route('/mutant/', methods=['POST'])
def detect_mutant():
    data = request.get_json()
    dna = data.get("dna", [])
    schema = DNASchema()

    validation_error = schema.validate_dna(dna)
    if validation_error:
        return validation_error

    mutante_checker = Mutante(dna)
    if mutante_checker.isMutante():
        return jsonify({"message": "Mutant DNA detected"}), 200
    else:
        return jsonify({"message": "Human DNA detected"}), 403
