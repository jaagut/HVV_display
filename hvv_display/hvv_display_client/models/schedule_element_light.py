from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ScheduleElementLight")


@attr.s(auto_attribs=True)
class ScheduleElementLight:
    """
    Attributes:
        departure_station_id (str):
        arrival_station_id (str):
        line_id (str):
    """

    departure_station_id: str
    arrival_station_id: str
    line_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        departure_station_id = self.departure_station_id
        arrival_station_id = self.arrival_station_id
        line_id = self.line_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "departureStationId": departure_station_id,
                "arrivalStationId": arrival_station_id,
                "lineId": line_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        departure_station_id = d.pop("departureStationId")

        arrival_station_id = d.pop("arrivalStationId")

        line_id = d.pop("lineId")

        schedule_element_light = cls(
            departure_station_id=departure_station_id,
            arrival_station_id=arrival_station_id,
            line_id=line_id,
        )

        schedule_element_light.additional_properties = d
        return schedule_element_light

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
