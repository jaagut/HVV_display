from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.departure import Departure
from ..models.dl_filter_entry import DLFilterEntry
from ..models.dl_response_return_code import DLResponseReturnCode
from ..models.dl_response_service_types_item import DLResponseServiceTypesItem
from ..models.gti_time import GTITime
from ..types import UNSET, Unset

T = TypeVar("T", bound="DLResponse")


@attr.s(auto_attribs=True)
class DLResponse:
    """
    Attributes:
        return_code (DLResponseReturnCode):
        time (GTITime):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        departures (Union[Unset, List[Departure]]):
        filter_ (Union[Unset, List[DLFilterEntry]]):
        service_types (Union[Unset, List[DLResponseServiceTypesItem]]):
    """

    return_code: DLResponseReturnCode
    time: GTITime
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    departures: Union[Unset, List[Departure]] = UNSET
    filter_: Union[Unset, List[DLFilterEntry]] = UNSET
    service_types: Union[Unset, List[DLResponseServiceTypesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        time = self.time.to_dict()

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        departures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.departures, Unset):
            departures = []
            for departures_item_data in self.departures:
                departures_item = departures_item_data.to_dict()

                departures.append(departures_item)

        filter_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()

                filter_.append(filter_item)

        service_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_types, Unset):
            service_types = []
            for service_types_item_data in self.service_types:
                service_types_item = service_types_item_data.value

                service_types.append(service_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "time": time,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if departures is not UNSET:
            field_dict["departures"] = departures
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if service_types is not UNSET:
            field_dict["serviceTypes"] = service_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = DLResponseReturnCode(d.pop("returnCode"))

        time = GTITime.from_dict(d.pop("time"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        departures = []
        _departures = d.pop("departures", UNSET)
        for departures_item_data in _departures or []:
            departures_item = Departure.from_dict(departures_item_data)

            departures.append(departures_item)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = DLFilterEntry.from_dict(filter_item_data)

            filter_.append(filter_item)

        service_types = []
        _service_types = d.pop("serviceTypes", UNSET)
        for service_types_item_data in _service_types or []:
            service_types_item = DLResponseServiceTypesItem(service_types_item_data)

            service_types.append(service_types_item)

        dl_response = cls(
            return_code=return_code,
            time=time,
            error_text=error_text,
            error_dev_info=error_dev_info,
            departures=departures,
            filter_=filter_,
            service_types=service_types,
        )

        dl_response.additional_properties = d
        return dl_response

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
