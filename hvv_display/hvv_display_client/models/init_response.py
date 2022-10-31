from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.init_response_return_code import InitResponseReturnCode
from ..models.property_ import Property
from ..types import UNSET, Unset

T = TypeVar("T", bound="InitResponse")


@attr.s(auto_attribs=True)
class InitResponse:
    """
    Attributes:
        return_code (InitResponseReturnCode):
        begin_of_service (str):
        end_of_service (str):
        id (str):
        data_id (str):
        build_date (str):
        build_time (str):
        build_text (str):
        version (str):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        properties (Union[Unset, List[Property]]):
    """

    return_code: InitResponseReturnCode
    begin_of_service: str
    end_of_service: str
    id: str
    data_id: str
    build_date: str
    build_time: str
    build_text: str
    version: str
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    properties: Union[Unset, List[Property]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        begin_of_service = self.begin_of_service
        end_of_service = self.end_of_service
        id = self.id
        data_id = self.data_id
        build_date = self.build_date
        build_time = self.build_time
        build_text = self.build_text
        version = self.version
        error_text = self.error_text
        error_dev_info = self.error_dev_info
        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "beginOfService": begin_of_service,
                "endOfService": end_of_service,
                "id": id,
                "dataId": data_id,
                "buildDate": build_date,
                "buildTime": build_time,
                "buildText": build_text,
                "version": version,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = InitResponseReturnCode(d.pop("returnCode"))

        begin_of_service = d.pop("beginOfService")

        end_of_service = d.pop("endOfService")

        id = d.pop("id")

        data_id = d.pop("dataId")

        build_date = d.pop("buildDate")

        build_time = d.pop("buildTime")

        build_text = d.pop("buildText")

        version = d.pop("version")

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Property.from_dict(properties_item_data)

            properties.append(properties_item)

        init_response = cls(
            return_code=return_code,
            begin_of_service=begin_of_service,
            end_of_service=end_of_service,
            id=id,
            data_id=data_id,
            build_date=build_date,
            build_time=build_time,
            build_text=build_text,
            version=version,
            error_text=error_text,
            error_dev_info=error_dev_info,
            properties=properties,
        )

        init_response.additional_properties = d
        return init_response

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
