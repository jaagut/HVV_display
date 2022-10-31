from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attribute import Attribute
from ..models.journey_sd_name import JourneySDName
from ..models.path import Path
from ..models.service import Service
from ..models.shop_info import ShopInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleElement")


@attr.s(auto_attribs=True)
class ScheduleElement:
    """
    Attributes:
        from_ (JourneySDName):
        to (JourneySDName):
        line (Service):
        paths (Union[Unset, List[Path]]):
        attributes (Union[Unset, List[Attribute]]):
        extra (Union[Unset, bool]):
        cancelled (Union[Unset, bool]):
        intermediate_stops (Union[Unset, List[JourneySDName]]):
        service_id (Union[Unset, int]):
        shop_info (Union[Unset, List[ShopInfo]]):
    """

    from_: JourneySDName
    to: JourneySDName
    line: Service
    paths: Union[Unset, List[Path]] = UNSET
    attributes: Union[Unset, List[Attribute]] = UNSET
    extra: Union[Unset, bool] = False
    cancelled: Union[Unset, bool] = False
    intermediate_stops: Union[Unset, List[JourneySDName]] = UNSET
    service_id: Union[Unset, int] = UNSET
    shop_info: Union[Unset, List[ShopInfo]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        line = self.line.to_dict()

        paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()

                paths.append(paths_item)

        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        extra = self.extra
        cancelled = self.cancelled
        intermediate_stops: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intermediate_stops, Unset):
            intermediate_stops = []
            for intermediate_stops_item_data in self.intermediate_stops:
                intermediate_stops_item = intermediate_stops_item_data.to_dict()

                intermediate_stops.append(intermediate_stops_item)

        service_id = self.service_id
        shop_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shop_info, Unset):
            shop_info = []
            for shop_info_item_data in self.shop_info:
                shop_info_item = shop_info_item_data.to_dict()

                shop_info.append(shop_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "line": line,
            }
        )
        if paths is not UNSET:
            field_dict["paths"] = paths
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if extra is not UNSET:
            field_dict["extra"] = extra
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if intermediate_stops is not UNSET:
            field_dict["intermediateStops"] = intermediate_stops
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if shop_info is not UNSET:
            field_dict["shopInfo"] = shop_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = JourneySDName.from_dict(d.pop("from"))

        to = JourneySDName.from_dict(d.pop("to"))

        line = Service.from_dict(d.pop("line"))

        paths = []
        _paths = d.pop("paths", UNSET)
        for paths_item_data in _paths or []:
            paths_item = Path.from_dict(paths_item_data)

            paths.append(paths_item)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        extra = d.pop("extra", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        intermediate_stops = []
        _intermediate_stops = d.pop("intermediateStops", UNSET)
        for intermediate_stops_item_data in _intermediate_stops or []:
            intermediate_stops_item = JourneySDName.from_dict(
                intermediate_stops_item_data
            )

            intermediate_stops.append(intermediate_stops_item)

        service_id = d.pop("serviceId", UNSET)

        shop_info = []
        _shop_info = d.pop("shopInfo", UNSET)
        for shop_info_item_data in _shop_info or []:
            shop_info_item = ShopInfo.from_dict(shop_info_item_data)

            shop_info.append(shop_info_item)

        schedule_element = cls(
            from_=from_,
            to=to,
            line=line,
            paths=paths,
            attributes=attributes,
            extra=extra,
            cancelled=cancelled,
            intermediate_stops=intermediate_stops,
            service_id=service_id,
            shop_info=shop_info,
        )

        schedule_element.additional_properties = d
        return schedule_element

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
