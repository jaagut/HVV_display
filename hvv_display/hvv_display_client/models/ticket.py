from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ticket")


@attr.s(auto_attribs=True)
class Ticket:
    """
    Attributes:
        type (str):
        level (str):
        tariff (str):
        price (Union[Unset, float]):
        reduced_price (Union[Unset, float]):
        currency (Union[Unset, str]):  Default: 'EUR'.
        range_ (Union[Unset, str]):
        ticket_remarks (Union[Unset, str]):
    """

    type: str
    level: str
    tariff: str
    price: Union[Unset, float] = UNSET
    reduced_price: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = "EUR"
    range_: Union[Unset, str] = UNSET
    ticket_remarks: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        level = self.level
        tariff = self.tariff
        price = self.price
        reduced_price = self.reduced_price
        currency = self.currency
        range_ = self.range_
        ticket_remarks = self.ticket_remarks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "level": level,
                "tariff": tariff,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if reduced_price is not UNSET:
            field_dict["reducedPrice"] = reduced_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if range_ is not UNSET:
            field_dict["range"] = range_
        if ticket_remarks is not UNSET:
            field_dict["ticketRemarks"] = ticket_remarks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        level = d.pop("level")

        tariff = d.pop("tariff")

        price = d.pop("price", UNSET)

        reduced_price = d.pop("reducedPrice", UNSET)

        currency = d.pop("currency", UNSET)

        range_ = d.pop("range", UNSET)

        ticket_remarks = d.pop("ticketRemarks", UNSET)

        ticket = cls(
            type=type,
            level=level,
            tariff=tariff,
            price=price,
            reduced_price=reduced_price,
            currency=currency,
            range_=range_,
            ticket_remarks=ticket_remarks,
        )

        ticket.additional_properties = d
        return ticket

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
