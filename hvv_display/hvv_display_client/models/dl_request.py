from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dl_filter_entry import DLFilterEntry
from ..models.dl_request_filter_type import DLRequestFilterType
from ..models.dl_request_service_types_item import DLRequestServiceTypesItem
from ..models.gti_time import GTITime
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DLRequest")


@attr.s(auto_attribs=True)
class DLRequest:
    """
    Attributes:
        time (GTITime):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, DLRequestFilterType]):  Default: DLRequestFilterType.NO_FILTER.
        station (Union[Unset, SDName]):
        stations (Union[Unset, List[SDName]]):
        max_list (Union[Unset, int]):
        max_time_offset (Union[Unset, int]):  Default: 120.
        all_stations_in_changing_node (Union[Unset, bool]):  Default: True.
        use_realtime (Union[Unset, bool]):
        return_filters (Union[Unset, bool]):
        filter_ (Union[Unset, List[DLFilterEntry]]):
        service_types (Union[Unset, List[DLRequestServiceTypesItem]]):
        departure (Union[Unset, bool]):  Default: True.
    """

    time: GTITime
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, DLRequestFilterType] = DLRequestFilterType.NO_FILTER
    station: Union[Unset, SDName] = UNSET
    stations: Union[Unset, List[SDName]] = UNSET
    max_list: Union[Unset, int] = UNSET
    max_time_offset: Union[Unset, int] = 120
    all_stations_in_changing_node: Union[Unset, bool] = True
    use_realtime: Union[Unset, bool] = False
    return_filters: Union[Unset, bool] = False
    filter_: Union[Unset, List[DLFilterEntry]] = UNSET
    service_types: Union[Unset, List[DLRequestServiceTypesItem]] = UNSET
    departure: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        station: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.station, Unset):
            station = self.station.to_dict()

        stations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stations, Unset):
            stations = []
            for stations_item_data in self.stations:
                stations_item = stations_item_data.to_dict()

                stations.append(stations_item)

        max_list = self.max_list
        max_time_offset = self.max_time_offset
        all_stations_in_changing_node = self.all_stations_in_changing_node
        use_realtime = self.use_realtime
        return_filters = self.return_filters
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

        departure = self.departure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if station is not UNSET:
            field_dict["station"] = station
        if stations is not UNSET:
            field_dict["stations"] = stations
        if max_list is not UNSET:
            field_dict["maxList"] = max_list
        if max_time_offset is not UNSET:
            field_dict["maxTimeOffset"] = max_time_offset
        if all_stations_in_changing_node is not UNSET:
            field_dict["allStationsInChangingNode"] = all_stations_in_changing_node
        if use_realtime is not UNSET:
            field_dict["useRealtime"] = use_realtime
        if return_filters is not UNSET:
            field_dict["returnFilters"] = return_filters
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if service_types is not UNSET:
            field_dict["serviceTypes"] = service_types
        if departure is not UNSET:
            field_dict["departure"] = departure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = GTITime.from_dict(d.pop("time"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, DLRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = DLRequestFilterType(_filter_type)

        _station = d.pop("station", UNSET)
        station: Union[Unset, SDName]
        if isinstance(_station, Unset):
            station = UNSET
        else:
            station = SDName.from_dict(_station)

        stations = []
        _stations = d.pop("stations", UNSET)
        for stations_item_data in _stations or []:
            stations_item = SDName.from_dict(stations_item_data)

            stations.append(stations_item)

        max_list = d.pop("maxList", UNSET)

        max_time_offset = d.pop("maxTimeOffset", UNSET)

        all_stations_in_changing_node = d.pop("allStationsInChangingNode", UNSET)

        use_realtime = d.pop("useRealtime", UNSET)

        return_filters = d.pop("returnFilters", UNSET)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = DLFilterEntry.from_dict(filter_item_data)

            filter_.append(filter_item)

        service_types = []
        _service_types = d.pop("serviceTypes", UNSET)
        for service_types_item_data in _service_types or []:
            service_types_item = DLRequestServiceTypesItem(service_types_item_data)

            service_types.append(service_types_item)

        departure = d.pop("departure", UNSET)

        dl_request = cls(
            time=time,
            language=language,
            version=version,
            filter_type=filter_type,
            station=station,
            stations=stations,
            max_list=max_list,
            max_time_offset=max_time_offset,
            all_stations_in_changing_node=all_stations_in_changing_node,
            use_realtime=use_realtime,
            return_filters=return_filters,
            filter_=filter_,
            service_types=service_types,
            departure=departure,
        )

        dl_request.additional_properties = d
        return dl_request

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
