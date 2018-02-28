#! /usr/bin/env python
import json
import os
import sys

example = {"arc_feature_cache":"baremetal/arc_feature/cache",
		"arc_feature_timer_interrupt":"baremetal/arc_feature/timer_interrupt",
		"arc_feature_udma":"baremetal/arc_feature/udma",
		"ble_hm1x":"baremetal/ble_hm1x",
		"blinky":"baremetal/blinky",
		"cxx":"baremetal/cxx",
		"graphic_u8glib":"baremetal/graphic_u8glib",
		"iot_coap_coap_server":"freertos/iot/coap/coap_server",
		"iot_lwm2m_lwm2m_client":"freertos/iot/lwm2m/lwm2m_client",
		"iot_lwm2m_lwm2m_server":"freertos/iot/lwm2m/lwm2m_server",
		"kernel":"freertos/kernel",
		"kernel_secure":"freertos/kernel_secure",
		"net_httpserver":"freertos/net/httpserver",
		"net_ntshell":"freertos/net/ntshell",
		"sec_mbedtls_dtls_client":"freertos/sec/mbedtls/dtls/client",
		"sec_mbedtls_dtls_server":"freertos/sec/mbedtls/dtls/server",
		"sec_mbedtls_ssl_client2":"freertos/sec/mbedtls/ssl/client2",
		"sec_mbedtls_ssl_server2":"freertos/sec/mbedtls/ssl/server2"
	}
'''
"bootloader":"baremetal/bootloader",
"dma_spiflash":"baremetal/dma_spiflash",
"openthread_cli":"baremetal/openthread/cli",
"openthread_ncp":"baremetal/openthread/ncp",
"secureshield_secret_normal":"baremetal/secureshield/secret_normal",
"secureshield_secret_secure":"baremetal/secureshield/secret_secure",
"secureshield_secret_secure_sid":"baremetal/secureshield/secret_secure_sid",
"secureshield_test_case":"baremetal/secureshield/test_case",

'''

result = {"arc_feature_cache":0,
		"arc_feature_timer_interrupt":0,
		"arc_feature_udma":0,
		"ble_hm1x":0,
		"blinky":0,
		"cxx":0,
		"graphic_u8glib":0,
		"iot_coap_coap_server":0,
		"iot_lwm2m_lwm2m_client":0,
		"iot_lwm2m_lwm2m_server":0,
		"kernel":0,
		"kernel_secure":0,
		"net_httpserver":0,
		"net_ntshell":0,
		"sec_mbedtls_dtls_client":0,
		"sec_mbedtls_dtls_server":0,
		"sec_mbedtls_ssl_client2":0,
		"sec_mbedtls_ssl_server2":0
		}


folder = ".travis"

if __name__ == '__main__':
	print(example)
	for (k,v) in example.items():
		print("example[%s]=" %k,v)
		pathin = "../example/"+v
		os.chdir(pathin)
		os.system("make "+sys.argv[1]+" clean")
		if os.system("make "+sys.argv[1]+" -k") != 0:
			result[k] = 1
		pathout = pathin.count('/')*"../"+folder
		os.chdir(pathout)
	print(result)

	for (k,v) in result.items():
		if v == 1:
			sys.exit(1)
	
	sys.exit(0)
