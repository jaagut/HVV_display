from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tariff_zone import TariffZone
from ..models.tariff_zone_neighbours_response_return_code import (
    TariffZoneNeighboursResponseReturnCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffZoneNeighboursResponse")


@attr.s(auto_attribs=True)
class TariffZoneNeighboursResponse:
    """
    Attributes:
        return_code (TariffZoneNeighboursResponseReturnCode):
        tariff_zones (List[TariffZone]):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
    """

    return_code: TariffZoneNeighboursResponseReturnCode
    tariff_zones: List[TariffZone]
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        tariff_zones = []
        for tariff_zones_item_data in self.tariff_zones:
            tariff_zones_item = tariff_zones_item_data.to_dict()

            tariff_zones.append(tariff_zones_item)

        error_text = self.error_text
        error_dev_info = self.error_dev_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "tariffZones": tariff_zones,
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
        return_code = TariffZoneNeighboursResponseReturnCode(d.pop("returnCode"))

        tariff_zones = []
        _tariff_zones = d.pop("tariffZones")
        for tariff_zones_item_data in _tariff_zones:
            tariff_zones_item = TariffZone.from_dict(tariff_zones_item_data)

            tariff_zones.append(tariff_zones_item)

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        tariff_zone_neighbours_response = cls(
            return_code=return_code,
            tariff_zones=tariff_zones,
            error_text=error_text,
            error_dev_info=error_dev_info,
        )

        tariff_zone_neighbours_response.additional_properties = d
        return tariff_zone_neighbours_response

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
