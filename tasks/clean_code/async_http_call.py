"""Asynchronous module for fetching data from URLs using httpx."""

import asyncio

import httpx


async def fetch_api(url: str, **kwargs) -> httpx.Response:
    """
    Fetches data from the given URL using an asynchronous HTTP client.

    Parameters:
    - url (str): The URL to fetch data from.
    - **kwargs: Additional keyword arguments passed to the HTTP client.

    Returns:
    httpx.Response: The HTTP response.
    """
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url=url, **kwargs)
    return response


async def main(urls: list[str]) -> None:
    """
    Asynchronously fetches data from a list of URLs and prints the results.

    Parameters:
    - urls (List[str]): A list of URLs to fetch data from.

    Returns:
    None
    """
    tasks = [fetch_api(url) for url in urls]
    responses = asyncio.gather(*tasks)

    for url, response in zip(urls, responses):
        print(f"(url: {url}) - (body: {response})")
