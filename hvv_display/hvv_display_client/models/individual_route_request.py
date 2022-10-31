from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.individual_route_request_filter_type import (
    IndividualRouteRequestFilterType,
)
from ..models.individual_route_request_profile import IndividualRouteRequestProfile
from ..models.individual_route_request_service_type import (
    IndividualRouteRequestServiceType,
)
from ..models.individual_route_request_type import IndividualRouteRequestType
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualRouteRequest")


@attr.s(auto_attribs=True)
class IndividualRouteRequest:
    """
    Attributes:
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, IndividualRouteRequestFilterType]):  Default:
            IndividualRouteRequestFilterType.NO_FILTER.
        starts (Union[Unset, List[SDName]]):
        dests (Union[Unset, List[SDName]]):
        max_length (Union[Unset, int]):
        max_results (Union[Unset, int]):
        type (Union[Unset, IndividualRouteRequestType]):  Default: IndividualRouteRequestType.EPSG_4326.
        service_type (Union[Unset, IndividualRouteRequestServiceType]):  Default:
            IndividualRouteRequestServiceType.FOOTPATH.
        profile (Union[Unset, IndividualRouteRequestProfile]):  Default: IndividualRouteRequestProfile.FOOT_NORMAL.
        speed (Union[Unset, str]):  Default: 'NORMAL'.
    """

    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, IndividualRouteRequestFilterType
    ] = IndividualRouteRequestFilterType.NO_FILTER
    starts: Union[Unset, List[SDName]] = UNSET
    dests: Union[Unset, List[SDName]] = UNSET
    max_length: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    type: Union[
        Unset, IndividualRouteRequestType
    ] = IndividualRouteRequestType.EPSG_4326
    service_type: Union[
        Unset, IndividualRouteRequestServiceType
    ] = IndividualRouteRequestServiceType.FOOTPATH
    profile: Union[
        Unset, IndividualRouteRequestProfile
    ] = IndividualRouteRequestProfile.FOOT_NORMAL
    speed: Union[Unset, str] = "NORMAL"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        starts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.starts, Unset):
            starts = []
            for starts_item_data in self.starts:
                starts_item = starts_item_data.to_dict()

                starts.append(starts_item)

        dests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dests, Unset):
            dests = []
            for dests_item_data in self.dests:
                dests_item = dests_item_data.to_dict()

                dests.append(dests_item)

        max_length = self.max_length
        max_results = self.max_results
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        service_type: Union[Unset, str] = UNSET
        if not isinstance(self.service_type, Unset):
            service_type = self.service_type.value

        profile: Union[Unset, str] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.value

        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if starts is not UNSET:
            field_dict["starts"] = starts
        if dests is not UNSET:
            field_dict["dests"] = dests
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if type is not UNSET:
            field_dict["type"] = type
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if profile is not UNSET:
            field_dict["profile"] = profile
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, IndividualRouteRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = IndividualRouteRequestFilterType(_filter_type)

        starts = []
        _starts = d.pop("starts", UNSET)
        for starts_item_data in _starts or []:
            starts_item = SDName.from_dict(starts_item_data)

            starts.append(starts_item)

        dests = []
        _dests = d.pop("dests", UNSET)
        for dests_item_data in _dests or []:
            dests_item = SDName.from_dict(dests_item_data)

            dests.append(dests_item)

        max_length = d.pop("maxLength", UNSET)

        max_results = d.pop("maxResults", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, IndividualRouteRequestType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = IndividualRouteRequestType(_type)

        _service_type = d.pop("serviceType", UNSET)
        service_type: Union[Unset, IndividualRouteRequestServiceType]
        if isinstance(_service_type, Unset):
            service_type = UNSET
        else:
            service_type = IndividualRouteRequestServiceType(_service_type)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, IndividualRouteRequestProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = IndividualRouteRequestProfile(_profile)

        speed = d.pop("speed", UNSET)

        individual_route_request = cls(
            language=language,
            version=version,
            filter_type=filter_type,
            starts=starts,
            dests=dests,
            max_length=max_length,
            max_results=max_results,
            type=type,
            service_type=service_type,
            profile=profile,
            speed=speed,
        )

        individual_route_request.additional_properties = d
        return individual_route_request

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
