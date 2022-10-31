from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.single_ticket_optimizer_request_filter_type import (
    SingleTicketOptimizerRequestFilterType,
)
from ..models.single_ticket_optimizer_request_route import (
    SingleTicketOptimizerRequestRoute,
)
from ..models.tariff_optimizer_ticket import TariffOptimizerTicket
from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTicketOptimizerRequest")


@attr.s(auto_attribs=True)
class SingleTicketOptimizerRequest:
    """
    Attributes:
        route (SingleTicketOptimizerRequestRoute):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, SingleTicketOptimizerRequestFilterType]):  Default:
            SingleTicketOptimizerRequestFilterType.NO_FILTER.
        with_return_journey (Union[Unset, bool]):
        number_of_adults (Union[Unset, int]):
        number_of_children (Union[Unset, int]):
        tickets (Union[Unset, List[TariffOptimizerTicket]]):
    """

    route: SingleTicketOptimizerRequestRoute
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, SingleTicketOptimizerRequestFilterType
    ] = SingleTicketOptimizerRequestFilterType.NO_FILTER
    with_return_journey: Union[Unset, bool] = UNSET
    number_of_adults: Union[Unset, int] = UNSET
    number_of_children: Union[Unset, int] = UNSET
    tickets: Union[Unset, List[TariffOptimizerTicket]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        route = self.route.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        with_return_journey = self.with_return_journey
        number_of_adults = self.number_of_adults
        number_of_children = self.number_of_children
        tickets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tickets, Unset):
            tickets = []
            for tickets_item_data in self.tickets:
                tickets_item = tickets_item_data.to_dict()

                tickets.append(tickets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "route": route,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if with_return_journey is not UNSET:
            field_dict["withReturnJourney"] = with_return_journey
        if number_of_adults is not UNSET:
            field_dict["numberOfAdults"] = number_of_adults
        if number_of_children is not UNSET:
            field_dict["numberOfChildren"] = number_of_children
        if tickets is not UNSET:
            field_dict["tickets"] = tickets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        route = SingleTicketOptimizerRequestRoute.from_dict(d.pop("route"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, SingleTicketOptimizerRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = SingleTicketOptimizerRequestFilterType(_filter_type)

        with_return_journey = d.pop("withReturnJourney", UNSET)

        number_of_adults = d.pop("numberOfAdults", UNSET)

        number_of_children = d.pop("numberOfChildren", UNSET)

        tickets = []
        _tickets = d.pop("tickets", UNSET)
        for tickets_item_data in _tickets or []:
            tickets_item = TariffOptimizerTicket.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        single_ticket_optimizer_request = cls(
            route=route,
            language=language,
            version=version,
            filter_type=filter_type,
            with_return_journey=with_return_journey,
            number_of_adults=number_of_adults,
            number_of_children=number_of_children,
            tickets=tickets,
        )

        single_ticket_optimizer_request.additional_properties = d
        return single_ticket_optimizer_request

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
