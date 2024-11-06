from flask import Blueprint, request, jsonify
from services.mutant_service import Mutante
from repositories.dna_repository import DNARepository

mutant_bp = Blueprint('mutant', __name__)

@mutant_bp.route('/mutant/', methods=['POST'])
def detect_mutant():
    data = request.get_json()
    dna = data.get("dna", [])
    
    response = process_dna(dna)
    
    if isinstance(response, tuple):
        return response  
    return jsonify({"error": "Unexpected error"}), 500

def process_dna(dna):
    if not isinstance(dna, list):
        return jsonify({"error": "Invalid DNA format: not a list"}), 400

    if len(dna) != 6:
        return jsonify({"error": "Invalid DNA format: DNA must contain exactly 6 parts"}), 400
    
    for row in dna:
        if not isinstance(row, str):
            return jsonify({"error": "Invalid DNA format: all elements must be strings"}), 400
        if len(row) != 6:
            return jsonify({"error": "Invalid DNA format: each part must contain exactly 6 letters"}), 400
    
    dna_repository = DNARepository()
    
    if dna_repository.obtener_adn(dna):
        return jsonify({"message": "DNA already processed"}), 200

    mutante_checker = Mutante(dna)
    is_mutant = mutante_checker.isMutante()

    dna_repository.save_result(dna, is_mutant)

    if is_mutant:
        return jsonify({"message": "Mutant DNA detected"}), 200
    else:
        return jsonify({"message": "Human DNA detected"}), 403
