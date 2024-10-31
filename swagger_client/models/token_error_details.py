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


class TokenErrorDetails(object):
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
        'punctuation': 'EditsSummary',
        'capitalization': 'EditsSummary',
        'inverse_text_normalization': 'EditsSummary',
        'lexical': 'EditsSummary',
        'others': 'EditsSummary'
    }

    attribute_map = {
        'punctuation': 'punctuation',
        'capitalization': 'capitalization',
        'inverse_text_normalization': 'inverseTextNormalization',
        'lexical': 'lexical',
        'others': 'others'
    }

    def __init__(self, punctuation=None, capitalization=None, inverse_text_normalization=None, lexical=None, others=None, _configuration=None):  # noqa: E501
        """TokenErrorDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._punctuation = None
        self._capitalization = None
        self._inverse_text_normalization = None
        self._lexical = None
        self._others = None
        self.discriminator = None

        if punctuation is not None:
            self.punctuation = punctuation
        if capitalization is not None:
            self.capitalization = capitalization
        if inverse_text_normalization is not None:
            self.inverse_text_normalization = inverse_text_normalization
        if lexical is not None:
            self.lexical = lexical
        if others is not None:
            self.others = others

    @property
    def punctuation(self):
        """Gets the punctuation of this TokenErrorDetails.  # noqa: E501


        :return: The punctuation of this TokenErrorDetails.  # noqa: E501
        :rtype: EditsSummary
        """
        return self._punctuation

    @punctuation.setter
    def punctuation(self, punctuation):
        """Sets the punctuation of this TokenErrorDetails.


        :param punctuation: The punctuation of this TokenErrorDetails.  # noqa: E501
        :type: EditsSummary
        """

        self._punctuation = punctuation

    @property
    def capitalization(self):
        """Gets the capitalization of this TokenErrorDetails.  # noqa: E501


        :return: The capitalization of this TokenErrorDetails.  # noqa: E501
        :rtype: EditsSummary
        """
        return self._capitalization

    @capitalization.setter
    def capitalization(self, capitalization):
        """Sets the capitalization of this TokenErrorDetails.


        :param capitalization: The capitalization of this TokenErrorDetails.  # noqa: E501
        :type: EditsSummary
        """

        self._capitalization = capitalization

    @property
    def inverse_text_normalization(self):
        """Gets the inverse_text_normalization of this TokenErrorDetails.  # noqa: E501


        :return: The inverse_text_normalization of this TokenErrorDetails.  # noqa: E501
        :rtype: EditsSummary
        """
        return self._inverse_text_normalization

    @inverse_text_normalization.setter
    def inverse_text_normalization(self, inverse_text_normalization):
        """Sets the inverse_text_normalization of this TokenErrorDetails.


        :param inverse_text_normalization: The inverse_text_normalization of this TokenErrorDetails.  # noqa: E501
        :type: EditsSummary
        """

        self._inverse_text_normalization = inverse_text_normalization

    @property
    def lexical(self):
        """Gets the lexical of this TokenErrorDetails.  # noqa: E501


        :return: The lexical of this TokenErrorDetails.  # noqa: E501
        :rtype: EditsSummary
        """
        return self._lexical

    @lexical.setter
    def lexical(self, lexical):
        """Sets the lexical of this TokenErrorDetails.


        :param lexical: The lexical of this TokenErrorDetails.  # noqa: E501
        :type: EditsSummary
        """

        self._lexical = lexical

    @property
    def others(self):
        """Gets the others of this TokenErrorDetails.  # noqa: E501


        :return: The others of this TokenErrorDetails.  # noqa: E501
        :rtype: EditsSummary
        """
        return self._others

    @others.setter
    def others(self, others):
        """Sets the others of this TokenErrorDetails.


        :param others: The others of this TokenErrorDetails.  # noqa: E501
        :type: EditsSummary
        """

        self._others = others

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
        if issubclass(TokenErrorDetails, dict):
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
        if not isinstance(other, TokenErrorDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenErrorDetails):
            return True

        return self.to_dict() != other.to_dict()
