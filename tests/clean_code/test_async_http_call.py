"""Test module for testing async fetch API."""

from unittest.mock import patch

import pytest
from httpx import Response

from src.clean_code.asynchronous.async_http_call import fetch_api, main


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url, expected_response",
    [
        ("https://example.com", Response(status_code=200, content=b"Mock Content1")),
        ("https://example.com", Response(status_code=201, content=b"Mock Content2")),
        ("https://example.com", Response(status_code=404)),
        ("https://example.com", Response(status_code=503)),
        ("https://example.com", Response(status_code=301)),
    ],
)
async def test_fetch_api(url: str, expected_response: Response) -> None:
    """
    Test the asynchronous function fetch_api.

    Parameters:
    - url (str): The URL to be used for fetching data.
    - expected_response (Response): The expected HTTP response.

    Raises:
    AssertionError: If the actual response is not equal to the expected response.
    """
    with patch(
        "src.clean_code.asynchronous.async_http_call.httpx.AsyncClient"
    ) as mock_client:
        mock_client.return_value.__aenter__.return_value.get.return_value = (
            expected_response
        )
        response = await fetch_api(url=url)

    assert response == expected_response
    mock_client.assert_called_once_with()
    mock_client.return_value.__aenter__.return_value.get.assert_called_once_with(
        url=url
    )


@pytest.mark.asyncio
async def test_main() -> None:
    """Test the asynchronous main function."""
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/comments/1",
    ]

    async def mock_fetch_api(url):  # pylint: disable=W0613
        return Response(status_code=200)

    with patch(
        "src.clean_code.asynchronous.async_http_call.fetch_api",
        side_effect=mock_fetch_api,
    ):
        await main(urls)
