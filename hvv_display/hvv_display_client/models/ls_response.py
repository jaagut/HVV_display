from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ls_response_return_code import LSResponseReturnCode
from ..models.station_list_entry import StationListEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="LSResponse")


@attr.s(auto_attribs=True)
class LSResponse:
    """
    Attributes:
        return_code (LSResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        data_release_id (Union[Unset, str]):
        stations (Union[Unset, List[StationListEntry]]):
    """

    return_code: LSResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    data_release_id: Union[Unset, str] = UNSET
    stations: Union[Unset, List[StationListEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        data_release_id = self.data_release_id
        stations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stations, Unset):
            stations = []
            for stations_item_data in self.stations:
                stations_item = stations_item_data.to_dict()

                stations.append(stations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if data_release_id is not UNSET:
            field_dict["dataReleaseID"] = data_release_id
        if stations is not UNSET:
            field_dict["stations"] = stations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = LSResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        data_release_id = d.pop("dataReleaseID", UNSET)

        stations = []
        _stations = d.pop("stations", UNSET)
        for stations_item_data in _stations or []:
            stations_item = StationListEntry.from_dict(stations_item_data)

            stations.append(stations_item)

        ls_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            data_release_id=data_release_id,
            stations=stations,
        )

        ls_response.additional_properties = d
        return ls_response

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
