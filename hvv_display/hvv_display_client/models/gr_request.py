from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cont_search_by_service_id import ContSearchByServiceId
from ..models.gr_request_coordinate_type import GRRequestCoordinateType
from ..models.gr_request_filter_type import GRRequestFilterType
from ..models.gr_request_realtime import GRRequestRealtime
from ..models.gr_request_to_dest_by import GRRequestToDestBy
from ..models.gr_request_to_start_by import GRRequestToStartBy
from ..models.gti_time import GTITime
from ..models.penalty import Penalty
from ..models.sd_name import SDName
from ..models.tariff_info_selector import TariffInfoSelector
from ..types import UNSET, Unset

T = TypeVar("T", bound="GRRequest")


@attr.s(auto_attribs=True)
class GRRequest:
    """
    Attributes:
        start (SDName):
        dest (SDName):
        time (GTITime):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, GRRequestFilterType]):  Default: GRRequestFilterType.NO_FILTER.
        via (Union[Unset, SDName]):
        time_is_departure (Union[Unset, bool]):
        with_paths (Union[Unset, bool]):
        number_of_schedules (Union[Unset, int]):
        penalties (Union[Unset, List[Penalty]]):
        tariff_details (Union[Unset, bool]):
        continous_search (Union[Unset, bool]):
        cont_search_by_service_id (Union[Unset, ContSearchByServiceId]):
        coordinate_type (Union[Unset, GRRequestCoordinateType]):  Default: GRRequestCoordinateType.EPSG_4326.
        schedules_before (Union[Unset, int]):
        schedules_after (Union[Unset, int]):
        tariff_info_selector (Union[Unset, List[TariffInfoSelector]]):
        return_reduced (Union[Unset, bool]):
        return_partial_tickets (Union[Unset, bool]):  Default: True.
        realtime (Union[Unset, GRRequestRealtime]):  Default: GRRequestRealtime.AUTO.
        intermediate_stops (Union[Unset, bool]):
        use_station_position (Union[Unset, bool]):  Default: True.
        forced_start (Union[Unset, SDName]):
        forced_dest (Union[Unset, SDName]):
        to_start_by (Union[Unset, GRRequestToStartBy]):
        to_dest_by (Union[Unset, GRRequestToDestBy]):
        return_cont_search_data (Union[Unset, bool]):
    """

    start: SDName
    dest: SDName
    time: GTITime
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, GRRequestFilterType] = GRRequestFilterType.NO_FILTER
    via: Union[Unset, SDName] = UNSET
    time_is_departure: Union[Unset, bool] = UNSET
    with_paths: Union[Unset, bool] = UNSET
    number_of_schedules: Union[Unset, int] = UNSET
    penalties: Union[Unset, List[Penalty]] = UNSET
    tariff_details: Union[Unset, bool] = False
    continous_search: Union[Unset, bool] = False
    cont_search_by_service_id: Union[Unset, ContSearchByServiceId] = UNSET
    coordinate_type: Union[
        Unset, GRRequestCoordinateType
    ] = GRRequestCoordinateType.EPSG_4326
    schedules_before: Union[Unset, int] = 0
    schedules_after: Union[Unset, int] = 0
    tariff_info_selector: Union[Unset, List[TariffInfoSelector]] = UNSET
    return_reduced: Union[Unset, bool] = False
    return_partial_tickets: Union[Unset, bool] = True
    realtime: Union[Unset, GRRequestRealtime] = GRRequestRealtime.AUTO
    intermediate_stops: Union[Unset, bool] = False
    use_station_position: Union[Unset, bool] = True
    forced_start: Union[Unset, SDName] = UNSET
    forced_dest: Union[Unset, SDName] = UNSET
    to_start_by: Union[Unset, GRRequestToStartBy] = UNSET
    to_dest_by: Union[Unset, GRRequestToDestBy] = UNSET
    return_cont_search_data: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.to_dict()

        dest = self.dest.to_dict()

        time = self.time.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        via: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.via, Unset):
            via = self.via.to_dict()

        time_is_departure = self.time_is_departure
        with_paths = self.with_paths
        number_of_schedules = self.number_of_schedules
        penalties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.penalties, Unset):
            penalties = []
            for penalties_item_data in self.penalties:
                penalties_item = penalties_item_data.to_dict()

                penalties.append(penalties_item)

        tariff_details = self.tariff_details
        continous_search = self.continous_search
        cont_search_by_service_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cont_search_by_service_id, Unset):
            cont_search_by_service_id = self.cont_search_by_service_id.to_dict()

        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        schedules_before = self.schedules_before
        schedules_after = self.schedules_after
        tariff_info_selector: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_info_selector, Unset):
            tariff_info_selector = []
            for tariff_info_selector_item_data in self.tariff_info_selector:
                tariff_info_selector_item = tariff_info_selector_item_data.to_dict()

                tariff_info_selector.append(tariff_info_selector_item)

        return_reduced = self.return_reduced
        return_partial_tickets = self.return_partial_tickets
        realtime: Union[Unset, str] = UNSET
        if not isinstance(self.realtime, Unset):
            realtime = self.realtime.value

        intermediate_stops = self.intermediate_stops
        use_station_position = self.use_station_position
        forced_start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forced_start, Unset):
            forced_start = self.forced_start.to_dict()

        forced_dest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forced_dest, Unset):
            forced_dest = self.forced_dest.to_dict()

        to_start_by: Union[Unset, str] = UNSET
        if not isinstance(self.to_start_by, Unset):
            to_start_by = self.to_start_by.value

        to_dest_by: Union[Unset, str] = UNSET
        if not isinstance(self.to_dest_by, Unset):
            to_dest_by = self.to_dest_by.value

        return_cont_search_data = self.return_cont_search_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "dest": dest,
                "time": time,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if via is not UNSET:
            field_dict["via"] = via
        if time_is_departure is not UNSET:
            field_dict["timeIsDeparture"] = time_is_departure
        if with_paths is not UNSET:
            field_dict["withPaths"] = with_paths
        if number_of_schedules is not UNSET:
            field_dict["numberOfSchedules"] = number_of_schedules
        if penalties is not UNSET:
            field_dict["penalties"] = penalties
        if tariff_details is not UNSET:
            field_dict["tariffDetails"] = tariff_details
        if continous_search is not UNSET:
            field_dict["continousSearch"] = continous_search
        if cont_search_by_service_id is not UNSET:
            field_dict["contSearchByServiceId"] = cont_search_by_service_id
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type
        if schedules_before is not UNSET:
            field_dict["schedulesBefore"] = schedules_before
        if schedules_after is not UNSET:
            field_dict["schedulesAfter"] = schedules_after
        if tariff_info_selector is not UNSET:
            field_dict["tariffInfoSelector"] = tariff_info_selector
        if return_reduced is not UNSET:
            field_dict["returnReduced"] = return_reduced
        if return_partial_tickets is not UNSET:
            field_dict["returnPartialTickets"] = return_partial_tickets
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if intermediate_stops is not UNSET:
            field_dict["intermediateStops"] = intermediate_stops
        if use_station_position is not UNSET:
            field_dict["useStationPosition"] = use_station_position
        if forced_start is not UNSET:
            field_dict["forcedStart"] = forced_start
        if forced_dest is not UNSET:
            field_dict["forcedDest"] = forced_dest
        if to_start_by is not UNSET:
            field_dict["toStartBy"] = to_start_by
        if to_dest_by is not UNSET:
            field_dict["toDestBy"] = to_dest_by
        if return_cont_search_data is not UNSET:
            field_dict["returnContSearchData"] = return_cont_search_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = SDName.from_dict(d.pop("start"))

        dest = SDName.from_dict(d.pop("dest"))

        time = GTITime.from_dict(d.pop("time"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, GRRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = GRRequestFilterType(_filter_type)

        _via = d.pop("via", UNSET)
        via: Union[Unset, SDName]
        if isinstance(_via, Unset):
            via = UNSET
        else:
            via = SDName.from_dict(_via)

        time_is_departure = d.pop("timeIsDeparture", UNSET)

        with_paths = d.pop("withPaths", UNSET)

        number_of_schedules = d.pop("numberOfSchedules", UNSET)

        penalties = []
        _penalties = d.pop("penalties", UNSET)
        for penalties_item_data in _penalties or []:
            penalties_item = Penalty.from_dict(penalties_item_data)

            penalties.append(penalties_item)

        tariff_details = d.pop("tariffDetails", UNSET)

        continous_search = d.pop("continousSearch", UNSET)

        _cont_search_by_service_id = d.pop("contSearchByServiceId", UNSET)
        cont_search_by_service_id: Union[Unset, ContSearchByServiceId]
        if isinstance(_cont_search_by_service_id, Unset):
            cont_search_by_service_id = UNSET
        else:
            cont_search_by_service_id = ContSearchByServiceId.from_dict(
                _cont_search_by_service_id
            )

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, GRRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = GRRequestCoordinateType(_coordinate_type)

        schedules_before = d.pop("schedulesBefore", UNSET)

        schedules_after = d.pop("schedulesAfter", UNSET)

        tariff_info_selector = []
        _tariff_info_selector = d.pop("tariffInfoSelector", UNSET)
        for tariff_info_selector_item_data in _tariff_info_selector or []:
            tariff_info_selector_item = TariffInfoSelector.from_dict(
                tariff_info_selector_item_data
            )

            tariff_info_selector.append(tariff_info_selector_item)

        return_reduced = d.pop("returnReduced", UNSET)

        return_partial_tickets = d.pop("returnPartialTickets", UNSET)

        _realtime = d.pop("realtime", UNSET)
        realtime: Union[Unset, GRRequestRealtime]
        if isinstance(_realtime, Unset):
            realtime = UNSET
        else:
            realtime = GRRequestRealtime(_realtime)

        intermediate_stops = d.pop("intermediateStops", UNSET)

        use_station_position = d.pop("useStationPosition", UNSET)

        _forced_start = d.pop("forcedStart", UNSET)
        forced_start: Union[Unset, SDName]
        if isinstance(_forced_start, Unset):
            forced_start = UNSET
        else:
            forced_start = SDName.from_dict(_forced_start)

        _forced_dest = d.pop("forcedDest", UNSET)
        forced_dest: Union[Unset, SDName]
        if isinstance(_forced_dest, Unset):
            forced_dest = UNSET
        else:
            forced_dest = SDName.from_dict(_forced_dest)

        _to_start_by = d.pop("toStartBy", UNSET)
        to_start_by: Union[Unset, GRRequestToStartBy]
        if isinstance(_to_start_by, Unset):
            to_start_by = UNSET
        else:
            to_start_by = GRRequestToStartBy(_to_start_by)

        _to_dest_by = d.pop("toDestBy", UNSET)
        to_dest_by: Union[Unset, GRRequestToDestBy]
        if isinstance(_to_dest_by, Unset):
            to_dest_by = UNSET
        else:
            to_dest_by = GRRequestToDestBy(_to_dest_by)

        return_cont_search_data = d.pop("returnContSearchData", UNSET)

        gr_request = cls(
            start=start,
            dest=dest,
            time=time,
            language=language,
            version=version,
            filter_type=filter_type,
            via=via,
            time_is_departure=time_is_departure,
            with_paths=with_paths,
            number_of_schedules=number_of_schedules,
            penalties=penalties,
            tariff_details=tariff_details,
            continous_search=continous_search,
            cont_search_by_service_id=cont_search_by_service_id,
            coordinate_type=coordinate_type,
            schedules_before=schedules_before,
            schedules_after=schedules_after,
            tariff_info_selector=tariff_info_selector,
            return_reduced=return_reduced,
            return_partial_tickets=return_partial_tickets,
            realtime=realtime,
            intermediate_stops=intermediate_stops,
            use_station_position=use_station_position,
            forced_start=forced_start,
            forced_dest=forced_dest,
            to_start_by=to_start_by,
            to_dest_by=to_dest_by,
            return_cont_search_data=return_cont_search_data,
        )

        gr_request.additional_properties = d
        return gr_request

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
