from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DLFilterEntry")


@attr.s(auto_attribs=True)
class DLFilterEntry:
    """
    Attributes:
        service_id (Union[Unset, str]):
        station_i_ds (Union[Unset, List[str]]):
        label (Union[Unset, str]):
        service_name (Union[Unset, str]):
    """

    service_id: Union[Unset, str] = UNSET
    station_i_ds: Union[Unset, List[str]] = UNSET
    label: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_id = self.service_id
        station_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.station_i_ds, Unset):
            station_i_ds = self.station_i_ds

        label = self.label
        service_name = self.service_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_id is not UNSET:
            field_dict["serviceID"] = service_id
        if station_i_ds is not UNSET:
            field_dict["stationIDs"] = station_i_ds
        if label is not UNSET:
            field_dict["label"] = label
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_id = d.pop("serviceID", UNSET)

        station_i_ds = cast(List[str], d.pop("stationIDs", UNSET))

        label = d.pop("label", UNSET)

        service_name = d.pop("serviceName", UNSET)

        dl_filter_entry = cls(
            service_id=service_id,
            station_i_ds=station_i_ds,
            label=label,
            service_name=service_name,
        )

        dl_filter_entry.additional_properties = d
        return dl_filter_entry

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
