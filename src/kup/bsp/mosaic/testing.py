# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import kup.bsp.mosaic


class KupBspMosaicLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=kup.bsp.mosaic)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'kup.bsp.mosaic:default')


KUP_BSP_MOSAIC_FIXTURE = KupBspMosaicLayer()


KUP_BSP_MOSAIC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KUP_BSP_MOSAIC_FIXTURE,),
    name='KupBspMosaicLayer:IntegrationTesting'
)


KUP_BSP_MOSAIC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KUP_BSP_MOSAIC_FIXTURE,),
    name='KupBspMosaicLayer:FunctionalTesting'
)


KUP_BSP_MOSAIC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KUP_BSP_MOSAIC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='KupBspMosaicLayer:AcceptanceTesting'
)
