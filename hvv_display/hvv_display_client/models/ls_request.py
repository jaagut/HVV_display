from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ls_request_coordinate_type import LSRequestCoordinateType
from ..models.ls_request_filter_type import LSRequestFilterType
from ..models.ls_request_modification_types_item import LSRequestModificationTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="LSRequest")


@attr.s(auto_attribs=True)
class LSRequest:
    """
    Attributes:
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, LSRequestFilterType]):  Default: LSRequestFilterType.NO_FILTER.
        data_release_id (Union[Unset, str]):
        modification_types (Union[Unset, List[LSRequestModificationTypesItem]]):
        coordinate_type (Union[Unset, LSRequestCoordinateType]):  Default: LSRequestCoordinateType.EPSG_4326.
        filter_equivalent (Union[Unset, bool]):
    """

    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, LSRequestFilterType] = LSRequestFilterType.NO_FILTER
    data_release_id: Union[Unset, str] = UNSET
    modification_types: Union[Unset, List[LSRequestModificationTypesItem]] = UNSET
    coordinate_type: Union[
        Unset, LSRequestCoordinateType
    ] = LSRequestCoordinateType.EPSG_4326
    filter_equivalent: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        data_release_id = self.data_release_id
        modification_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modification_types, Unset):
            modification_types = []
            for modification_types_item_data in self.modification_types:
                modification_types_item = modification_types_item_data.value

                modification_types.append(modification_types_item)

        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        filter_equivalent = self.filter_equivalent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if data_release_id is not UNSET:
            field_dict["dataReleaseID"] = data_release_id
        if modification_types is not UNSET:
            field_dict["modificationTypes"] = modification_types
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type
        if filter_equivalent is not UNSET:
            field_dict["filterEquivalent"] = filter_equivalent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, LSRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = LSRequestFilterType(_filter_type)

        data_release_id = d.pop("dataReleaseID", UNSET)

        modification_types = []
        _modification_types = d.pop("modificationTypes", UNSET)
        for modification_types_item_data in _modification_types or []:
            modification_types_item = LSRequestModificationTypesItem(
                modification_types_item_data
            )

            modification_types.append(modification_types_item)

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, LSRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = LSRequestCoordinateType(_coordinate_type)

        filter_equivalent = d.pop("filterEquivalent", UNSET)

        ls_request = cls(
            language=language,
            version=version,
            filter_type=filter_type,
            data_release_id=data_release_id,
            modification_types=modification_types,
            coordinate_type=coordinate_type,
            filter_equivalent=filter_equivalent,
        )

        ls_request.additional_properties = d
        return ls_request

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
