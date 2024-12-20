PERMISSION_CALLS = "calls"  # Access to call logs
PERMISSION_CAMERA = "camera"  # Access camera
PERMISSION_CONTACTS = "contacts"  # Access to contact list
PERMISSION_DOWNLOADER = "downloader"  # Access to downloader
PERMISSION_EXPLORER = "explorer"  # Access to filesystem
PERMISSION_HOME = "home"  # Manage alarm and connected objects
PERMISSION_PARENTAL = "parental"  # Access to parental control
PERMISSION_PLAYER = "player"  # Control freebox player
PERMISSION_PVR = "pvr"  # Access personal video recorder
PERMISSION_SETTINGS = "settings"  # Allow modifying the Freebox settings (reading settings is always allowed) # noqa B950
PERMISSION_TV = "tv"  # Access tv guide

FREEBOX_ECC_ROOT_CA = (
    "-----BEGIN CERTIFICATE-----\n"
    "MIICWTCCAd+gAwIBAgIJAMaRcLnIgyukMAoGCCqGSM49BAMCMGExCzAJBgNVBAYT"
    "AkZSMQ8wDQYDVQQIDAZGcmFuY2UxDjAMBgNVBAcMBVBhcmlzMRMwEQYDVQQKDApG"
    "cmVlYm94IFNBMRwwGgYDVQQDDBNGcmVlYm94IEVDQyBSb290IENBMB4XDTE1MDkw"
    "MTE4MDIwN1oXDTM1MDgyNzE4MDIwN1owYTELMAkGA1UEBhMCRlIxDzANBgNVBAgM"
    "BkZyYW5jZTEOMAwGA1UEBwwFUGFyaXMxEzARBgNVBAoMCkZyZWVib3ggU0ExHDAa"
    "BgNVBAMME0ZyZWVib3ggRUNDIFJvb3QgQ0EwdjAQBgcqhkjOPQIBBgUrgQQAIgNi"
    "AASCjD6ZKn5ko6cU5Vxh8GA1KqRi6p2GQzndxHtuUmwY8RvBbhZ0GIL7bQ4f08ae"
    "JOv0ycWjEW0fyOnAw6AYdsN6y1eNvH2DVfoXQyGoCSvXQNAUxla+sJuLGICRYiZz"
    "mnijYzBhMB0GA1UdDgQWBBTIB3c2GlbV6EIh2ErEMJvFxMz/QTAfBgNVHSMEGDAW"
    "gBTIB3c2GlbV6EIh2ErEMJvFxMz/QTAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB"
    "/wQEAwIBhjAKBggqhkjOPQQDAgNoADBlAjA8tzEMRVX8vrFuOGDhvZr7OSJjbBr8"
    "gl2I70LeVNGEXZsAThUkqj5Rg9bV8xw3aSMCMQCDjB5CgsLH8EdZmiksdBRRKM2r"
    "vxo6c0dSSNrr7dDN+m2/dRvgoIpGL2GauOGqDFY=\n"
    "-----END CERTIFICATE-----"
)
FREEBOX_ECC_INTERMEDIATE_CA = (
    "-----BEGIN CERTIFICATE-----\n"
    "MIICTjCCAdOgAwIBAgICEzgwCgYIKoZIzj0EAwIwYTELMAkGA1UEBhMCRlIxDzAN"
    "BgNVBAgMBkZyYW5jZTEOMAwGA1UEBwwFUGFyaXMxEzARBgNVBAoMCkZyZWVib3gg"
    "U0ExHDAaBgNVBAMME0ZyZWVib3ggRUNDIFJvb3QgQ0EwHhcNMjQwOTExMTY1NzMw"
    "WhcNMzQwOTA5MTY1NzMwWjBZMQswCQYDVQQGEwJGUjEPMA0GA1UECAwGRnJhbmNl"
    "MRMwEQYDVQQKDApGcmVlYm94IFNBMSQwIgYDVQQDDBtGcmVlYm94IEVDQyBJbnRl"
    "cm1lZGlhdGUgQ0EwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAASZh/Apn56RulcNKDqV"
    "gVqTDusvVQK9kIgJD39MzpnbsxMWv16RKs5JXGNb21z5QsmDnKcjZt9TE+BPh4l0"
    "KDmMtAL5q+I/r0lFuJE7JohWN47rPWb7hOl2N9RDY+6HqQyjZjBkMB0GA1UdDgQW"
    "BBT6m56/7eLixv5eBCT7XHDeHaItXTAfBgNVHSMEGDAWgBTIB3c2GlbV6EIh2ErE"
    "MJvFxMz/QTASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAKBggq"
    "hkjOPQQDAgNpADBmAjEAxxMePcul3xoJAWMai6KPFNSV+MJnNxJ1dxpcWxE04E4a"
    "ry3KEvz2sAAtrf44kR3KAjEAjRTZoi4ZHKlOML1XBo20FGkVZjWmNxVWncYiFvg8"
    "VFlUKziUxvOt/CVZaq0j7mJS\n"
    "-----END CERTIFICATE-----"
)

FREEBOX_CA = FREEBOX_ECC_ROOT_CA + "\n" + FREEBOX_ECC_INTERMEDIATE_CA
