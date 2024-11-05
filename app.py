from flask import Flask
from controllers.mutant_controller import mutant_bp
import subprocess, os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    app.register_blueprint(mutant_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
