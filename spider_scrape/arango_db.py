# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""ArangoDB tools package."""

from contextlib import closing
from typing import Sequence, Union

from arango import ArangoClient
from attr import define, field

from spider_scrape.db import DataManager


@define
class ArangoDataManager(DataManager):
    hosts: Union[str, Sequence[str]]
    db_name: str
    username: str
    password: str
    collection_name: str
    attribute_name: str
    batch_size: int = field(default=20)

    def _get_arango_client(self):
        arango_client = ArangoClient(hosts=self.hosts)
        return arango_client

    def _get_connection(self, arango_client):
        connection = arango_client.db(self.db_name, username=self.username, password=self.password)
        return connection

    def load_batch(self) -> Sequence:
        with closing(self._get_arango_client()) as arango_client:
            connection = self._get_connection(arango_client)
            bind_vars = {"@coll": self.collection_name, "attribute": self.attribute_name}
            cursor = connection.aql.execute(
                "FOR doc IN @@coll FILTER !HAS(doc, @attribute) RETURN doc",
                bind_vars=bind_vars,
                batch_size=self.batch_size,
            )
            with closing(cursor) as closing_cursor:
                batch = closing_cursor.batch()
        return batch

    def save_batch(self, batch: Sequence):
        with closing(self._get_arango_client()) as arango_client:
            connection = self._get_connection(arango_client)
            collection = connection.collection(self.collection_name)
            collection.import_bulk(batch, on_duplicate="update")
