# coding: utf-8

"""
    Speech Services API version 3.2

    Speech Services API version 3.2.  # noqa: E501

    OpenAPI spec version: 3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ResponseBlock(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, name=None, size=None, _configuration=None):  # noqa: E501
        """ResponseBlock - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this ResponseBlock.  # noqa: E501

        The name of the block.  # noqa: E501

        :return: The name of this ResponseBlock.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseBlock.

        The name of the block.  # noqa: E501

        :param name: The name of this ResponseBlock.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ResponseBlock.  # noqa: E501

        The size of the block.  # noqa: E501

        :return: The size of this ResponseBlock.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResponseBlock.

        The size of the block.  # noqa: E501

        :param size: The size of this ResponseBlock.  # noqa: E501
        :type: int
        """

        self._size = size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResponseBlock, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseBlock):
            return True

        return self.to_dict() != other.to_dict()
