from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ll_request_filter_type import LLRequestFilterType
from ..models.ll_request_modification_types_item import LLRequestModificationTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="LLRequest")


@attr.s(auto_attribs=True)
class LLRequest:
    """
    Attributes:
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, LLRequestFilterType]):  Default: LLRequestFilterType.NO_FILTER.
        with_sublines (Union[Unset, bool]):
        data_release_id (Union[Unset, str]):
        modification_types (Union[Unset, List[LLRequestModificationTypesItem]]):
    """

    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, LLRequestFilterType] = LLRequestFilterType.NO_FILTER
    with_sublines: Union[Unset, bool] = UNSET
    data_release_id: Union[Unset, str] = UNSET
    modification_types: Union[Unset, List[LLRequestModificationTypesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        with_sublines = self.with_sublines
        data_release_id = self.data_release_id
        modification_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modification_types, Unset):
            modification_types = []
            for modification_types_item_data in self.modification_types:
                modification_types_item = modification_types_item_data.value

                modification_types.append(modification_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if with_sublines is not UNSET:
            field_dict["withSublines"] = with_sublines
        if data_release_id is not UNSET:
            field_dict["dataReleaseID"] = data_release_id
        if modification_types is not UNSET:
            field_dict["modificationTypes"] = modification_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, LLRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = LLRequestFilterType(_filter_type)

        with_sublines = d.pop("withSublines", UNSET)

        data_release_id = d.pop("dataReleaseID", UNSET)

        modification_types = []
        _modification_types = d.pop("modificationTypes", UNSET)
        for modification_types_item_data in _modification_types or []:
            modification_types_item = LLRequestModificationTypesItem(
                modification_types_item_data
            )

            modification_types.append(modification_types_item)

        ll_request = cls(
            language=language,
            version=version,
            filter_type=filter_type,
            with_sublines=with_sublines,
            data_release_id=data_release_id,
            modification_types=modification_types,
        )

        ll_request.additional_properties = d
        return ll_request

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
