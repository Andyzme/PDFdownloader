from data import session
from data.models.product import Product


def homepage() -> dict:
    products = session.query(Product).all()
    products_layout_format = []
    row = []
    # NOTE: return a n x 6 list of dicts to return
    for product in products:
        row.append(product.name)
        if len(row) == 6:
            products_layout_format.append(row)
            row = []
    products_layout_format.append(row)
    return {"products": products_layout_format}
