# Copyright (c) 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""DB tools package."""

from abc import ABC, abstractmethod

from attr import define


@define
class DataManager(ABC):
    @abstractmethod
    def load_batch(self):
        pass

    @abstractmethod
    def save_batch(self, batch):
        pass
