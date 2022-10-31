from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_type_simple_type import ServiceTypeSimpleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceType")


@attr.s(auto_attribs=True)
class ServiceType:
    """
    Attributes:
        simple_type (ServiceTypeSimpleType):
        short_info (Union[Unset, str]):
        long_info (Union[Unset, str]):
        model (Union[Unset, str]):
    """

    simple_type: ServiceTypeSimpleType
    short_info: Union[Unset, str] = UNSET
    long_info: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        simple_type = self.simple_type.value

        short_info = self.short_info
        long_info = self.long_info
        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "simpleType": simple_type,
            }
        )
        if short_info is not UNSET:
            field_dict["shortInfo"] = short_info
        if long_info is not UNSET:
            field_dict["longInfo"] = long_info
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        simple_type = ServiceTypeSimpleType(d.pop("simpleType"))

        short_info = d.pop("shortInfo", UNSET)

        long_info = d.pop("longInfo", UNSET)

        model = d.pop("model", UNSET)

        service_type = cls(
            simple_type=simple_type,
            short_info=short_info,
            long_info=long_info,
            model=model,
        )

        service_type.additional_properties = d
        return service_type

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
