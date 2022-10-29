DROP TABLE IF EXISTS events;

CREATE TABLE events
(
   eventId               BIGINT NOT NULL,
   event                 TEXT,
   serverUtcTimestampMs  BIGINT,
   utcTimestampMs        BIGINT,
   PRIMARY KEY(eventId)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties`;

CREATE TABLE `events.properties`
(
   eventId                          BIGINT NOT NULL,
   accessMethod                     DOUBLE,
   accessType                       DOUBLE,
   accountType                      DOUBLE,
   apiVersion                       TEXT,
   appRelease                       TEXT,
   appVersion                       TEXT,
   cartEstimatedTotal               DOUBLE,
   cartId                           TEXT,
   cartType                         DOUBLE,
   cartVariantSubtotalValue         DOUBLE,
   cartVariantsSubtotalValue        DOUBLE,
   categoryId                       TEXT,
   changeType                       DOUBLE,
   columnModulePosition             DOUBLE,
   columnPosition                   DOUBLE,
   correlationId                    TEXT,
   currentCartSharedId              DOUBLE,
   customType                       TEXT,
   customerItemPickingNotes         DOUBLE,
   deviceId                         TEXT,
   email                            TEXT,
   esNumResults                     DOUBLE,
   esTime                           DOUBLE,
   existingUser                     BIT,
   featureType                      DOUBLE,
   footerIntent                     DOUBLE,
   hasCookiedEmail                  BIT,
   hasExpressItem                   BIT,
   hasFreebieItem                   BIT,
   hasPurchasedBefore               TEXT,
   hasSampleItem                    BIT,
   hasStandardItem                  BIT,
   headerIntent                     DOUBLE,
   headerPlacement                  DOUBLE,
   inStock                          BIT,
   increment                        BIT,
   intentRelatedId                  TEXT,
   intentType                       DOUBLE,
   ip                               TEXT,
   ipAddress                        TEXT,
   isBrochureGate                   BIT,
   isFirstOrder                     BIT,
   isFreeShippingNoLimit            BIT,
   isFreeShippingPerkUser           BIT,
   isLoggedIn                       BIT,
   isReprocessed                    BIT,
   libVersion                       TEXT,
   manufacturer                     TEXT,
   membershipStatus                 DOUBLE,
   moduleName                       TEXT,
   modulePosition                   DOUBLE,
   moduleTotal                      DOUBLE,
   moduleType                       DOUBLE,
   name                             TEXT,
   newMembershipStatus              DOUBLE,
   newTotalQuantity                 DOUBLE,
   numResults                       DOUBLE,
   numUniqueVariants                DOUBLE,
   numVariants                      DOUBLE,
   obgibDeliveryDate                DOUBLE,
   obgibState                       DOUBLE,
   oldMembershipStatus              DOUBLE,
   optIn                            BIT,
   originalDeviceId                 TEXT,
   os                               TEXT,
   osVersion                        TEXT,
   page                             TEXT,
   pdpIntent                        DOUBLE,
   platform                         TEXT,
   pleIntent                        DOUBLE,
   plePosition                      DOUBLE,
   pleTotal                         DOUBLE,
   postalCode                       TEXT,
   price                            DOUBLE,
   qty                              DOUBLE,
   qualifiesForFreeExpressDelivery  BIT,
   qualifiesForFreeShipping         BIT,
   quantity                         DOUBLE,
   query                            TEXT,
   referrerUrl                      TEXT,
   remoteAddress                    TEXT,
   rowPosition                      DOUBLE,
   rowsTotal                        DOUBLE,
   sessionId                        TEXT,
   setWillAutoRenewOff              BIT,
   shouldAutoRenew                  BIT,
   smartbrand                       DOUBLE,
   sortMethod                       TEXT,
   sourceId                         TEXT,
   sourceScreenName                 TEXT,
   sourceSubArea                    DOUBLE,
   sourceType                       DOUBLE,
   text                             TEXT,
   triggeredByUser                  BIT,
   type                             TEXT,
   userAgent                        TEXT,
   userId                           TEXT,
   utm_ad_id                        DOUBLE,
   utm_campaign                     DOUBLE,
   utm_content                      DOUBLE,
   utm_experiment                   DOUBLE,
   utm_medium                       DOUBLE,
   utm_purpose                      DOUBLE,
   utm_source                       DOUBLE,
   utm_target                       DOUBLE,
   utm_term                         DOUBLE,
   v                                TEXT,
   variantGids                      TEXT,
   variantId                        TEXT,
   vitalType                        DOUBLE,
   vitalTypeDisplay                 TEXT,
   vitalValue                       DOUBLE,
   warehouseId                      TEXT,
   webSlugConfigId                  TEXT,
   
   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT

)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.address`;

CREATE TABLE `events.properties.address`
(
   eventId                    BIGINT NOT NULL,
   `__v`                      DOUBLE,
   `_id`                      TEXT,
   accountScope               DOUBLE,
   addressLine1               TEXT,
   addressLine2               TEXT,
   city                       TEXT,
   country                    TEXT,
   createdAt                  TEXT,
   firstName                  TEXT,
   ignoreAddressVerification  BIT,
   isCommercialAddress        BIT,
   lastName                   TEXT,
   latitude                   DOUBLE,
   longitude                  DOUBLE,
   maximumShipmentWeight      DOUBLE,
   postalCode                 TEXT,
   shippingLabelProfile       DOUBLE,
   state                      TEXT,
   updatedAt                  TEXT,
   `user`                     TEXT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT

)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.address.telephoneVerification`;

CREATE TABLE `events.properties.address.telephoneVerification`
(
   eventId   BIGINT NOT NULL,
   verified  BIT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.bsProperties`;

CREATE TABLE `events.properties.bsProperties`
(
   eventId              BIGINT NOT NULL,
   expressWarehouseId   TEXT,
   postalCode           TEXT,
   standardWarehouseId  TEXT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.performance`;

CREATE TABLE `events.properties.performance`
(
   eventId   BIGINT NOT NULL,
   domReady  DOUBLE,
   ttfb      DOUBLE,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.report`;

CREATE TABLE `events.properties.report`
(
   eventId         BIGINT NOT NULL,
   holdout         BIT,
   priceOptimized  BIT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.smartbrand`;

CREATE TABLE `events.properties.smartbrand`
(
   eventId       BIGINT NOT NULL,
   adCostMicro   DOUBLE,
   adCpcMicro    DOUBLE,
   adGid         DOUBLE,
   adGroupGid    DOUBLE,
   adGroupId     TEXT,
   adId          TEXT,
   campaignGid   DOUBLE,
   campaignId    TEXT,
   keywordBidId  TEXT,
   placement     TEXT,
   variantGid    DOUBLE,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.thestralFeatures`;

CREATE TABLE `events.properties.thestralFeatures`
(
   eventId                                   BIGINT NOT NULL,
   `Holden test`                             TEXT,
   UPMobileCart                              TEXT,
   affinityItems                             TEXT,
   amexCheckout                              TEXT,
   apruveOauthEnabled                        TEXT,
   attachCouponIdToCartVariants              TEXT,
   augmentedReality                          TEXT,
   autoSaveCategoryFilter                    TEXT,
   autoSaveSubscriptionsGallery              TEXT,
   automationTestThestral14                  TEXT,
   backendPurchaseEventEnabled               TEXT,
   boxTops                                   TEXT,
   boxedPlus                                 TEXT,
   boxedUpCashRewards                        TEXT,
   boxedUpMaxCartQuantity                    TEXT,
   brandFilter                               TEXT,
   businessAccountPermissions                TEXT,
   cacheBsTracking                           TEXT,
   cartResolverPlacement                     TEXT,
   cashRewardsMessage                        TEXT,
   categoryLite                              TEXT,
   checkoutV2                                TEXT,
   colourChange                              TEXT,
   dallas                                    TEXT,
   dataDome                                  TEXT,
   debounceCartRefresh                       TEXT,
   deliveryDelay                             TEXT,
   disableGeolocation                        TEXT,
   disableMobileAppleSignIn                  TEXT,
   disableRegistrationEmails                 TEXT,
   donationEnabled                           TEXT,
   dynamicFulfillment                        TEXT,
   dynamicFulfillmentPricing                 TEXT,
   dynamicInventory                          TEXT,
   dynamicInventoryTEST                      TEXT,
   emailRollout                              TEXT,
   emptycartad                               TEXT,
   enableAutoSavePdpAtc                      TEXT,
   enableAutoSavePleEntry                    TEXT,
   enableAutoSaveShipNow                     TEXT,
   enableBoxedSubscriptions                  TEXT,
   enableBoxedUpSku                          TEXT,
   enableCartBuilder                         TEXT,
   enableCartV3                              TEXT,
   enableCategoryPageGate                    TEXT,
   enableCheckoutActionsV2                   TEXT,
   enableCheckoutTotalAlert                  TEXT,
   enableCheckoutV2                          TEXT,
   enableCoinbase                            TEXT,
   enableCoupons                             TEXT,
   enableDirectPLM                           TEXT,
   enableExitIntent                          TEXT,
   enableExitNewUser                         TEXT,
   enableExitSurvey                          TEXT,
   enableHalloweenNav                        TEXT,
   enableHolidayNav21                        TEXT,
   enableHomePageGate                        TEXT,
   enableHomepageImageSoftGate               TEXT,
   enableLeaveCheckoutSearch                 TEXT,
   enableLoyaltyFeatures                     TEXT,
   enablePLEV2                               TEXT,
   enablePersonalizedModule                  TEXT,
   enablePostAddToCart                       TEXT,
   enableProductListV2                       TEXT,
   enableProductPageGate                     TEXT,
   enableSampleUpsell                        TEXT,
   enableSeasonalLogo                        TEXT,
   enableShippingFeesTest                    TEXT,
   enableStateShoppingBan                    TEXT,
   enableSurchargeSiteMessage                TEXT,
   enableWebPendingPoints                    TEXT,
   excludeRedeemedCouponsFromClientResponse  TEXT,
   extensions                                TEXT,
   fastlyExpressWarehouseForState            TEXT,
   fastlyFindAllOrders                       TEXT,
   fastlyFindAllProductListEntities          TEXT,
   fastlyFindAllWarehouse                    TEXT,
   fastlyFindByClientType                    TEXT,
   fastlyNextDayDelivery                     TEXT,
   fastlyVariantsGetExpirationDate           TEXT,
   featuredTab                               TEXT,
   ftueVid                                   TEXT,
   gateTest                                  TEXT,
   googlePay                                 TEXT,
   googleSignIn                              TEXT,
   groupOrder                                TEXT,
   hideAccountInviteMobile                   TEXT,
   holdenDatadogTest                         TEXT,
   homeSectionTestMobile                     TEXT,
   homeV2                                    TEXT,
   homepageCache                             TEXT,
   infraCartUseSlsFirebaseWritesEnabled      TEXT,
   inviteCodeUsageEnabled                    TEXT,
   iosCart                                   TEXT,
   iosFilters                                TEXT,
   iosPostOrderAttach                        TEXT,
   iosTrackUserUsage                         TEXT,
   loggedInFlagTest                          TEXT,
   luckyCustomerSession                      TEXT,
   mastercardWorldEliteEnabled               TEXT,
   mobilePostOrderAttach                     TEXT,
   multiFulfiller                            TEXT,
   navRestructure                            TEXT,
   newFTUEAndroid                            TEXT,
   newOrderDetailsEnabled                    TEXT,
   onSale                                    TEXT,
   payItForward                              TEXT,
   pdpDeliveryMessaging                      TEXT,
   pdpRefresh                                TEXT,
   personalizedAdsHomepage                   TEXT,
   personalizedAdsPDP                        TEXT,
   personalizedSortingForCoupons             TEXT,
   pleVariantTest                            TEXT,
   plesAutoComplete                          TEXT,
   plesMicroservice                          TEXT,
   plmPricing                                TEXT,
   pnPriming                                 TEXT,
   promoVariantCart                          TEXT,
   prunedPriceModifiers                      TEXT,
   purchaseVariantEvent                      TEXT,
   reorderSort                               TEXT,
   sanathTest                                TEXT,
   shippingMiddlewareCache                   TEXT,
   shopTab                                   TEXT,
   showAutoSaveNewTag                        TEXT,
   showComplementVariants                    TEXT,
   showCovidExpressMessaging                 TEXT,
   showGlobalPromotionsForBusinessUsers      TEXT,
   showHomeModuleRedesign                    TEXT,
   showInterestWordAlert                     TEXT,
   showReplenishments                        TEXT,
   silentCartVerify                          TEXT,
   smartCart                                 TEXT,
   standardCategoryGroup                     TEXT,
   standardCategoryGroupMobile               TEXT,
   strictPasswordRequirementsWeb             TEXT,
   switchToCartRecommendation                TEXT,
   syntheticInventoryFromPLM                 TEXT,
   `test thestral ui update`                 TEXT,
   traceCartCtrlChange                       TEXT,
   uniqueCartVariantFvfmEnabled              TEXT,
   upCatBanner                               TEXT,
   upNonMemberLandingPageTest                TEXT,
   useTestRec                                TEXT,
   webPostOrderAttach                        TEXT,
   yourItems                                 TEXT,
   
   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.userAgent`;

CREATE TABLE `events.properties.userAgent`
(
   eventId  BIGINT NOT NULL,
   browser  TEXT,
   device   TEXT,
   os       TEXT,
   string   TEXT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS `events.properties.variants`;

CREATE TABLE `events.properties.variants`
(
   eventId   BIGINT NOT NULL,
   quantity  DOUBLE,
   variant   TEXT,

   FOREIGN KEY (eventId)
      REFERENCES events(eventId)
      ON UPDATE CASCADE ON DELETE RESTRICT
)
ENGINE=InnoDB;
