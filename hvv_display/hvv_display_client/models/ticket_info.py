from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ticket_info_region_type import TicketInfoRegionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketInfo")


@attr.s(auto_attribs=True)
class TicketInfo:
    """
    Attributes:
        tariff_kind_label (str):
        tariff_level_label (str):
        via_path_id (int):
        tariff_kind_id (Union[Unset, int]):
        tariff_level_id (Union[Unset, int]):
        tariff_group_id (Union[Unset, int]):
        tariff_group_label (Union[Unset, str]):
        base_price (Union[Unset, float]):
        extra_fare_price (Union[Unset, float]):
        reduced_base_price (Union[Unset, float]):
        reduced_extra_fare_price (Union[Unset, float]):
        currency (Union[Unset, str]):  Default: 'EUR'.
        region_type (Union[Unset, TicketInfoRegionType]):
        not_recommended (Union[Unset, bool]):
        shop_link_regular (Union[Unset, str]):
        shop_link_extra_fare (Union[Unset, str]):
        start_station_id (Union[Unset, str]):
        end_station_id (Union[Unset, str]):
    """

    tariff_kind_label: str
    tariff_level_label: str
    via_path_id: int
    tariff_kind_id: Union[Unset, int] = UNSET
    tariff_level_id: Union[Unset, int] = UNSET
    tariff_group_id: Union[Unset, int] = UNSET
    tariff_group_label: Union[Unset, str] = UNSET
    base_price: Union[Unset, float] = UNSET
    extra_fare_price: Union[Unset, float] = UNSET
    reduced_base_price: Union[Unset, float] = UNSET
    reduced_extra_fare_price: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = "EUR"
    region_type: Union[Unset, TicketInfoRegionType] = UNSET
    not_recommended: Union[Unset, bool] = False
    shop_link_regular: Union[Unset, str] = UNSET
    shop_link_extra_fare: Union[Unset, str] = UNSET
    start_station_id: Union[Unset, str] = UNSET
    end_station_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff_kind_label = self.tariff_kind_label
        tariff_level_label = self.tariff_level_label
        via_path_id = self.via_path_id
        tariff_kind_id = self.tariff_kind_id
        tariff_level_id = self.tariff_level_id
        tariff_group_id = self.tariff_group_id
        tariff_group_label = self.tariff_group_label
        base_price = self.base_price
        extra_fare_price = self.extra_fare_price
        reduced_base_price = self.reduced_base_price
        reduced_extra_fare_price = self.reduced_extra_fare_price
        currency = self.currency
        region_type: Union[Unset, str] = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value

        not_recommended = self.not_recommended
        shop_link_regular = self.shop_link_regular
        shop_link_extra_fare = self.shop_link_extra_fare
        start_station_id = self.start_station_id
        end_station_id = self.end_station_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tariffKindLabel": tariff_kind_label,
                "tariffLevelLabel": tariff_level_label,
                "viaPathId": via_path_id,
            }
        )
        if tariff_kind_id is not UNSET:
            field_dict["tariffKindID"] = tariff_kind_id
        if tariff_level_id is not UNSET:
            field_dict["tariffLevelID"] = tariff_level_id
        if tariff_group_id is not UNSET:
            field_dict["tariffGroupID"] = tariff_group_id
        if tariff_group_label is not UNSET:
            field_dict["tariffGroupLabel"] = tariff_group_label
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if extra_fare_price is not UNSET:
            field_dict["extraFarePrice"] = extra_fare_price
        if reduced_base_price is not UNSET:
            field_dict["reducedBasePrice"] = reduced_base_price
        if reduced_extra_fare_price is not UNSET:
            field_dict["reducedExtraFarePrice"] = reduced_extra_fare_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if region_type is not UNSET:
            field_dict["regionType"] = region_type
        if not_recommended is not UNSET:
            field_dict["notRecommended"] = not_recommended
        if shop_link_regular is not UNSET:
            field_dict["shopLinkRegular"] = shop_link_regular
        if shop_link_extra_fare is not UNSET:
            field_dict["shopLinkExtraFare"] = shop_link_extra_fare
        if start_station_id is not UNSET:
            field_dict["startStationId"] = start_station_id
        if end_station_id is not UNSET:
            field_dict["endStationId"] = end_station_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tariff_kind_label = d.pop("tariffKindLabel")

        tariff_level_label = d.pop("tariffLevelLabel")

        via_path_id = d.pop("viaPathId")

        tariff_kind_id = d.pop("tariffKindID", UNSET)

        tariff_level_id = d.pop("tariffLevelID", UNSET)

        tariff_group_id = d.pop("tariffGroupID", UNSET)

        tariff_group_label = d.pop("tariffGroupLabel", UNSET)

        base_price = d.pop("basePrice", UNSET)

        extra_fare_price = d.pop("extraFarePrice", UNSET)

        reduced_base_price = d.pop("reducedBasePrice", UNSET)

        reduced_extra_fare_price = d.pop("reducedExtraFarePrice", UNSET)

        currency = d.pop("currency", UNSET)

        _region_type = d.pop("regionType", UNSET)
        region_type: Union[Unset, TicketInfoRegionType]
        if isinstance(_region_type, Unset):
            region_type = UNSET
        else:
            region_type = TicketInfoRegionType(_region_type)

        not_recommended = d.pop("notRecommended", UNSET)

        shop_link_regular = d.pop("shopLinkRegular", UNSET)

        shop_link_extra_fare = d.pop("shopLinkExtraFare", UNSET)

        start_station_id = d.pop("startStationId", UNSET)

        end_station_id = d.pop("endStationId", UNSET)

        ticket_info = cls(
            tariff_kind_label=tariff_kind_label,
            tariff_level_label=tariff_level_label,
            via_path_id=via_path_id,
            tariff_kind_id=tariff_kind_id,
            tariff_level_id=tariff_level_id,
            tariff_group_id=tariff_group_id,
            tariff_group_label=tariff_group_label,
            base_price=base_price,
            extra_fare_price=extra_fare_price,
            reduced_base_price=reduced_base_price,
            reduced_extra_fare_price=reduced_extra_fare_price,
            currency=currency,
            region_type=region_type,
            not_recommended=not_recommended,
            shop_link_regular=shop_link_regular,
            shop_link_extra_fare=shop_link_extra_fare,
            start_station_id=start_station_id,
            end_station_id=end_station_id,
        )

        ticket_info.additional_properties = d
        return ticket_info

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
