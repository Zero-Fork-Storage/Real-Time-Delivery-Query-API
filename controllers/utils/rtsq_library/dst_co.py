class DST_Company:
    def __init__(self):
        self.company_code = {
            "건영택배": "18	", "경동택배": "23", "홈픽택배": "54",
            "굿투럭": "40", "농협택배": "53", "대신택배": "22",
            "로젠택배": "06", "롯데택배": "08", "세방": "52",
            "애니트랙": "43", "우체국택배": "01", "일양로지스": "11",
            "천일택배": "17", "한덱스": "20", "한의사랑택배": "16",
            "한진택배": "05", "합동택배": "32", "호남택배": "45",
            "CJ대한통운": "04", "CU편의점택배": "46", "CVSnet 편의점택배": "24",
            "KGB택배": "56", "KGL네트웍스": "30", "SLX": "44",
            "하이택배": "58", "FLF퍼레버택배": "64",
            "롯데글로벌 로지스": "99", "TNT Express": "25", "USPS": "26",
            "APEX(ECMS Express)": "38", "에어보이익스프레스": "29", "Cway Express": "57",
            "DHL": "13", "범한판토스": "37", "EMS": "12",
            "Fedex": "21", "CJ대한통운 국제특송": "42", "GSMNtoN(인로스)": "28",
            "i-Parcel": "34", "DHL Global Mail": "33", "EuroParcel(유로택배)": "55",
            "UPS": "14", "GSI Express": "41"
        }

    def search(self, name):
        code = self.company_code[f'{name}']
        return code


Code = DST_Company()