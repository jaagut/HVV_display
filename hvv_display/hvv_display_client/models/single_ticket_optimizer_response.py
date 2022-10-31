from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.single_ticket_optimizer_response_return_code import (
    SingleTicketOptimizerResponseReturnCode,
)
from ..models.tariff_optimizer_ticket import TariffOptimizerTicket
from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTicketOptimizerResponse")


@attr.s(auto_attribs=True)
class SingleTicketOptimizerResponse:
    """
    Attributes:
        return_code (SingleTicketOptimizerResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        tickets (Union[Unset, List[TariffOptimizerTicket]]):
    """

    return_code: SingleTicketOptimizerResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    tickets: Union[Unset, List[TariffOptimizerTicket]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
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
                "returnCode": return_code,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if tickets is not UNSET:
            field_dict["tickets"] = tickets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = SingleTicketOptimizerResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        tickets = []
        _tickets = d.pop("tickets", UNSET)
        for tickets_item_data in _tickets or []:
            tickets_item = TariffOptimizerTicket.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        single_ticket_optimizer_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            tickets=tickets,
        )

        single_ticket_optimizer_response.additional_properties = d
        return single_ticket_optimizer_response

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
