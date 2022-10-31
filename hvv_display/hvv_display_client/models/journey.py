from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.journey_vehicle_type import JourneyVehicleType
from ..models.path_segment import PathSegment
from ..models.service import Service
from ..types import UNSET, Unset

T = TypeVar("T", bound="Journey")


@attr.s(auto_attribs=True)
class Journey:
    """
    Attributes:
        journey_id (str):
        line (Service):
        vehicle_type (JourneyVehicleType):
        realtime (Union[Unset, bool]):
        segments (Union[Unset, List[PathSegment]]):
    """

    journey_id: str
    line: Service
    vehicle_type: JourneyVehicleType
    realtime: Union[Unset, bool] = UNSET
    segments: Union[Unset, List[PathSegment]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        journey_id = self.journey_id
        line = self.line.to_dict()

        vehicle_type = self.vehicle_type.value

        realtime = self.realtime
        segments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()

                segments.append(segments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "journeyID": journey_id,
                "line": line,
                "vehicleType": vehicle_type,
            }
        )
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        journey_id = d.pop("journeyID")

        line = Service.from_dict(d.pop("line"))

        vehicle_type = JourneyVehicleType(d.pop("vehicleType"))

        realtime = d.pop("realtime", UNSET)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = PathSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        journey = cls(
            journey_id=journey_id,
            line=line,
            vehicle_type=vehicle_type,
            realtime=realtime,
            segments=segments,
        )

        journey.additional_properties = d
        return journey

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
