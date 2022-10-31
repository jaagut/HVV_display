from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attribute import Attribute
from ..models.course_element import CourseElement
from ..models.dc_response_return_code import DCResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DCResponse")


@attr.s(auto_attribs=True)
class DCResponse:
    """
    Attributes:
        return_code (DCResponseReturnCode):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        course_elements (Union[Unset, List[CourseElement]]):
        extra (Union[Unset, bool]):
        cancelled (Union[Unset, bool]):
        attributes (Union[Unset, List[Attribute]]):
    """

    return_code: DCResponseReturnCode
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    course_elements: Union[Unset, List[CourseElement]] = UNSET
    extra: Union[Unset, bool] = False
    cancelled: Union[Unset, bool] = False
    attributes: Union[Unset, List[Attribute]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        course_elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.course_elements, Unset):
            course_elements = []
            for course_elements_item_data in self.course_elements:
                course_elements_item = course_elements_item_data.to_dict()

                course_elements.append(course_elements_item)

        extra = self.extra
        cancelled = self.cancelled
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

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
        if course_elements is not UNSET:
            field_dict["courseElements"] = course_elements
        if extra is not UNSET:
            field_dict["extra"] = extra
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = DCResponseReturnCode(d.pop("returnCode"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        course_elements = []
        _course_elements = d.pop("courseElements", UNSET)
        for course_elements_item_data in _course_elements or []:
            course_elements_item = CourseElement.from_dict(course_elements_item_data)

            course_elements.append(course_elements_item)

        extra = d.pop("extra", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        dc_response = cls(
            return_code=return_code,
            error_text=error_text,
            error_dev_info=error_dev_info,
            course_elements=course_elements,
            extra=extra,
            cancelled=cancelled,
            attributes=attributes,
        )

        dc_response.additional_properties = d
        return dc_response

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
