from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_type import ServiceType
from ..models.subline_list_entry import SublineListEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="LineListEntry")


@attr.s(auto_attribs=True)
class LineListEntry:
    """
    Attributes:
        id (str):
        type (ServiceType):
        name (Union[Unset, str]):
        carrier_name_short (Union[Unset, str]):
        carrier_name_long (Union[Unset, str]):
        sublines (Union[Unset, List[SublineListEntry]]):
        exists (Union[Unset, bool]):  Default: True.
    """

    id: str
    type: ServiceType
    name: Union[Unset, str] = UNSET
    carrier_name_short: Union[Unset, str] = UNSET
    carrier_name_long: Union[Unset, str] = UNSET
    sublines: Union[Unset, List[SublineListEntry]] = UNSET
    exists: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.to_dict()

        name = self.name
        carrier_name_short = self.carrier_name_short
        carrier_name_long = self.carrier_name_long
        sublines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sublines, Unset):
            sublines = []
            for sublines_item_data in self.sublines:
                sublines_item = sublines_item_data.to_dict()

                sublines.append(sublines_item)

        exists = self.exists

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if carrier_name_short is not UNSET:
            field_dict["carrierNameShort"] = carrier_name_short
        if carrier_name_long is not UNSET:
            field_dict["carrierNameLong"] = carrier_name_long
        if sublines is not UNSET:
            field_dict["sublines"] = sublines
        if exists is not UNSET:
            field_dict["exists"] = exists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = ServiceType.from_dict(d.pop("type"))

        name = d.pop("name", UNSET)

        carrier_name_short = d.pop("carrierNameShort", UNSET)

        carrier_name_long = d.pop("carrierNameLong", UNSET)

        sublines = []
        _sublines = d.pop("sublines", UNSET)
        for sublines_item_data in _sublines or []:
            sublines_item = SublineListEntry.from_dict(sublines_item_data)

            sublines.append(sublines_item)

        exists = d.pop("exists", UNSET)

        line_list_entry = cls(
            id=id,
            type=type,
            name=name,
            carrier_name_short=carrier_name_short,
            carrier_name_long=carrier_name_long,
            sublines=sublines,
            exists=exists,
        )

        line_list_entry.additional_properties = d
        return line_list_entry

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
