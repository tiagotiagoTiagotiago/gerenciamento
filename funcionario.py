from app import db

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    informacoes_veiculo = db.Column(db.String(200), nullable=True)
    informacoes_ferramentas = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'informacoes_veiculo': self.informacoes_veiculo,
            'informacoes_ferramentas': self.informacoes_ferramentas
        }
