from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tariff_info import TariffInfo
from ..models.tariff_response_return_code import TariffResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffResponse")


@attr.s(auto_attribs=True)
class TariffResponse:
    """
    Attributes:
        return_code (TariffResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        tariff_infos (Union[Unset, List[TariffInfo]]):
    """

    return_code: TariffResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    tariff_infos: Union[Unset, List[TariffInfo]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        tariff_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tariff_infos, Unset):
            tariff_infos = []
            for tariff_infos_item_data in self.tariff_infos:
                tariff_infos_item = tariff_infos_item_data.to_dict()

                tariff_infos.append(tariff_infos_item)

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
        if tariff_infos is not UNSET:
            field_dict["tariffInfos"] = tariff_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = TariffResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        tariff_infos = []
        _tariff_infos = d.pop("tariffInfos", UNSET)
        for tariff_infos_item_data in _tariff_infos or []:
            tariff_infos_item = TariffInfo.from_dict(tariff_infos_item_data)

            tariff_infos.append(tariff_infos_item)

        tariff_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            tariff_infos=tariff_infos,
        )

        tariff_response.additional_properties = d
        return tariff_response

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
