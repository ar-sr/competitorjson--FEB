import requests
import pandas as pd


competitor_list=[
    {
    
    'url':"https://shop.sprouts.com/api/v2/store_products?limit=60&search_term= ",
    'cookie':"_gcl_au=1.1.1870522609.1706678526; BVBRANDID=44bd90f1-c5b6-4f2a-b533-a2aa621c15aa; _fbp=fb.1.1706678528061.2114288924; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; __stripe_mid=69b2421c-f664-47b0-8ada-3194ed0b62d7f36b12; __cf_bm=lgw2xDhTdiare0ScDioqNO0EutjvCCu_wEgMWN1WBQ4-1707114788-1-AdC78VWrDbu1JkJnIl5zNIo2DRy5nedcTLoCX2xCNe0ohmOGTuiO262/cIFQVL409RbDcrOJExbpfRusqgPjlgM=; dotcomSearchId=a9d554b2-299b-493f-85c9-e3c3ee2374c3; session-sprouts=.eJwdzkFvgjAAhuH_0rMaCptGbk4ZK7ElOrDAhQAtsdgioyCC2X8f2eG7vJfveYG0bLm-ArvMpOYLkDa8VVnN6w7YXdvPRXOtxb1Ou_uN18AGfPSuuVsIX3gonBAkwtuu5ggL8zLOmwpTPnK5bZI9WiOFhyRAEFe78Rh8KhLsOuKeRvINBVbYPNKzjAMmycRuxI0tPCKN6suURF6Z0ZPwK2SQafcklTMQMYiYnruMvv9_Raa8oarpGX3q435GqW3PKXywCAu_Po-MhhopeWWzAwfFQKrY8g_hhCNjxZzZ7tCfj3aDssNGLy2Vp_uvZHmySoyd0jHvjXAOXRPEYAF6zdtUMGCbbxsDrqGx_v0Dvn1qTg.GKIS2w.x6ad_R9vBZoWwSb0SqfKYzbnbO0; _ga=GA1.2.1479835951.1706678528; _uetsid=e3542a80c41011ee8df3997928063361; _uetvid=b021a2c0bff811ee97982b12ce0f9533; _ga_LPZ816BHL5=GS1.1.1707128730.4.1.1707114843.60.0.0; _dd_s=rum=1&id=fb2edccc-bdca-4a50-bcb5-3604f16c3fb6&created=1707114774893&expire=1707115743747; _gid=GA1.2.1087611198.1707128730; _gat_UA-47434162-1=1; __stripe_sid=878306b4-2230-44e8-8901-12c006c31d9fef638e; BVBRANDSID=99cfa3cf-b854-4842-a1fc-dcc0d8bd271b; loyaltyID=undefined"
},

{
    'url':"https://shop.thefreshmarket.com/api/v2/store_products?limit=60&search_term= ",
    'cookie':"osano_consentmanager_uuid=307c376c-f10d-4107-a573-c7e1f10af7f3; osano_consentmanager=3x8MgIHnK_nVJk5KmuOnd2sHDJYR8FP6k1pCkCaxdqC0pkZknRQR80VRjB6Kbgp7iGjMUnsPLnme8DWmUxRLBTj48Z3TkM1LJINdRgM__wpe-q8XngljF-JbFVnkfXq4LfhXRd5iPf89ikmPWXa635YOVLE924Ot8lU-D_E4Xy6P1mJcughXVg5oPt56dUVNqJH39oco4BAJ-E9jqf6qFimUuhbedA890lkIoINBn4wilHtXcqRTKzrDKkkaBU4EXcSmTg2iAG1Ry3jlpaURHTclVU9KceLsUfw0QQ==; _gcl_au=1.1.1454964145.1706631619; _gid=GA1.2.921200125.1706631621; _fbp=fb.1.1706631621548.1772768121; _pin_unauth=dWlkPU5qZzVOR1ZsTlRVdFl6SmtZeTAwWmpNekxUazBaVGd0TURoa01EWmxabVF4TkRNMg; ajs_anonymous_id=d6854b93-7b07-407f-a94f-839dc66712ed; __stripe_mid=6a035359-a082-4788-a444-cbc813a5b8ab5862e9; fw_se={%22value%22:%22fws2.904b7ea3-3c52-4b73-982f-fe0d1a5c7217.3.1706678484364%22%2C%22createTime%22:%222024-01-31T05:21:24.364Z%22}; _uetsid=76a87b70bf8b11eeb2461f63bc1d7a0c; _uetvid=76a8e760bf8b11ee8e7067f8c6f9fc7b; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T05:22:41.980Z%22}; _ga_EMDXDP2N4W=GS1.2.1706678486.2.1.1706678564.44.0.0; __stripe_sid=4de0f57b-def4-4649-9359-d819c0aac2c083aadd; __cf_bm=yKgtT0SxPcrWLh9iLS4z.5LN74Bl9gGS1bQ5nIlm1ws-1706679642-1-AQnN0qxyxZkNsf4EPffEx3ZkrpN7ENQJY2c8Qjwrw0X6fvsHxqE/74zELvOt4w5Uu5QgZKDHPi0k7f6cNWRKCUA=; session-prd-tfm=.eJxNic2OgjAYAN-lZ2MoWn-4bRTYNlJCFmTphQAW_VBAKaxSs---HPcwmWTmjdKyk-qCrDK7KTlD6V12ddbIpkdW3w1TUVIpaJu0b6-yQRaSI7vkbgE-MBppijmw7XyKuDCP44QuzNtPftvexY6uaFUsRWUbSegZh_BK_LDoucsgAQxJ5dSHONA89ha8nry3lwKoos1Ri29WZnEAfhWNXEcm197ysGMX4eJ7_v_XBOfuU9HaGXKTkDze4mKkq9Mnw-LrCVnsGLRqX1x_mLzyXn5o4zKYZxs_OLfQqeZJyt3eJqPI-qhU6WN9TgY4JnYPxoMzx1VohgYluxROyCLmmqzWi83vHyX9aTc.GJtu-A.RJLQ3Mfh0E7W1nhZBpran31K4Yg; _gat_UA-000000000-1=1; _dd_s=rum=0&expire=1706680572827; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T05:41:13.278Z%22}; fw_uid={%22value%22:%2226a02601-620e-4807-af18-cc8bd1ab86fd%22%2C%22createTime%22:%222024-01-31T05:41:13.294Z%22}; _ga=GA1.1.1783481186.1706631620; _ga_2NZ40CS25B=GS1.1.1706678485.4.1.1706679673.57.0.0"
    
},

{
    'url':"https://shop.wegmans.com/api/v2/store_products?limit=60&search_term= ",
    'cookie':"ajs_anonymous_id=33183b74-475b-4f1f-937a-d4c903166054; lux_uid=170711513897640590; wfmStoreId=16; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; _gcl_au=1.1.1663954989.1707115142; _fbp=fb.1.1707115141645.1115619076; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; wfm.tracking.sessionStart=1707115142229; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY0NjQ5NTU5MTIxODI0NjUwMDk1MTk2MzEyMDc4MDcyNzI4MDU3MVIRCIC697_XMRgBKgRJTkQxMAPwAYC697_XMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; sa-user-id=s%253A0-e09a6035-dbb5-5e72-6b55-d4a3d3151d09.WK86YvxnZaUk2O8ll%252FOSaJxdVCJWK6v2%252FMo%252B86BXRTo; sa-user-id-v2=s%253A4JpgNdu1XnJrVdSj0xUdCTEvxIg.OsMBR8tfqvcRCZQZMgco%252BASkDbGnoOEQX8tIn%252BvQjqk; sa-user-id-v3=s%253AAQAKIPKv96fHV4WdcPyxHZU-JjNyp1oVxB6O7vrm6gYp1lxTEAEYAyDVvLmsBjABOgROQQ4MQgT5oNN3.azv4yw2dCUXGVQGQrSFzNh%252FOh7lIuF0%252BBt1j5UyoYMw; __stripe_mid=df9962f1-2f54-4604-bc12-c105a3e092882ff550; __stripe_sid=07536ca0-9bd1-43e8-a5a0-0b570e2adce25a7db3; wfm.tracking.s10=1; ajs_anonymous_id=33183b74-475b-4f1f-937a-d4c903166054; wfm.tracking.x2p=1; at_check=true; inRedirectGoldPanAudience=1; __cf_bm=jdxmDHFhgNs4P.DuX1L6pEhX4riX_Kyfa2ZoZs18i.c-1707116112-1-AQwyyj1BvcsvnbNsvvacmDtaTpZRzRCokFJAwHR8F/qikg0tCmZWkrsJb1JnXBLSzNG/fd/VeZh43IfslirQlsY=; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; at_check=true; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C46495591218246500951963120780727280571%7CMCAAMLH-1707720913%7C12%7CMCAAMB-1707720913%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707123313s%7CNONE%7CMCSYNCSOP%7C411-19766%7CvVersion%7C5.5.0%7CMCCIDH%7C0; dotcomSearchId=56a64478-df43-4e00-b9ee-e9bbd498113b; s_gpv=Search%20Results:%20apple%20|%20Wegmans; session-prd-weg=.eJwdjstygjAAAP8lZ-sAggo3i9ZJamBANIYLgySWAEGHgI84_fcyPexlL7tvkF06rkrgXfJG8QnIbryTecvbHnh9N4xGcaXEtc36a81b4AH-QuV5W4hQIHjQ0AwEcqejNAvr-BrRhdXcz417S304h_Jgp0nkhCSudyRuqKZ9sI1lIAwb6696l6CK6sKmEtshoQbdQwXbo05P6JKTSIRVZOI1nYXr2sL-Q1AS9zlx_lsnq6lhdRsYeaqdP05Jd-DEvLMTFmEbvxg5KCibko0fOCkegd48g2Sj8cyYBs569ZM9tp-pVYnF3lYDqmYL7YuPnu3Pne-WUbRk30-JVmACBsW7TDDg2Y4xXyzdufH7Byg4aY4.GKIZXg.Gw2FRrT9Rq2hLmxW9Dov_ukDaw4; _uetsid=3f99c340c3f111eea2fbe1a3c3513819; _uetvid=3f99e440c3f111eebd48914dcddadd20; _dd_s=rum=0&expire=1707117411116; mbox=session#3d6742eab86b4277958477fbae19a371#1707118372|PC#3d6742eab86b4277958477fbae19a371.41_0#1770361291"

},


]


searchterm='Apple'
cookie=competetor_list[0]['cookie']



HEADERS={
    

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie   
    
    
}


URL=competetor_list[0]["url"]+"apple"
responses=requests.get(URL,headers=HEADERS)


data =responses.json()
items=data.get('items')
# for item in items:
#     print(items.get('name'))

print("........filtered data are below...............")


for item in items:
    for category in item.get('categories'):
        if (category.get('name')=='Fruits'):
            if(searchterm in item.get('name')):
                print(item.get('name'))
                
                
                





    # df_items=pd.DataFrame(items)
    # cleaned_items=df_items[['name','base_price']]

    # cleaned_items.to_excel(f"scraped/{search_term}.xlsx",index=False)





