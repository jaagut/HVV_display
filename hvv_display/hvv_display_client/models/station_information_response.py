from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gti_time import GTITime
from ..models.partial_station import PartialStation
from ..models.station_information_response_return_code import (
    StationInformationResponseReturnCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StationInformationResponse")


@attr.s(auto_attribs=True)
class StationInformationResponse:
    """
    Attributes:
        return_code (StationInformationResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        partial_stations (Union[Unset, List[PartialStation]]):
        last_update (Union[Unset, GTITime]):
    """

    return_code: StationInformationResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    partial_stations: Union[Unset, List[PartialStation]] = UNSET
    last_update: Union[Unset, GTITime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        partial_stations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_stations, Unset):
            partial_stations = []
            for partial_stations_item_data in self.partial_stations:
                partial_stations_item = partial_stations_item_data.to_dict()

                partial_stations.append(partial_stations_item)

        last_update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.to_dict()

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
        if partial_stations is not UNSET:
            field_dict["partialStations"] = partial_stations
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = StationInformationResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        partial_stations = []
        _partial_stations = d.pop("partialStations", UNSET)
        for partial_stations_item_data in _partial_stations or []:
            partial_stations_item = PartialStation.from_dict(partial_stations_item_data)

            partial_stations.append(partial_stations_item)

        _last_update = d.pop("lastUpdate", UNSET)
        last_update: Union[Unset, GTITime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = GTITime.from_dict(_last_update)

        station_information_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            partial_stations=partial_stations,
            last_update=last_update,
        )

        station_information_response.additional_properties = d
        return station_information_response

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
