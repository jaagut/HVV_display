from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.person_info_person_type import PersonInfoPersonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonInfo")


@attr.s(auto_attribs=True)
class PersonInfo:
    """
    Attributes:
        person_type (Union[Unset, PersonInfoPersonType]):
        person_count (Union[Unset, int]):
    """

    person_type: Union[Unset, PersonInfoPersonType] = UNSET
    person_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        person_type: Union[Unset, str] = UNSET
        if not isinstance(self.person_type, Unset):
            person_type = self.person_type.value

        person_count = self.person_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_type is not UNSET:
            field_dict["personType"] = person_type
        if person_count is not UNSET:
            field_dict["personCount"] = person_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _person_type = d.pop("personType", UNSET)
        person_type: Union[Unset, PersonInfoPersonType]
        if isinstance(_person_type, Unset):
            person_type = UNSET
        else:
            person_type = PersonInfoPersonType(_person_type)

        person_count = d.pop("personCount", UNSET)

        person_info = cls(
            person_type=person_type,
            person_count=person_count,
        )

        person_info.additional_properties = d
        return person_info

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
