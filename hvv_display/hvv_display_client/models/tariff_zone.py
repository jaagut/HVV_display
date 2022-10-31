from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="TariffZone")


@attr.s(auto_attribs=True)
class TariffZone:
    """
    Attributes:
        zone (str):
        ring (str):
        neighbours (List[str]):
    """

    zone: str
    ring: str
    neighbours: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zone = self.zone
        ring = self.ring
        neighbours = self.neighbours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone": zone,
                "ring": ring,
                "neighbours": neighbours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zone = d.pop("zone")

        ring = d.pop("ring")

        neighbours = cast(List[str], d.pop("neighbours"))

        tariff_zone = cls(
            zone=zone,
            ring=ring,
            neighbours=neighbours,
        )

        tariff_zone.additional_properties = d
        return tariff_zone

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
