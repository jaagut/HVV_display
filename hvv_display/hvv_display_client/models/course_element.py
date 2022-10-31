import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.attribute import Attribute
from ..models.path import Path
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseElement")


@attr.s(auto_attribs=True)
class CourseElement:
    """
    Attributes:
        from_station (SDName):
        to_station (SDName):
        dep_time (datetime.datetime):
        arr_time (datetime.datetime):
        from_platform (Union[Unset, str]):
        from_realtime_platform (Union[Unset, str]):
        to_platform (Union[Unset, str]):
        to_realtime_platform (Union[Unset, str]):
        model (Union[Unset, str]):
        dep_delay (Union[Unset, int]):
        arr_delay (Union[Unset, int]):
        from_extra (Union[Unset, bool]):
        from_cancelled (Union[Unset, bool]):
        to_extra (Union[Unset, bool]):
        to_cancelled (Union[Unset, bool]):
        attributes (Union[Unset, List[Attribute]]):
        path (Union[Unset, Path]):
    """

    from_station: SDName
    to_station: SDName
    dep_time: datetime.datetime
    arr_time: datetime.datetime
    from_platform: Union[Unset, str] = UNSET
    from_realtime_platform: Union[Unset, str] = UNSET
    to_platform: Union[Unset, str] = UNSET
    to_realtime_platform: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    dep_delay: Union[Unset, int] = UNSET
    arr_delay: Union[Unset, int] = UNSET
    from_extra: Union[Unset, bool] = False
    from_cancelled: Union[Unset, bool] = False
    to_extra: Union[Unset, bool] = False
    to_cancelled: Union[Unset, bool] = False
    attributes: Union[Unset, List[Attribute]] = UNSET
    path: Union[Unset, Path] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_station = self.from_station.to_dict()

        to_station = self.to_station.to_dict()

        dep_time = self.dep_time.isoformat()

        arr_time = self.arr_time.isoformat()

        from_platform = self.from_platform
        from_realtime_platform = self.from_realtime_platform
        to_platform = self.to_platform
        to_realtime_platform = self.to_realtime_platform
        model = self.model
        dep_delay = self.dep_delay
        arr_delay = self.arr_delay
        from_extra = self.from_extra
        from_cancelled = self.from_cancelled
        to_extra = self.to_extra
        to_cancelled = self.to_cancelled
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        path: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromStation": from_station,
                "toStation": to_station,
                "depTime": dep_time,
                "arrTime": arr_time,
            }
        )
        if from_platform is not UNSET:
            field_dict["fromPlatform"] = from_platform
        if from_realtime_platform is not UNSET:
            field_dict["fromRealtimePlatform"] = from_realtime_platform
        if to_platform is not UNSET:
            field_dict["toPlatform"] = to_platform
        if to_realtime_platform is not UNSET:
            field_dict["toRealtimePlatform"] = to_realtime_platform
        if model is not UNSET:
            field_dict["model"] = model
        if dep_delay is not UNSET:
            field_dict["depDelay"] = dep_delay
        if arr_delay is not UNSET:
            field_dict["arrDelay"] = arr_delay
        if from_extra is not UNSET:
            field_dict["fromExtra"] = from_extra
        if from_cancelled is not UNSET:
            field_dict["fromCancelled"] = from_cancelled
        if to_extra is not UNSET:
            field_dict["toExtra"] = to_extra
        if to_cancelled is not UNSET:
            field_dict["toCancelled"] = to_cancelled
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_station = SDName.from_dict(d.pop("fromStation"))

        to_station = SDName.from_dict(d.pop("toStation"))

        dep_time = isoparse(d.pop("depTime"))

        arr_time = isoparse(d.pop("arrTime"))

        from_platform = d.pop("fromPlatform", UNSET)

        from_realtime_platform = d.pop("fromRealtimePlatform", UNSET)

        to_platform = d.pop("toPlatform", UNSET)

        to_realtime_platform = d.pop("toRealtimePlatform", UNSET)

        model = d.pop("model", UNSET)

        dep_delay = d.pop("depDelay", UNSET)

        arr_delay = d.pop("arrDelay", UNSET)

        from_extra = d.pop("fromExtra", UNSET)

        from_cancelled = d.pop("fromCancelled", UNSET)

        to_extra = d.pop("toExtra", UNSET)

        to_cancelled = d.pop("toCancelled", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        _path = d.pop("path", UNSET)
        path: Union[Unset, Path]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = Path.from_dict(_path)

        course_element = cls(
            from_station=from_station,
            to_station=to_station,
            dep_time=dep_time,
            arr_time=arr_time,
            from_platform=from_platform,
            from_realtime_platform=from_realtime_platform,
            to_platform=to_platform,
            to_realtime_platform=to_realtime_platform,
            model=model,
            dep_delay=dep_delay,
            arr_delay=arr_delay,
            from_extra=from_extra,
            from_cancelled=from_cancelled,
            to_extra=to_extra,
            to_cancelled=to_cancelled,
            attributes=attributes,
            path=path,
        )

        course_element.additional_properties = d
        return course_element

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
