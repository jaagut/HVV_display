from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ticket_list_response_return_code import TicketListResponseReturnCode
from ..models.ticket_list_ticket_infos import TicketListTicketInfos
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketListResponse")


@attr.s(auto_attribs=True)
class TicketListResponse:
    """
    Attributes:
        return_code (TicketListResponseReturnCode):
        ticket_infos (List[TicketListTicketInfos]):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
    """

    return_code: TicketListResponseReturnCode
    ticket_infos: List[TicketListTicketInfos]
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        ticket_infos = []
        for ticket_infos_item_data in self.ticket_infos:
            ticket_infos_item = ticket_infos_item_data.to_dict()

            ticket_infos.append(ticket_infos_item)

        error_text = self.error_text
        error_dev_info = self.error_dev_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "ticketInfos": ticket_infos,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = TicketListResponseReturnCode(d.pop("returnCode"))

        ticket_infos = []
        _ticket_infos = d.pop("ticketInfos")
        for ticket_infos_item_data in _ticket_infos:
            ticket_infos_item = TicketListTicketInfos.from_dict(ticket_infos_item_data)

            ticket_infos.append(ticket_infos_item)

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        ticket_list_response = cls(
            return_code=return_code,
            ticket_infos=ticket_infos,
            error_text=error_text,
            error_dev_info=error_dev_info,
        )

        ticket_list_response.additional_properties = d
        return ticket_list_response

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
