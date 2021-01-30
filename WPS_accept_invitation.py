invite_userid = 226436868

import requests

sids = [
    "V02ST6jrlh6rhtsog2NHKEnESQFpXLs00a63472800452724b6",
    "V02S0V0Uk7qGzIKX8AcMM6lBdThowH400a070c330045272429",
    "V02SVzBUVnIXnfZ-LeYnTCqcX0fymuE00ae6274c0045272135",
    "V02Sg9Iu2nC8pqzq_sOnghz2QevU2Ww00ac3a78200397119b9",
    "V02S9U8ZdWOih4I28lhXU96LsMRVUls00a5857530045271efe",
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02ScVbtm2pQD49ArcgGLv360iqQFLs014c8062e000b6c37b6",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
    "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
for i in sids:
    requests.post(invite_url, headers={'sid': i}, data={'invite_userid': invite_userid})
    
