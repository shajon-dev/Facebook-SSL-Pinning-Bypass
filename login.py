# https://tools.shajon.dev/curl-converter | By SHAJON-404

import requests
import json

url = 'https://b-graph.facebook.com/graphql'

headers = {
    "x-fb-request-analytics-tags": json.dumps({
        "network_tags": {
            "product": "350685531728",
            "request_category": "graphql",
            "purpose": "fetch",
            "retry_attempt": "0",
        },
        "application_tags": "graphservice",
    }, separators=(',', ':')),
    "x-fb-rmd": "state=URL_ELIGIBLE",
    "priority": "u=0",
    "user-agent": "[FBAN/FB4A;FBAV/572.0.0.38.71;FBBV/1027405223;FBDM/{density=2.7250001,width=1080,height=2292};FBLC/en_US;FBRV/0;FBCR/;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO CK7n;FBSV/14;FBOP/1;FBCA/arm64-v8a:;]",
    "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "x-zero-f-device-id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
    "x-fb-integrity-machine-id": "_CsUarnAGO26R-jA8Ex_soMR",
    "x-graphql-request-purpose": "fetch",
    "x-fb-device-group": "3753",
    "x-tigon-is-retry": "False",
    "x-graphql-client-library": "graphservice",
    "content-type": "application/x-www-form-urlencoded",
    "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "x-zero-state": "unknown",
    "x-meta-zca": "empty_token",
    "app-scope-id-header": "f52d4f4b-cb48-46d4-ae4a-c5cd2d6c4ccd",
    "x-fb-connection-type": "WIFI",
    "x-meta-usdid": "37df2729-46e9-4628-bf98-7305db330f02.1785680215.MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp91HXSTnulj8eflhhbsIbDM4OZJ6sqSMdnGleXVgR7Dw5groyCsLNWxTna2bPKeUuRNeZT5cizlmgfXPvWmZUA.MEQCIHw_wTq5p99-VzKrOOil3DjAEh9s0ncvvCzcOwBekOdUAiAulU_5_eXjJoh4ZpeKeFMnnglqpZsx80KOU6Tb0dBvOA",
    "x-fb-http-engine": "Tigon/Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "x-fb-conn-uuid-client": "1vVArZNnn5VIpEaghGc77g==",
}

data = {
    "method": "post",
    "format": "json",
    "server_timestamps": "true",
    "locale": "en_US",
    "purpose": "fetch",
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "119940804217123473292370195792",
    "fb_api_client_context": json.dumps({
        "is_background": False,
    }, separators=(',', ':')),
    "variables": json.dumps({
        "params": {
            "params": json.dumps({
                "params": json.dumps({
                    "server_params": {
                        "device_id": "f52d4f4b-cb48-46d4-ae4a-c5cd2d6c4ccd",
                        "server_login_source": "login",
                        "waterfall_id": "22d6947d-6bd2-46d1-9a9a-0cb536171c02",
                        "attestation_result": {
                            "errorMessage": "KeyAttestationException: No key found!",
                        },
                        "machine_id": "_CsUarnAGO26R-jA8Ex_soMR",
                        "from_native_screen": True,
                        "credential_type": "password",
                        "password": "#PWD_FB4A:2:1785677456:Aej2NWEPBJ3uOXmY4KUAAT1FLwBzTzrHHEVFnSr4cyDP4jIQxpj5MDhcb+8ycQ0EZtvoWBKJtvHAv26OL9OCB2igXnBkyEGtwpgt9+ROVI87s8MIZyhVhHLUDfCzaLpJDVyvrcVnnThDnpQr1vnViq5ceht3vLIBbMKfmb57U4S3itRDGc4moZ4Ac8f+KQ1NSUT+r/TU/JA2Nu//EysoDVw268RyzmKB8wNWCJj/mHM3Sy3HP3jCSVui/ZcRDWntVWGAVxZrquPgBy7aiA4d8wfL9CbHvg5hDcp1o2vEkoNygJZQAUF0zrbOlJrJKSZKoZmdmIvakT1jh2GrYLy61Zqg28YfJ1UI5cJmBkoxCDoB2FHxEcSHQciAdZGaY2bXb8GO24VCdgER6fbPPDw=",
                        "try_num": "1",
                        "family_device_id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
                        "event_flow": "login_manual",
                        "event_step": "home_page",
                        "is_from_logged_in_switcher": False,
                        "contact_point": "fuck. zuckk",
                    },
                }),
            }),
            "bloks_versioning_id": "1d00510fa1b00e7c90e763a616436417bad7c9b30ac6374f25d2e75419eb30da",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request",
        },
        "scale": "3",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "a07b73c926a84224348806e6cd486365",
            "pixel_ratio": 3,
            "is_push_on": True,
            "is_flipper_enabled": False,
            "android_device_performance_class": 0,
            "debug_tooling_metadata_token": None,
            "gpu_memory_mb": 7655,
            "theme_params": [
                {
                    "value": [],
                    "design_system_name": "FDS",
                },
            ],
            "bloks_version": "1d00510fa1b00e7c90e763a616436417bad7c9b30ac6374f25d2e75419eb30da",
            "android_os_api_level": 34,
        },
    }),
    "fb_api_analytics_tags": json.dumps([
        "GraphServices",
    ], separators=(',', ':')),
    "client_trace_id": "31887204-4227-444e-abdf-1f42096e9caa",
}

response = requests.post(url, headers=headers, data=data)
print(f"Response Status Code: {response.status_code}")
print(f"Response Body: {response.text}")