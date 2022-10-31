from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.elevator import Elevator
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialStation")


@attr.s(auto_attribs=True)
class PartialStation:
    """
    Attributes:
        lines (Union[Unset, List[str]]):
        station_outline (Union[Unset, str]):
        elevators (Union[Unset, List[Elevator]]):
    """

    lines: Union[Unset, List[str]] = UNSET
    station_outline: Union[Unset, str] = UNSET
    elevators: Union[Unset, List[Elevator]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines

        station_outline = self.station_outline
        elevators: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elevators, Unset):
            elevators = []
            for elevators_item_data in self.elevators:
                elevators_item = elevators_item_data.to_dict()

                elevators.append(elevators_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines is not UNSET:
            field_dict["lines"] = lines
        if station_outline is not UNSET:
            field_dict["stationOutline"] = station_outline
        if elevators is not UNSET:
            field_dict["elevators"] = elevators

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lines = cast(List[str], d.pop("lines", UNSET))

        station_outline = d.pop("stationOutline", UNSET)

        elevators = []
        _elevators = d.pop("elevators", UNSET)
        for elevators_item_data in _elevators or []:
            elevators_item = Elevator.from_dict(elevators_item_data)

            elevators.append(elevators_item)

        partial_station = cls(
            lines=lines,
            station_outline=station_outline,
            elevators=elevators,
        )

        partial_station.additional_properties = d
        return partial_station

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
