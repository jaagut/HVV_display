from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cn_request_coordinate_type import CNRequestCoordinateType
from ..models.cn_request_filter_type import CNRequestFilterType
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="CNRequest")


@attr.s(auto_attribs=True)
class CNRequest:
    """
    Attributes:
        the_name (SDName):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, CNRequestFilterType]):  Default: CNRequestFilterType.NO_FILTER.
        max_list (Union[Unset, int]):
        max_distance (Union[Unset, int]):
        coordinate_type (Union[Unset, CNRequestCoordinateType]):  Default: CNRequestCoordinateType.EPSG_4326.
        tariff_details (Union[Unset, bool]):
        allow_type_switch (Union[Unset, bool]):  Default: True.
    """

    the_name: SDName
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, CNRequestFilterType] = CNRequestFilterType.NO_FILTER
    max_list: Union[Unset, int] = UNSET
    max_distance: Union[Unset, int] = UNSET
    coordinate_type: Union[
        Unset, CNRequestCoordinateType
    ] = CNRequestCoordinateType.EPSG_4326
    tariff_details: Union[Unset, bool] = False
    allow_type_switch: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        the_name = self.the_name.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        max_list = self.max_list
        max_distance = self.max_distance
        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        tariff_details = self.tariff_details
        allow_type_switch = self.allow_type_switch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "theName": the_name,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if max_list is not UNSET:
            field_dict["maxList"] = max_list
        if max_distance is not UNSET:
            field_dict["maxDistance"] = max_distance
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type
        if tariff_details is not UNSET:
            field_dict["tariffDetails"] = tariff_details
        if allow_type_switch is not UNSET:
            field_dict["allowTypeSwitch"] = allow_type_switch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        the_name = SDName.from_dict(d.pop("theName"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, CNRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = CNRequestFilterType(_filter_type)

        max_list = d.pop("maxList", UNSET)

        max_distance = d.pop("maxDistance", UNSET)

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, CNRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = CNRequestCoordinateType(_coordinate_type)

        tariff_details = d.pop("tariffDetails", UNSET)

        allow_type_switch = d.pop("allowTypeSwitch", UNSET)

        cn_request = cls(
            the_name=the_name,
            language=language,
            version=version,
            filter_type=filter_type,
            max_list=max_list,
            max_distance=max_distance,
            coordinate_type=coordinate_type,
            tariff_details=tariff_details,
            allow_type_switch=allow_type_switch,
        )

        cn_request.additional_properties = d
        return cn_request

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
