from app import db
from datetime import datetime

class Certificado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    data_emissao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_expiracao = db.Column(db.DateTime, nullable=False)

    funcionario = db.relationship('Funcionario', backref='certificados')

    def to_dict(self):
        return {
            'id': self.id,
            'funcionario_id': self.funcionario_id,
            'nome': self.nome,
            'data_emissao': self.data_emissao.isoformat(),
            'data_expiracao': self.data_expiracao.isoformat()
        }
