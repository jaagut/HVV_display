from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gti_time import GTITime
from ..models.schedule_element_light import ScheduleElementLight
from ..models.tariff_request_filter_type import TariffRequestFilterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffRequest")


@attr.s(auto_attribs=True)
class TariffRequest:
    """
    Attributes:
        schedule_elements (List[ScheduleElementLight]):
        departure (GTITime):
        arrival (GTITime):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, TariffRequestFilterType]):  Default: TariffRequestFilterType.NO_FILTER.
        return_reduced (Union[Unset, bool]):
        return_partial_tickets (Union[Unset, bool]):  Default: True.
    """

    schedule_elements: List[ScheduleElementLight]
    departure: GTITime
    arrival: GTITime
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, TariffRequestFilterType
    ] = TariffRequestFilterType.NO_FILTER
    return_reduced: Union[Unset, bool] = False
    return_partial_tickets: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule_elements = []
        for schedule_elements_item_data in self.schedule_elements:
            schedule_elements_item = schedule_elements_item_data.to_dict()

            schedule_elements.append(schedule_elements_item)

        departure = self.departure.to_dict()

        arrival = self.arrival.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        return_reduced = self.return_reduced
        return_partial_tickets = self.return_partial_tickets

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleElements": schedule_elements,
                "departure": departure,
                "arrival": arrival,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if return_reduced is not UNSET:
            field_dict["returnReduced"] = return_reduced
        if return_partial_tickets is not UNSET:
            field_dict["returnPartialTickets"] = return_partial_tickets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schedule_elements = []
        _schedule_elements = d.pop("scheduleElements")
        for schedule_elements_item_data in _schedule_elements:
            schedule_elements_item = ScheduleElementLight.from_dict(
                schedule_elements_item_data
            )

            schedule_elements.append(schedule_elements_item)

        departure = GTITime.from_dict(d.pop("departure"))

        arrival = GTITime.from_dict(d.pop("arrival"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, TariffRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = TariffRequestFilterType(_filter_type)

        return_reduced = d.pop("returnReduced", UNSET)

        return_partial_tickets = d.pop("returnPartialTickets", UNSET)

        tariff_request = cls(
            schedule_elements=schedule_elements,
            departure=departure,
            arrival=arrival,
            language=language,
            version=version,
            filter_type=filter_type,
            return_reduced=return_reduced,
            return_partial_tickets=return_partial_tickets,
        )

        tariff_request.additional_properties = d
        return tariff_request

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
