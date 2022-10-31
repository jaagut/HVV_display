from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tariff_kind_ticket_type import TariffKindTicketType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffKind")


@attr.s(auto_attribs=True)
class TariffKind:
    """
    Attributes:
        label (str):
        id (Union[Unset, int]):
        requires_person_type (Union[Unset, bool]):
        ticket_type (Union[Unset, TariffKindTicketType]):
        level_combinations (Union[Unset, List[int]]):
    """

    label: str
    id: Union[Unset, int] = UNSET
    requires_person_type: Union[Unset, bool] = False
    ticket_type: Union[Unset, TariffKindTicketType] = UNSET
    level_combinations: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        id = self.id
        requires_person_type = self.requires_person_type
        ticket_type: Union[Unset, str] = UNSET
        if not isinstance(self.ticket_type, Unset):
            ticket_type = self.ticket_type.value

        level_combinations: Union[Unset, List[int]] = UNSET
        if not isinstance(self.level_combinations, Unset):
            level_combinations = self.level_combinations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if requires_person_type is not UNSET:
            field_dict["requiresPersonType"] = requires_person_type
        if ticket_type is not UNSET:
            field_dict["ticketType"] = ticket_type
        if level_combinations is not UNSET:
            field_dict["levelCombinations"] = level_combinations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        id = d.pop("id", UNSET)

        requires_person_type = d.pop("requiresPersonType", UNSET)

        _ticket_type = d.pop("ticketType", UNSET)
        ticket_type: Union[Unset, TariffKindTicketType]
        if isinstance(_ticket_type, Unset):
            ticket_type = UNSET
        else:
            ticket_type = TariffKindTicketType(_ticket_type)

        level_combinations = cast(List[int], d.pop("levelCombinations", UNSET))

        tariff_kind = cls(
            label=label,
            id=id,
            requires_person_type=requires_person_type,
            ticket_type=ticket_type,
            level_combinations=level_combinations,
        )

        tariff_kind.additional_properties = d
        return tariff_kind

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
