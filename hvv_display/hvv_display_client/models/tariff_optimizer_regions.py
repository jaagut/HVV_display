from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tariff_regions import TariffRegions
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffOptimizerRegions")


@attr.s(auto_attribs=True)
class TariffOptimizerRegions:
    """
    Attributes:
        zones (Union[Unset, List[TariffRegions]]):
        rings (Union[Unset, List[TariffRegions]]):
        counties (Union[Unset, List[TariffRegions]]):
    """

    zones: Union[Unset, List[TariffRegions]] = UNSET
    rings: Union[Unset, List[TariffRegions]] = UNSET
    counties: Union[Unset, List[TariffRegions]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = []
            for zones_item_data in self.zones:
                zones_item = zones_item_data.to_dict()

                zones.append(zones_item)

        rings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rings, Unset):
            rings = []
            for rings_item_data in self.rings:
                rings_item = rings_item_data.to_dict()

                rings.append(rings_item)

        counties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.counties, Unset):
            counties = []
            for counties_item_data in self.counties:
                counties_item = counties_item_data.to_dict()

                counties.append(counties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zones is not UNSET:
            field_dict["zones"] = zones
        if rings is not UNSET:
            field_dict["rings"] = rings
        if counties is not UNSET:
            field_dict["counties"] = counties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zones = []
        _zones = d.pop("zones", UNSET)
        for zones_item_data in _zones or []:
            zones_item = TariffRegions.from_dict(zones_item_data)

            zones.append(zones_item)

        rings = []
        _rings = d.pop("rings", UNSET)
        for rings_item_data in _rings or []:
            rings_item = TariffRegions.from_dict(rings_item_data)

            rings.append(rings_item)

        counties = []
        _counties = d.pop("counties", UNSET)
        for counties_item_data in _counties or []:
            counties_item = TariffRegions.from_dict(counties_item_data)

            counties.append(counties_item)

        tariff_optimizer_regions = cls(
            zones=zones,
            rings=rings,
            counties=counties,
        )

        tariff_optimizer_regions.additional_properties = d
        return tariff_optimizer_regions

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
