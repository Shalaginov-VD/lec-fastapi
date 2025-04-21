from sqlalchemy.orm import Session
from database import engine
import models as m

m.Base.metadata.drop_all(bind = engine)
m.Base.metadata.create_all(bind = engine)

with Session(bind = engine) as session:
    # c1 = m.Category(name = 'Еда')
    # session.add(c1)

    c1 = m.Genre(title = 'Фантастика')
    session.add(c1)

    # p1 = m.Product(name = 'Молоко', category = c1)
    # session.add(p1)

    p1 = m.Movie(title = 'Властелин колец', rating = '9')
    session.add(p1)

    session.commit()