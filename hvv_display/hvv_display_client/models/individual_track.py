from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.individual_track_type import IndividualTrackType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualTrack")


@attr.s(auto_attribs=True)
class IndividualTrack:
    """
    Attributes:
        type (IndividualTrackType):
        time (Union[Unset, int]):
        length (Union[Unset, int]):
    """

    type: IndividualTrackType
    time: Union[Unset, int] = UNSET
    length: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        time = self.time
        length = self.length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time
        if length is not UNSET:
            field_dict["length"] = length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = IndividualTrackType(d.pop("type"))

        time = d.pop("time", UNSET)

        length = d.pop("length", UNSET)

        individual_track = cls(
            type=type,
            time=time,
            length=length,
        )

        individual_track.additional_properties = d
        return individual_track

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
