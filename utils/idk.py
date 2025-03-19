from requests import Session


class TwoCaptcha:
    def __init__(self, site_Key: str, token: str):
        self.base_url = "https://2captcha.com/api/v1/captcha-demo/recaptcha/verify"
        self.session = Session()
        self.site_Key = site_Key
        self.token = token
        self.headers = {
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": "i18next=de; guest_currency=eur; user_country=de; original_referer=https%3A%2F%2Fwww.google.com%2F; timezone=Europe%2FBerlin; first_visited_page=%2Fde%2Fdemo%2Frecaptcha-v2; last_visited_page=%2Fde%2Fdemo%2Frecaptcha-v3",
            "Host": "2captcha.com",
            "Origin": "https://2captcha.com",
            "Referer": "https://2captcha.com/de/demo/recaptcha-v3",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        }

    def solve_captcha(self) -> str:
        try:
            response = self.session.post(
                self.base_url,
                headers=self.headers,
                json={"siteKey": self.site_Key, "answer": self.token},
            ).json()
            if response["success"] != True:
                raise Exception(response)
            return print("Solved captcha in [{}]".format(response["challenge_ts"]))
        except Exception as e:
            print("Failed to solve captcha: {}".format(str(e)))


if __name__ == "__main__":
    solver = TwoCaptcha("6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge", "03AFcWeA4VGqbdOqC2GbdoI76JL3geCDr-u6-DYozrSHlANzp9tW07GnTKfg3LEzxIZiQbJnJXkO_kgI7EieFDpjtD79_5V7ZDlnY98T7_1LsDaktRhDZdy7s9OsgoNiosneLaShUIt5EHjjLOQsyMlHXAFbQNw_tZmtKneRopE_B7IZjgGMpwSU0ge_ASiOiZGbH1OrRdAerQaygZUfK4t_wqy-FlwdEISD-XePk_EwgMEEQ9euer74HjZ5RAr4r3aYYjyQ1hcthqmsSJAgeCE4jZMqluYLbWV2sD42In_LgdH9m8-AdPdjOEwIbfqhyIBrWWd2HiEqwd7ZgGpSU9kTPH6xXFCo4Oo_iHPpii5e2Ot7KTWHBvNZGf2pt9Af-Yn3LItnLwmAIc7aiayKrNmGPpFRKiX8agcfvR6JwE_BL-4PiMlQf019dpNVm7gOG1eEuZzj1paLct_a8PYpzP-wnO-f1gF1xsjxKaXzAWs8TmrJ6xBlY89Jc5AEVPm0waO1cm-NapqIrvO9Uq5MHrWOMy30viTFY4NrLmvWOjggOdrRWjzWL8hYYiTympk2nkW7dlmqxlONy-N839gvGKf2mrWRo3gbP6vNYiwIrWh5nvgrV4FvTNIRY4A2GNsknVDkbruv_HCN3luQSV2hlU6sn44lxkRe-FqwwOYh-rEnUVjlvmh2Cq1fKr9cB7VRTfPztTVluijWA6sAQuMu9BBMomWmvk8fFx-ujs3GToU3c1YrHg9O3OIZapSEQLDayNqByYb2OouusiqQxc-AemN0uaTVvMqr_tgYbM2m_BxiBwOzHnXQKqdfLGJEAlLpRFZWiGkLfy_PbvjxTuVFSg_R_2dp645vouhc0in3gUdI2UYynVpEEfUfvJAKqxeZ6fPB-atoMJHNkV").solve_captcha()
    print(solver)
