import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cont_search_by_service_id import ContSearchByServiceId
from ..models.schedule_element import ScheduleElement
from ..models.sd_name import SDName
from ..models.tariff_info import TariffInfo
from ..models.ticket import Ticket
from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@attr.s(auto_attribs=True)
class Schedule:
    """
    Attributes:
        start (SDName):
        dest (SDName):
        route_id (Union[Unset, int]):
        time (Union[Unset, int]):
        footpath_time (Union[Unset, int]):
        planned_departure_time (Union[Unset, datetime.datetime]):
        real_departure_time (Union[Unset, datetime.datetime]):
        planned_arrival_time (Union[Unset, datetime.datetime]):
        real_arrival_time (Union[Unset, datetime.datetime]):
        tickets (Union[Unset, List[Ticket]]):
        tariff_infos (Union[Unset, List[TariffInfo]]):
        schedule_elements (Union[Unset, List[ScheduleElement]]):
        cont_search_before (Union[Unset, ContSearchByServiceId]):
        cont_search_after (Union[Unset, ContSearchByServiceId]):
    """

    start: SDName
    dest: SDName
    route_id: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    footpath_time: Union[Unset, int] = UNSET
    planned_departure_time: Union[Unset, datetime.datetime] = UNSET
    real_departure_time: Union[Unset, datetime.datetime] = UNSET
    planned_arrival_time: Union[Unset, datetime.datetime] = UNSET
    real_arrival_time: Union[Unset, datetime.datetime] = UNSET
    tickets: Union[Unset, List[Ticket]] = UNSET
    tariff_infos: Union[Unset, List[TariffInfo]] = UNSET
    schedule_elements: Union[Unset, List[ScheduleElement]] = UNSET
    cont_search_before: Union[Unset, ContSearchByServiceId] = UNSET
    cont_search_after: Union[Unset, ContSearchByServiceId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.to_dict()

        dest = self.dest.to_dict()

        route_id = self.route_id
        time = self.time
        footpath_time = self.footpath_time
        planned_departure_time: Union[Unset, str] = UNSET
        if not isinstance(self.planned_departure_time, Unset):
            planned_departure_time = self.planned_departure_time.isoformat()

        real_departure_time: Union[Unset, str] = UNSET
        if not isinstance(self.real_departure_time, Unset):
            real_departure_time = self.real_departure_time.isoformat()

        planned_arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.planned_arrival_time, Unset):
            planned_arrival_time = self.planned_arrival_time.isoformat()

        real_arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.real_arrival_time, Unset):
            real_arrival_time = self.real_arrival_time.isoformat()

        tickets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tickets, Unset):
            tickets = []
            for tickets_item_data in self.tickets:
                tickets_item = tickets_item_data.to_dict()

                tickets.append(tickets_item)

        tariff_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_infos, Unset):
            tariff_infos = []
            for tariff_infos_item_data in self.tariff_infos:
                tariff_infos_item = tariff_infos_item_data.to_dict()

                tariff_infos.append(tariff_infos_item)

        schedule_elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedule_elements, Unset):
            schedule_elements = []
            for schedule_elements_item_data in self.schedule_elements:
                schedule_elements_item = schedule_elements_item_data.to_dict()

                schedule_elements.append(schedule_elements_item)

        cont_search_before: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cont_search_before, Unset):
            cont_search_before = self.cont_search_before.to_dict()

        cont_search_after: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cont_search_after, Unset):
            cont_search_after = self.cont_search_after.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "dest": dest,
            }
        )
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if time is not UNSET:
            field_dict["time"] = time
        if footpath_time is not UNSET:
            field_dict["footpathTime"] = footpath_time
        if planned_departure_time is not UNSET:
            field_dict["plannedDepartureTime"] = planned_departure_time
        if real_departure_time is not UNSET:
            field_dict["realDepartureTime"] = real_departure_time
        if planned_arrival_time is not UNSET:
            field_dict["plannedArrivalTime"] = planned_arrival_time
        if real_arrival_time is not UNSET:
            field_dict["realArrivalTime"] = real_arrival_time
        if tickets is not UNSET:
            field_dict["tickets"] = tickets
        if tariff_infos is not UNSET:
            field_dict["tariffInfos"] = tariff_infos
        if schedule_elements is not UNSET:
            field_dict["scheduleElements"] = schedule_elements
        if cont_search_before is not UNSET:
            field_dict["contSearchBefore"] = cont_search_before
        if cont_search_after is not UNSET:
            field_dict["contSearchAfter"] = cont_search_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = SDName.from_dict(d.pop("start"))

        dest = SDName.from_dict(d.pop("dest"))

        route_id = d.pop("routeId", UNSET)

        time = d.pop("time", UNSET)

        footpath_time = d.pop("footpathTime", UNSET)

        _planned_departure_time = d.pop("plannedDepartureTime", UNSET)
        planned_departure_time: Union[Unset, datetime.datetime]
        if isinstance(_planned_departure_time, Unset):
            planned_departure_time = UNSET
        else:
            planned_departure_time = isoparse(_planned_departure_time)

        _real_departure_time = d.pop("realDepartureTime", UNSET)
        real_departure_time: Union[Unset, datetime.datetime]
        if isinstance(_real_departure_time, Unset):
            real_departure_time = UNSET
        else:
            real_departure_time = isoparse(_real_departure_time)

        _planned_arrival_time = d.pop("plannedArrivalTime", UNSET)
        planned_arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_planned_arrival_time, Unset):
            planned_arrival_time = UNSET
        else:
            planned_arrival_time = isoparse(_planned_arrival_time)

        _real_arrival_time = d.pop("realArrivalTime", UNSET)
        real_arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_real_arrival_time, Unset):
            real_arrival_time = UNSET
        else:
            real_arrival_time = isoparse(_real_arrival_time)

        tickets = []
        _tickets = d.pop("tickets", UNSET)
        for tickets_item_data in _tickets or []:
            tickets_item = Ticket.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        tariff_infos = []
        _tariff_infos = d.pop("tariffInfos", UNSET)
        for tariff_infos_item_data in _tariff_infos or []:
            tariff_infos_item = TariffInfo.from_dict(tariff_infos_item_data)

            tariff_infos.append(tariff_infos_item)

        schedule_elements = []
        _schedule_elements = d.pop("scheduleElements", UNSET)
        for schedule_elements_item_data in _schedule_elements or []:
            schedule_elements_item = ScheduleElement.from_dict(
                schedule_elements_item_data
            )

            schedule_elements.append(schedule_elements_item)

        _cont_search_before = d.pop("contSearchBefore", UNSET)
        cont_search_before: Union[Unset, ContSearchByServiceId]
        if isinstance(_cont_search_before, Unset):
            cont_search_before = UNSET
        else:
            cont_search_before = ContSearchByServiceId.from_dict(_cont_search_before)

        _cont_search_after = d.pop("contSearchAfter", UNSET)
        cont_search_after: Union[Unset, ContSearchByServiceId]
        if isinstance(_cont_search_after, Unset):
            cont_search_after = UNSET
        else:
            cont_search_after = ContSearchByServiceId.from_dict(_cont_search_after)

        schedule = cls(
            start=start,
            dest=dest,
            route_id=route_id,
            time=time,
            footpath_time=footpath_time,
            planned_departure_time=planned_departure_time,
            real_departure_time=real_departure_time,
            planned_arrival_time=planned_arrival_time,
            real_arrival_time=real_arrival_time,
            tickets=tickets,
            tariff_infos=tariff_infos,
            schedule_elements=schedule_elements,
            cont_search_before=cont_search_before,
            cont_search_after=cont_search_after,
        )

        schedule.additional_properties = d
        return schedule

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
