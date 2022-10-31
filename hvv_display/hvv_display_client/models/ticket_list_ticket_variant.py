import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ticket_list_ticket_variant_discount import TicketListTicketVariantDiscount
from ..models.ticket_list_ticket_variant_ticket_class import (
    TicketListTicketVariantTicketClass,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketListTicketVariant")


@attr.s(auto_attribs=True)
class TicketListTicketVariant:
    """
    Attributes:
        ticket_class (TicketListTicketVariantTicketClass):
        discount (TicketListTicketVariantDiscount):
        validity_begin (datetime.date):
        validity_end (datetime.date):
        ticket_id (Union[Unset, int]):
        ka_nummer (Union[Unset, int]):
        price (Union[Unset, float]):
        currency (Union[Unset, str]):  Default: 'EUR'.
    """

    ticket_class: TicketListTicketVariantTicketClass
    discount: TicketListTicketVariantDiscount
    validity_begin: datetime.date
    validity_end: datetime.date
    ticket_id: Union[Unset, int] = UNSET
    ka_nummer: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = "EUR"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ticket_class = self.ticket_class.value

        discount = self.discount.value

        validity_begin = self.validity_begin.isoformat()
        validity_end = self.validity_end.isoformat()
        ticket_id = self.ticket_id
        ka_nummer = self.ka_nummer
        price = self.price
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticketClass": ticket_class,
                "discount": discount,
                "validityBegin": validity_begin,
                "validityEnd": validity_end,
            }
        )
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if ka_nummer is not UNSET:
            field_dict["kaNummer"] = ka_nummer
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ticket_class = TicketListTicketVariantTicketClass(d.pop("ticketClass"))

        discount = TicketListTicketVariantDiscount(d.pop("discount"))

        validity_begin = isoparse(d.pop("validityBegin")).date()

        validity_end = isoparse(d.pop("validityEnd")).date()

        ticket_id = d.pop("ticketId", UNSET)

        ka_nummer = d.pop("kaNummer", UNSET)

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        ticket_list_ticket_variant = cls(
            ticket_class=ticket_class,
            discount=discount,
            validity_begin=validity_begin,
            validity_end=validity_end,
            ticket_id=ticket_id,
            ka_nummer=ka_nummer,
            price=price,
            currency=currency,
        )

        ticket_list_ticket_variant.additional_properties = d
        return ticket_list_ticket_variant

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
