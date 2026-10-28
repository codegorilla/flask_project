from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.extensions import db

class User (db.Model):

  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True, nullable=False)
  email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True, nullable=False)
  password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

  def set_password (self, password):
    self.password_hash = generate_password_hash(password)

  def check_password (self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__ (self) -> str:
    return f"<User {self.id} {self.username}>"
