from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ticket_list_request_filter_type import TicketListRequestFilterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketListRequest")


@attr.s(auto_attribs=True)
class TicketListRequest:
    """
    Attributes:
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, TicketListRequestFilterType]):  Default: TicketListRequestFilterType.NO_FILTER.
        station_key (Union[Unset, str]):
    """

    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, TicketListRequestFilterType
    ] = TicketListRequestFilterType.NO_FILTER
    station_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        station_key = self.station_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if station_key is not UNSET:
            field_dict["stationKey"] = station_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, TicketListRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = TicketListRequestFilterType(_filter_type)

        station_key = d.pop("stationKey", UNSET)

        ticket_list_request = cls(
            language=language,
            version=version,
            filter_type=filter_type,
            station_key=station_key,
        )

        ticket_list_request.additional_properties = d
        return ticket_list_request

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
