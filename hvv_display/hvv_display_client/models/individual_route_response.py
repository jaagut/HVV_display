from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.individual_route import IndividualRoute
from ..models.individual_route_response_return_code import (
    IndividualRouteResponseReturnCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualRouteResponse")


@attr.s(auto_attribs=True)
class IndividualRouteResponse:
    """
    Attributes:
        return_code (IndividualRouteResponseReturnCode):
        routes (List[IndividualRoute]):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
    """

    return_code: IndividualRouteResponseReturnCode
    routes: List[IndividualRoute]
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        routes = []
        for routes_item_data in self.routes:
            routes_item = routes_item_data.to_dict()

            routes.append(routes_item)

        error_text = self.error_text
        error_dev_info = self.error_dev_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "routes": routes,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = IndividualRouteResponseReturnCode(d.pop("returnCode"))

        routes = []
        _routes = d.pop("routes")
        for routes_item_data in _routes:
            routes_item = IndividualRoute.from_dict(routes_item_data)

            routes.append(routes_item)

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        individual_route_response = cls(
            return_code=return_code,
            routes=routes,
            error_text=error_text,
            error_dev_info=error_dev_info,
        )

        individual_route_response.additional_properties = d
        return individual_route_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
