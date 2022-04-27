from dependency_injector import containers, providers
from srs.data.context import ContextMonitoring
from srs.data.stores.customers_store import CustomerStore


class Container(containers.DeclarativeContainer):
    database = providers.Singleton(ContextMonitoring)
    customers_service = providers.Factory(CustomerStore, context=database)


container = Container()
