#
# DRM Transport Certificate
#
id=transportCert.profile
name=DRM Key Transport Cert profile
description=This profile creates a certificate that is good for transporting private key materials
list=2,4,5,6,7
2.default.class=com.netscape.cms.profile.def.ValidityDefault
2.default.name=Validity Default
2.default.params.range=720
2.default.params.startTime=0
4.default.class=com.netscape.cms.profile.def.AuthorityKeyIdentifierExtDefault
4.default.name=Authority Key Identifier Default
5.default.class=com.netscape.cms.profile.def.AuthInfoAccessExtDefault
5.default.name=AIA Extension Default
5.default.params.authInfoAccessADEnable_0=true
5.default.params.authInfoAccessADLocationType_0=URIName
5.default.params.authInfoAccessADLocation_0=
5.default.params.authInfoAccessADMethod_0=1.3.6.1.5.5.7.48.1
5.default.params.authInfoAccessCritical=false
5.default.params.authInfoAccessNumADs=1
6.default.class=com.netscape.cms.profile.def.KeyUsageExtDefault
6.default.name=Key Usage Default
6.default.params.keyUsageCritical=true
6.default.params.keyUsageDigitalSignature=true
6.default.params.keyUsageNonRepudiation=true
6.default.params.keyUsageDataEncipherment=true
6.default.params.keyUsageKeyEncipherment=true
6.default.params.keyUsageKeyAgreement=false
6.default.params.keyUsageKeyCertSign=false
6.default.params.keyUsageCrlSign=false
6.default.params.keyUsageEncipherOnly=false
6.default.params.keyUsageDecipherOnly=false
7.default.class=com.netscape.cms.profile.def.ExtendedKeyUsageExtDefault
7.default.name=Extended Key Usage Extension Default
7.default.params.exKeyUsageCritical=false
7.default.params.exKeyUsageOIDs=1.3.6.1.5.5.7.3.1,1.3.6.1.5.5.7.3.2
