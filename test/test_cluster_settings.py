# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import argocd_client
from argocd_client.models.cluster_settings import ClusterSettings  # noqa: E501
from argocd_client.rest import ApiException

class TestClusterSettings(unittest.TestCase):
    """ClusterSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClusterSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.cluster_settings.ClusterSettings()  # noqa: E501
        if include_optional :
            return ClusterSettings(
                app_label_key = '0', 
                config_management_plugins = [
                    argocd_client.models.config_management_plugin_contains_config_management_plugin_configuration.ConfigManagementPlugin contains config management plugin configuration(
                        generate = argocd_client.models.command_holds_binary_path_and_arguments_list.Command holds binary path and arguments list(
                            args = [
                                '0'
                                ], 
                            command = [
                                '0'
                                ], ), 
                        init = argocd_client.models.command_holds_binary_path_and_arguments_list.Command holds binary path and arguments list(), 
                        name = '0', )
                    ], 
                dex_config = argocd_client.models.cluster_dex_config.clusterDexConfig(
                    connectors = [
                        argocd_client.models.cluster_connector.clusterConnector(
                            name = '0', 
                            type = '0', )
                        ], ), 
                google_analytics = argocd_client.models.cluster_google_analytics_config.clusterGoogleAnalyticsConfig(
                    anonymize_users = True, 
                    tracking_id = '0', ), 
                help = argocd_client.models.help_settings.Help settings(
                    chat_text = '0', 
                    chat_url = '0', ), 
                kustomize_options = argocd_client.models.kustomize_options_are_options_for_kustomize_to_use_when_building_manifests.KustomizeOptions are options for kustomize to use when building manifests(
                    binary_path = '0', 
                    build_options = '0', ), 
                kustomize_versions = [
                    '0'
                    ], 
                oidc_config = argocd_client.models.cluster_oidc_config.clusterOIDCConfig(
                    cli_client_id = '0', 
                    client_id = '0', 
                    id_token_claims = {
                        'key' : argocd_client.models.oidc_claim.oidcClaim(
                            essential = True, 
                            value = '0', 
                            values = [
                                '0'
                                ], )
                        }, 
                    issuer = '0', 
                    name = '0', 
                    scopes = [
                        '0'
                        ], ), 
                plugins = [
                    argocd_client.models.plugin_settings.Plugin settings(
                        name = '0', )
                    ], 
                resource_overrides = {
                    'key' : argocd_client.models.resource_override_holds_configuration_to_customize_resource_diffing_and_health_assessment.ResourceOverride holds configuration to customize resource diffing and health assessment(
                        actions = '0', 
                        health_lua = '0', 
                        ignore_differences = argocd_client.models.v1alpha1_override_ignore_diff.v1alpha1OverrideIgnoreDiff(
                            j_son_pointers = [
                                '0'
                                ], ), 
                        known_type_fields = [
                            argocd_client.models.known_type_field_contains_mapping_between_crd_field_and_known_kubernetes_type.KnownTypeField contains mapping between CRD field and known Kubernetes type(
                                field = '0', 
                                type = '0', )
                            ], )
                    }, 
                status_badge_enabled = True, 
                ui_css_url = '0', 
                url = '0', 
                user_logins_disabled = True
            )
        else :
            return ClusterSettings(
        )

    def testClusterSettings(self):
        """Test ClusterSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()