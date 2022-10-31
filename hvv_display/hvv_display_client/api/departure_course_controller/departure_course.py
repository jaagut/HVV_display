from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.dc_request import DCRequest
from ...models.dc_response import DCResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: DCRequest,
) -> Dict[str, Any]:
    url = "{}/gti/public/departureCourse".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DCResponse]:
    if response.status_code == 200:
        response_200 = DCResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DCResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: DCRequest,
) -> Response[DCResponse]:
    """
    Args:
        json_body (DCRequest):

    Returns:
        Response[DCResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: DCRequest,
) -> Optional[DCResponse]:
    """
    Args:
        json_body (DCRequest):

    Returns:
        Response[DCResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: DCRequest,
) -> Response[DCResponse]:
    """
    Args:
        json_body (DCRequest):

    Returns:
        Response[DCResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: DCRequest,
) -> Optional[DCResponse]:
    """
    Args:
        json_body (DCRequest):

    Returns:
        Response[DCResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
