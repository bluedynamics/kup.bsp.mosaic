# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from kup.bsp.mosaic.testing import KUP_BSP_MOSAIC_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that kup.bsp.mosaic is properly installed."""

    layer = KUP_BSP_MOSAIC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kup.bsp.mosaic is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kup.bsp.mosaic'))

    def test_browserlayer(self):
        """Test that IKupBspMosaicLayer is registered."""
        from kup.bsp.mosaic.interfaces import (
            IKupBspMosaicLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IKupBspMosaicLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KUP_BSP_MOSAIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['kup.bsp.mosaic'])

    def test_product_uninstalled(self):
        """Test if kup.bsp.mosaic is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kup.bsp.mosaic'))

    def test_browserlayer_removed(self):
        """Test that IKupBspMosaicLayer is removed."""
        from kup.bsp.mosaic.interfaces import \
            IKupBspMosaicLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IKupBspMosaicLayer,
           utils.registered_layers())
