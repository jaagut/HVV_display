from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gti_time import GTITime
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContSearchByServiceId")


@attr.s(auto_attribs=True)
class ContSearchByServiceId:
    """
    Attributes:
        line_key (str):
        planned_dep_arr_time (GTITime):
        service_id (Union[Unset, int]):
        additional_offset (Union[Unset, int]):
    """

    line_key: str
    planned_dep_arr_time: GTITime
    service_id: Union[Unset, int] = UNSET
    additional_offset: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_key = self.line_key
        planned_dep_arr_time = self.planned_dep_arr_time.to_dict()

        service_id = self.service_id
        additional_offset = self.additional_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineKey": line_key,
                "plannedDepArrTime": planned_dep_arr_time,
            }
        )
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if additional_offset is not UNSET:
            field_dict["additionalOffset"] = additional_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_key = d.pop("lineKey")

        planned_dep_arr_time = GTITime.from_dict(d.pop("plannedDepArrTime"))

        service_id = d.pop("serviceId", UNSET)

        additional_offset = d.pop("additionalOffset", UNSET)

        cont_search_by_service_id = cls(
            line_key=line_key,
            planned_dep_arr_time=planned_dep_arr_time,
            service_id=service_id,
            additional_offset=additional_offset,
        )

        cont_search_by_service_id.additional_properties = d
        return cont_search_by_service_id

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
