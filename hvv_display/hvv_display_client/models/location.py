from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.location_type import LocationType
from ..models.sd_name import SDName
from ..models.service import Service
from ..types import UNSET, Unset

T = TypeVar("T", bound="Location")


@attr.s(auto_attribs=True)
class Location:
    """
    Attributes:
        type (Union[Unset, LocationType]):  Default: LocationType.SINGLE_LINE.
        name (Union[Unset, str]):
        line (Union[Unset, Service]):
        begin (Union[Unset, SDName]):
        end (Union[Unset, SDName]):
        both_directions (Union[Unset, bool]):  Default: True.
    """

    type: Union[Unset, LocationType] = LocationType.SINGLE_LINE
    name: Union[Unset, str] = UNSET
    line: Union[Unset, Service] = UNSET
    begin: Union[Unset, SDName] = UNSET
    end: Union[Unset, SDName] = UNSET
    both_directions: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name
        line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        begin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.begin, Unset):
            begin = self.begin.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        both_directions = self.both_directions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if line is not UNSET:
            field_dict["line"] = line
        if begin is not UNSET:
            field_dict["begin"] = begin
        if end is not UNSET:
            field_dict["end"] = end
        if both_directions is not UNSET:
            field_dict["bothDirections"] = both_directions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, LocationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = LocationType(_type)

        name = d.pop("name", UNSET)

        _line = d.pop("line", UNSET)
        line: Union[Unset, Service]
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Service.from_dict(_line)

        _begin = d.pop("begin", UNSET)
        begin: Union[Unset, SDName]
        if isinstance(_begin, Unset):
            begin = UNSET
        else:
            begin = SDName.from_dict(_begin)

        _end = d.pop("end", UNSET)
        end: Union[Unset, SDName]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = SDName.from_dict(_end)

        both_directions = d.pop("bothDirections", UNSET)

        location = cls(
            type=type,
            name=name,
            line=line,
            begin=begin,
            end=end,
            both_directions=both_directions,
        )

        location.additional_properties = d
        return location

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
