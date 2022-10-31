from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tariff_county import TariffCounty
from ..models.tariff_kind import TariffKind
from ..models.tariff_level import TariffLevel
from ..models.tariff_meta_data_response_return_code import (
    TariffMetaDataResponseReturnCode,
)
from ..models.tariff_zone import TariffZone
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffMetaDataResponse")


@attr.s(auto_attribs=True)
class TariffMetaDataResponse:
    """
    Attributes:
        return_code (TariffMetaDataResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        tariff_kinds (Union[Unset, List[TariffKind]]):
        tariff_levels (Union[Unset, List[TariffLevel]]):
        tariff_counties (Union[Unset, List[TariffCounty]]):
        tariff_zones (Union[Unset, List[TariffZone]]):
        tariff_rings (Union[Unset, List[str]]):
    """

    return_code: TariffMetaDataResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    tariff_kinds: Union[Unset, List[TariffKind]] = UNSET
    tariff_levels: Union[Unset, List[TariffLevel]] = UNSET
    tariff_counties: Union[Unset, List[TariffCounty]] = UNSET
    tariff_zones: Union[Unset, List[TariffZone]] = UNSET
    tariff_rings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        tariff_kinds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_kinds, Unset):
            tariff_kinds = []
            for tariff_kinds_item_data in self.tariff_kinds:
                tariff_kinds_item = tariff_kinds_item_data.to_dict()

                tariff_kinds.append(tariff_kinds_item)

        tariff_levels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_levels, Unset):
            tariff_levels = []
            for tariff_levels_item_data in self.tariff_levels:
                tariff_levels_item = tariff_levels_item_data.to_dict()

                tariff_levels.append(tariff_levels_item)

        tariff_counties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_counties, Unset):
            tariff_counties = []
            for tariff_counties_item_data in self.tariff_counties:
                tariff_counties_item = tariff_counties_item_data.to_dict()

                tariff_counties.append(tariff_counties_item)

        tariff_zones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_zones, Unset):
            tariff_zones = []
            for tariff_zones_item_data in self.tariff_zones:
                tariff_zones_item = tariff_zones_item_data.to_dict()

                tariff_zones.append(tariff_zones_item)

        tariff_rings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tariff_rings, Unset):
            tariff_rings = self.tariff_rings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if tariff_kinds is not UNSET:
            field_dict["tariffKinds"] = tariff_kinds
        if tariff_levels is not UNSET:
            field_dict["tariffLevels"] = tariff_levels
        if tariff_counties is not UNSET:
            field_dict["tariffCounties"] = tariff_counties
        if tariff_zones is not UNSET:
            field_dict["tariffZones"] = tariff_zones
        if tariff_rings is not UNSET:
            field_dict["tariffRings"] = tariff_rings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = TariffMetaDataResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        tariff_kinds = []
        _tariff_kinds = d.pop("tariffKinds", UNSET)
        for tariff_kinds_item_data in _tariff_kinds or []:
            tariff_kinds_item = TariffKind.from_dict(tariff_kinds_item_data)

            tariff_kinds.append(tariff_kinds_item)

        tariff_levels = []
        _tariff_levels = d.pop("tariffLevels", UNSET)
        for tariff_levels_item_data in _tariff_levels or []:
            tariff_levels_item = TariffLevel.from_dict(tariff_levels_item_data)

            tariff_levels.append(tariff_levels_item)

        tariff_counties = []
        _tariff_counties = d.pop("tariffCounties", UNSET)
        for tariff_counties_item_data in _tariff_counties or []:
            tariff_counties_item = TariffCounty.from_dict(tariff_counties_item_data)

            tariff_counties.append(tariff_counties_item)

        tariff_zones = []
        _tariff_zones = d.pop("tariffZones", UNSET)
        for tariff_zones_item_data in _tariff_zones or []:
            tariff_zones_item = TariffZone.from_dict(tariff_zones_item_data)

            tariff_zones.append(tariff_zones_item)

        tariff_rings = cast(List[str], d.pop("tariffRings", UNSET))

        tariff_meta_data_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            tariff_kinds=tariff_kinds,
            tariff_levels=tariff_levels,
            tariff_counties=tariff_counties,
            tariff_zones=tariff_zones,
            tariff_rings=tariff_rings,
        )

        tariff_meta_data_response.additional_properties = d
        return tariff_meta_data_response

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
