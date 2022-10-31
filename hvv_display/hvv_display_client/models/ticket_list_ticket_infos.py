from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.person_info import PersonInfo
from ..models.ticket_list_ticket_infos_region_type import (
    TicketListTicketInfosRegionType,
)
from ..models.ticket_list_ticket_variant import TicketListTicketVariant
from ..models.validity_period import ValidityPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketListTicketInfos")


@attr.s(auto_attribs=True)
class TicketListTicketInfos:
    """
    Attributes:
        tariff_kind_label (str):
        tariff_level_label (str):
        tariff_kind_id (Union[Unset, int]):
        tariff_level_id (Union[Unset, int]):
        tariff_group_id (Union[Unset, int]):
        tariff_group_label (Union[Unset, str]):
        region_type (Union[Unset, TicketListTicketInfosRegionType]):
        selectable_regions (Union[Unset, int]):
        required_start_station (Union[Unset, bool]):
        person_infos (Union[Unset, List[PersonInfo]]):
        validity_periods (Union[Unset, List[ValidityPeriod]]):
        variants (Union[Unset, List[TicketListTicketVariant]]):
    """

    tariff_kind_label: str
    tariff_level_label: str
    tariff_kind_id: Union[Unset, int] = UNSET
    tariff_level_id: Union[Unset, int] = UNSET
    tariff_group_id: Union[Unset, int] = UNSET
    tariff_group_label: Union[Unset, str] = UNSET
    region_type: Union[Unset, TicketListTicketInfosRegionType] = UNSET
    selectable_regions: Union[Unset, int] = 0
    required_start_station: Union[Unset, bool] = False
    person_infos: Union[Unset, List[PersonInfo]] = UNSET
    validity_periods: Union[Unset, List[ValidityPeriod]] = UNSET
    variants: Union[Unset, List[TicketListTicketVariant]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff_kind_label = self.tariff_kind_label
        tariff_level_label = self.tariff_level_label
        tariff_kind_id = self.tariff_kind_id
        tariff_level_id = self.tariff_level_id
        tariff_group_id = self.tariff_group_id
        tariff_group_label = self.tariff_group_label
        region_type: Union[Unset, str] = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value

        selectable_regions = self.selectable_regions
        required_start_station = self.required_start_station
        person_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.person_infos, Unset):
            person_infos = []
            for person_infos_item_data in self.person_infos:
                person_infos_item = person_infos_item_data.to_dict()

                person_infos.append(person_infos_item)

        validity_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validity_periods, Unset):
            validity_periods = []
            for validity_periods_item_data in self.validity_periods:
                validity_periods_item = validity_periods_item_data.to_dict()

                validity_periods.append(validity_periods_item)

        variants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()

                variants.append(variants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tariffKindLabel": tariff_kind_label,
                "tariffLevelLabel": tariff_level_label,
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
        if region_type is not UNSET:
            field_dict["regionType"] = region_type
        if selectable_regions is not UNSET:
            field_dict["selectableRegions"] = selectable_regions
        if required_start_station is not UNSET:
            field_dict["requiredStartStation"] = required_start_station
        if person_infos is not UNSET:
            field_dict["personInfos"] = person_infos
        if validity_periods is not UNSET:
            field_dict["validityPeriods"] = validity_periods
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tariff_kind_label = d.pop("tariffKindLabel")

        tariff_level_label = d.pop("tariffLevelLabel")

        tariff_kind_id = d.pop("tariffKindID", UNSET)

        tariff_level_id = d.pop("tariffLevelID", UNSET)

        tariff_group_id = d.pop("tariffGroupID", UNSET)

        tariff_group_label = d.pop("tariffGroupLabel", UNSET)

        _region_type = d.pop("regionType", UNSET)
        region_type: Union[Unset, TicketListTicketInfosRegionType]
        if isinstance(_region_type, Unset):
            region_type = UNSET
        else:
            region_type = TicketListTicketInfosRegionType(_region_type)

        selectable_regions = d.pop("selectableRegions", UNSET)

        required_start_station = d.pop("requiredStartStation", UNSET)

        person_infos = []
        _person_infos = d.pop("personInfos", UNSET)
        for person_infos_item_data in _person_infos or []:
            person_infos_item = PersonInfo.from_dict(person_infos_item_data)

            person_infos.append(person_infos_item)

        validity_periods = []
        _validity_periods = d.pop("validityPeriods", UNSET)
        for validity_periods_item_data in _validity_periods or []:
            validity_periods_item = ValidityPeriod.from_dict(validity_periods_item_data)

            validity_periods.append(validity_periods_item)

        variants = []
        _variants = d.pop("variants", UNSET)
        for variants_item_data in _variants or []:
            variants_item = TicketListTicketVariant.from_dict(variants_item_data)

            variants.append(variants_item)

        ticket_list_ticket_infos = cls(
            tariff_kind_label=tariff_kind_label,
            tariff_level_label=tariff_level_label,
            tariff_kind_id=tariff_kind_id,
            tariff_level_id=tariff_level_id,
            tariff_group_id=tariff_group_id,
            tariff_group_label=tariff_group_label,
            region_type=region_type,
            selectable_regions=selectable_regions,
            required_start_station=required_start_station,
            person_infos=person_infos,
            validity_periods=validity_periods,
            variants=variants,
        )

        ticket_list_ticket_infos.additional_properties = d
        return ticket_list_ticket_infos

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
