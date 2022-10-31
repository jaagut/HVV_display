from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gr_response_return_code import GRResponseReturnCode
from ..models.individual_track import IndividualTrack
from ..models.schedule import Schedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="GRResponse")


@attr.s(auto_attribs=True)
class GRResponse:
    """
    Attributes:
        return_code (GRResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        schedules (Union[Unset, List[Schedule]]):
        realtime_schedules (Union[Unset, List[Schedule]]):
        realtime_affected (Union[Unset, bool]):
        individual_track (Union[Unset, IndividualTrack]):
    """

    return_code: GRResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    schedules: Union[Unset, List[Schedule]] = UNSET
    realtime_schedules: Union[Unset, List[Schedule]] = UNSET
    realtime_affected: Union[Unset, bool] = False
    individual_track: Union[Unset, IndividualTrack] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()

                schedules.append(schedules_item)

        realtime_schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.realtime_schedules, Unset):
            realtime_schedules = []
            for realtime_schedules_item_data in self.realtime_schedules:
                realtime_schedules_item = realtime_schedules_item_data.to_dict()

                realtime_schedules.append(realtime_schedules_item)

        realtime_affected = self.realtime_affected
        individual_track: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.individual_track, Unset):
            individual_track = self.individual_track.to_dict()

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
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if realtime_schedules is not UNSET:
            field_dict["realtimeSchedules"] = realtime_schedules
        if realtime_affected is not UNSET:
            field_dict["realtimeAffected"] = realtime_affected
        if individual_track is not UNSET:
            field_dict["individualTrack"] = individual_track

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = GRResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = Schedule.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        realtime_schedules = []
        _realtime_schedules = d.pop("realtimeSchedules", UNSET)
        for realtime_schedules_item_data in _realtime_schedules or []:
            realtime_schedules_item = Schedule.from_dict(realtime_schedules_item_data)

            realtime_schedules.append(realtime_schedules_item)

        realtime_affected = d.pop("realtimeAffected", UNSET)

        _individual_track = d.pop("individualTrack", UNSET)
        individual_track: Union[Unset, IndividualTrack]
        if isinstance(_individual_track, Unset):
            individual_track = UNSET
        else:
            individual_track = IndividualTrack.from_dict(_individual_track)

        gr_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            schedules=schedules,
            realtime_schedules=realtime_schedules,
            realtime_affected=realtime_affected,
            individual_track=individual_track,
        )

        gr_response.additional_properties = d
        return gr_response

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
