from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.line_list_entry import LineListEntry
from ..models.ll_response_return_code import LLResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LLResponse")


@attr.s(auto_attribs=True)
class LLResponse:
    """
    Attributes:
        return_code (LLResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        data_release_id (Union[Unset, str]):
        lines (Union[Unset, List[LineListEntry]]):
    """

    return_code: LLResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    data_release_id: Union[Unset, str] = UNSET
    lines: Union[Unset, List[LineListEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        data_release_id = self.data_release_id
        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()

                lines.append(lines_item)

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
        if data_release_id is not UNSET:
            field_dict["dataReleaseID"] = data_release_id
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = LLResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        data_release_id = d.pop("dataReleaseID", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = LineListEntry.from_dict(lines_item_data)

            lines.append(lines_item)

        ll_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            data_release_id=data_release_id,
            lines=lines,
        )

        ll_response.additional_properties = d
        return ll_response

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
