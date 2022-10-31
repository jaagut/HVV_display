from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.time_period import TimePeriod
from ..models.validity_period_day import ValidityPeriodDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidityPeriod")


@attr.s(auto_attribs=True)
class ValidityPeriod:
    """
    Attributes:
        day (ValidityPeriodDay):
        time_validities (Union[Unset, List[TimePeriod]]):
    """

    day: ValidityPeriodDay
    time_validities: Union[Unset, List[TimePeriod]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day.value

        time_validities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_validities, Unset):
            time_validities = []
            for time_validities_item_data in self.time_validities:
                time_validities_item = time_validities_item_data.to_dict()

                time_validities.append(time_validities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
            }
        )
        if time_validities is not UNSET:
            field_dict["timeValidities"] = time_validities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = ValidityPeriodDay(d.pop("day"))

        time_validities = []
        _time_validities = d.pop("timeValidities", UNSET)
        for time_validities_item_data in _time_validities or []:
            time_validities_item = TimePeriod.from_dict(time_validities_item_data)

            time_validities.append(time_validities_item)

        validity_period = cls(
            day=day,
            time_validities=time_validities,
        )

        validity_period.additional_properties = d
        return validity_period

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
