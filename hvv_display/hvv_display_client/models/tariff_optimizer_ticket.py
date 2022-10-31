from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tariff_optimizer_ticket_person_type import TariffOptimizerTicketPersonType
from ..models.tariff_optimizer_ticket_region_type import TariffOptimizerTicketRegionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffOptimizerTicket")


@attr.s(auto_attribs=True)
class TariffOptimizerTicket:
    """
    Attributes:
        tariff_regions (List[str]):
        region_type (TariffOptimizerTicketRegionType):
        person_type (TariffOptimizerTicketPersonType):
        tariff_kind_id (Union[Unset, int]):
        tariff_kind_label (Union[Unset, str]):
        tariff_level_id (Union[Unset, int]):
        tariff_level_label (Union[Unset, str]):
        count (Union[Unset, int]):
        extra_fare (Union[Unset, bool]):
        cent_price (Union[Unset, int]):
    """

    tariff_regions: List[str]
    region_type: TariffOptimizerTicketRegionType
    person_type: TariffOptimizerTicketPersonType
    tariff_kind_id: Union[Unset, int] = UNSET
    tariff_kind_label: Union[Unset, str] = UNSET
    tariff_level_id: Union[Unset, int] = UNSET
    tariff_level_label: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    extra_fare: Union[Unset, bool] = UNSET
    cent_price: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff_regions = self.tariff_regions

        region_type = self.region_type.value

        person_type = self.person_type.value

        tariff_kind_id = self.tariff_kind_id
        tariff_kind_label = self.tariff_kind_label
        tariff_level_id = self.tariff_level_id
        tariff_level_label = self.tariff_level_label
        count = self.count
        extra_fare = self.extra_fare
        cent_price = self.cent_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tariffRegions": tariff_regions,
                "regionType": region_type,
                "personType": person_type,
            }
        )
        if tariff_kind_id is not UNSET:
            field_dict["tariffKindId"] = tariff_kind_id
        if tariff_kind_label is not UNSET:
            field_dict["tariffKindLabel"] = tariff_kind_label
        if tariff_level_id is not UNSET:
            field_dict["tariffLevelId"] = tariff_level_id
        if tariff_level_label is not UNSET:
            field_dict["tariffLevelLabel"] = tariff_level_label
        if count is not UNSET:
            field_dict["count"] = count
        if extra_fare is not UNSET:
            field_dict["extraFare"] = extra_fare
        if cent_price is not UNSET:
            field_dict["centPrice"] = cent_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tariff_regions = cast(List[str], d.pop("tariffRegions"))

        region_type = TariffOptimizerTicketRegionType(d.pop("regionType"))

        person_type = TariffOptimizerTicketPersonType(d.pop("personType"))

        tariff_kind_id = d.pop("tariffKindId", UNSET)

        tariff_kind_label = d.pop("tariffKindLabel", UNSET)

        tariff_level_id = d.pop("tariffLevelId", UNSET)

        tariff_level_label = d.pop("tariffLevelLabel", UNSET)

        count = d.pop("count", UNSET)

        extra_fare = d.pop("extraFare", UNSET)

        cent_price = d.pop("centPrice", UNSET)

        tariff_optimizer_ticket = cls(
            tariff_regions=tariff_regions,
            region_type=region_type,
            person_type=person_type,
            tariff_kind_id=tariff_kind_id,
            tariff_kind_label=tariff_kind_label,
            tariff_level_id=tariff_level_id,
            tariff_level_label=tariff_level_label,
            count=count,
            extra_fare=extra_fare,
            cent_price=cent_price,
        )

        tariff_optimizer_ticket.additional_properties = d
        return tariff_optimizer_ticket

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
