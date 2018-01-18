# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PolicyRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'api_groups': 'list[str]',
        'attribute_restrictions': 'RuntimeRawExtension',
        'non_resource_ur_ls': 'list[str]',
        'resource_names': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'attribute_restrictions': 'attributeRestrictions',
        'non_resource_ur_ls': 'nonResourceURLs',
        'resource_names': 'resourceNames',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, attribute_restrictions=None, non_resource_ur_ls=None, resource_names=None, resources=None, verbs=None):
        """
        V1PolicyRule - a model defined in Swagger
        """

        self._api_groups = None
        self._attribute_restrictions = None
        self._non_resource_ur_ls = None
        self._resource_names = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        self.api_groups = api_groups
        if attribute_restrictions is not None:
          self.attribute_restrictions = attribute_restrictions
        if non_resource_ur_ls is not None:
          self.non_resource_ur_ls = non_resource_ur_ls
        if resource_names is not None:
          self.resource_names = resource_names
        self.resources = resources
        self.verbs = verbs

    @property
    def api_groups(self):
        """
        Gets the api_groups of this V1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed

        :return: The api_groups of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """
        Sets the api_groups of this V1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed

        :param api_groups: The api_groups of this V1PolicyRule.
        :type: list[str]
        """
        if api_groups is None:
            raise ValueError("Invalid value for `api_groups`, must not be `None`")

        self._api_groups = api_groups

    @property
    def attribute_restrictions(self):
        """
        Gets the attribute_restrictions of this V1PolicyRule.
        AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.

        :return: The attribute_restrictions of this V1PolicyRule.
        :rtype: RuntimeRawExtension
        """
        return self._attribute_restrictions

    @attribute_restrictions.setter
    def attribute_restrictions(self, attribute_restrictions):
        """
        Sets the attribute_restrictions of this V1PolicyRule.
        AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.

        :param attribute_restrictions: The attribute_restrictions of this V1PolicyRule.
        :type: RuntimeRawExtension
        """

        self._attribute_restrictions = attribute_restrictions

    @property
    def non_resource_ur_ls(self):
        """
        Gets the non_resource_ur_ls of this V1PolicyRule.
        NonResourceURLsSlice is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.

        :return: The non_resource_ur_ls of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._non_resource_ur_ls

    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls):
        """
        Sets the non_resource_ur_ls of this V1PolicyRule.
        NonResourceURLsSlice is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.

        :param non_resource_ur_ls: The non_resource_ur_ls of this V1PolicyRule.
        :type: list[str]
        """

        self._non_resource_ur_ls = non_resource_ur_ls

    @property
    def resource_names(self):
        """
        Gets the resource_names of this V1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :return: The resource_names of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """
        Sets the resource_names of this V1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :param resource_names: The resource_names of this V1PolicyRule.
        :type: list[str]
        """

        self._resource_names = resource_names

    @property
    def resources(self):
        """
        Gets the resources of this V1PolicyRule.
        Resources is a list of resources this rule applies to.  ResourceAll represents all resources.

        :return: The resources of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1PolicyRule.
        Resources is a list of resources this rule applies to.  ResourceAll represents all resources.

        :param resources: The resources of this V1PolicyRule.
        :type: list[str]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources

    @property
    def verbs(self):
        """
        Gets the verbs of this V1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :return: The verbs of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :param verbs: The verbs of this V1PolicyRule.
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")

        self._verbs = verbs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other