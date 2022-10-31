from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.announcement_request_filter_planned import (
    AnnouncementRequestFilterPlanned,
)
from ..models.announcement_request_filter_type import AnnouncementRequestFilterType
from ..models.time_range import TimeRange
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnouncementRequest")


@attr.s(auto_attribs=True)
class AnnouncementRequest:
    """
    Attributes:
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, AnnouncementRequestFilterType]):  Default: AnnouncementRequestFilterType.NO_FILTER.
        names (Union[Unset, List[str]]):
        time_range (Union[Unset, TimeRange]):
        full (Union[Unset, bool]):
        filter_planned (Union[Unset, AnnouncementRequestFilterPlanned]):
        show_broadcast_relevant (Union[Unset, bool]):
    """

    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, AnnouncementRequestFilterType
    ] = AnnouncementRequestFilterType.NO_FILTER
    names: Union[Unset, List[str]] = UNSET
    time_range: Union[Unset, TimeRange] = UNSET
    full: Union[Unset, bool] = False
    filter_planned: Union[Unset, AnnouncementRequestFilterPlanned] = UNSET
    show_broadcast_relevant: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        time_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        full = self.full
        filter_planned: Union[Unset, str] = UNSET
        if not isinstance(self.filter_planned, Unset):
            filter_planned = self.filter_planned.value

        show_broadcast_relevant = self.show_broadcast_relevant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if names is not UNSET:
            field_dict["names"] = names
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if full is not UNSET:
            field_dict["full"] = full
        if filter_planned is not UNSET:
            field_dict["filterPlanned"] = filter_planned
        if show_broadcast_relevant is not UNSET:
            field_dict["showBroadcastRelevant"] = show_broadcast_relevant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, AnnouncementRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = AnnouncementRequestFilterType(_filter_type)

        names = cast(List[str], d.pop("names", UNSET))

        _time_range = d.pop("timeRange", UNSET)
        time_range: Union[Unset, TimeRange]
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = TimeRange.from_dict(_time_range)

        full = d.pop("full", UNSET)

        _filter_planned = d.pop("filterPlanned", UNSET)
        filter_planned: Union[Unset, AnnouncementRequestFilterPlanned]
        if isinstance(_filter_planned, Unset):
            filter_planned = UNSET
        else:
            filter_planned = AnnouncementRequestFilterPlanned(_filter_planned)

        show_broadcast_relevant = d.pop("showBroadcastRelevant", UNSET)

        announcement_request = cls(
            language=language,
            version=version,
            filter_type=filter_type,
            names=names,
            time_range=time_range,
            full=full,
            filter_planned=filter_planned,
            show_broadcast_relevant=show_broadcast_relevant,
        )

        announcement_request.additional_properties = d
        return announcement_request

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
