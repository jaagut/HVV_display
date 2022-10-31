from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cn_response_return_code import CNResponseReturnCode
from ..models.regional_sd_name import RegionalSDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="CNResponse")


@attr.s(auto_attribs=True)
class CNResponse:
    """
    Attributes:
        return_code (CNResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        results (Union[Unset, List[RegionalSDName]]):
    """

    return_code: CNResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    results: Union[Unset, List[RegionalSDName]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = CNResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = RegionalSDName.from_dict(results_item_data)

            results.append(results_item)

        cn_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            results=results,
        )

        cn_response.additional_properties = d
        return cn_response

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
