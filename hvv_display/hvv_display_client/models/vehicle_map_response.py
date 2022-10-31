from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.journey import Journey
from ..models.vehicle_map_response_return_code import VehicleMapResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleMapResponse")


@attr.s(auto_attribs=True)
class VehicleMapResponse:
    """
    Attributes:
        return_code (VehicleMapResponseReturnCode):
        journeys (List[Journey]):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
    """

    return_code: VehicleMapResponseReturnCode
    journeys: List[Journey]
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        journeys = []
        for journeys_item_data in self.journeys:
            journeys_item = journeys_item_data.to_dict()

            journeys.append(journeys_item)

        error_text = self.error_text
        error_dev_info = self.error_dev_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "journeys": journeys,
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
        return_code = VehicleMapResponseReturnCode(d.pop("returnCode"))

        journeys = []
        _journeys = d.pop("journeys")
        for journeys_item_data in _journeys:
            journeys_item = Journey.from_dict(journeys_item_data)

            journeys.append(journeys_item)

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        vehicle_map_response = cls(
            return_code=return_code,
            journeys=journeys,
            error_text=error_text,
            error_dev_info=error_dev_info,
        )

        vehicle_map_response.additional_properties = d
        return vehicle_map_response

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
