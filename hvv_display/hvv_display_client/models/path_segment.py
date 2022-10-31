from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vehicle_map_path import VehicleMapPath
from ..types import UNSET, Unset

T = TypeVar("T", bound="PathSegment")


@attr.s(auto_attribs=True)
class PathSegment:
    """
    Attributes:
        start_stop_point_key (str):
        end_stop_point_key (str):
        start_station_name (str):
        start_station_key (str):
        end_station_name (str):
        end_station_key (str):
        track (VehicleMapPath):
        destination (str):
        start_date_time (Union[Unset, int]):
        end_date_time (Union[Unset, int]):
        realtime_delay (Union[Unset, int]):
        is_first (Union[Unset, bool]):
        is_last (Union[Unset, bool]):
    """

    start_stop_point_key: str
    end_stop_point_key: str
    start_station_name: str
    start_station_key: str
    end_station_name: str
    end_station_key: str
    track: VehicleMapPath
    destination: str
    start_date_time: Union[Unset, int] = UNSET
    end_date_time: Union[Unset, int] = UNSET
    realtime_delay: Union[Unset, int] = UNSET
    is_first: Union[Unset, bool] = UNSET
    is_last: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_stop_point_key = self.start_stop_point_key
        end_stop_point_key = self.end_stop_point_key
        start_station_name = self.start_station_name
        start_station_key = self.start_station_key
        end_station_name = self.end_station_name
        end_station_key = self.end_station_key
        track = self.track.to_dict()

        destination = self.destination
        start_date_time = self.start_date_time
        end_date_time = self.end_date_time
        realtime_delay = self.realtime_delay
        is_first = self.is_first
        is_last = self.is_last

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startStopPointKey": start_stop_point_key,
                "endStopPointKey": end_stop_point_key,
                "startStationName": start_station_name,
                "startStationKey": start_station_key,
                "endStationName": end_station_name,
                "endStationKey": end_station_key,
                "track": track,
                "destination": destination,
            }
        )
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if realtime_delay is not UNSET:
            field_dict["realtimeDelay"] = realtime_delay
        if is_first is not UNSET:
            field_dict["isFirst"] = is_first
        if is_last is not UNSET:
            field_dict["isLast"] = is_last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_stop_point_key = d.pop("startStopPointKey")

        end_stop_point_key = d.pop("endStopPointKey")

        start_station_name = d.pop("startStationName")

        start_station_key = d.pop("startStationKey")

        end_station_name = d.pop("endStationName")

        end_station_key = d.pop("endStationKey")

        track = VehicleMapPath.from_dict(d.pop("track"))

        destination = d.pop("destination")

        start_date_time = d.pop("startDateTime", UNSET)

        end_date_time = d.pop("endDateTime", UNSET)

        realtime_delay = d.pop("realtimeDelay", UNSET)

        is_first = d.pop("isFirst", UNSET)

        is_last = d.pop("isLast", UNSET)

        path_segment = cls(
            start_stop_point_key=start_stop_point_key,
            end_stop_point_key=end_stop_point_key,
            start_station_name=start_station_name,
            start_station_key=start_station_key,
            end_station_name=end_station_name,
            end_station_key=end_station_key,
            track=track,
            destination=destination,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            realtime_delay=realtime_delay,
            is_first=is_first,
            is_last=is_last,
        )

        path_segment.additional_properties = d
        return path_segment

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
