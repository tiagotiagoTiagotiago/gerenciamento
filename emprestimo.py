from app import db
from datetime import datetime

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    data_emprestimo = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_devolucao = db.Column(db.DateTime, nullable=True)

    funcionario = db.relationship('Funcionario', backref='emprestimos')
    produto = db.relationship('Produto', backref='emprestimos')

    def to_dict(self):
        return {
            'id': self.id,
            'funcionario_id': self.funcionario_id,
            'produto_id': self.produto_id,
            'data_emprestimo': self.data_emprestimo.isoformat(),
            'data_devolucao': self.data_devolucao.isoformat() if self.data_devolucao else None
        }
