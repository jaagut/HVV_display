from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attribute")


@attr.s(auto_attribs=True)
class Attribute:
    """
    Attributes:
        value (str):
        title (Union[Unset, str]):
        is_planned (Union[Unset, bool]):
        types (Union[Unset, List[str]]):
        id (Union[Unset, str]):
    """

    value: str
    title: Union[Unset, str] = UNSET
    is_planned: Union[Unset, bool] = UNSET
    types: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        title = self.title
        is_planned = self.is_planned
        types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if is_planned is not UNSET:
            field_dict["isPlanned"] = is_planned
        if types is not UNSET:
            field_dict["types"] = types
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        title = d.pop("title", UNSET)

        is_planned = d.pop("isPlanned", UNSET)

        types = cast(List[str], d.pop("types", UNSET))

        id = d.pop("id", UNSET)

        attribute = cls(
            value=value,
            title=title,
            is_planned=is_planned,
            types=types,
            id=id,
        )

        attribute.additional_properties = d
        return attribute

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
