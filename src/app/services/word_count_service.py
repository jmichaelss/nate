import requests as _requests
from bs4 import BeautifulSoup as _BeautifulSoup
import re
from pydantic import HttpUrl, AnyUrl
from typing import List
import collections as _collections
from fastapi import HTTPException


def access_and_parse_html(url) -> _BeautifulSoup:
    """Make a request to the webpage

    Args:
        url (AnyUrl): The desired url to be accessed and scraped

    Returns:
        _BeautifulSoup: A parsed http response that makes it easy to extract data
    """
    try:
        page = _requests.get(url)
        soup = _BeautifulSoup(page.text, "html.parser")
        return soup
    except:
        raise HTTPException(
            status_code=400, detail="The provided URL is Invalid")


def clean_text_from_html(soup: _BeautifulSoup) -> list[str]:
    """Clean up the text data from the parsed http reponse

    Args:
        soup (_BeautifulSoup): The parsed html page that was parsed using beautiful soup

    Returns:
        list[str]: A list with containing the words from the tags excluding script,
        style, head, noscript, tile and meta tags.
    """
    try:
        text_from_html: str = soup.find('html').text
        remove_punctions_and_nums = re.sub('[^A-Za-z]+', ' ', text_from_html)
        text_list: List = remove_punctions_and_nums.split()
        return text_list
    except:
        raise HTTPException(
            status_code=204, detail="No text was found on this page")


def get_word_count_from_text_list(url) -> _collections.Counter:
    """Get a count of the words frequency on the web page using beautiful soup as the parser
        and the collections package

    Args:
        url (AnyUrl): The desired url to be accessed and scraped

    Returns:
        _collections.Counter: A count of the word occurances sorted in descending order of frequency
    """
    if url:
        text_from_html = access_and_parse_html(url)
        cleaned_text = clean_text_from_html(text_from_html)
        word_count = _collections.Counter(cleaned_text)
        return word_count.most_common()
