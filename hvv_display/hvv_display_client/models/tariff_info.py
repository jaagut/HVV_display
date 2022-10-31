from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tariff_info_extra_fare_type import TariffInfoExtraFareType
from ..models.tariff_region_info import TariffRegionInfo
from ..models.ticket_info import TicketInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffInfo")


@attr.s(auto_attribs=True)
class TariffInfo:
    """
    Attributes:
        tariff_name (str):
        tariff_regions (Union[Unset, List[TariffRegionInfo]]):
        region_texts (Union[Unset, List[str]]):
        extra_fare_type (Union[Unset, TariffInfoExtraFareType]):  Default: TariffInfoExtraFareType.NO.
        ticket_infos (Union[Unset, List[TicketInfo]]):
        ticket_remarks (Union[Unset, str]):
    """

    tariff_name: str
    tariff_regions: Union[Unset, List[TariffRegionInfo]] = UNSET
    region_texts: Union[Unset, List[str]] = UNSET
    extra_fare_type: Union[Unset, TariffInfoExtraFareType] = TariffInfoExtraFareType.NO
    ticket_infos: Union[Unset, List[TicketInfo]] = UNSET
    ticket_remarks: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff_name = self.tariff_name
        tariff_regions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_regions, Unset):
            tariff_regions = []
            for tariff_regions_item_data in self.tariff_regions:
                tariff_regions_item = tariff_regions_item_data.to_dict()

                tariff_regions.append(tariff_regions_item)

        region_texts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.region_texts, Unset):
            region_texts = self.region_texts

        extra_fare_type: Union[Unset, str] = UNSET
        if not isinstance(self.extra_fare_type, Unset):
            extra_fare_type = self.extra_fare_type.value

        ticket_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ticket_infos, Unset):
            ticket_infos = []
            for ticket_infos_item_data in self.ticket_infos:
                ticket_infos_item = ticket_infos_item_data.to_dict()

                ticket_infos.append(ticket_infos_item)

        ticket_remarks = self.ticket_remarks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tariffName": tariff_name,
            }
        )
        if tariff_regions is not UNSET:
            field_dict["tariffRegions"] = tariff_regions
        if region_texts is not UNSET:
            field_dict["regionTexts"] = region_texts
        if extra_fare_type is not UNSET:
            field_dict["extraFareType"] = extra_fare_type
        if ticket_infos is not UNSET:
            field_dict["ticketInfos"] = ticket_infos
        if ticket_remarks is not UNSET:
            field_dict["ticketRemarks"] = ticket_remarks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tariff_name = d.pop("tariffName")

        tariff_regions = []
        _tariff_regions = d.pop("tariffRegions", UNSET)
        for tariff_regions_item_data in _tariff_regions or []:
            tariff_regions_item = TariffRegionInfo.from_dict(tariff_regions_item_data)

            tariff_regions.append(tariff_regions_item)

        region_texts = cast(List[str], d.pop("regionTexts", UNSET))

        _extra_fare_type = d.pop("extraFareType", UNSET)
        extra_fare_type: Union[Unset, TariffInfoExtraFareType]
        if isinstance(_extra_fare_type, Unset):
            extra_fare_type = UNSET
        else:
            extra_fare_type = TariffInfoExtraFareType(_extra_fare_type)

        ticket_infos = []
        _ticket_infos = d.pop("ticketInfos", UNSET)
        for ticket_infos_item_data in _ticket_infos or []:
            ticket_infos_item = TicketInfo.from_dict(ticket_infos_item_data)

            ticket_infos.append(ticket_infos_item)

        ticket_remarks = d.pop("ticketRemarks", UNSET)

        tariff_info = cls(
            tariff_name=tariff_name,
            tariff_regions=tariff_regions,
            region_texts=region_texts,
            extra_fare_type=extra_fare_type,
            ticket_infos=ticket_infos,
            ticket_remarks=ticket_remarks,
        )

        tariff_info.additional_properties = d
        return tariff_info

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
