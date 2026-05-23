import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interacao com banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"ola": "Mundo"}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interacao com banco")
def test_list_insert_documents():
    orders_repository = OrdersRepository(conn)
    list_of_documents = [{"exe1": "aqui1"}, {"exe2": "aqui2"}, {"exe3": "aqui3"}]
    orders_repository.insert_list_of_documents(list_of_documents)
