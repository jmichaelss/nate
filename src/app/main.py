from fastapi import FastAPI, HTTPException
from app.services import word_count_service
# from app.services import word_count_service
import re
from pydantic import AnyUrl, HttpUrl, BaseModel, AnyHttpUrl
from fastapi_health import health
from typing import Pattern
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()


class UrlData(BaseModel):
    url: str


@app.post("/wordcount/")
async def word_count(url: UrlData):
    """Returns JSON Response of texts and their corresponding frequency 
    via the word-count-service from the provided URL

    Args:
        url (UrlData): URL to be loaded. This should not begin with "http://" or "https://"
    """
    half_url = url.url
    full_url: AnyHttpUrl = f"http://{half_url}"
    try:
        json_compatible_item_data = jsonable_encoder(
            dict(word_count_service.get_word_count_from_text_list(full_url)))
        return JSONResponse(content=json_compatible_item_data)
    except Exception as error:
        raise error


def get_session():
    return True


app.add_api_route("/health", health([get_session]))
