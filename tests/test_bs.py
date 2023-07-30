# Copyright (c) 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT


from spider_scrape.bs import normalize_text


def test_normalize_text():
    text = "Hello  you!"
    result = normalize_text(text)
    assert isinstance(result, str)
    assert result == "Hello you!"
