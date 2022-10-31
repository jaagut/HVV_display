from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pc_response_return_code import PCResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PCResponse")


@attr.s(auto_attribs=True)
class PCResponse:
    """
    Attributes:
        return_code (PCResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        is_hvv (Union[Unset, bool]):
    """

    return_code: PCResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    is_hvv: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        is_hvv = self.is_hvv

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
        if is_hvv is not UNSET:
            field_dict["isHVV"] = is_hvv

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = PCResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        is_hvv = d.pop("isHVV", UNSET)

        pc_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            is_hvv=is_hvv,
        )

        pc_response.additional_properties = d
        return pc_response

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
