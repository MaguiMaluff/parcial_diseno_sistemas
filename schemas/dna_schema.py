class DNASchema():    
    def validate_dna(self, dna):

        if not isinstance(dna, list):
            return {"error": "Invalid DNA format: not a list"}, 400

        if len(dna) != 6:
            return {"error": "Invalid DNA format: DNA must contain exactly 6 parts"}, 400

        for row in dna:
            if not isinstance(row, str):
                return {"error": "Invalid DNA format: all elements must be strings"}, 400
            if len(row) != 6:
                return {"error": "Invalid DNA format: each part must contain exactly 6 letters"}, 400

        return None
