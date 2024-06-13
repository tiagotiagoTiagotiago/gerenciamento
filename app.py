from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from models import produto, funcionario, emprestimo, certificado
        db.create_all()

    from routes.produto import produto_bp
    from routes.funcionario import funcionario_bp
    from routes.emprestimo import emprestimo_bp
    from routes.certificado import certificado_bp

    app.register_blueprint(produto_bp, url_prefix='/produtos')
    app.register_blueprint(funcionario_bp, url_prefix='/funcionarios')
    app.register_blueprint(emprestimo_bp, url_prefix='/emprestimos')
    app.register_blueprint(certificado_bp, url_prefix='/certificados')

    return app
