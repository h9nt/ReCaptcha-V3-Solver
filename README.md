# ReCaptcha-V3-Solver

> [!NOTE]
> Full Requests based & No Weird External ass apis, free for me cuz i know the full process xD. <br>

> [!WARNING]
> i decided to leak my solver, cuz it's flagged asf, do with it whatever u want. 

###  Score Breakdown
| Score | Meaning     | Recommended Action                |
| :-------- | :------- | :------------------------- |
| **1.0** | ✅ Very likely a human (**Best**) | Grant access with no extra verification. |
| **0.9 - 0.7** | 👍 Likely a human (**Good**) | Allow access but monitor for unusual activity. |
| **0.5** | ⚠️ Uncertain (**Medium Risk**) | Add extra verification (e.g., email confirmation, reCAPTCHA v2). |
| **0.3 - 0.1** | ❌ Likely a bot (**Bad**) | Require additional verification (**e.g., CAPTCHA challenge, 2FA**). |
| **0.0** | 🚫 Almost certainly a bot (**Worst**) | Block or heavily restrict access. |

### Prewiew 
![demo](https://github.com/user-attachments/assets/03a72a70-4db2-41a1-8723-9363b544ff00)

Example Response: 

```json
{
  "success": true,
  "challenge_ts": "2025-02-25T16:49:50Z",
  "hostname": "2captcha.com",
  "score": 0.3,
  "action": "demo_action"
}
