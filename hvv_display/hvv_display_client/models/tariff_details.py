from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffDetails")


@attr.s(auto_attribs=True)
class TariffDetails:
    """
    Attributes:
        inner_city (Union[Unset, bool]):
        city (Union[Unset, bool]):
        city_traffic (Union[Unset, bool]):
        gratis (Union[Unset, bool]):
        greater_area (Union[Unset, bool]):
        sh_village_id (Union[Unset, int]):
        sh_tariff_zone (Union[Unset, int]):
        tariff_zones (Union[Unset, List[int]]):
        regions (Union[Unset, List[int]]):
        counties (Union[Unset, List[str]]):
        rings (Union[Unset, List[str]]):
        fare_stage (Union[Unset, bool]):
        fare_stage_number (Union[Unset, int]):
        tariff_names (Union[Unset, List[str]]):
        unique_values (Union[Unset, bool]):
    """

    inner_city: Union[Unset, bool] = UNSET
    city: Union[Unset, bool] = UNSET
    city_traffic: Union[Unset, bool] = UNSET
    gratis: Union[Unset, bool] = UNSET
    greater_area: Union[Unset, bool] = UNSET
    sh_village_id: Union[Unset, int] = UNSET
    sh_tariff_zone: Union[Unset, int] = UNSET
    tariff_zones: Union[Unset, List[int]] = UNSET
    regions: Union[Unset, List[int]] = UNSET
    counties: Union[Unset, List[str]] = UNSET
    rings: Union[Unset, List[str]] = UNSET
    fare_stage: Union[Unset, bool] = UNSET
    fare_stage_number: Union[Unset, int] = UNSET
    tariff_names: Union[Unset, List[str]] = UNSET
    unique_values: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inner_city = self.inner_city
        city = self.city
        city_traffic = self.city_traffic
        gratis = self.gratis
        greater_area = self.greater_area
        sh_village_id = self.sh_village_id
        sh_tariff_zone = self.sh_tariff_zone
        tariff_zones: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tariff_zones, Unset):
            tariff_zones = self.tariff_zones

        regions: Union[Unset, List[int]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        counties: Union[Unset, List[str]] = UNSET
        if not isinstance(self.counties, Unset):
            counties = self.counties

        rings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rings, Unset):
            rings = self.rings

        fare_stage = self.fare_stage
        fare_stage_number = self.fare_stage_number
        tariff_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tariff_names, Unset):
            tariff_names = self.tariff_names

        unique_values = self.unique_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inner_city is not UNSET:
            field_dict["innerCity"] = inner_city
        if city is not UNSET:
            field_dict["city"] = city
        if city_traffic is not UNSET:
            field_dict["cityTraffic"] = city_traffic
        if gratis is not UNSET:
            field_dict["gratis"] = gratis
        if greater_area is not UNSET:
            field_dict["greaterArea"] = greater_area
        if sh_village_id is not UNSET:
            field_dict["shVillageId"] = sh_village_id
        if sh_tariff_zone is not UNSET:
            field_dict["shTariffZone"] = sh_tariff_zone
        if tariff_zones is not UNSET:
            field_dict["tariffZones"] = tariff_zones
        if regions is not UNSET:
            field_dict["regions"] = regions
        if counties is not UNSET:
            field_dict["counties"] = counties
        if rings is not UNSET:
            field_dict["rings"] = rings
        if fare_stage is not UNSET:
            field_dict["fareStage"] = fare_stage
        if fare_stage_number is not UNSET:
            field_dict["fareStageNumber"] = fare_stage_number
        if tariff_names is not UNSET:
            field_dict["tariffNames"] = tariff_names
        if unique_values is not UNSET:
            field_dict["uniqueValues"] = unique_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inner_city = d.pop("innerCity", UNSET)

        city = d.pop("city", UNSET)

        city_traffic = d.pop("cityTraffic", UNSET)

        gratis = d.pop("gratis", UNSET)

        greater_area = d.pop("greaterArea", UNSET)

        sh_village_id = d.pop("shVillageId", UNSET)

        sh_tariff_zone = d.pop("shTariffZone", UNSET)

        tariff_zones = cast(List[int], d.pop("tariffZones", UNSET))

        regions = cast(List[int], d.pop("regions", UNSET))

        counties = cast(List[str], d.pop("counties", UNSET))

        rings = cast(List[str], d.pop("rings", UNSET))

        fare_stage = d.pop("fareStage", UNSET)

        fare_stage_number = d.pop("fareStageNumber", UNSET)

        tariff_names = cast(List[str], d.pop("tariffNames", UNSET))

        unique_values = d.pop("uniqueValues", UNSET)

        tariff_details = cls(
            inner_city=inner_city,
            city=city,
            city_traffic=city_traffic,
            gratis=gratis,
            greater_area=greater_area,
            sh_village_id=sh_village_id,
            sh_tariff_zone=sh_tariff_zone,
            tariff_zones=tariff_zones,
            regions=regions,
            counties=counties,
            rings=rings,
            fare_stage=fare_stage,
            fare_stage_number=fare_stage_number,
            tariff_names=tariff_names,
            unique_values=unique_values,
        )

        tariff_details.additional_properties = d
        return tariff_details

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
