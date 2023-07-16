# Copyright (c) 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""Scraper package."""

from abc import ABC, abstractmethod
from typing import Optional, Sequence
from attr import define
from spider_scrape.db import DataManager


@define
class SpiderScraper(ABC):
    data_manager: DataManager

    @abstractmethod
    def process_batch(self, batch: Sequence):
        pass

    def run(self):
        while True:
            batch = self.data_manager.load_batch()
            if len(batch) == 0:
                break
            new_batch = self.process_batch(batch)
            if len(new_batch) > 0:
                self.data_manager.save_batch(new_batch)
