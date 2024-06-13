from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Adicionando a coluna 'tipo'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'quantidade': self.quantidade,
            'preco': float(self.preco),
            'tipo': self.tipo
        }
