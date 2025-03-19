from requests       import Session
from h9nt           import PbEnc
from colorama       import Fore, Style, init
from os             import system
from user_agent     import generate_user_agent
from re             import search
from threading      import Thread, active_count
from rich.console   import Console
from rich.align     import Align          
from json           import dumps
from time           import sleep
import shutil


init(autoreset=True)
system("cls")


class ReCaptchaV3:
    def __init__(self):
        self.site_key = "6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge"
        self.session = Session()
        self.ua = generate_user_agent()
        self.solved = 0
        self.failed = 0
        self.console = Console()
        #self.proxy_url = "https://advanced.name/freeproxy/67bcf0d20471a"
        #self.session.proxies = {"http": self.proxy_url, "https": self.proxy_url}
        self.anchor_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=de&v=IyZ984yGrXrBd6ihLOYGwy9X&size=invisible&cb=377vfyrpt3t7"

    def resp_(self, response_body: str) -> str:
        try:
            match = search(
                r'<input[^>]+id=["\']recaptcha-token["\'][^>]+value=["\']([^"\']+)["\']',
                response_body,
            )
            return match.group(1) if match else None
        except Exception:
            return False

    def uvresp(self, response_body: str) -> str:
        try:
            match = search(r'\["uvresp","(.*?)"', response_body)
            if match:
                uvresp_value = match.group(1)
                return uvresp_value
            else:
                return None
        except Exception:
            return

    def fetch_token(self):
        try:
            response = self.session.get(
                self.anchor_url,
                headers={
                    "Connection": "keep-alive",
                    "Cookie": "_GRECAPTCHA=09AP_l5mNo0Zjeym4ZkJSlx8xmd9feUB4mHjNPsQYSKny8yki4h3X1AQJTa-LS7WX3UO5COdczJKtLENvjtyDnSNg",
                    "Host": "www.google.com",
                    "Referer": "https://pubtok.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                    "X-Browser-Channel": "stable",
                    "X-Browser-Copyright": "Copyright 2025 Google LLC. All rights reserved.",
                    "X-Browser-Validation": "AAV+/uoCDRQwZrp3SAYQ2ve+P6s=",
                    "X-Browser-Year": "2025",
                    "X-Client-Data": "CMeDywE=",
                },
            )
            return self.resp_(response.text)
        except Exception as e:
            print(f"{Fore.RED}Error fetching token: {e}{Style.RESET_ALL}")
            return False

    def make_reload(self) -> str:
        try:
            self.payload = {
                1: "IyZ984yGrXrBd6ihLOYGwy9X",
                2: self.fetch_token(),
                4: "!BAKgAgcKAAQeGkcWbQEHewDV6gQ1cL_2P-CPS-HnZBXJo6iW0ofC6aFyVmSL7VIUIH1MP-eFM1JHqEYM0sMTgB-WjbA42XaeU49FQdvXtDUDYSVYV1dqFFWUTq54y9OV0iEinfp9lIhuhYYrp4DxG_uyRTCAKzh-UxvqXZpkqmVfXZLwaTPKzd7CEK8Z7jbasqC5KZdcf_Lv0tzKZxf9VVhOWqDHPJ7WdDqhrkX3DBIGKOF_s173NzLh10REjRA6SqItWxdruRAc3iC0zpmyIgqxC-g-uRWf3oNLDsOZHuKgxStNSKUpnAJu-8MfERBEgRRcNqJgb3qYQuRLS9wnAPiU906rFHHTGBYAFreY4NjUW1j0NGYImp1cKk_0lFPU-bElyc5Eg6_6LGcCar2Rv38_r7FrQydHBzMBbtTzolbTqKcKrSuUTMVRpQbgnRhfqVv3dhHc-up9SVYx1tm32e4tBzX8XQJJSOEB06CQBTFpEfbuYPiCdvG_8Mo7VFldeFELGIRvfv6ILjpPM6rylWtF3Tuwwqtlt-cRC-37lUBcK2oK_yuksaYCgdlbOw2ce4fC-VD6iz7yqZ8Kov76FMIzFw4tfTDa9tJJJFyJfcWnHo_absNkgI9SQJF-JaWrGuY2or20NZGkryUW1ODGBZbCu8tXeuQpchXFURocYN01s_28M1XXGyy_BVgA5Hw-s9TEmu2xDas929oJm01cQkw5GYqzu8YCxRLgAsIyQSyfznXKVa0EB9dbQDvj1X3CMFO0yZNsSr6h-xLS_IcqWwiiC9A40c-TSkusbFlEIoGtJQhuK5ecxEwln4S9wkOLCjRsCHg4TK6ajS_ov7Gg1lNY7VlnVPCQikVqIenItJQIB4bmGzzQU-7IhR1Yd6CwFaM1jgO-7litWoNfA_bvMNroNB15gKj-o59S7C7SZBQFNST2D47mnvQ2iGi3s3gAxBr55Btap7RkmVfXqieRfCO7xYo4OTr2RZdGMBpIy-7aQdfvvrpDVTkyzF9yuXk6xAbS8tCKAFAr13-rFcakoSByWqimanaEL4_9aF8RzyjUq4vNX0g1WRvNzNjD8_7ZrYthpWRJ4_4oBcxNAJsc-Vz6Vp-D4Tt5CUBChGXGdnoLLNp5wrFtVA",
                5: "-699923380",
                6: "q",
                7: "05AB8KyRAdvLwrgYMP3RQe2qjTbtevO3YKCzzuxMZ5zBIcYYc_uoVn0-K5tbOqz7hZkCEnZyvNC-JPf8vrSeVDuxTdf9hYDBAOMI2_S5KDJEVhS5byk-ilZkA4vtdgXJYEFr7Zy6Tx0SzAciPz29XVDXdefRhbu3VqDxs4IBCLy-SX0ZT95cWG56otT-QV05_Xv6e6Q0VJp_-TLZeL2fWmW0mXKCiPNEUDAV1-waWRUkoKcoh9iYuKsK1Un8PCYF531w9MGgLQ3Q2I44VptHtowk9Az-pjiQVKsqKUavwL5RdPC0aM8k3K6z0MUMqvTOGv2QgIo-Jy8YvCEJ-Bh1tSUXny-lsJ94TbPmukUcPzijLmTFWR2peWyHZ-DfdmKnRb8781yIjApPXTHchzAPuMAlKGSWOQAqmyLob-aoJmcnXf-QvJpffRvBF28xJvBosmYvMExK_X3ELa6h5rldWc4ZQcDR5OaohQ_0R_nmjaI6f6agXILAZeiHDCPzAMrOZG7CLdrJCMD9o9gskQeSTBupyvv_kHkWWqAENG7-p809DAKiJp_jSsfRBVEzO1bf1H_bKIfIwtxbLnNwrS4a17SORDFmykoXwX5Qugh0g-MtfUPzuFRIXpG2vaVo-tGCqJ-5FduyqGrngTtUZ5tQvPiwa_sOwepm7-GPhyKVj4d7kPXAi9b0toAfpstOPEvx6C4HPinug9JLCbSUM1TB5T70dusfsRD6Edtzp8QOcDqPSsKfNNydFpcLv7nzgUDDOI-Ids5_1D0uuW0QQRkPcAJRqxmcQt0XPyFJyWo_MrmoBEXgaJRxmxzwnC3rOYuLvQcbk27BbKszH0tfxUefAba4xF53LQov-BcZ-N2zg4Ag0w7VxlnCox8Yt4c4pVVJ472ilHUACCGZ7QaOUvTvUm3I_la5fJ7ABjeQexpPE2G38dCLvV_HO1-RiCkkXz41xamUoJwDkAxjcYixKwo5-LHyf7BfELZgvZwWFEbs3tthl2jU9gwoBMduXj7S0no2dEBk2EgCAevHjPSNai082y0OnuJrVidguq154KMr3naO0eqlfPhDmf-F66DXSMU98U_AfEa47hmMAvnyG0zVJ1F-KJvxQQN72LQEK-NcNtwRYIFePuwLhAwB44iqxjRGp_DB3hhySjF6eG1iYhjFZ3C6F5xaRhah3wMpaXhwd79Z4HvKF3-YcwtfekVWOjVNJjfP6DrmUiria4Ni_H25Mt",
                8: "demo_action",
                14: self.site_key,
                16: "0tC5RaG9_T6G4v8-f8QgPH-9BWF9vP0VseYyTla_HzyE4P08fcYiPn2_B2N_vvxEoLz8PYXh_j1-xyM_frwEYHy__UWhvf0-huL_Pn_EIDx_vLgVkWYOciazK1KO05vAY7ilPRHNtVqWZvKu16N7n9hY6NU01SJmdkKfPleC_1d_lIDc1eHVVebGip7m499UF9jY3NEA1T6G4v8-f8QgPH-9BWF9vP5Gor7-P4fj_D98xSE9fL4GYn69_0ejv_88O5TU8KTpkWap0ybbgs9Qa5BghR0JEYmR4s7-2vvr3_Bj0SjhENUiHgoe20srTAfklOh9HQjd8mZaTuKe0pb_U6fUMDyk8SIBfnnXF1rUNGAEXCwUfNkhYZm-JnKjgv_7VJRY6ZUyDjY13qq_M-vQK1e8GGyY7P1lsebCPzqX1_Brl_xQpNkZPaXyIwJ_etQUGLRlRV0dHm5SYnZjUugvQ1e8GGyM1P1lsd7CPzqX1G-g3PTVGPFmEeKe2xrezCfsnGUA7NWVVaX2vhLas7egG5AogE0FZiWdrp53HtdH9-x4GGigmRYd9dGV_lKmzxM_p_AdAH141hau6dY-kucXV3_kMF1AvbkWVeYultfIM2fwUGClgVFhohWV_lqa8xs_p_AZAH141hYucvJff1-DwKvQpM2Y8ZXibrpnSwLv79w0q9Q8mNUtVX3mMldCv7sUVBSUcamRkkYSpzLGj-grF3_QJFyQvSVxloH--leXKCtXvBBkmOD9ZbHSwj86l9f0a5f8WKzNFT2l8g8Cf3rUFKTr1DyQ5RltfeYuc0K_uxRUbSgUfNkhVZG-Jm6zgv_7VJR8qW0VfdZurt9uo8OTm-D1COGtXYVyaZX-cq7nM1Of2AxYfOkNTkG-uhdXc_w7rEk0xWWhaboqQqs_Z3ADpCiVLTiZPfFuSsJjZxNEKCg0PP09cSHyElYiozb_85w__EywWPFiLW36dv7nU5MXxAyQ8Rz5GRXhnmr-T2t3E2-YdFVsjXYBXma222urR_eQBFhVSUm58eYyxhbS_5-bkLBUgHGtca2x9hYPH39Xo9CoIQSg6ZFRFX3aLk6WvydzjIP9RaG9_T45ltbbc-wsJIDstUyV3SphnsqGFn7bH1efvCRwqYD9-VaWstJWvxtvj9f8ZKzxwT45lta-kuP0M6CZKLTZOhHp6kaDRx7j5_OocGD0mTYtloXyWxse5AP0JM0xJSjaGfIiypba2tPr99QkkR0dnZYmKkqOnpucD-fw3TTNrMHiEZXyyyN34AO4s8wlQXnpaWou2i7K76_Xx-zM_STY3gHuse7zFtPnF7CcUBhpHb4lvqmV_m6S0y9bl9AQXHzxMXJBvroXV5frF3_YJEygvSVtsoH_R6O__zw7lNTs_b2ySZ6eDq9jQzO8LGEcFHzRFW2t3i5ypuMjP7PwIQB9eNYWIrIfM2frcGAoZR1Y6R2WXdXXAz77nBeUs9QcvQFh2bZicrau6ycPyADosPDpWim13hL-8vMfgDAALHCQ1SUhygYedlrvL1gQs80o9P3hkjJa8y6nB2f4WAA9HMWRwS4SFlLbM4sfc2vkHBRpAb4p3eq--17TW4OQBBxQcQEVob3aszdS1_N0LBggqKlpERYR2lKbR4O378i30KTNYbF1rqLp1j6S8xdbp-AwUKDY_XGx4sI_OpfXs9x0sPEh2NU9pdIqUo7zK1ejvCxonYD9-VaWgqaOlv9Tr-wwPKTxJgF-edcW5-rXP5vsMFx85TFiQb8HY3--__tUlKzc3Okx4n7iAlOu7yer9ExcsSkl2ZmZ0u7zI7cDQGi8fJiNRWYqss6y1zPrgCScmFytibGtsfIm7s8m7--bkJioVQTtMdqu8q7fU9fvqIiwrO2tmZmmjr62p6_DA1CsnOlI8bFacqo-XstzJ4Rz8OyoUJGVnV4Wlpqa959_mKw0WFUhtXmWVdKC57fLM9xX0OzdMdkd4qqy5q-iz6_TjLyFMQWdVdImMnMrn5vv3DDoVSWc7iWihsp-757nm5Co2FlxAb1yEoImstO203-gfJ0ZQTG9Menl7ts-j9voPKiwZTlpJYYpke6y3ueT75_kmJ1w8bGqddHWW2ua3zPYr-RxYKnJ7eaq3qsLI_NX3-DsAFz5JeWd1e7iXxbrr7uMsIDZEbHWOnIimpsG21tYmDyYnW2dfdqt7ts3b5-v5FjY5TENyQJ14iZzP6-fJ7AUmAEJnU1aCp7y7tOrt-eQJJww3RXx4nK2yoMnpuvoOEjUAXURxa2areYDayNbqD-b0IilnNWtsi3Sfutvm--krJiA2V2Z7dZSGts_j5fYZJvUiM0h6aoKJe6C8xf340OAJNS5bOWqMdoack9rPyesmPBU2PDdgZKt5m9vM7dkRKjYfJGo3YGRjr6vE5-v4Dyo3OEw8d1yNlImAk9zJ9wInGiYmPE9giJ2qjMnos-3U5QY2TVolP1Rqe4ePrLzwzw7lNTBIVGGGhJunx7Slv9br8wUPKTtLgF-edcXE1MPqBAs5TD9Fi51-k8enuvoL5QcOGCdMNYqWgHS2r8b64ecV8AhcRTVoVJauysa3yv_s6DoVE1Z8i5yElbqktsTgGucKKSlNV2WNhaq9tLSz1xHnCjdSV32Da5aqoKbJ2P0CFBUZUEB8h3J0k7qqxbP9AhUwR1FCSExye7rCrMbOw8Xf9AkVKy9JW2ugf76V5dwdIy4rKkBifppVb4STqbfH0-j4Bw8sPEiAX551xcrq7MXf9AgZKy9JW2ugf76V5fjWDPY3M016eImWopXJ5vgJDAI3H05bbW16ZbiWqt-2tc_k-gsXHzlLW5BvroXVzPz4KhQnTyxpaGimuc3O49To6fUQGDU0S35pgnaYpN3R2OUUKTQsY091XJePqJeVr8bU6_f_GSs7cE-OZbXS69ng9OAnIkZePFickp3KpMi01BogFT8mZnZ1bWWurb3Zyv0GHTYGRTptX3yfl829oNnkB-wdKCw6PI11iJartbr3yQv6NUg8ZmuHc4q6nKzDzOf9IC88Rzc3NU9keoWcn7nL2hDvLgVVbIpYl5a6hZ-0ydbk7wkbKmA_WGNzi4_OpfXsJCspFkl3e4J6q5yXp9z9xd_0CBokL0lbaqB_vpXG4PcfNDYnNXFsnXmwodDbt-3W_AD1DyQ5RlhmfIyUqLq_3Oz4MA9OJXVwjYiHyO3b9dMqNgQyNTN8aKuZhqjW5PYPBQQEJTxqWm6qmKew7Pa1z-T5AxUfOUtYkG-uhdXp1wYdJ00kRmVnfJedlcu40doMFgYZU0Zwi5SNiMyUutAMGtXvBBooOj9Za3iwj86l9e_1JkMqYGtJbWl8n7LV6gwMCgkdOkZ7XYt6poO9pe3n8fkECypsc2JkrLu-pOXI-RYUOD4kRkhmeqa3oc3au-AGLRBEOUdneombhpaxtdX77ePzPjcpeot2n4qims3nyhQsMEFPNlGBlHqzhMbJ58D2HCwoOktMRGSjpoiyo7vHERUSOUVqZFZ6d66p1dq64uX7FRlGSkZHfGOzqqS07QvxAxkkSUc4inhjh8qv5Mjsxd_2ChcpL0RTY6B_vpXl1hrkJAcWSXZfaICElKe0_eUaARIDXD9Ya2touLmTo6W_1On1Cw8pO0aAX551xd_w9hYU9R4USnRgWIC9tZfBx_nc9h0WTjt5dnyCqMy0uu38CvotGFZhR2xFX3aJmKevydvlIP8-Tl41caK3e6StxQUEISf1DxU8TEWQb66FuvICCh8o8yZbdYKQmGV_haS2xsUQ7y4FNmuFkqCsyNCVr7XU5vb1QFAvQ09VmrzR1_IKFtUg_z5OcYiPn2-Ej6OvtQr6NwQqanaIUqd1xtO5s8n9Cu4mPDlYa2d2uM2b5srg-fgFOzNfclxzmqmImL-26QrsMyMyX0x-eZ54oaTC5crYAw4-WkxQhXl2dJak2uXUD-sPFF1kUnV4hXeEu7ryxO8kBgMcVjqBl3pzta6m0ez9HPM-U01WSI9-hcXEtsjg8Bk7FClreWGcXpqa0crVAekEJkc8SlF7bnSAkIXQrwEYHy__UWhvf0-OscjP36_E09_z_wVVZGZSraWGlJXgvxEoLz8PYXh_j1-xyM_fr-4RKC8_DyMvQ09VnMCYttbj6fr6DEZrJXBPobi_z5_xCA8f7y5RaG9_T2Rvg4-Vzgb39-4iOjRkapuqtZXEu8T64PDlMA9OcYiPn2-Ej6SvtRfqHUcvIzdFdJp7zdjX2-IT__kaSzdvZoeFfLmuw7nFExYSPVYmVUdum7qJqt_pCesU9StaTWSEhKGEuqnHxOT3BSU-UkxsjI6mq8SxvLv_xRDvLlFob39PY2-Dj5WzCfsEN0FXHlBmcXmNl7DhzQQcGDkdWU1qaJGpsLqgsKXwzw4xSE9fL0RPY291sObY4PzoEhg5ZDxWcaOlndq0wNDFEO8uUWhvf09kb4SPlbbY1QIJJxNtNVdrdITC1Kv06BwmEUI0OlOMb32Oipe56wUYIhUeKCVoiZKsjLXW1_XC9ekzQxQ3cVZcZXzM2sv4Cs4g-x1EIzhKd2JlsI_O8QgPH-8EDyQvNYxrhseutNzr2BcmJA5UToSYZ5Wh1bbyxMUQ7y5RaG9_T2Nvho-V5u31KfUWLFs2dVaeepuSusQJDvgaSiAwJXBPjrHIz9-vw8_j7_VLPDhGa3uYnLesxMXqGvg-EzRAUEWQb67R6O__z-TvBA8VUHVZoG6hsp7rAvH0DChWZlBUdHW4rd2688rp4zI9NFpUVXinbsm23-_KGA0yKy1nWGRTZobMq9-67c78NhxEVm5tZIqQvNbAyAj7FDAsVUZpX5uZmqTauc7U7Pz2NxVDZ15lZbeY28PECfH3PQRWHjx6YHBlsMCf8QgPH-8uBTZQa2hnqJu9qNDrDygQBUcpUYpgcGV_maO8x9vk-QoPLDxIgF-xyM_frwEYHy__PhVlV3B0ZX-Uq7TMz-n7BUBQ",
                20: "tbMywwLDQ2NV0sWzEsMCw0NzJdXSxudWxsLFtudWxsLG51bGwsbnVsbCxbMjMsMS40MDQzNDc4MjQwMTM3NTE1LDAuMDA2OTAxNzA5MzkxNTIwNTc0LDE0XSxbOTIsMC4zNjA4Njk1NjMxNDQxODYzLDAuMDA3MDk0MDE3MDUzMjYxNzgxNSwyXSwwLDBdLFsiMmNhcHRjaGEuY29tIiwic3RhdGljLmNsb3VkZmxhcmVpbnNpZ2h0cy5jb20iLCJ3d3cuZ29vZ2xlLmNvbSIsInd3dy5nc3RhdGljLmNvbSJdLFs5LDUyM11d",
                21: "0aAB8KyRBJtGWleKSZJ4eLSYfpteExs9iYSw_QbcvvZgDb9T-7OzPbkn_451mfDmzcj7IqYON0Sh_IZ-dOqpQch9BBvu0WezKZX_aZuJaE65XCVtL0Gg",
                22: "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",
                25: "W1tbNTAwNiw1MF0sWzY0NjA3LDFdLFszNTgzNywxXSxbNDU0NjQsMV1dXQ",
            }
            response = self.session.post(
                f"https://www.google.com/recaptcha/api2/reload?k={self.site_key}",
                headers={
                    "Accept": "*/*",
                    "Connection": "Keep-Alive",
                    "Content-Type": "application/x-protobuffer",
                    "Cookie": "_GRECAPTCHA=09AP_l5mNg-PdtOveZSO8Emr5aG8oiLI8ABQvJ48KSoCwTdeOtNJjY7PBanGYGH9sCTjystwdqFtXC1h9jFhpoYjE",
                    "Host": "www.google.com",
                    "Origin": "https://www.google.com",
                    "Referer": "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=de&v=IyZ984yGrXrBd6ihLOYGwy9X&size=invisible&cb=377vfyrpt3t7",
                    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Storage-Access": "active",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                    "X-Client-Data": "CKyJywE=",
                },
                data=PbEnc().encrypt_pb_payload(self.payload),
            )
            self.rresp = PbEnc().get_rresp(response.text)["rresp"]
            return PbEnc().get_rresp(response.text)["rresp"]
        except Exception as e:
            print(f"Error occurred during reCAPTCHA reload: {e}")
            return False

    def clr(self) -> str:
        try:
            self.payload1 = {
                1: self.site_key,
                2: self.rresp,
                3: "IyZ984yGrXrBd6ihLOYGwy9X",
                4: {
                    1: 230,
                    3: 1,
                    5: {
                        1: [
                            {1: 1, 2: 156, 3: 282},
                            {1: 2, 2: 4985, 3: 130},
                            {1: 4, 2: 5116, 3: 96, 5: {2: 13395}},
                        ]
                    },
                },
            }
            response = self.session.post(
                f"https://www.google.com/recaptcha/api2/clr?k={self.site_key}",
                headers={
                    "Accept": "*/*",
                    "Connection": "Keep-Alive",
                    "Content-Type": "application/x-protobuffer",
                    "Cookie": "_GRECAPTCHA=09AP_l5mNg-PdtOveZSO8Emr5aG8oiLI8ABQvJ48KSoCwTdeOtNJjY7PBanGYGH9sCTjystwdqFtXC1h9jFhpoYjE",
                    "Host": "www.google.com",
                    "Origin": "https://www.google.com",
                    "Referer": "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=de&v=IyZ984yGrXrBd6ihLOYGwy9X&size=invisible&cb=377vfyrpt3t7",
                    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Storage-Access": "active",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                    "X-Client-Data": "CKyJywE=",
                },
                data=PbEnc().encrypt_pb_payload(self.payload1),
            )
            if response.status_code != 200:
                print(f"CLR request failed with status code: {response.status_code}")
                return False
            return response
        except Exception as e:
            print(f"Error occurred during clear reCAPTCHA: {e}")
            return False

    def clr1(self) -> str:
        try:
            self.payload2 = {
                1: self.site_key,
                2: self.rresp,
                3: "IyZ984yGrXrBd6ihLOYGwy9X",
                4: {
                    3: 1,
                    5: {
                        1: [
                            {1: 6, 2: 5478, 3: 117},
                            {1: 3, 2: 5468, 3: 244},
                            {1: 1, 2: 641, 3: 282},
                            {1: 2, 2: 5470, 3: 130},
                            {1: 4, 2: 5601, 3: 96, 5: {2: 13395}},
                        ]
                    },
                },
            }
            response = self.session.post(
                f"https://www.google.com/recaptcha/api2/clr?k={self.site_key}",
                headers={
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Connection": "Keep-Alive",
                    "Host": "www.google.com",
                    "Origin": "https://2captcha.com",
                    "Referer": "https://2captcha.com/",
                    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                    "X-Client-Data": "CKyJywE=",
                },
                data=PbEnc().encrypt_pb_payload(self.payload2),
            )
            if response.status_code != 200:
                return response
        except Exception as e:
            print(f"Error occurred during clear reCAPTCHA: {e}")
            return ""

    def solve(self) -> str:
        try:
            token = self.fetch_token()
            if not token:
                print(token)

            reload_response = self.make_reload()
            if not reload_response:
                print(reload_response)

            clr_request = self.clr()
            if not clr_request:
                print(clr_request)

            clr1_request = self.clr1()
            if not clr1_request:
                print(clr1_request)

            self.data = {"siteKey": self.site_key, "answer": self.rresp}

            response = self.session.post(
                "https://2captcha.com/api/v1/captcha-demo/recaptcha/verify",
                headers={
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Cookie": "i18next=de; guest_currency=eur; user_country=de; original_referer=https%3A%2F%2Fwww.google.com%2F; timezone=Europe%2FBerlin; first_visited_page=%2Fde%2Fdemo%2Frecaptcha-v2; last_visited_page=%2Fde%2Fdemo%2Frecaptcha-v3",
                    "Host": "2captcha.com",
                    "Origin": "https://2captcha.com",
                    "Referer": "https://2captcha.com/de/demo/recaptcha-v3",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                },
                json=self.data,
            ).json()
            if "success" not in response or response["success"] != True:
                print(f"{Fore.RED} Captcha failed! {Style.RESET_ALL}")
                self.failed += 1
                return False
            else:
                self.solved += 1
                self.solved_time = response["challenge_ts"]
                print(f"{Fore.CYAN} {Fore.YELLOW}[{Fore.RESET}{response['challenge_ts']}{Fore.YELLOW}]{Fore.RESET} Captcha solved!")
                print(f"{Fore.LIGHTRED_EX} Raw result:  {dumps(response)}")
                return True

            # self.display()
        except Exception as e:
            print(
                f"{Fore.RED} Error occurred during solving captcha: {e}{Style.RESET_ALL}"
            )
            return False

    def display(self):
        terminal_width = shutil.get_terminal_size().columns
        display_text = f"[!] Solved: {self.solved} | Failed: {self.failed} | Time >>> [{self.solved_time}]"
        centered_text = display_text.center(terminal_width)
        self.console.print(Align.center(centered_text), style="bold green")

    def start(self, threads: int) -> None:
        thread_list = []
        for _ in range(threads):
            t = Thread(target=self.solve)
            t.start()
            thread_list.append(t)
            sleep(1)

        for t in thread_list:
            t.join()


if __name__ == "__main__":
    sleep(1)
    solver = ReCaptchaV3()
    solver.start(10)
