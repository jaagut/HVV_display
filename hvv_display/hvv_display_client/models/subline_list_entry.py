from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.station_light import StationLight
from ..models.subline_list_entry_vehicle_type import SublineListEntryVehicleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SublineListEntry")


@attr.s(auto_attribs=True)
class SublineListEntry:
    """
    Attributes:
        subline_number (str):
        vehicle_type (SublineListEntryVehicleType):
        station_sequence (Union[Unset, List[StationLight]]):
    """

    subline_number: str
    vehicle_type: SublineListEntryVehicleType
    station_sequence: Union[Unset, List[StationLight]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subline_number = self.subline_number
        vehicle_type = self.vehicle_type.value

        station_sequence: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.station_sequence, Unset):
            station_sequence = []
            for station_sequence_item_data in self.station_sequence:
                station_sequence_item = station_sequence_item_data.to_dict()

                station_sequence.append(station_sequence_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sublineNumber": subline_number,
                "vehicleType": vehicle_type,
            }
        )
        if station_sequence is not UNSET:
            field_dict["stationSequence"] = station_sequence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subline_number = d.pop("sublineNumber")

        vehicle_type = SublineListEntryVehicleType(d.pop("vehicleType"))

        station_sequence = []
        _station_sequence = d.pop("stationSequence", UNSET)
        for station_sequence_item_data in _station_sequence or []:
            station_sequence_item = StationLight.from_dict(station_sequence_item_data)

            station_sequence.append(station_sequence_item)

        subline_list_entry = cls(
            subline_number=subline_number,
            vehicle_type=vehicle_type,
            station_sequence=station_sequence,
        )

        subline_list_entry.additional_properties = d
        return subline_list_entry

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
